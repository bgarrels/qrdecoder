# Installation Instructions #


---

## Windows ##

---

### Directions ###
  * Download and unpack qrDecode zip file to any directory.

### Run ###
  * Run `qrDecoder.exe`

### Testing ###
Tested on Windows Vista & 7 with Python 2.7.2, SIP 4.13, PyQt 4.8.6, zbar 0.10, PIL 1.1.7


---

## GNU/Linux using Python ##

---

### Dependencies ###
  * [qrDecoder source](http://code.google.com/p/qrdecoder/downloads/list)
  * [Python](http://python.org/) by Python Software Foundation
  * [SIP](http://www.riverbankcomputing.co.uk/software/sip/intro) by Phil Thompson
  * [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/) by Phil Thompson
  * [zbar](http://zbar.sourceforge.net/) by Jeff Brown
  * [Python Imaging Library (PIL)](http://www.pythonware.com/products/pil/) by Secret Labs AB & Fredrik Lundh
  * gtk2-engines-pixbuf in Ubuntu Natty

### Directions ###
  * Install Python 2.7
```
sudo apt-get install python2.7
```
  * Install Python Imaging Library (PIL)
```
sudo apt-get install python-imaging
```
  * Install PyQt4.
```
sudo apt-get install python-qt4
```
  * Install zbar.
```
sudo apt-get install python-zbar
```
  * Download and unpack qrDecode source tarball to any directory.
```
wget http://qrdecoder.googlecode.com/files/qrdecoder-x.x.x.tar.gz
```
Where `x.x.x` is the version of qrdecoder
  * Unpack the tarball.
```
tar -xvf qrdecoder-x.x.x.tar.gz
```
  * Change into the qrDecoder directory.
```
cd qrdecoder-x.x.x
```

### Run ###
  * Start qrDecoder.
```
python qrdecoder.pyw
```

In Natty, I get an error `Gtk-WARNING **: Unable to locate theme engine in module_path: "pixmap"`

To get rid of this error, install `gtk2-engines-pixbuf`
```
sudo apt-get install gtk2-engines-pixbuf
```

### Testing ###
Tested on Ubuntu 11.10 Natty with Python 2.7.2, SIP 4.12.4, PyQt 4.8.5, zbar 0.10, PIL 1.1.7, gtk2-engines-pixbuf 2.24.6.