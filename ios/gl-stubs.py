#!/usr/bin/env python3
"""The OpenGL ES functions Odin's code names (OpenGL ES 3.2, Khronos's
gl32.h) that iOS's OpenGL ES 3.0 does not have, as functions that do
nothing: Odin draws with Vulkan (MoltenVK) on iOS, its OpenGL renderer is
only compiled. Usage: gl-stubs.py <gl32.h> <the SDK's OpenGLES/ES3/gl.h> <out.c>"""
import re, sys

khronos, apple, out = sys.argv[1:4]
proto = re.compile(r'GL_APICALL\s+(.+?)\s*GL_APIENTRY\s+(gl\w+)\s*\(([^)]*)\)\s*;', re.S)
have = set(re.findall(r'\b(gl[A-Z]\w+)\s*\(', open(apple).read()))
lines = ['/* Made by ios/gl-stubs.py: the OpenGL ES 3.1 and 3.2 functions iOS lacks, doing nothing */',
         '#include <GLES3/gl32.h>', '']
count = 0
for ret, name, args in proto.findall(open(khronos).read()):
    if name in have:
        continue
    ret = ' '.join(ret.split())
    body = '' if ret == 'void' else ' return 0;'
    lines.append('GL_APICALL %s GL_APIENTRY %s(%s) {%s }' % (ret, name, ' '.join(args.split()), body))
    count += 1
open(out, 'w').write('\n'.join(lines) + '\n')
print('%d functions stubbed' % count)
