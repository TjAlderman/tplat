`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/10/2024 10:15:31 PM
// Design Name: 
// Module Name: multiple_seven_segment_display_TOP
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


module multiple_seven_segment_display_TOP(
    input wire clk,
    output wire [6:0] ssdCathode,
    output reg [3:0] ssdAnode
    );

// 1kHz signal to drive display selection
wire beat;
clock_divider_HB hb1 (.clk(clk), .enable(1'b1), .reset(1'b0), .beat(beat));

// 2-bit overflow counter to cycle through SSD displays
reg [1:0] activeDisplay;
always @ (posedge beat) begin
    activeDisplay <= activeDisplay + 1'b1;
end

// Display logic
reg [3:0] ssdValue;
always @(*) begin
    case(activeDisplay)
        2'd0 : begin
            ssdValue = 4'd4;
            ssdAnode = 4'b0111;
        end
        2'd1 : begin
            ssdValue = 4'd2;
            ssdAnode = 4'b1011;
        end
        2'd2 : begin
            ssdValue = 4'd4;
            ssdAnode = 4'b1101;
        end
        2'd3 : begin
            ssdValue = 4'd2;
            ssdAnode = 4'b1110;
        end
        default : begin
            ssdValue = 4'd10; // Undefined
            ssdAnode = 4'b1111; // None active
        end
    endcase
end

// Display decoder
seven_segment_decoder decoder (.bcd(ssdValue), .ssd(ssdCathode));

endmodule