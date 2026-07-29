`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/08/2024 07:50:33 PM
// Design Name: 
// Module Name: single_seven_segment_display_TOP
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


module single_seven_segment_display_TOP(
    input wire clk,
    input wire reset,
    input wire enable,
    output wire [6:0] ssdCathode,
    output wire [3:0] ssdAnode
    );

// Instantiate 1 Hz clk    
wire beat;
clock_divider_HB hb1 (.clk(clk), .enable(enable), .reset(reset), .beat(beat));

// Increment counter every second
// Counter creates a sequence of digits to be display on SSD
reg [3:0] counter;
always @ (posedge clk) begin
    if ((reset == 1'b1) || (counter >= 4'd10)) begin
        counter <= 4'b0;
    end else if (beat == 1'b1) begin
        counter <= counter + 1'b1;
    end else begin
        counter <= counter;
    end
end

// Instatiate SSD decoder
seven_segment_decoder decoder (.bcd(counter), .ssd(ssdCathode));

// Define which of the four SSD digits to illuminate
assign ssdAnode = 4'b1110;

endmodule
