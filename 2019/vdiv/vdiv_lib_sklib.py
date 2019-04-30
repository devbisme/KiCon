from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

vdiv_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(name='R',dest=TEMPLATE,tool=SKIDL,keywords='r res resistor',description='Resistor',ref_prefix='R',num_units=1,fplist=['R_*'],do_erc=True,footprint='KiCad_V5/Resistor_SMD.pretty:R_0805_2012Metric',pins=[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)]),
        Part(name='PIC10F220-IP',dest=TEMPLATE,tool=SKIDL,keywords='FLASH 8-Bit CMOS Microcontroller',description='512W Flash, 24B SRAM, PDIP8',ref_prefix='U',num_units=1,fplist=['DIP*8*W7.62mm*'],do_erc=True,aliases=['PIC10F222-IP'],footprint='KiCad_V5/Package_DIP.pretty:DIP-8_W7.62mm',pins=[
            Pin(num='2',name='VDD',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='3',name='GP2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='4',name='GP1',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='5',name='GP0',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='7',name='VSS',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='8',name='GP3',func=Pin.types.INPUT,do_erc=True)])])