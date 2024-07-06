`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/04/2024 09:46:48 PM
// Design Name: 
// Module Name: TB_mux_1bit
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


module TB_mux_1bit;

// Inputs to UUT
    reg X;
    reg S;
    reg Y;

// Output to UUT
    wire Z;
    
// Instantiate the design to be tested
    mux_with_delays UUT(
        .X(X),
        .S(S),
        .Y(Y),
        .Z(Z)
    );

// Duration of simulation. Set to 300 timesteps. 
    initial begin: stopat
        #300; $finish;
    end

// Signal changes: #xx means enact change after xx timestamps
    initial begin
        X = 1'b0;
        Y = 1'b1;
        S = 1'b1;
        
        // After 30ns, flip X to 0
        #30X = 1'b1;
        // After another 30ns, flip S to 1
        #30S = 1'b0;
        // etc.
        #30Y = 1'b0;
        
        #30X = 1'b0;
        #30Y = 1'b1;
        #30S = 1'b1;
        
        #30X = 1'b1;
        #30Y = 1'b0;
        #30S = 1'b0;
    end
endmodule