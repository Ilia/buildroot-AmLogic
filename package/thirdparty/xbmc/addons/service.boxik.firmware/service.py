#!/usr/bin/python
import sys
import os
import lib.common as common

__addonversion__ = common.__addonversion__
__INSTALLSDCARD__ = common.__INSTALLSDCARD__


class Main:
    def __init__(self):
        if not sys.argv[0]:
            pass
            #TODO: NOT WORKING CURRENTLY
            import xbmc
            #xbmc.executebuiltin('XBMC.AlarmClock(BOXiKCheckAtBoot,XBMC.RunScript(service.boxik.firmware, auto),00:00:10,silent)')
            #xbmc.executebuiltin('XBMC.AlarmClock(BOXiKCheckWhileRunning,XBMC.RunScript(service.boxik.firmware, auto),04:00:00,silent,loop)')
        else:
            try:
                if sys.argv[1] == 'auto':
                    if common.get_remote_version() != common.get_local_version() and common.new_update():
                        if os.path.exists(__INSTALLSDCARD__):
                            common.download_firmware()
                        else:
                            common.message("New update available")
                elif sys.argv[1] == 'manual':
                    common.manual_update()
                else:
                    pass
            except IndexError:
                pass

if (__name__ == "__main__"):
    Main()
