# Summary #

This page contains instructions on how to build qrDecoder from source in Windows.




---

# Build QT Designer Files #

---

## Description ##
Compile all QT Designer .ui & .qrc files into .py files.

## Dependencies ##
  * makefile from [qrDecoder source](http://code.google.com/p/qrdecoder/downloads/list)

### Linux: ###
  * [GNU make](http://www.gnu.org/software/make/)
  * pyqt4-dev-tools - required for pyuic4 & pyrcc4

### Windows: ###
  * [GnuWin](http://gnuwin32.sourceforge.net/packages/make.htm)
  * [PyQt4](http://www.riverbankcomputing.co.uk/software/pyqt/)

## Installation ##
### Linux ###
  * Install GNU make
```
sudo apt-get install make
```
  * Install pyqt4-dev-tools
```
sudo apt-get install pyqt4-dev-tools
```

### Windows ###
  * Download and install GnuWin
  * Add GnuWin\bin to 'path' [environmental variable.](http://www.computerhope.com/issues/ch000549.htm)
```
e.g. C:\Program Files\GnuWin\bin
```
  * Add PyQt4 directory to 'path' environmental variable.
```
e.g. C:\Python27\Lib\site-packages\PyQt4
```

## Directions ##
  * Fill in any variables under the 'EDIT' section.
  * In the source directory, run the following command:
```
make
```

## Testing ##
### Linux ###
Ubuntu 11.10 Natty with make 3.81 & pyqt4-dev-tools 4.8.5

### Windows ###
Windows Vista and 7 with GnuWin 3.81 & PyQt4 4.8.6.


---

# Build Windows Executable #

---

## Description ##
Compile Python script into Windows executable.

## Dependencies ##
  * setup.py from [qrDecoder source](http://code.google.com/p/qrdecoder/downloads/list)
  * [cx\_freeze](http://cx-freeze.sourceforge.net/)

## Directions ##
In the source directory, run the following command:
```
python setup.py build
```

## Testing ##
Tested on Windows Vista and 7 with Python 2.7.2 and cx\_freeze 4.2.3.