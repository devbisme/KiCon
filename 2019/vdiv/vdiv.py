from skidl import *

vdd = Net('Vdd')
gnd = Net('GND')
vin = Net('Vin')

#r1 = Part('device','R',value='4.7K')
r1 = Part('device','R',value='4.7K',footprint='KiCad_V5/Resistor_SMD.pretty:R_0805_2012Metric')
r2 = r1(value='2.2K')
vin += r1[1]
r1[2] += r2[1]
r2[2] += gnd

# uc = Part('MCU_Microchip_PIC10',
          # 'PIC10F220-IP')
uc = Part('MCU_Microchip_PIC10',
          'PIC10F220-IP', footprint='KiCad_V5/Package_DIP.pretty:DIP-8_W7.62mm')
uc['VDD'] += vdd
uc['VSS'] += gnd
uc['gp0'] += r2[1]

ERC()
generate_netlist()
