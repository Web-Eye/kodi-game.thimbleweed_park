# -*- coding: utf-8 -*-
# Copyright 2024 WebEye
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Thimbleweed Park Launcher for Kodi
"""

import xbmc
import xbmcaddon
import xbmcvfs
import os.path
import stat
import time

from subprocess import check_output, CalledProcessError


def process_status(process_name):
    try:
        check_output(["pgrep", process_name])
        return True
    except CalledProcessError:
        return False


class KodiAddon(object):
    def __init__(self):
        self._addon = xbmcaddon.Addon()
        self._ADDON_ID = 'game.thimbleweed_park'
        self._path = xbmcvfs.translatePath('special://home/addons/' + self._ADDON_ID)

    def run(self):
        xbmc.executebuiltin('InhibitScreensaver(true)')
        check_output(['bash', '/home/frank/Games/GOG Games/Thimbleweed Park/start.sh'])


        xbmc.executebuiltin('InhibitScreensaver(false)')
        xbmc.executebuiltin('ActivateWindow(home)')


def main():
    addon = KodiAddon()
    addon.run()


main()
