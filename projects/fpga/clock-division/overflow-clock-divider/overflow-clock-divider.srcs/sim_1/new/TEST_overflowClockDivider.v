`timescale 1ns / 1ps



module TEST_overflowClockDivider(
    );
    
reg clk; 

initial begin 
    clk = 0;
    forever #5 clk=~clk; //clock generation with period 10ns (100MHz)
end

reg reset, enable;
wire dclk;

overflow_clock_divider UUT (.clk(clk),.reset(reset),.enable(enable),.dividedClk(dclk)); //instantiation of module to test

initial begin // simulation inputs to block
    reset=0;
    enable=0;
    #7 reset = 1; //assert reset earlier to reduce the length of unkown in output
    #24 enable = 1;
    #5 reset = 0;
end

endmodule
