#!/usr/bin/env python
import sys

i = 0
src_filename = ''
dst_prefix = ''

if len(sys.argv) < 5:
    print 'Syntax: -f [filename] -d [destination_prefix]'
    exit(1)
for arg in sys.argv:
    if arg == '-f':
       src_filename = sys.argv[i+1]
    if arg == '-d':
       dst_prefix = sys.argv[i+1]
    i = i+1

print src_filename
print dst_prefix
