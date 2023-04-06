#!/usr/bin/env python
# Copyright (C) 2018 Mathieu Duponchelle <mathieu@centricular.com>
# Copyright (C) 2023 L. E. Segovia <amy@amyspark.me>
#
# This file is part of the FFmpeg Meson build
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, see <http://www.gnu.org/licenses/>.


import re
import os
import io
from pathlib import PurePosixPath
from pprint import pprint
from collections import defaultdict

ASM_EXTS = ['asm', 'S']

SOURCE_TYPE_EXTS_MAP = {
    'c': ['c', 'cpp'],
    'asm': ASM_EXTS,
}

def make_to_meson(target: str, paths: list[str]):
    source_maps = {}

    skipped = set('mk')

    for path in paths:
        with open(path, 'r') as f:
            accum = []
            accumulate = False
            source_type = None

            for l in f.readlines():
                l = l.strip().split('#', 1)[0].strip()

                if accumulate:
                    ofiles = l
                elif option := re.match(r'([A-Z0-9_]+)-yes\s+\+=\s+([a-zA-Z0-9_/.]+)$', l):
                    component = ''.join(option.group(1).split('_SRCS')).lower()
                    label = ''
                    ofiles = option.group(2)
                    source_type = PurePosixPath(option.group(2)).suffix.strip('.')
                elif option := re.match(r'([A-Z0-9_]+)-.+(?:HAVE_|CONFIG_)([A-Z0-9_]+).+\+=\s+([a-zA-Z0-9_/.]+)$', l):
                    # remove the component suffix
                    component = ''.join(option.group(1).split('_SRCS')).lower()
                    label = option.group(2)
                    ofiles = option.group(3)
                    source_type = PurePosixPath(option.group(3)).suffix.strip('.')
                elif option := re.match(r'([A-Z0-9_]+)-yes\s+\+=\s+(.+)\$\(ASM\)\s*', l):
                    # remove the component suffix and patch the extension in
                    component = ''.join(option.group(1).split('_SRCS')).lower()
                    label = ''
                    ofiles = f'{option.group(2)}.asm'
                    source_type = 'c'
                elif option := re.match(r'([A-Z0-9_]+)-.+(?:HAVE_|CONFIG_)([A-Z0-9_]+).+\+=\s+(.+)\$\(ASM\)\s*', l):
                    # remove the component suffix and patch the extension in
                    component = ''.join(option.group(1).split('_SRCS')).lower()
                    label = option.group(2)
                    ofiles = f'{option.group(3)}.asm'
                    source_type = 'c'
                else:
                    continue

                accumulate = ofiles.endswith('\\')
                ofiles = ofiles.strip('\\')
                ofiles = ofiles.split()
                ifiles = [ofile for ofile in ofiles if os.path.exists(os.path.join(target, ofile))]

                if len([of for of in ofiles if not of.startswith("$")]) != len(ifiles):
                    print("WARNING: %s and %s size don't match, not building!" % ([of for of in ofiles if not of.startswith("$")], ifiles))
                    skipped.add(label)

                if accumulate:
                    accum += ifiles
                else:
                    component_sources: dict(list(str)) = source_maps.setdefault(source_type, {}).setdefault(component, {})
                    component_sources[label] = component_sources.setdefault(label, list()) + accum + ifiles
                    accum = []

            # Makefiles can end with '\' and this is just a porting script ;)
            if accum:
                component_sources: dict(list(str)) = source_maps.setdefault(source_type, {}).setdefault(component, {})
                component_sources[label] = component_sources.setdefault(label, list()) + accum
                accum = []


    lines = []
    has_not_generated = False
    try:
        with open(os.path.join(target, 'meson.build'), 'r') as meson_file:
            for l in meson_file.readlines():
                if l == '#### --- GENERATED --- ####\n':
                    lines += [l, '\n']
                    has_not_generated = True
                    break
                lines.append(l)
    except FileNotFoundError:
        pass

    f = io.StringIO()

    # types -> component -> label (feature)
    source_types = (
        ('', source_maps.setdefault('c', {})),
        ('headers_', source_maps.setdefault('h', {})),
        ('asm_', source_maps.setdefault('asm', {})),
    )

    for source_type, components in source_types:
        for component, component_sources in components.items():
            default_sources = component_sources.pop('', [])

            if default_sources:
                f.write(f'{component}_{source_type}sources = files(\n')
                for source in default_sources:
                    if '$' in source:
                        print ('Warning: skipping %s' % source)
                        continue
                    f.write(f"\t'{source}',\n")
                f.write(')\n\n')

            f.write(f'{component}_{source_type}optional_sources = {{\n')
            for label in sorted (component_sources):
                if label in skipped:
                    f.write(f"\t# '{label.lower()}' : files(\n")
                else:
                    f.write(f"\t'{label.lower()}' : files(\n")
                l = len (component_sources[label])
                for i, source in enumerate(component_sources[label]):
                    if '$' in source:
                        print ('Warning: skipping %s' % source)
                        continue
                    f.write(f"\t\t'{source}'{',' if i + 1 < l else ''}\n")
                f.write('\t),\n')
            f.write('}\n\n')

    if has_not_generated:
        lines.append(f.getvalue())
        with open(os.path.join(target, 'meson.build'), 'r') as meson_file:
            out_generated = False
            for l in meson_file.readlines():
                if l == '#### --- END GENERATED --- ####\n':
                    out_generated = True
                if out_generated:
                    lines.append(l)
        content = ''.join(lines)
    else:
        content = f.getvalue()


    with open(os.path.join(target, 'meson.build'), 'w') as meson_file:
        meson_file.write(content)

paths = {
    'vp8': [
        'vp8/vp8_common.mk',
        'vp8/vp8cx.mk',
        'vp8/vp8dx.mk',
    ],
    'vp9': [
        'vp9/vp9_common.mk',
        'vp9/vp9cx.mk',
        'vp9/vp9dx.mk',
    ],
    'vpx_dsp': [
        'vpx_dsp/vpx_dsp.mk',
    ],
    'vpx_scale': [
        'vpx_scale/vpx_scale.mk',
    ],
}

if __name__=='__main__':
    for component, path in paths.items():
        make_to_meson(component, path)
