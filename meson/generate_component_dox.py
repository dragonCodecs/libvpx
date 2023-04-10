#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: LGPL-2.1-or-later

from argparse import ArgumentParser, FileType
from io import TextIOWrapper
from pathlib import Path

if __name__ == '__main__':
	parser = ArgumentParser(description='Create a Doxyfile for an component')
	parser.add_argument('--component', required=True, help='Component type')
	parser.add_argument('--output', type=FileType('w', encoding='utf-8'), required=True, help='Write to this file')
	parser.add_argument('source', type=Path, help='Source file of the component')
	args = parser.parse_args()

	f: TextIOWrapper = args.output

	source: Path = args.source
	page_name = source.stem.replace('.', '_')

	f.write(f'/*!\page {args.component}_{page_name} {page_name} \n')
	f.write(f'   \includelineno {source.resolve(strict=True).as_posix()}\n')
	f.write('*/\n')
