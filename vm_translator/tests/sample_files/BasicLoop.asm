
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

@0
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
@13
M=D
@LCL
D=M
@0
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
                
(BasicLoop.LOOP)
            
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
                
@SP
AM=M-1
D=M
M=0
@SP
A=M-1
M=D+M
D=0
        
@SP
AM=M-1
D=M
M=0
@13
M=D
@LCL
D=M
@0
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
                
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
        
@SP
AM=M-1
D=M
M=0
@13
M=D
@ARG
D=M
@0
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
                
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
@BasicLoop.LOOP
D;JNE

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
                