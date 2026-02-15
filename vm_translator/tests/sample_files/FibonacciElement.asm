
@256
D=A
@SP
M=D
                    
// [call Sys.init 0] push return-address
@Sys.Sys.init.SYS0.RET
D=A
@SP
A=M
M=D
@SP
M=M+1
//[call Sys.init 0] push LCL, push ARG, push THIS, push THAT
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

//[call Sys.init 0] set ARG and LCL
@SP
D=M
@LCL
M=D
@5
D=D-A
@ARG
M=D
@Sys.init
0;JMP
(Sys.Sys.init.SYS0.RET)

(Main.fibonacci)

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
                
@2
D=A
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
A=A-1
D=D-M
M=-1
@END_4
D;JGT
@SP
A=M-1
M=0
(END_4)
D=0
        
@SP
AM=M-1
D=M
@Main.N_LT_2
D;JNE

@Main.N_GE_2
0;JMP
        
(Main.N_LT_2)
            
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

(Main.N_GE_2)
            
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
                
@2
D=A
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
        
// [call Main.fibonacci 1] push return-address
@Main.Main.fibonacci.14.RET
D=A
@SP
A=M
M=D
@SP
M=M+1
//[call Main.fibonacci 1] push LCL, push ARG, push THIS, push THAT
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

//[call Main.fibonacci 1] set ARG and LCL
@SP
D=M
@LCL
M=D
@6
D=D-A
@ARG
M=D
@Main.fibonacci
0;JMP
(Main.Main.fibonacci.14.RET)

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
                
@1
D=A
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
        
// [call Main.fibonacci 1] push return-address
@Main.Main.fibonacci.18.RET
D=A
@SP
A=M
M=D
@SP
M=M+1
//[call Main.fibonacci 1] push LCL, push ARG, push THIS, push THAT
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

//[call Main.fibonacci 1] set ARG and LCL
@SP
D=M
@LCL
M=D
@6
D=D-A
@ARG
M=D
@Main.fibonacci
0;JMP
(Main.Main.fibonacci.18.RET)

@SP
AM=M-1
D=M
M=0
@SP
A=M-1
M=D+M
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

(Sys.init)

@4
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
// [call Main.fibonacci 1] push return-address
@Sys.Main.fibonacci.23.RET
D=A
@SP
A=M
M=D
@SP
M=M+1
//[call Main.fibonacci 1] push LCL, push ARG, push THIS, push THAT
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

//[call Main.fibonacci 1] set ARG and LCL
@SP
D=M
@LCL
M=D
@6
D=D-A
@ARG
M=D
@Main.fibonacci
0;JMP
(Sys.Main.fibonacci.23.RET)

(Sys.END)
            
@Sys.END
0;JMP
        