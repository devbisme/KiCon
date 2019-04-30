EESchema Schematic File Version 4
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MCU_Microchip_PIC10:PIC10F200-IP U1
U 1 1 5C66B078
P 5550 3575
F 0 "U1" H 5100 4175 50  0000 C CNN
F 1 "PIC10F200-IP" H 5125 4075 50  0000 C CNN
F 2 "Package_DIP:DIP-8_W7.62mm" H 5600 4225 50  0001 L CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/41239D.pdf" H 5550 3575 50  0001 C CNN
	1    5550 3575
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5C66B787
P 4450 2975
F 0 "R1" H 4520 3021 50  0000 L CNN
F 1 "R" H 4520 2930 50  0000 L CNN
F 2 "" V 4380 2975 50  0001 C CNN
F 3 "~" H 4450 2975 50  0001 C CNN
	1    4450 2975
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5C66BB81
P 4450 3900
F 0 "R2" H 4520 3946 50  0000 L CNN
F 1 "R" H 4520 3855 50  0000 L CNN
F 2 "" V 4380 3900 50  0001 C CNN
F 3 "~" H 4450 3900 50  0001 C CNN
	1    4450 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	4450 2825 4450 2575
Wire Wire Line
	5550 4175 5550 4275
Wire Wire Line
	5550 2975 5550 2725
Text Label 4450 2575 0    50   ~ 0
Vin
Text Label 5550 2725 0    50   ~ 0
Vdd
Text Label 4450 4600 0    50   ~ 0
GND
Wire Wire Line
	4450 4050 4450 4275
Wire Wire Line
	4450 3125 4450 3475
Wire Wire Line
	4950 3475 4450 3475
Connection ~ 4450 3475
Wire Wire Line
	4450 3475 4450 3750
Wire Wire Line
	5550 4275 4450 4275
Connection ~ 4450 4275
Wire Wire Line
	4450 4275 4450 4600
$EndSCHEMATC
