#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: ts=4 sts=4 sw=4 tw=79 sta et
"""
An interface script for using lirc with Firefox, requires pylirc and xdotool
"""

__author__  = 'Patrick Butler'
__email__   = 'pbutler at killertux org'
__license__ = "GPLv2"

import subprocess
import sys
import pylirc

def main(args):
    """
    Fires of firefox, then inits pylirc and waits for remote presses
    """
    ffox = subprocess.Popen(["/usr/bin/firefox"] + args[1:])
    try:
        if not pylirc.init("firefox", "~/.lircrc", 1):
            return "Failed"
        stop = False
        while not stop:
            codes = pylirc.nextcode(1)
            if codes is None:
                continue
            for code in codes:
                #print code
                if code is None:
                    continue
                if code["config"] == "EXIT":
                    stop = True
                    break
                args = code["config"].split()
                subprocess.Popen(["xdotool"] + args )
    except KeyboardInterrupt:
        print "Exiting...."
    p1 = subprocess.Popen(["xdotool", "search", "--title", "Mozilla Firefox"], stdout = subprocess.PIPE)
    p1.wait()
    windows = p1.stdout.readline().split()
    for window in windows:
        print window
        subprocess.Popen(["xdotool", "windowfocus", str(window)])
        subprocess.Popen(["xdotool", "key", "ctrl+q"])
    return 0

if __name__ == "__main__":
    sys.exit( main( sys.argv ) )
