import os,sys
import libvirt

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from host import vmmhost 
from vm import vm

cvm = vm()
conn = libvirt.open("qemu:///system")
chost = vmmhost('123123', conn)
ret = chost.get_hw_info()
print ret

#print ret
