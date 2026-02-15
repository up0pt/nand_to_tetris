
(SimpleFunction.SimpleFunction.test)

@SP
A=M
M=0
@SP
M=M+1

@SP
A=M
M=0
@SP
M=M+1

@LCL
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@LCL
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@SP
AM=M-1
D=M
M=0
@SP
A=M-1
M=D+M
D=0
        
@SP
A=M-1
M=!M
        
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@SP
AM=M-1
D=M
M=0
@SP
A=M-1
M=D+M
D=0
        
@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@SP
AM=M-1
D=M
M=0
@SP
A=M-1
M=M-D
D=0
        
//[return] FRAME = LCL
@LCL
D=M
@5
M=D
//[return] RET = *(FRAME-5)
@5
A=D-A
D=M
@6
M=D
//[return] *ARG = pop()
@SP
A=M-1
D=M
@ARG
A=M
M=D
//[return] SP = ARG + 1
@ARG
D=M
@SP
M=D+1
//[return] THAT = *(FRAME-1)
@5
AM=M-1
D=M
@THAT
M=D
//[return] THIS = *(FRAME-2)
@5
AM=M-1
D=M
@THIS
M=D
//[return] ARG = *(FRAME-3)
@5
AM=M-1
D=M
@ARG
M=D
//[return] LCL = *(FRAME-4)
@5
AM=M-1
D=M
@LCL
M=D
//[return] goto RET
@6
A=M
0;JMP
