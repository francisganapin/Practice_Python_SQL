import struct

data = struct.pack('if',1,2.5)
print(data)


i, f = struct.unpack('if',data)
print(i,f)