import os

from setuptools import find_packages
from setuptools import setup


def read_file(name):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir_path, name)) as opened_file:
        return opened_file.read().strip()


version = read_file('version.txt')
description = read_file('README.rst')

setup(
    name='imagedownloader',
    version=version,
    description=description,
    long_description='',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='',
    license='BSD-3 clause',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    downloadimages=imagedownloader:downloadimages
    """
)
