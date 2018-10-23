#!/bin/env python
# -*- coding: utf-8 -*- 
#################################################################################
# Name          : setup
# Description   : python setup files for commandline.
# Version       : 0.1
# Environment   : Python 2.7
# Date          : Jun 16 2014
# Author        : Rex Kang
# Help          : python -h
# Licence       : GPL - http://www.fsf.org/licenses/gpl.txt
################################################################################

from distutils.core import setup
import py2exe

setup(
    description = "gbk2utf8", 
    options = 
    {"py2exe":
        {
        "compressed": 1,
        "bundle_files": 2,
        "optimize": 2,
        "dll_excludes":["w9xpopen.exe"],
        }
    },
    console = ['gbk2utf8.py'],
    zipfile=None,
    )