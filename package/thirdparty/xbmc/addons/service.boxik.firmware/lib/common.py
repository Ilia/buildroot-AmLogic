# -*- coding: utf-8 -*-
#
#     Copyright (C) 2013 Team-XBMC
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

import xbmc
import xbmcaddon
import xbmcgui
import urllib2
import os
import hashlib

__addon__        = xbmcaddon.Addon()
__addonversion__ = __addon__.getAddonInfo('version')
__addonname__    = __addon__.getAddonInfo('name')
__addonpath__    = __addon__.getAddonInfo('path').decode('utf-8')
__icon__         = __addon__.getAddonInfo('icon')
__localize__     = __addon__.getLocalizedString

__REMOTESERVER__  = "http://mogilia.com/xbmc/update/"
__INSTALLSDCARD__ = "/media/usb0/"
__VERSIONFILE__   = "version.ini"
__VERSIONLOCAL__  = __addonpath__ + "/" + __VERSIONFILE__
__VERSIONREMOTE__ = __REMOTESERVER__ + __VERSIONFILE__
__FWEXTENSION__   = ".zip"


def log(txt):
    if isinstance(txt, str):
        txt = txt.decode("utf-8")
    message = u'%s: %s' % ("XBMC Version Check", txt)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)


def message(txt):
    xbmc.executebuiltin("XBMC.Notification(%s, %s, %d, %s)" % (__addonname__, txt, 5000, __icon__))


def download_files(files):
    for file, filename in files.iteritems():
        url = __REMOTESERVER__ + file
        u = urllib2.urlopen(url)
        f = open(__INSTALLSDCARD__ + filename, 'w')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        #print("Downloading: {0} Bytes: {1}".format(file, file_size))

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            p = float(file_size_dl) / file_size
            status = r"{0}  [{1:.2%}]".format(file_size_dl, p)
            status = status + chr(8)*(len(status)+1)
            #sys.stdout.write(status)

        f.close()
    return True


def check_md5(files):
    for o_file, md5file in files.iteritems():
        if md5Checksum(__INSTALLSDCARD__ + o_file) != read_local_file(__INSTALLSDCARD__ + md5file).strip():
            return False
    return True


def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


def download_firmware():
    try:
        version = get_remote_version()
        message('Downloading new firmware [%s]' % version)
        files = {
            "factory_update_param.aml": "factory_update_param.aml", 
            "factory_update_param.md5": "factory_update_param.md5", 
            "update_1.0.3.zip": "update.zip", 
            "update_1.0.3.md5": "update.md5"
        }
        checks = {
            "factory_update_param.aml": "factory_update_param.md5", 
            "update.zip": "update.md5"
        }

        if download_files(files) and check_md5(checks):
            if xbmcgui.Dialog().yesno(__addonname__, "Would you like to update now?", "Restart is required"):
                set_version(version) 
                os.system('touch /media/usb0/restart_allowed') 
                ##os.system('reboot recovery')
        else:
            message('Download failed, please update manually')
    except urllib2.HTTPError:  
        return False


def new_update():
    try:
        version = get_remote_version()
        urllib2.urlopen(__REMOTESERVER__ + 'update_' + version + __FWEXTENSION__)
        return True
    except urllib2.HTTPError:
        return False


def manual_update():
    if xbmcgui.Dialog().yesno(__addonname__, "Do you have the update.zip on SD Card?", "Selecting 'Yes' will reboot your device to start the update."):
        os.system('/bin/sh /etc/init.d/S95xbmc stop; reboot recovery;')   


def set_version(version):
    f = open(__VERSIONLOCAL__, 'w')
    f.write(version)
    f.close()


def get_local_version():
    return read_local_file(__VERSIONLOCAL__)


def get_remote_version():
    u = urllib2.urlopen(__VERSIONREMOTE__)
    version = u.read()  
    return str(version).strip()


def read_local_file(file):
    with open(file, 'r') as f:
        firstline = f.readline()
        return str(firstline).strip()
