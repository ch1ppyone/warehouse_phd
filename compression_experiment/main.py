import os
import bz2
import lzma
import zlib
import matplotlib.pyplot as plt

methods = ['Uncompressed',  'bzip2', 'LZMA2', 'Deflate']
sizes = []

fp = open("test.avi","rb")
sizes.append(os.path.getsize('test.avi') >> 20);

data = fp.read()
bindata = bytearray(data)


#bzip2
print("Create bzip2...")
bzip2 = bz2.compress(bindata, 9)
open("test.mp4.bzip2", 'wb').write(bzip2)
print("bzip2 created!")
sizes.append(os.path.getsize('test.mp4.bzip2') >> 20);

#LZMA2
print("Create LZMA2...")
xz = lzma.compress(bindata)
open("test.mp4.xz", 'wb').write(xz)
print("LZMA2 created!")
sizes.append(os.path.getsize('test.mp4.xz') >> 20);

#deflate
print("Create Deflate...")
deflate = zlib.compress(bindata, 5)
open("test.mp4.deflate", 'wb').write(deflate)
print("Deflate created!")
sizes.append(os.path.getsize('test.mp4.deflate') >> 20);

fp.close()

plt.bar(methods, sizes)
plt.show()

