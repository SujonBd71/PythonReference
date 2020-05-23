from ctypes import cdll
from ctypes import CFUNCTYPE
import ctypes
# mydll = cdll.LoadLibrary('test.dll')
mydll = cdll.LoadLibrary('dll_proj3.dll')
print(mydll)
print(mydll.sum)
print(mydll.sum_cb)

sm = mydll.sum(5, 10)
print(sm)

mydll.sum_cb(50, 10, None)


def sum_pycb(s):
    print(s)


callback_type = CFUNCTYPE(None, ctypes.c_int )
cb = callback_type(sum_pycb)
mydll.sum_cb(10, 20, cb)



