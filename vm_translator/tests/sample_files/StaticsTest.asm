
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

(Class1.set)

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
@Class1.0
M=D
                
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
@Class1.1
M=D
                
@0
D=A
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

(Class1.get)

@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@Class1.1
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

(Sys.init)

@6
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
// [call Class1.set 2] push return-address
@Sys.Class1.set.16.RET
D=A
@SP
A=M
M=D
@SP
M=M+1
//[call Class1.set 2] push LCL, push ARG, push THIS, push THAT
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

//[call Class1.set 2] set ARG and LCL
@SP
D=M
@LCL
M=D
@7
D=D-A
@ARG
M=D
@Class1.set
0;JMP
(Sys.Class1.set.16.RET)

@SP
AM=M-1
D=M
M=0
@5
M=D
                    
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
// [call Class2.set 2] push return-address
@Sys.Class2.set.20.RET
D=A
@SP
A=M
M=D
@SP
M=M+1
//[call Class2.set 2] push LCL, push ARG, push THIS, push THAT
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

//[call Class2.set 2] set ARG and LCL
@SP
D=M
@LCL
M=D
@7
D=D-A
@ARG
M=D
@Class2.set
0;JMP
(Sys.Class2.set.20.RET)

@SP
AM=M-1
D=M
M=0
@5
M=D
                    
// [call Class1.get 0] push return-address
@Sys.Class1.get.22.RET
D=A
@SP
A=M
M=D
@SP
M=M+1
//[call Class1.get 0] push LCL, push ARG, push THIS, push THAT
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

//[call Class1.get 0] set ARG and LCL
@SP
D=M
@LCL
M=D
@5
D=D-A
@ARG
M=D
@Class1.get
0;JMP
(Sys.Class1.get.22.RET)

// [call Class2.get 0] push return-address
@Sys.Class2.get.23.RET
D=A
@SP
A=M
M=D
@SP
M=M+1
//[call Class2.get 0] push LCL, push ARG, push THIS, push THAT
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

//[call Class2.get 0] set ARG and LCL
@SP
D=M
@LCL
M=D
@5
D=D-A
@ARG
M=D
@Class2.get
0;JMP
(Sys.Class2.get.23.RET)

(Sys.END)
            
@Sys.END
0;JMP
        
(Class2.set)

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
@Class2.0
M=D
                
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
@Class2.1
M=D
                
@0
D=A
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

(Class2.get)

@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@Class2.1
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
