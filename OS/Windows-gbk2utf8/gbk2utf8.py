#!/bin/env python
# -*- coding: utf-8 -*- 
__description__ = """
  gbk2utf8
  Desc: A program for convert string, from windows local codec to utf-8.
  Usage:
\t gbk2utf8.exe <gbk_string>
\t or
\t bperror xxx xxx 2>&1 | gbk2tuf8.exe
  Ver : 1.0
  Env : Python 2.7
  Date: Jun 16 2014
  Lic : GPL - http://www.fsf.org/licenses/gpl.txt
  Report bugs to: rex.kang@qq.com
"""

import sys

DEBUG=False

def main():
    source = ""
    result = ""
    codec = sys.getfilesystemencoding()
    if source == "" and not sys.stdin.isatty():
        for line in sys.stdin.readlines():
            source += line
        if DEBUG: print "Read stdin: ----------\n%s" % repr(source)
    else:
        if len(sys.argv)<>2: usage()
        if sys.argv[1] == "-h": usage()
        source = sys.argv[1]
        if DEBUG: print "Read param: %s" % repr(source)
    try:
        #result = source.decode('utf-8').encode(sys.getfilesystemencoding())
        result = source.decode(codec).encode('utf-8')
        if DEBUG: print "Decoded:----------\n%s" % repr(result)
    except Exception,e:
        result = "string: %s" % str(e)
    finally:
        sys.stdout.write(result.strip())

def usage():
    print __description__
    sys.exit(0)
    
main()
