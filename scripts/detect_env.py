#!/usr/bin/python
"""
Detect platform name and SIP/Python/PyQt/PySide version.

Test environment:

    Mac OS X 10.6.8
    Debian Linux Testing

References:
 - http://www.pyside.org/docs/pyside/pysideversion.html
"""

import sys
import platform

args = sys.argv[1:]
if not args:
    try:
        import PySide
        from PySide import QtCore
        print "Using PySide ..."
        print

    except ImportError:
        PySide = None
        from PyQt4 import QtCore

elif args[0] == "PySide":
    import PySide
    from PySide import QtCore
    print "Using PySide ..."
    print

elif args[0] == "PyQt4":
    PySide = None
    from PyQt4 import QtCore
else:
    print "Usage:"
    print "     python %s" % sys.argv[0]
    print "     python %s PySide" % sys.argv[0]
    print "     python %s PyQt4" % sys.argv[0]
    print

try:
    import sip
except ImportError:
    sip = None


def get_qt_version():
    if not PySide:
        return getattr(QtCore, "QT_VERSION_STR")
    else:
        return QtCore.__version__

def get_pyside_version():
    return PySide and PySide.__version__

def main():
    print 'Platform: %s' % sys.platform
    print "Python version: %s" % platform.python_version()
    print "Qt version: %s" % get_qt_version()

    if sip:
        print "SIP version: %s" % sip.SIP_VERSION_STR
    if PySide:
        print "PySide version: %s" % PySide.__version__
    else:
        print "PyQt version: %s" % QtCore.PYQT_VERSION_STR

if __name__ == "__main__":
    main()
