#!/usr/bin/python
# -*- coding: utf-8 -*-
import qrcode
from optparse import OptionParser
import sys

parser = OptionParser()
parser.add_option('-d', '--data', dest='data', help='data to be processed')

white_block = '\033[0;37;47m  '
black_block = '\033[0;37;40m  '
new_line = '\033[0m\n'

def main():
    (options, args) = parser.parse_args()
    if not options.data:
        print 'data must be specified. see %s -h' % sys.argv[0]
    else:
        qr = qrcode.QRCode(version=5)
        qr.add_data(options.data)
        qr.make()
        output = ''
        output += new_line
        output += white_block*(qr.modules_count+2) + new_line
        for r in range(qr.modules_count):
            output += white_block
            for c in range(qr.modules_count):
                if qr.modules[r][c]:
                    output += black_block
                else:
                    output += white_block
            output += white_block + new_line
        output += white_block*(qr.modules_count+2) + new_line
        print output

if __name__ == '__main__':
    main()
