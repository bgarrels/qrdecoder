#http://sourceforge.net/projects/zbar/forums/forum/664596/topic/4361149

## Summary ##

One of my biggest difficulties of making qrDecoder was the installation of the zbar python module on windows.  [easy\_install](http://pypi.python.org/pypi/setuptools) and [pip](http://www.pip-installer.org/en/latest/index.html) didn't work because it couldn't process the setup.py file. `python setup.py install` didn't work on the source file because it needed a compiler.

## Windows Installation Directions ##

  * Make sure you have [Python](http://python.org) installed
  * Download and install [zbar Windows Installer](http://zbar.sourceforge.net/)
  * Download and install [MinGW](http://www.mingw.org/).
  * Add `Zbar\bin` & `MinGW\bin` to the Windows [path environmental variable](http://www.computerhope.com/issues/ch000549.htm)
> > `e.g. C:\MinGw\bin`
  * Download [zbar python module source](http://pypi.python.org/pypi/zbar).
  * Extract the zbar python module source to a working directory.
  * Modify the zbar `setup.py` file.  From [zbar's forum](http://sourceforge.net/projects/zbar/forums/forum/664596/topic/4361149?message=9381132):
```
 1) Add

        from distutils.sysconfig import get_config_vars

    to line 3 of setup.py.

 2) Add the following parameters to the Extension call:

            library_dirs=["""d:\zbar\lib"""],
            include_dirs=[get_config_vars('INCLUDEDIR'),
                          get_config_vars('INCLUDEPY'),
                          """d:\zbar\include"""]
```
  * Run the following code inside the working directory to install zbar:
```
    python setup.py build --compiler=mingw32

    python setup.py install
```