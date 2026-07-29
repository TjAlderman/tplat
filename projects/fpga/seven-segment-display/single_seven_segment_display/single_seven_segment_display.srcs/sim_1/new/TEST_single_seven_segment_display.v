`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/08/2024 08:53:56 PM
// Design Name: 
// Module Name: TEST_single_seven_segment_display
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module TEST_single_seven_segment_display();

reg clk; 

initial begin 
    clk=0;
    forever #5 clk=~clk; //clock generation with period 10ns (100MHz)
end

reg reset, enable;
wire [3:0] ssdAnode;
wire [6:0] ssdCathode;

single_seven_segment_display_TOP UUT (.clk(clk),.reset(reset),.enable(enable),.ssdAnode(ssdAnode),.ssdCathode(ssdCathode)); //instantiation of module to test

initial begin
    reset = 1; // assert reset at beginning 
    enable = 0;
    #100 enable = 1;
    #20 reset = 0;
end

endmodule
