#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# setup.py v0.1.1 for qrDecoder 0.1.2
# Copyright (C) Nicholas Wilde <ncwilde43@gmail.com>
#
# Description:
# ------------
#    Create Windows excecutable with cx_freeze & setup.py for qrdecoder
#
# Directions:
# -----------
#  - Install cx_freeze <http://cx-freeze.sourceforge.net/>
#  - use command to compile
#
#      python setup.py build
#
# Changelog:
# ----------
#  Version 0.1.2 (2011-12-11) 
#   - Added if statement for base
#   - Added VERSION file
#
#  Version 0.1.1 (2011-11-25)
#   - Added 'PcxImagePlugin','TiffImagePlugin','TgaImagePlugin' includes
#   - Added 'README','LICENSE','CHANGELOG' includefiles
#
#  Version 0.1 (2011-11-22)
#   - Initial Release
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

appName = 'qrDecoder'
appNameLower = appName.lower()

import sys, re, os
from cx_Freeze import setup, Executable

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Get qrdecoder version
f = open('VERSION', 'r')
version = f.readline()
f.close()

# Are we compiling in Windows?
if sys.platform == "win32":
    base = 'Win32GUI'
else:
    base = 'None'

includefiles = ['README','LICENSE','CHANGELOG','VERSION']

includes = ['sip', 'PyQt4.QtCore','PyQt4.QtGui','PyQt4','zbar','Image','sys',
            'src.ui.ui_mainwindow','src.ui.images_rc','src.ui.ui_aboutwindow',  
            'PcxImagePlugin','TiffImagePlugin','TgaImagePlugin','os']

exe = Executable(
                    script = appNameLower + '.pyw',
                    base = base,
                    targetName = appName + '.exe',
                    copyDependentFiles = True,
                    icon = 'src/resources/icon.ico',
                    )

setup(
        name = appName,
        version = version,
        description = 'A small desktop program that decodes QR codes.',
        author = u'Nicholas Wilde',
        author_email = 'ncwilde43@gmail.com',
        license= 'GNU GPL v3',
        url = 'http://qrdecoder.googlecode.com/',
        long_description = read('README'),
        options = {'build_exe': {'optimize': 2,
                                 'includes': includes,
                                 'include_files': includefiles,
                                 'build_exe': 'build/' + appNameLower
                                }
                    },
        executables = [exe]
        )
