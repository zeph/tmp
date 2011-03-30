#!/usr/bin/env python
import sys
import os.path, time
import shutil

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

print (src_filename, dst_prefix)

f = open(src_filename, 'r')
for filename_raw in f:
   filename_path = filename_raw.strip()
   mtime = time.localtime(os.path.getmtime(filename_path))
   mtime_p = time.strftime("%Y-%m-%d", mtime)
   print (filename_path, mtime_p)
   filename = os.path.basename(filename_path)
   filename_dst = os.path.join( dst_prefix , mtime_p , filename )
   print filename_dst
   intermediate = os.path.dirname(filename_dst)
   if not os.path.exists(intermediate):
        os.makedirs(intermediate)
   shutil.copyfile(filename_path, filename_dst)
