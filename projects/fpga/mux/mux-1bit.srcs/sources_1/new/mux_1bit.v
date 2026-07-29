`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/04/2024 09:43:04 PM
// Design Name: 
// Module Name: mux_1bit
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


module mux_1bit(
    input wire X,
    input wire Y,
    input wire S,
    output wire Z
    );
    
assign Z = (X & S) | (Y & (~S));
    
endmodule
