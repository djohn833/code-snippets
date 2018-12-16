import bz2
import gzip
import lzma
from zipfile import *

# Repeatedly unwraps XZ, GZip, and BZip2 encoded files
def unwrap_file(filename):
    x = open(filename, 'rb')
    while True:
        header = x.read(6)
        x.seek(0)
        if header.startswith(b'\xfd7zXZ\x00'):
            x = lzma.open(x, 'r')
        elif header.startswith(b'\x1F\x8B'):
            x = gzip.open(x, 'r')
        elif header.startswith(b'\x42\x5A\x68'):
            x = bz2.open(x, 'r')
        else:
            return x

z = ZipFile('asdfasdf')

# Repeatedly unzip nested zips.
while True:
    for name in z.namelist():
        z.extract(name)
        if is_zipfile(name):
            z.close()
            z = ZipFile(name)
            break
    else:
        break
