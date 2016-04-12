from GoodFETARM9 import *

"""


"""
#
# Base Memory Addresses
#
FLASH_BASE =    0x100000
TCx_BASE =      0xfffa0000      # Timer/Counter
UDP_BASE =      0xfffa4000      # USB Device Port
TWI_BASE =      0xfffac000      # Two-Wire-Interface Controller
USART0_BASE =   0xfffb0000      # Universal Syncronous/Asyncronous Receiver/Transmitter 0
USART1_BASE =   0xfffb4000      # Universal Syncronous/Asyncronous Receiver/Transmitter 1
#PWMC_BASE =     0xfffcc000      # PWM Controller
SSC_BASE =      0xfffbc000      # Syncronous Serial Controller
ADC_BASE =      0xfffe0000      # Analog-Digital Converter
SPI_BASE =      0xfffc8000      # Serial Peripheral Interface
SYSC_BASE =     0xffffc000      # System
AIC_BASE =      0xfffff000      # Advanced Interrupt Controller
DBGU_BASE =     0xfffff200      # Debug unit
PIOA_BASE =     0xfffff400      # Programmable IO
PMC_BASE =      0xfffffc00      # Power Management Controller
RSTC_BASE =     0xfffffd00      # Reset Controller
RTT_BASE =      0xfffffd20      # Real-Time Timer
PIT_BASE =      0xfffffd30      # Periodic Interval Timer
WDT_BASE =      0xfffffd40      # Watchdog Timer
#VREG_BASE =     0xfffffd60      # Voltage Regulator
#MC_BASE =       0xffffff00      # Memory Controller

PERIPHERAL_BASE=0xf0000000
PERIPH0_BASE =  0xf0004000
PERIPH1_BASE =  0xf0008000
# etc...


class GoodFETAT91SAM9G20(GoodFETARM9):
    def getChipID(self):
        chipid = self.ARMreadMem(SF_CIDR,1)
        return chipid[0]

    def FFPI_Read(self):
        raise Exception("Not implemented yet...")
    def FFPI_PageProgram(self):
        raise Exception("Not implemented yet...")
    def FFPI_PageErase(self):
        raise Exception("Not implemented yet...")
    def FFPI_FullErase(self):
        raise Exception("Not implemented yet...")
    def FFPI_Lock(self):
        raise Exception("Not implemented yet...")
    def FFPI_Unlock(self):
        raise Exception("Not implemented yet...")
    def FFPI_Protect(self):
        raise Exception("Not implemented yet...")

# todo:
# * Test Pin, SAM-BA, Tri-state
# 
