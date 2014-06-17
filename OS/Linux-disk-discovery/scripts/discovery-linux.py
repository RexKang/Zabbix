#!/bin/env python
# -*- coding=utf-8 -*-

__author__ = u'rex.kang@qq.com'
__createdTime__ = u'20140609'
__modifiedTime__ = u'20140609'
__description__ = u'A Script for Linux Entity Discovery'
__version__ = u'v0.1'
__license__ = u'GPL - http://www.fsf.org/licenses/gpl.txt'
__history__ = [
    [u'v0.1',u'20140609', u'add discovery body'],
]
__usage__ = """path - /proc/diskstats,/proc/cpuinfo etc.
find - number"""

# TODO: add row method

try:
    import simplejson as json
except ImportError:
    import json
import sys;
    
    
def discovery(path='/proc/diskstats', find='3'):
    data={'data':[]}
    if path and find:
        try:
            col = int(find)-1
            with open(path, 'r') as file:
                for line in file:
                    line=line.split()
                    data['data'].append({'{#OBJNAME}': line[col]})
            json_data = json.dumps(data)
            print json_data
        except ValueError:
            print 'Error, find must be integer!'
        except IOError:
            print 'Error: File does not exist.'
        except Exception,e:
            print str(e)
    else:
        help()


def help():
    print 'author: %s' % __author__
    print 'created: %s' % __createdTime__
    print 'modified: %s' % __modifiedTime__
    print 'description: %s' % __description__
    print 'version: %s' % __version__
    print 'license: %s' % __license__
    print 'history:'
    for history in __history__:
        print '    %s: %s, %s' % (history[0], history[1], history[2])
    print 'usage:\n%s' % __usage__


if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 2:
        path = sys.argv[1]
        find = sys.argv[2]
        discovery(path, find)
    else:
        discovery()