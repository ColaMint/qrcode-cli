#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='qrcode_cli',
    version='0.1',
    url='https://github.com/lincolnloop/python-qrcode',
    description='QR Code shell generator',
    license='MIT',
    author='Everley',
    author_email='463785757@qq.com',
    platforms=['any'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'qrcode-cli= qrcode_cli.main:main',
        ],
    },
    install_requires=['Pillow', 'qrcode'],
    include_package_data=True,
)
