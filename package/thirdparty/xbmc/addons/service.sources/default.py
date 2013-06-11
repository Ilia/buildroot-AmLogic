#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2013 BOXiK
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#    This script is based on script.randomitems & script.wacthlist
#    Thanks to their original authors

import os
import sys
import xbmc
import shutil

class Main:
    def __init__(self):
        if not sys.argv[0]:
            xbmc.executebuiltin('XBMC.AlarmClock(BOXiKCreateSources,XBMC.RunScript(service.sources, auto),00:00:00,silent)')
        if not os.path.exists( xbmc.translatePath('special://home/userdata/sources.xml')):
            shutil.copy2(os.path.dirname(os.path.abspath(__file__)) + '/resources/sources.xml', xbmc.translatePath('special://home/userdata/sources.xml'))
            xbmc.executebuiltin("ReloadSources")

if (__name__ == "__main__"):
    Main()
    del Main