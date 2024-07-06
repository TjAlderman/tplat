`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/04/2024 10:54:34 PM
// Design Name: 
// Module Name: mux_with_delays
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


module mux_with_delays(
    input wire X,
    input wire Y,
    input wire S,
    output wire Z
    );

// Instantiate intermediate signals
wire A, B, C, D;
// Define intermediate signals and give them delay of #5 timescale steps (i.e. 5ns)
// Delay parameters are only relevant in simulation. Once a design is implemented in hardware,
// actual signal delays will be determined by the physics of the microchip and cannot be set
// programmatically.
assign #5 C = (~S);
assign #5 A = X & S;
assign #5 B = Y & C;
assign #5 D = X & Y;
assign #5 Z = A | B | D;
endmodule
