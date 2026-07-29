`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/04/2024 10:34:57 PM
// Design Name: 
// Module Name: full_adder_1bit
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


module full_adder_1bit(
    input wire X,
    input wire Y,
    input wire C_in,
    output wire Z,
    output wire C_out
    );

assign Z = (X&(~Y)&(~C_in)) | ((~X)&Y&(~C_in)) | ((~X)&(~Y)&C_in) | (X&Y&C_in);
assign C_out = (X&Y) | (X&C_in) | (Y&C_in);
    
endmodule
