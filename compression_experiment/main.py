import os
import gzip
import bz2
import lzma
import zlib
import matplotlib.pyplot as plt

methods = ['Uncompressed', 'gzip', 'bzip2', 'xz', 'deflate']
sizes = []

fp = open("test.avi","rb")
sizes.append(os.path.getsize('test.avi') >> 20);

data = fp.read()
bindata = bytearray(data)


#gzip
print("Create gzip...")
with gzip.open("test.mp4.gz", "wb") as f:
    f.write(bindata)
print("gzip created!")

sizes.append(os.path.getsize('test.mp4.gz') >> 20);

#bzip2
print("Create bzip2...")
bzip2 = bz2.compress(bindata, 9)
open("test.mp4.bzip2", 'wb').write(bzip2)
print("bzip2 created!")
sizes.append(os.path.getsize('test.mp4.bzip2') >> 20);

#xz
print("Create xz...")
xz = lzma.compress(bindata)
open("test.mp4.xz", 'wb').write(xz)
print("xz created!")
sizes.append(os.path.getsize('test.mp4.xz') >> 20);

#deflate
print("Create deflate...")
deflate = zlib.compress(bindata, 5)
open("test.mp4.deflate", 'wb').write(deflate)
print("deflate created!")
sizes.append(os.path.getsize('test.mp4.deflate') >> 20);

fp.close()

plt.bar(methods, sizes)
plt.show()

