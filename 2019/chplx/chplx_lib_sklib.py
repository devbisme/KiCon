from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

chplx_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(name='LED',dest=TEMPLATE,tool=SKIDL,keywords='led diode',description='LED generic',ref_prefix='D',num_units=1,fplist=['LED*', 'LED_SMD:*', 'LED_THT:*'],do_erc=True,pins=[
            Pin(num='1',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.PASSIVE,do_erc=True)])])