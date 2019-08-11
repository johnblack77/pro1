from ctypes import *
dll = CDLL("libDemo.dylib")
print (dll.add(1, 102))