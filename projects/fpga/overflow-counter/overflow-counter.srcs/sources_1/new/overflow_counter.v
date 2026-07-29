`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/06/2024 01:15:58 PM
// Design Name: 
// Module Name: overflow_counter
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


module overflow_counter(
    input wire clk,
    input wire reset,
    input wire enable,
    output wire [15:0] led
    );
    
reg [31:0] counter;

always @(posedge clk) begin
    if (reset == 1'b1) begin
        counter <= 32'd0;
     end else if (enable == 1'b1) begin
        counter <= counter + 1'b1;
     end else begin
        counter <= counter; // Redundant line to make sure procedural block covers all conditions (good practice)
     end
end

assign led = counter[31:16]; // Assign the 16 MSB of counter to led

endmodule
