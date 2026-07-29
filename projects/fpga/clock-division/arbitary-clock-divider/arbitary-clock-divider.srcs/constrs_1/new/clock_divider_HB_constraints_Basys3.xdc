set_property -dict { PACKAGE_PIN U16   IOSTANDARD LVCMOS33 } [get_ports dividedClk]
set_property -dict { PACKAGE_PIN E19   IOSTANDARD LVCMOS33 } [get_ports beat]

set_property -dict { PACKAGE_PIN W5    IOSTANDARD LVCMOS33 } [get_ports clk]
create_clock -period 10.00 [get_ports clk]

set_property -dict { PACKAGE_PIN V17   IOSTANDARD LVCMOS33 } [get_ports enable]
set_property -dict { PACKAGE_PIN U18   IOSTANDARD LVCMOS33 } [get_ports reset]