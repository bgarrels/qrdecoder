#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# qrDecoder v0.1.2
# Copyright (C) 2011 Nicholas Wilde <ncwilde43@gmail.com>
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

# Import Stuff
import sys, os, zbar, Image, sip, string, logging
import PcxImagePlugin, TgaImagePlugin, TiffImagePlugin
sip.setapi("QVariant", 2)
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from src.ui.ui_mainwindow import Ui_MainWindow
from src.ui.ui_aboutwindow import Ui_aboutDialog
import src.ui.images_rc

# App Name
__appName__ = 'qrDecoder'
__verFileName__ = 'VERSION'
__configFileName__ = 'settings'

# Enable logging for both console and file
# http://docs.python.org/howto/logging-cookbook.html#multiple-handlers-and-formatters
__logFileName__ = __appName__.lower() + '.log'
logger = logging.getLogger('error_logging')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler(__logFileName__)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# Determine if application is a script file or frozen exe and get appPath
# http://stackoverflow.com/a/404750/1061279
if hasattr(sys, 'frozen'):
    __appPath__ = os.path.dirname(sys.executable)
elif __file__:
    __appPath__ = os.path.dirname(__file__)
__verPath__ = os.path.join(__appPath__, __verFileName__)

# Get qrdecoder version from VERSION file
try:
    f = open(__verPath__, 'r')
    __version__ = f.readline()
    f.close()
    __winTitle__ = __appName__+' - v' + __version__
except:
    logger.error(__verFileName__ + ' file is missing.')
    __winTitle__ = __appName__

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ABOUT WINDOW =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# About window properties
class AboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("About")
        # Info displayed in the About window
        __info__ = ("<b>"+ __winTitle__ + "</b>"
            "<p>Author: Nicholas Wilde"
            "<p>E-mail: <a href='mailto:ncwilde43@gmail.com'>ncwilde43@gmail.com</a>"
            "<p>Home page: <a href='http://code.google.com/p/qrdecoder/'>http://qrdecoder.googlecode.com</a>"
            "<p>License: <a href='http://www.gnu.org/licenses/gpl-3.0.txt'>GNU GPLv3</a>"
            )
        self.label.setText(__info__)
        self.connect(QtGui.QShortcut(QKeySequence("Ctrl+W"),self),
            SIGNAL("activated()"), SLOT("accept()"))
        self.connect(self.pushButton_OK, SIGNAL("clicked()"), SLOT("accept()"))
        del __info__

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- MAIN WINDOW =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Main Window properties
class qrDecoder(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        
        # Read settings from settings.ini file
        self.settingsFile()
        self.readSettings()
        
        # Have window accept drops
        self.setAcceptDrops(True)
        
        # Fix window size
        self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
        
        # Set window title
        self.setWindowTitle(__winTitle__)

        # Set qlineedit to read only so user can copy but not edit.
        self.lineEdit_code.setReadOnly(1)
        
        # Disable copy push button
        self.pushButton_copy.setEnabled(0)
        
        # Button commands
        self.connect(self.pushButton_browse, SIGNAL("clicked()"), self.selectImage)
        self.connect(self.pushButton_about, SIGNAL("clicked()"), self.about)
        self.connect(self.pushButton_decode, SIGNAL("clicked()"), self.decodeImage)
        self.connect(self.pushButton_clear, SIGNAL("clicked()"), self.clearFields)
        self.connect(self.pushButton_exit, SIGNAL("clicked()"), self.exitApplication)
        self.connect(self.pushButton_copy, SIGNAL("clicked()"), self.copy2Clipboard)
        
        # Keyboard Shortcuts
        self.connect(QtGui.QShortcut(QKeySequence("Ctrl+W"),self),
            SIGNAL("activated()"), self.exitApplication)
        
    # Call the About window
    def about(self):
        dialog = AboutDialog(self)
        dialog.exec_()

    # Bring up the select file dialog once the browse button has been clicked
    def selectImage(self):
        fileName = QFileDialog.getOpenFileName(self, "Select Image", "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif *.pcx *.tga *.tif); \
                ;All Files (*.*)")
        if fileName:
            self.clearFields()
            self.lineEdit_location.setText(fileName)
            self.decodeImage()
            
    # Use zbar to decode image
    def decodeImage(self):
        # Taken from zbar\examples\scan_image.py
        # create a reader
        scanner = zbar.ImageScanner()

        # configure the reader
        scanner.parse_config('enable')

        # obtain image data
#        try:
        pil = Image.open(unicode(self.lineEdit_location.text())).convert('L')
#        except IOError:
#            logging.error('Cannot open ' + unicode(self.lineEdit_location.text()))
            
            
        width, height = pil.size
        raw = pil.tostring()

        # wrap image data
        image = zbar.Image(width, height, 'Y800', raw)

        # scan the image for barcodes
        scanner.scan(image)

        # extract results
        for symbol in image:
            # do something useful with results
            if symbol.type is not symbol.QRCODE:
                self.statusBar().showMessage("Image does not contain a QR code.",
                    2000)
                return
            self.lineEdit_code.clear()
            self.lineEdit_code.setText(symbol.data)
            if not self.pushButton_copy.isEnabled():
                self.pushButton_copy.setEnabled(1)
            self.statusBar().showMessage("QR code decoded.", 2000)

        # clean up
        del(image)
    
    # Clear all fields
    def clearFields(self):
        self.lineEdit_location.clear()
        self.lineEdit_code.clear()
        if self.pushButton_copy.isEnabled():
            self.pushButton_copy.setEnabled(0)

    # Determine if drag even should happen
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    # What to do when the drag event happens
    def dropEvent(self, event):
        data = event.mimeData()
        for url in data.urls():
            fileName = url.toLocalFile()
            fileInfo = QFileInfo(fileName)
            if fileInfo.isFile():
                self.lineEdit_location.clear()
                self.lineEdit_code.clear()
                self.lineEdit_location.setText(fileName)
                self.decodeImage()
            else:
                event.ignore()

    # Copy decoded text to clipboard
    def copy2Clipboard(self):
        if self.lineEdit_code.text():
            clipboard = QtGui.QApplication.clipboard()
            clipboard.setText(self.lineEdit_code.text())
            event = QtCore.QEvent(QtCore.QEvent.Clipboard)
            QtGui.QApplication.sendEvent(clipboard, event)
            self.statusBar().showMessage("Copied.", 2000)
    
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=- WINDOW CONTROLS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    # Center the window        
    def centerWindow(self):
        screen = QtGui.QDesktopWidget().availableGeometry() 
        size = self.geometry()
        self.move(int((screen.width()-size.width())/2),
            int((screen.height()-size.height())/2))

    # Move the window
    def moveWindow(self):
        screen = QtGui.QDesktopWidget().availableGeometry() 
        size = self.geometry()
        self.move(int(self.settings.value("MainWindow/x", (screen.width()-size.width())/2)),
            int(self.settings.value("MainWindow/y", (screen.height()-size.height())/2)))

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- SETTINGS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    # Read settings on startup
    def readSettings(self):
        numScreens = QtGui.QDesktopWidget().numScreens()
        screen = QtGui.QDesktopWidget().availableGeometry(numScreens-1) 
        size = self.geometry()
        # Get edge locations of window
        if self.settings.value("MainWindow/x"):
            windowLeft = int(self.settings.value("MainWindow/x"))
            windowRight = int(self.settings.value("MainWindow/x")) + size.width()
            windowTop = int(self.settings.value("MainWindow/y"))
            windowBottom = int(self.settings.value("MainWindow/y")) + size.height()
            screenRight = int(screen.width()) + screen.x()
            screenLeft = QtGui.QDesktopWidget().availableGeometry().x()
            screenBottom = int(screen.height()) + screen.y()
            screenTop = QtGui.QDesktopWidget().availableGeometry().y()
            
            # If part of the window is off the screen, center it.
            if (windowRight > screenRight) \
                or (windowBottom > screenBottom) \
                or (windowLeft < screenLeft) \
                or (windowTop < screenTop):
                self.centerWindow()
            else:
                self.moveWindow()
        else:
            self.centerWindow()
            
    # Determine where to save settings file
    def settingsFile(self):
        global __configFileName__
        if sys.platform.startswith('win'):
            __configFileName__ += '.ini'
            __configFilePath__ = os.path.join(__appPath__, __configFileName__)
            self.settings = QSettings(__configFilePath__, QSettings.IniFormat)
            if not self.settings.isWritable(): # Use %appdata% if install dir is read only
                self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope,
                    __appName__, __configFileName__)
        elif sys.platform.startswith('lin'): # Read settings.conf file
            self.settings = QSettings(__appName__.lower(), __configFileName__)
        else:
            self.settings = QSettings(__appName__.lower(), __configFileName__)

    # Save application settings
    def writeSettings(self):
        # Save window location
        self.settings.beginGroup("MainWindow")
        self.settings.setValue("x", self.x())
        self.settings.setValue("y", self.y())
        self.settings.endGroup()
        
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- EXIT =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # Call exitApplication() when "x" close button is pressed.
    def closeEvent(self, event):
        self.exitApplication()
        event.accept()
 
    # Actions to perform on application close
    def exitApplication(self):
        self.writeSettings()
        self.close()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    application.setOrganizationName('Nicholas Wilde')
    application.setOrganizationDomain('qrdecoder.googlecode.com')
    application.setApplicationName(__appName__)
    mainWindow = qrDecoder()
    mainWindow.show()
    sys.exit(application.exec_())
