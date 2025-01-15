	@100
	D=A
	@address 
	M=D

	@10
	D=A
	@count
	M=D

	@i
	M=0

(LOOP)
	@i
	D=M

	@count
	D=M-D

	@IDLE
	D;JEQ

	@i
	D=M

	@address
	A=D+M
	M=-1

	@i
	M=M+1

	@LOOP
	0;JMP
	
(IDLE)
	@IDLE
	0;JMP