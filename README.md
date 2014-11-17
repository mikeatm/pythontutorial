#Class Notes

## Virtualenvs (Demo) 

Virtualenvs are isolated complete python environments, 

  - pip can be used to install python modules in them.
  - are normally run as normal user
  - no root priviledges are needed to install python modules in them. 

## Creating a virtualenv

```bash
[mike@localhost demo]$ virtualenv  -p python   testenv 
Already using interpreter /usr/bin/python
New python executable in testenv/bin/python
Installing Setuptools..............................................................................................................................................................................................................................done.
Installing Pip.....................................................................................................................................................................................................................................................................................................................................done.
[mike@localhost demo]$ ls
testenv
[mike@localhost demo]$ 
```

This  virtualenv can be used by:

```bash
[mikef@localhost demo]$ source testenv/bin/activate
(testenv)[mikef@localhost demo]$ which python
~/demo/testenv/bin/python
```

The python in use is then not what is available system wide.

## Installing python module packages with pip 

```bash
(testenv)[mike@localhost demo]$ pip install psutil
Downloading/unpacking psutil
  Downloading psutil-2.1.3.tar.gz (224kB): 224kB downloaded
  Running setup.py egg_info for package psutil
    
    warning: no previously-included files matching '*' found under directory 'docs/_build'
Installing collected packages: psutil
  Running setup.py install for psutil
    building '_psutil_linux' extension
    gcc -pthread -fno-strict-aliasing -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -I/usr/include/python2.7 -c psutil/_psutil_linux.c -o build/temp.linux-x86_64-2.7/psutil/_psutil_linux.o
    gcc -pthread -shared -Wl,-z,relro build/temp.linux-x86_64-2.7/psutil/_psutil_linux.o -L/usr/lib64 -lpython2.7 -o build/lib.linux-x86_64-2.7/_psutil_linux.so
    building '_psutil_posix' extension
    gcc -pthread -fno-strict-aliasing -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -I/usr/include/python2.7 -c psutil/_psutil_posix.c -o build/temp.linux-x86_64-2.7/psutil/_psutil_posix.o
    gcc -pthread -shared -Wl,-z,relro build/temp.linux-x86_64-2.7/psutil/_psutil_posix.o -L/usr/lib64 -lpython2.7 -o build/lib.linux-x86_64-2.7/_psutil_posix.so
    
    warning: no previously-included files matching '*' found under directory 'docs/_build'
Successfully installed psutil
Cleaning up...
(testenv)[mike@localhost demo]$
```

the pip command will fetch the source from the cheese shop (pypi.python.org) compile it if neccesary and
install it to the current virtualenv

## Leaving the virtualenv

You can deactivate the virtualenv and use the system wide python via :

```bash
(testenv)[mike@localhost demo]$ deactivate
[mike@localhost demo]$ 
```

## If you dont have virtualenv itself installed

You can get its source from pypi and use it  thus:

```bash
[mike@localhost demo]$ wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.6.tar.gz#md5=f61cdd983d2c4e6aeabb70b1060d6f49
--2014-11-17 10:08:57--  https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.6.tar.gz
Resolving pypi.python.org (pypi.python.org)... 185.31.17.223
Connecting to pypi.python.org (pypi.python.org)|185.31.17.223|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1610581 (1.5M) [application/octet-stream]
Saving to: ‘virtualenv-1.11.6.tar.gz’

100%[=======================================================================================================================>] 1,610,581   4.65MB/s   in 0.3s   

2014-11-17 10:08:58 (4.65 MB/s) - ‘virtualenv-1.11.6.tar.gz’ saved [1610581/1610581]

[mike@localhost demo]$ tar -xf virtualenv-1.11.6.tar.gz 
[mike@localhost demo]$ ls virtualenv-1.11.6/
AUTHORS.txt  docs         MANIFEST.in  README.rst  setup.cfg  virtualenv.egg-info  virtualenv.py
bin          LICENSE.txt  PKG-INFO     scripts     setup.py   virtualenv_embedded  virtualenv_support
[mike@localhost demo]$ python virtualenv-1.11.6/virtualenv.py   -p python  newenv 
Already using interpreter /usr/bin/python
New python executable in newenv/bin/python
Installing setuptools, pip...done.
[mike@localhost demo]$ ls
newenv  testenv  virtualenv-1.11.6  virtualenv-1.11.6.tar.gz
[mike@localhost demo]$ source newenv/bin/activate
(newenv)[mike@localhost demo]$ deactivate
[mike@localhost demo]$
```

## Instructions 

Use the virtualenvs in the excercises, dont install python packages to the system-wide python location. 

