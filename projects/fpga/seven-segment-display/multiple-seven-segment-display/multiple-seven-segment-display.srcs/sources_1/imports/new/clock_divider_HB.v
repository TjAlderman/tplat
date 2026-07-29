`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/07/2024 09:01:55 PM
// Design Name: 
// Module Name: clock_divider_HB
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


module clock_divider_HB (
    input wire clk,
    input wire enable,
    input wire reset,
    output reg dividedClk,
    output wire beat
    );
    
reg [31:0] counter;
parameter THRESHOLD = 50_000; // Generate 1 kHz divided clk

always @(posedge clk) begin
    if (reset == 1'b1 || counter >= THRESHOLD-1) begin
        counter <= 32'd0;
    end else if (enable == 1'b1) begin
        counter <= counter + 1'b1;
    end
end

always @(posedge clk) begin
    if (reset == 1'b1) begin
        dividedClk <= 1'b0;
    end else if (counter >= THRESHOLD-1) begin
        dividedClk <= ~dividedClk;
    end
end

assign beat=(counter==THRESHOLD-1)&(dividedClk);

endmodule
