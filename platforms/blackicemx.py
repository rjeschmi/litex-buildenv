from litex.build.generic_platform import *
from litex.build.lattice import LatticePlatform
from litex.build.lattice.programmer import IceStormProgrammer


_io = [
    ("user_led",    0, Pins("49"), IOStandard("LVCMOS33")),
    ("user_led",    1, Pins("52"), IOStandard("LVCMOS33")),
    ("user_led",    2, Pins("55"), IOStandard("LVCMOS33")),
    ("user_led",    3, Pins("56"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("rx", Pins("62")),
        Subsignal("tx", Pins("61"), Misc("PULLUP")),
        IOStandard("LVCMOS33")
    ),

    ("spiflash2x", 0,
        Subsignal("dcs",      Pins("75"), IOStandard("LVCMOS33")),
        Subsignal("dclk",       Pins("76"), IOStandard("LVCMOS33")),
        Subsignal("io0",      Pins("73"), IOStandard("LVCMOS33")),
        Subsignal("io1",       Pins("74"), IOStandard("LVCMOS33")),
        
    ),

    ("spiflash4x", 0,
        Subsignal("miso",      Pins("68"), IOStandard("LVCMOS33")),
        Subsignal("mosi",      Pins("67"), IOStandard("LVCMOS33")),
        Subsignal("wp",      Pins("64"), IOStandard("LVCMOS33")),
        Subsignal("hold", Pins("63"), IOStandard("LVCMOS33")),
        Subsignal("ss", Pins("71"), IOStandard("LVCMOS33")),
        Subsignal("sck",  Pins("70"), IOStandard("LVCMOS33")),
    ),

    ("clk", 0, Pins("60"), IOStandard("LVCMOS33")) # 25Mhz oscillator on board
]

_connectors = [
    ("PMOD1", "38 37 32 31"),
    ("PMOD2", "34 33 29 28"),
    ("PMOD3", "18 17 12 11"),
    ("PMOD4", "16 15 10 9"),
    ("PMOD5", "136 137 134 135"),
    ("PMOD6", "141 142 138 139"),
    ("PMOD7", "1 2 7 8"),
    ("PMOD8", "143 144 3 4"),
    ("PMOD9", "106 105 101 99"),
    ("PMOD10", "104 102 49 52"),
    ("PMOD11", "19 20 23 24"),
    ("PMOD12", "21 22 25 26"),
]



class Platform(LatticePlatform):
    default_clk_name = "clk"
    default_clk_period = 25

    gateware_size = 0x20000


    def __init__(self):
        LatticePlatform.__init__(self, "ice40-hx4k-tqfp144", _io, _connectors,
                                 toolchain="icestorm")

    def create_programmer(self):
        return IceStormProgrammer()
