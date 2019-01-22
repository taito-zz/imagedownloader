================
Image Downloader
================

This package provides a command to download images from url.
With that command, html from the url is parsed, fetching value of ``src`` attribute from ``img`` tags.
It attempts to download those images.

This package is developed for python-3.6, so within this package, run::

   virtualenv -p $(which python3.6) .
   ./bin/python setup.py install

Now you can run::

   ./bin/downloadimages -h

Example::

   mkdir -p ~/Downloads/varjo
   ./bin/downloadimages -u https://varjo.com/ -p ~/Downloads/varjo

Running the test::

   ./bin/python setup.py test
