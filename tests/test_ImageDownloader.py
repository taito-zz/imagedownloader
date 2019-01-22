import unittest

from unittest import mock

import requests

from imagedownloader import ImageDownloader


class TestCase(unittest.TestCase):

    @mock.patch('imagedownloader.requests.get')
    def test_instance(self, get):
        html = """<html>
    <body>
        <img src="http://aaa.bbb.ccc/image1.jpg" />
        <img src="http://www.abc.com/image2.png" />
        <img src="/image3.png" />
        <img src="image4.png" />
        <img src="/image2.png" />
        <img src="image2.png" />
        <img src="../image5.png" />
    </body>
</html>
"""
        get().text = html
        instance = ImageDownloader('http://www.abc.com')
        self.assertEqual(instance.url, 'http://www.abc.com')
        self.assertIsNone(instance.path)
        self.assertEqual(instance.logger.name, 'imagedownloader')

    # @mock.patch('imagedownloader.requests.get')
    # def test_call(self, get):
    #     html = """<html>
    # <body>
    #     <img src="http://aaa.bbb.ccc/image1.jpg" />
    #     <img src="http://www.abc.com/image2.png" />
    #     <img src="/image3.png" />
    #     <img src="image4.png" />
    #     <img src="/image2.png" />
    #     <img src="image2.png" />
    #     <img src="../image5.png" />
    # </body>
# </html>
# """
    #     get().text = html
    #     instance = ImageDownloader('http://www.abc.com')
    #     instance()
        sources = {
            'http://aaa.bbb.ccc/image1.jpg',
            'http://www.abc.com/image2.png',
            'http://www.abc.com/image3.png',
            'http://www.abc.com/image4.png',
            'http://www.abc.com/image5.png',
        }
        self.assertEqual(instance.parser.sources, {
            'http://aaa.bbb.ccc/image1.jpg',
            'http://www.abc.com/image2.png',
            '/image3.png',
            'image4.png',
            '/image2.png',
            'image2.png',
            '../image5.png',
        })
        self.assertEqual(instance.sources, sources)

        instance = ImageDownloader('http://www.abc.com/aaa/')
        # instance()
        sources = {
            'http://aaa.bbb.ccc/image1.jpg',
            'http://www.abc.com/image2.png',
            'http://www.abc.com/image3.png',
            'http://www.abc.com/aaa/image2.png',
            'http://www.abc.com/aaa/image4.png',
            'http://www.abc.com/image5.png',
        }
        self.assertEqual(instance.sources, sources)

        instance = ImageDownloader('http://www.abc.com/aaa')
        # instance()
        sources = {
            'http://aaa.bbb.ccc/image1.jpg',
            'http://www.abc.com/image2.png',
            'http://www.abc.com/image3.png',
            'http://www.abc.com/image4.png',
            'http://www.abc.com/image5.png',
        }
        self.assertEqual(instance.sources, sources)

    def test_url_doesnot_exist(self):
        with self.assertRaises(requests.exceptions.ConnectionError):
            ImageDownloader('http://url.doesnot.exist')

    @mock.patch('imagedownloader.requests.get')
    @mock.patch('imagedownloader.urlretrieve')
    def test_call(self, urlretrieve, get):
        html = """<html>
    <body>
        <img src="http://aaa.bbb.ccc/image1.jpg" />
        <img src="http://www.abc.com/image2.png" />
        <img src="/image3.png" />
        <img src="image4.png" />
        <img src="/image2.png" />
        <img src="image2.png" />
        <img src="../image5.png" />
    </body>
</html>
"""
        get().text = html
        instance = ImageDownloader('http://www.abc.com')
        instance()
        self.assertEqual(urlretrieve.call_count, 5)
