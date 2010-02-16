#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: ts=4 sts=4 sw=4 tw=79 sta et
"""
Python source code - replace this with a description of the code and write the code below this text.
"""

__author__ = 'Patrick Butler'
__email__  = 'pbutler@killertux.org'

import subprocess
import sys
import pylirc

def main(args):
    ffox = subprocess.Popen(["/usr/bin/firefox"] + args[1:])
    try:
        if not pylirc.init("firefox", "~/.lircrc", 1):
            return "Failed"
        while True:
            codes = pylirc.nextcode(1)
            if codes is None:
                continue
            for code in codes:
                #print code
                if code is None:
                    continue
                if code["config"] == "EXIT":
                    return
                args = code["config"].split()
                subprocess.Popen(["xdotool"] + args )
    except KeyboardInterrupt:
        print "Exiting...."
    return 0

if __name__ == "__main__":
    sys.exit( main( sys.argv ) )
