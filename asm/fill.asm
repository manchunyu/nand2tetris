@24575
D=A
@last_screen_register
M=D

(LOOP)
	@SCREEN
	D=A
	@address
	M=D

	@24576 // Keyboard
	D=M

	@FILL
	D;JNE

	@CLEAR
	D;JEQ

	@LOOP
	0;JMP


(FILL)
	
	@address
	D=M

	@last_screen_register
	D=M-D

	@LOOP
	D;JLT

	@address
	A=M
	M=-1

	@address
	M=M+1

	@FILL
	0;JMP

(CLEAR)
	@address
	D=M

	@last_screen_register
	D=M-D

	@LOOP
	D;JLT

	@address
	A=M
	M=0

	@address
	M=M+1

	@CLEAR
	0;JMP




	