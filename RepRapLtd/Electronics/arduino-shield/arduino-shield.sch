EESchema Schematic File Version 4
EELAYER 30 0
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
L arduino-shield-rescue:Arduino_UNO_R3_Shield-reprapltd-kicad A1
U 1 1 60BE011A
P 3750 4375
F 0 "A1" H 3750 5556 50  0000 C CNN
F 1 "Arduino_UNO_R3_Shield" H 3750 5465 50  0000 C CNN
F 2 "reprapltd-kicad:Arduino_UNO_R3_Shield" H 3750 4375 50  0001 C CIN
F 3 "https://www.arduino.cc/en/Main/arduinoBoardUno" H 3750 4375 50  0001 C CNN
	1    3750 4375
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J1
U 1 1 60BE17C9
P 5350 3575
F 0 "J1" H 5430 3617 50  0000 L CNN
F 1 "Conn_01x03" H 5430 3526 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5350 3575 50  0001 C CNN
F 3 "~" H 5350 3575 50  0001 C CNN
	1    5350 3575
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J2
U 1 1 60BE1C74
P 5350 3925
F 0 "J2" H 5430 3967 50  0000 L CNN
F 1 "Conn_01x03" H 5430 3876 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5350 3925 50  0001 C CNN
F 3 "~" H 5350 3925 50  0001 C CNN
	1    5350 3925
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J3
U 1 1 60BE2BFA
P 5350 4275
F 0 "J3" H 5430 4317 50  0000 L CNN
F 1 "Conn_01x03" H 5430 4226 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5350 4275 50  0001 C CNN
F 3 "~" H 5350 4275 50  0001 C CNN
	1    5350 4275
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J4
U 1 1 60BE2FF9
P 5350 4625
F 0 "J4" H 5430 4667 50  0000 L CNN
F 1 "Conn_01x03" H 5430 4576 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5350 4625 50  0001 C CNN
F 3 "~" H 5350 4625 50  0001 C CNN
	1    5350 4625
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J5
U 1 1 60BE33C8
P 5350 4975
F 0 "J5" H 5430 5017 50  0000 L CNN
F 1 "Conn_01x03" H 5430 4926 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5350 4975 50  0001 C CNN
F 3 "~" H 5350 4975 50  0001 C CNN
	1    5350 4975
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J6
U 1 1 60BE38CE
P 5350 5325
F 0 "J6" H 5430 5367 50  0000 L CNN
F 1 "Conn_01x03" H 5430 5276 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5350 5325 50  0001 C CNN
F 3 "~" H 5350 5325 50  0001 C CNN
	1    5350 5325
	1    0    0    -1  
$EndComp
Wire Wire Line
	5150 3675 4650 3675
Wire Wire Line
	4650 3675 4650 4375
Wire Wire Line
	4650 4375 4250 4375
Wire Wire Line
	5150 4025 4725 4025
Wire Wire Line
	4725 4025 4725 4475
Wire Wire Line
	4725 4475 4250 4475
Wire Wire Line
	5150 4375 4800 4375
Wire Wire Line
	4800 4375 4800 4575
Wire Wire Line
	4800 4575 4250 4575
Wire Wire Line
	5150 4725 4800 4725
Wire Wire Line
	4800 4725 4800 4675
Wire Wire Line
	4800 4675 4250 4675
Wire Wire Line
	5150 5075 4725 5075
Wire Wire Line
	4725 5075 4725 4775
Wire Wire Line
	4725 4775 4250 4775
Wire Wire Line
	5150 5425 4625 5425
Wire Wire Line
	4625 5425 4625 4875
Wire Wire Line
	4625 4875 4250 4875
Wire Wire Line
	3850 5475 3850 5550
Wire Wire Line
	3850 5550 3800 5550
Wire Wire Line
	3750 5550 3750 5475
Wire Wire Line
	3650 5475 3650 5550
Wire Wire Line
	3650 5550 3750 5550
Connection ~ 3750 5550
$Comp
L power:+5V #PWR0101
U 1 1 60BE6A92
P 3950 3100
F 0 "#PWR0101" H 3950 2950 50  0001 C CNN
F 1 "+5V" H 3965 3273 50  0000 C CNN
F 2 "" H 3950 3100 50  0001 C CNN
F 3 "" H 3950 3100 50  0001 C CNN
	1    3950 3100
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0102
U 1 1 60BE6F96
P 5075 3225
F 0 "#PWR0102" H 5075 3075 50  0001 C CNN
F 1 "+5V" H 5090 3398 50  0000 C CNN
F 2 "" H 5075 3225 50  0001 C CNN
F 3 "" H 5075 3225 50  0001 C CNN
	1    5075 3225
	1    0    0    -1  
$EndComp
Wire Wire Line
	3950 3375 3950 3100
Wire Wire Line
	5150 3475 5075 3475
Wire Wire Line
	5075 3475 5075 3225
Wire Wire Line
	5150 3825 5075 3825
Wire Wire Line
	5075 3825 5075 3475
Connection ~ 5075 3475
Wire Wire Line
	5150 4175 5075 4175
Wire Wire Line
	5075 4175 5075 3825
Connection ~ 5075 3825
Wire Wire Line
	5150 4525 5075 4525
Wire Wire Line
	5075 4525 5075 4175
Connection ~ 5075 4175
Wire Wire Line
	5150 4875 5075 4875
Wire Wire Line
	5075 4875 5075 4525
Connection ~ 5075 4525
Wire Wire Line
	5150 5225 5075 5225
Wire Wire Line
	5075 5225 5075 4875
Connection ~ 5075 4875
$Comp
L power:GND #PWR0103
U 1 1 60BE9E81
P 3800 5700
F 0 "#PWR0103" H 3800 5450 50  0001 C CNN
F 1 "GND" H 3805 5527 50  0000 C CNN
F 2 "" H 3800 5700 50  0001 C CNN
F 3 "" H 3800 5700 50  0001 C CNN
	1    3800 5700
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 60BEA35A
P 4975 5600
F 0 "#PWR0104" H 4975 5350 50  0001 C CNN
F 1 "GND" H 4980 5427 50  0000 C CNN
F 2 "" H 4975 5600 50  0001 C CNN
F 3 "" H 4975 5600 50  0001 C CNN
	1    4975 5600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 5700 3800 5550
Connection ~ 3800 5550
Wire Wire Line
	3800 5550 3750 5550
Wire Wire Line
	5150 5325 4975 5325
Wire Wire Line
	4975 5325 4975 5600
Wire Wire Line
	4975 5325 4975 4975
Wire Wire Line
	4975 4975 5150 4975
Connection ~ 4975 5325
Wire Wire Line
	4975 4975 4975 4625
Wire Wire Line
	4975 4625 5150 4625
Connection ~ 4975 4975
Wire Wire Line
	4975 4625 4975 4275
Wire Wire Line
	4975 4275 5150 4275
Connection ~ 4975 4625
Wire Wire Line
	4975 4275 4975 3925
Wire Wire Line
	4975 3925 5150 3925
Connection ~ 4975 4275
Wire Wire Line
	4975 3925 4975 3575
Wire Wire Line
	4975 3575 5150 3575
Connection ~ 4975 3925
$Comp
L Connector_Generic:Conn_01x02 J9
U 1 1 60BE4CB8
P 2750 3750
F 0 "J9" V 2714 3562 50  0000 R CNN
F 1 "Conn_01x02" V 2623 3562 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2750 3750 50  0001 C CNN
F 3 "~" H 2750 3750 50  0001 C CNN
	1    2750 3750
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J8
U 1 1 60BE5F6E
P 2375 3750
F 0 "J8" V 2339 3562 50  0000 R CNN
F 1 "Conn_01x02" V 2248 3562 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2375 3750 50  0001 C CNN
F 3 "~" H 2375 3750 50  0001 C CNN
	1    2375 3750
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J7
U 1 1 60BE658F
P 2025 3750
F 0 "J7" V 1989 3562 50  0000 R CNN
F 1 "Conn_01x02" V 1898 3562 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2025 3750 50  0001 C CNN
F 3 "~" H 2025 3750 50  0001 C CNN
	1    2025 3750
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2850 3950 2850 3975
Wire Wire Line
	2850 3975 3250 3975
Wire Wire Line
	2475 3950 2475 4075
Wire Wire Line
	2475 4075 3250 4075
Wire Wire Line
	2125 3950 2125 4175
Wire Wire Line
	2125 4175 3250 4175
Wire Wire Line
	2750 3950 2750 4025
Wire Wire Line
	2750 4025 2375 4025
Wire Wire Line
	2375 4025 2375 3950
Wire Wire Line
	2375 4025 2025 4025
Wire Wire Line
	2025 4025 2025 3950
Connection ~ 2375 4025
$Comp
L power:GND #PWR0105
U 1 1 60BED2CC
P 2025 4275
F 0 "#PWR0105" H 2025 4025 50  0001 C CNN
F 1 "GND" H 2030 4102 50  0000 C CNN
F 2 "" H 2025 4275 50  0001 C CNN
F 3 "" H 2025 4275 50  0001 C CNN
	1    2025 4275
	1    0    0    -1  
$EndComp
Wire Wire Line
	2025 4025 2025 4275
Connection ~ 2025 4025
$Comp
L Device:R_Small R1
U 1 1 60BEF562
P 2950 5200
F 0 "R1" H 3009 5246 50  0000 L CNN
F 1 "180R" H 3009 5155 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 2950 5200 50  0001 C CNN
F 3 "~" H 2950 5200 50  0001 C CNN
	1    2950 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3250 5075 2950 5075
Wire Wire Line
	2950 5075 2950 5100
$Comp
L Connector_Generic:Conn_01x02 J10
U 1 1 60BF1843
P 2750 5525
F 0 "J10" H 2668 5200 50  0000 C CNN
F 1 "Conn_01x02" H 2668 5291 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2750 5525 50  0001 C CNN
F 3 "~" H 2750 5525 50  0001 C CNN
	1    2750 5525
	-1   0    0    1   
$EndComp
Wire Wire Line
	2950 5300 2950 5425
$Comp
L power:GND #PWR0106
U 1 1 60BF35E8
P 2950 5650
F 0 "#PWR0106" H 2950 5400 50  0001 C CNN
F 1 "GND" H 2955 5477 50  0000 C CNN
F 2 "" H 2950 5650 50  0001 C CNN
F 3 "" H 2950 5650 50  0001 C CNN
	1    2950 5650
	1    0    0    -1  
$EndComp
Wire Wire Line
	2950 5525 2950 5650
$EndSCHEMATC
