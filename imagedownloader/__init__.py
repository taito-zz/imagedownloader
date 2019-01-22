import argparse
import logging
import os

from html.parser import HTMLParser
from logging.config import dictConfig
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlretrieve

import requests


class HtmlParser(HTMLParser):

    sources = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            try:
                self.sources.add(dict(attrs)['src'])
            except KeyError:
                pass


class ImageDownloader(object):
    """
    :param str url: URLwhere image will be fetched form
    :param str path: Directory path where images will be download
    """

    def __init__(self, url="", path=None, logger=None):
        if logger is None:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.url = url
        self.path = path
        self.parser = HtmlParser()
        self.sources = set()
        response = requests.get(self.url)
        self.parser.feed(response.text)
        for src in self.parser.sources:
            parsed = urlparse(src)
            if not parsed.query:
                if not parsed.scheme:
                    src = urljoin(self.url, src)
                self.sources.add(src)

    def __call__(self):
        """Download"""
        if self.path is None:
            base_path = os.getcwd()
        else:
            base_path = self.path
        for src in self.sources:
            self.logger.info('Fetching image from {}'.format(src))
            dest = os.path.join(base_path, os.path.basename(src))
            urlretrieve(src, dest)


def downloadimages():
    parser = argparse.ArgumentParser(description='Download images from single webpage(url)')
    parser.add_argument(
        '-u', '--url',
        required=True,
        help='URL where image sources will be fetched from',
    )
    parser.add_argument(
        '-p', '--path',
        required=False,
        help='Directory path where images will be downloaded',
    )
    args = parser.parse_args()

    # Logging
    logger = logging.getLogger(__name__)
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'imagedownloader': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'INFO',
            },
        },
    }

    dictConfig(LOGGING)

    downloader = ImageDownloader(url=args.url, path=args.path, logger=logger)
    return downloader()
