#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: LGPL-2.1-or-later

import re
import subprocess
from warnings import warn, WarningMessage

def parse_options(lines: list[str]) -> dict:
    current_options: dict = {}
    boolean_regexp = r'--(enable|disable)-([^\s]+)\s+(.+)'
    combo_regexp = r'^--([a-z0-9_\-]+)=\{?([A-Za-z]+\|[A-Za-z|]+)\}?\s+(.+)$'
    stock_regexp = r'^--([a-z0-9_\-]+)(?:=[A-Za-z]+)?\s+(.+)$'
    codec_regexp = r'^([a-z0-9_\-]+):(\s+(encoder|decoder)){1,2}$'

    for line in lines:
        line = line.strip()
        option = re.match(boolean_regexp, line)
        if option:
            current_options[option.group(2).lower().replace('-', '_')] = {
                'type': 'boolean',
                'value': 'true' if option.group(1) != 'enable' else 'false',
                'description': option.group(3).strip()
            }
            continue
        option = re.match(combo_regexp, line)
        if option:
            current_options[option.group(1).lower().replace('-', '_')] = {
                'type': 'combo',
                'choices': option.group(2).split('|'),
                'description': option.group(3)
            }
            continue
        option = re.match(codec_regexp, line)
        if option:
            feature = option.group(2).strip()
            current_options[f'{option.group(1)}_{feature}'.lower().replace('-', '_')] = {
                'type': 'boolean',
                'value': 'true',
                'description': f'Enable the {option.group(1).upper()} {feature} only'
            }
            if option.group(3):
                additional_feature = option.group(3).strip()
                current_options[f'{option.group(1)}_{additional_feature}'.lower().replace('-', '_')] = {
                    'type': 'boolean',
                    'value': 'true',
                    'description': f'Enable the {option.group(1).upper()} {additional_feature} only'
                }
                current_options[f'{option.group(1)}'.lower().replace('-', '_')] = {
                    'type': 'boolean',
                    'value': 'true',
                    'description': f'Enable the {option.group(1).upper()} codec'
                }
            else:
                current_options[f'{option.group(1)}'.lower().replace('-', '_')] = {
                    'type': 'boolean',
                    'value': 'true',
                    'description': f'Enable the {option.group(1).upper()} {feature}'
                }
            continue
        option = re.match(stock_regexp, line)
        if option:
            current_options[option.group(1).lower().replace('-', '_')] = {
                'type': 'string',
                'value': '',
                'description': option.group(2)
            }
        elif line.startswith('--') and not re.match(r'.+\<[a-z]+\>.*', line):
            warn(f"Unhandled option: {line}, check that you fixed the spacing in the configure scripts!", FutureWarning)

    return current_options

MESON_HANDLED_OPTIONS = [
    'help',
    'log',
    'target',
    'extra_cflags',
    'extra_cxxflags',
    'extra_warnings',
    'werror',
    'optimizations',
    'pic',
    'ccache',
    'debug',
    'gcov',
    'dependency_tracking',
    'libc',
    'as',
    'shared',
    'static',
    'small',
]

def filter_meson_handled_options(pair) -> bool:
    k, _v = pair
    return k not in MESON_HANDLED_OPTIONS

def update_meson_options(options: dict):
    has_generated = False
    lines = []
    with open('meson_options.txt', 'r', encoding='utf8') as meson_file:
        opening = '#### --- GENERATED EXTERN OPTIONS --- ####\n'
        closing = opening.replace('GENERATED', 'END GENERATED')
        for l in meson_file.readlines():
            if l == opening:
                has_generated = True
                lines.append(l)
                for key, kv in dict(filter(filter_meson_handled_options, options.items())).items():
                    if kv['type'] == 'combo':
                        choices = ', '.join([f"'{i}'" for i in kv['choices']])
                        lines.append(f"option('{key}', type: 'combo', choices: [{choices}], description: '{kv['description']}')\n")
                    elif kv['type'] == 'boolean':
                        lines.append(f"option('{key}', type: 'boolean', value: {kv['value']}, description: '{kv['description']}')\n")
                    else:
                        lines.append(f"option('{key}', type: 'string', value: '{kv['value']}', description: '{kv['description']}')\n")
            elif l == closing:
                lines.append(l)
                has_generated = False
            elif not has_generated:
                lines.append(l)

    with open('meson_options.txt', 'w') as meson_file:
        meson_file.write(''.join(lines))

if __name__=='__main__':
    # ./configure --help > tmp_meson_options.txt
    with open('tmp_meson_options.txt', 'r', encoding='utf-8') as f:
        options = parse_options(f.readlines())
        update_meson_options(options)
