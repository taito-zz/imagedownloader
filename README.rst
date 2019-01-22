This package provides a image downloader against url.

This package is developed for python-3.6, so within this package, run::

   virtualenv -p $(which python3.6) .
   ./bin/python setup.py install

Now you can run::

   ./bin/downloadimages -h

Example::

   mkdir -p ~/Downloads/varjo
   ./bin/downloadimages -u https://varjo.com/ -p ~/Downloads/varjo
