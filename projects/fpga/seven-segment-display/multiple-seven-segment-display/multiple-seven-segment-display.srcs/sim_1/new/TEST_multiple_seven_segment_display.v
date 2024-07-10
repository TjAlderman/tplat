`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/10/2024 10:45:30 PM
// Design Name: 
// Module Name: TEST_multiple_seven_segment_display
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


module TEST_multiple_seven_segment_display();

reg clk; 

initial begin 
    clk=0;
    forever #5 clk=~clk; //clock generation with period 10ns (100MHz)
end

wire [3:0] ssdAnode;
wire [6:0] ssdCathode;

multiple_seven_segment_display_TOP UUT (.clk(clk),.ssdAnode(ssdAnode),.ssdCathode(ssdCathode)); //instantiation of module to test

endmodule
