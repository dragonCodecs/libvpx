#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: LGPL-2.1-or-later

from argparse import ArgumentParser
from pathlib import Path
import re
from warnings import warn

def parse_options(lines: list[str]) -> list[str]:
    options = []
    for line in lines:
        if option := re.match(r'#define\s+(VPX_ARCH|HAVE|CONFIG)(_[A-Z0-9_]+)\s+([01])', line):
            if option.group(3) == '1':
                options.append(f'{option.group(1)}{option.group(2)}')
    return options


def print_webm_license(prefix='', suffix='') -> list[str]:
    return [
        f'{prefix} Copyright (c) 2011 The WebM project authors. All Rights Reserved.{suffix}\n',
        f'{prefix} {suffix}\n',
        f'{prefix} Use of this source code is governed by a BSD-style license{suffix}\n',
        f'{prefix} that can be found in the LICENSE file in the root of the source{suffix}\n',
        f'{prefix} tree. An additional intellectual property rights grant can be found{suffix}\n',
        f'{prefix} in the file PATENTS.  All contributing project authors may{suffix}\n',
        f'{prefix} be found in the AUTHORS file in the root of the source tree.{suffix}\n',
    ]


def create_config_mk_file(options: list[str], output: Path):
    with open(output, 'w', encoding='utf-8') as f:
        lines = print_webm_license(prefix='##')
        lines += [f'{option}=yes\n' for option in options]
        f.writelines(lines)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input', type=Path, help='Path to configuration header')
    parser.add_argument('output', type=Path, help='Path to config.mk')
    args = parser.parse_args()
    with open(args.input, 'r', encoding='utf-8') as f:
        options = parse_options(f.readlines())
        create_config_mk_file(options, args.output)
