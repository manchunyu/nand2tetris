// Adds 2 numbers
// RAM[2] = RAM[1] + RAM[0]
// Usage: put the values that u wish to add
//        in RAM[1] and RAM[0]


	@0
	D=M
	
	@1
	D=D+M
	
	@2
	M=D
	
	0;JMP