`timescale 1ns / 1ps

module TB_Test_Add_1();

// Inputs
   reg Y;
   reg X;
   reg Cin;

// Output
   wire Z;
   wire Cout;

// Instantiate the UUT
   my_adder UUT (
		.X(X), 
		.Y(Y), 
		.C_in(Cin), 
		.Z(Z), 
		.C_out(Cout)
   );
	
// Duration of simulation
	initial begin: stopat
		#12; $finish;
	end

// Initialize Inputs
	initial begin
		Y = 0;
		X = 0;
		Cin = 0;
	end
	
	initial begin
		#1X = 1'b0;
		Y = 1'b0;
		Cin = 1'b0;
		
		#1X = 1'b1;
		Y = 1'b0;
		Cin = 1'b0;
		
		#1X = 1'b0;
		Y = 1'b1;
		Cin = 1'b0;
		
		#1X = 1'b1;
		Y = 1'b1;
		Cin = 1'b0;
		
		#1X = 1'b0;
		Y = 1'b0;
		Cin = 1'b1;
		
		#1X = 1'b1;
		Y = 1'b0;
		Cin = 1'b1;
		
		#1X = 1'b0;
		Y = 1'b1;
		Cin = 1'b1;
		
		#1X = 1'b1;
		Y = 1'b1;
		Cin = 1'b1;
		
	end

endmodule
