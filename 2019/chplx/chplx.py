from skidl import *

b = Bus('chplx', 4)
for hi in b:
    for lo in b:
        if hi != lo:
            led = Part('device','LED')
            hi += led['A']
            lo += led['K']

ERC()
generate_netlist()
