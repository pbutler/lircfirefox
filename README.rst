=============
LIRC Firefox
=============

Requirements
------------

#. Python 2.x http://www.python.org
#. lirc  http://www.lirc.org
#. xdotool http://www.semicomplete.com/projects/xdotool/
#. pylirc http://pylirc.mccabe.nu/

Usage with mythfrontend
-----------------------

Set Browser in the Web Config to::

    lircfirefox.py %URL%

Copy lirc.firefox to your ~/.lirc/firefox and add the following line to your .lircrc::

      include ~/.lirc/xawtv

