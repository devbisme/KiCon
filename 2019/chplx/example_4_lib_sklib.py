from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

example_4_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(name='PIC16F83-XXSO',dest=TEMPLATE,tool=SKIDL,description='PIC16F84, 1KB Flash, 68B SRAM, 64B EEPROM, SOIC18',keywords='Flash-Based 8-Bit Microcontroller',ref_prefix='U',num_units=1,fplist=['SO*'],do_erc=True,aliases=['PIC16F84-XXSO'],footprint='KiCad_V5/Package_SO.pretty:SOIC-18W_7.5x11.6mm_P1.27mm',pins=[
            Pin(num='1',name='RA2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='2',name='RA3',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='3',name='TOCKI/RA4',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='4',name='~MCLR~',func=Pin.types.INPUT,do_erc=True),
            Pin(num='5',name='VSS',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='6',name='INT/RB0',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='7',name='RB1',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='8',name='RB2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='9',name='RB3',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='10',name='RB4',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='11',name='RB5',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='12',name='RB6',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='13',name='RB7',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='14',name='VDD',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='15',name='OSC2/CLKOUT',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='16',name='OSC1/CLKIN',func=Pin.types.INPUT,do_erc=True),
            Pin(num='17',name='RA0',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='18',name='RA1',func=Pin.types.BIDIR,do_erc=True)]),
        Part(name='C',dest=TEMPLATE,tool=SKIDL,description='Unpolarized capacitor',keywords='cap capacitor',ref_prefix='C',num_units=1,fplist=['C_*'],do_erc=True,footprint='KiCad_V5/Capacitor_SMD.pretty:C_0805_2012Metric',pins=[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)]),
        Part(name='Crystal',dest=TEMPLATE,tool=SKIDL,description='Two pin crystal',keywords='quartz ceramic resonator oscillator',ref_prefix='Y',num_units=1,fplist=['Crystal*'],do_erc=True,footprint='KiCad_V5/Crystal.pretty:Crystal_SMD_0603-2Pin_6.0x3.5mm',pins=[
            Pin(num='1',name='1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='2',func=Pin.types.PASSIVE,do_erc=True)]),
        Part(name='LED',dest=TEMPLATE,tool=SKIDL,description='LED generic',keywords='led diode',ref_prefix='D',num_units=1,fplist=['LED*', 'LED_SMD:*', 'LED_THT:*'],do_erc=True,footprint='KiCad_V5/LED_SMD.pretty:LED_0805_2012Metric_Castellated',pins=[
            Pin(num='1',name='K',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.types.PASSIVE,do_erc=True)]),
        Part(name='D',dest=TEMPLATE,tool=SKIDL,description='Diode',keywords='diode',ref_prefix='D',num_units=1,fplist=['TO-???*', '*_Diode_*', '*SingleDiode*', 'D_*'],do_erc=True,footprint='KiCad_V5/Diode_SMD.pretty:D_0805_2012Metric',pins=[
            Pin(num='1',name='K',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.types.PASSIVE,do_erc=True)]),
        Part(name='SW_SPST',dest=TEMPLATE,tool=SKIDL,description='Single Pole Single Throw (SPST) switch',keywords='switch lever',ref_prefix='SW',num_units=1,do_erc=True,footprint='KiCad_V5/Button_Switch_SMD.pretty:SW_SPST_CK_RS282G05A3',pins=[
            Pin(num='1',name='A',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='B',func=Pin.types.PASSIVE,do_erc=True)])])