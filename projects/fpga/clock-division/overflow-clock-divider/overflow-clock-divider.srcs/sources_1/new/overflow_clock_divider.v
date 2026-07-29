`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/06/2024 02:06:29 PM
// Design Name: 
// Module Name: overflow_clock_divider
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


module overflow_clock_divider(
    input wire clk,
    input wire reset,
    input wire enable,
    output wire dividedClk
);
    
reg [26:0] counter; // Instantiate 27-bit overflow counter

always @(posedge clk) begin
    if (reset == 1'b1) begin
        counter <= 27'd0;
    end else if (enable == 1'b1) begin
        counter <= counter + 1'b1;
    end
end
    
assign dividedClk = counter[26]; // Assign the divided clock to be the MSB of the overflow counter
    
endmodule
