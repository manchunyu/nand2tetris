// Height
	@R0
	D=M
	@height
	M=D

// Screen address
	@SCREEN
	D=A
	@address
	M=D 

// Counter
	@counter
	M=0

// Spaces
	@32
	D=A
	@spaces
	M=D

(DRAW)
	@counter
	D=M
	@height
	D=M-D
	@END
	D;JEQ

	@address
	A=M
	M=-1

	@counter
	M=M+1
	@spaces
	D=M
	@address
	M=D+M

	@DRAW
	0;JMP

(END)
	@END
	0;JMP
