#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: LGPL-2.1-or-later

import re

THINGS = [
    'build/make/configure.sh',
    'configure',
]

def parse_options() -> dict:
    current_options: dict = {}
    toggle_regexp = r'^\s+\$\{toggle_([a-z0-9_]+)\}\s+(.+)$'
    for thing in THINGS:
        with open(thing, 'r', encoding='utf-8') as infile:
            for line in infile.readlines():
                option = re.match(toggle_regexp, line)
                if option:
                    current_options[option.group(1)] = option.group(2)
    return current_options
    
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
                for key, description in options.items():
                    lines.append(f"option('{key}', type: 'feature', value: 'auto', description: '{description}')\n")
            elif l == closing:
                lines.append(l)
                has_generated = False
            elif not has_generated:
                lines.append(l)

    with open('meson_options.txt', 'w') as meson_file:
        meson_file.write(''.join(lines))

if __name__=='__main__':
    options = parse_options()
    update_meson_options(options)
