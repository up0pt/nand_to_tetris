
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@17
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
M=0
@END_3
D;JNE
@SP
A=M-1
M=-1
(END_3)
D=0
        
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@16
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
M=0
@END_6
D;JNE
@SP
A=M-1
M=-1
(END_6)
D=0
        
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@17
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
M=0
@END_9
D;JNE
@SP
A=M-1
M=-1
(END_9)
D=0
        
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@891
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
@END_12
D;JGT
@SP
A=M-1
M=0
(END_12)
D=0
        
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@892
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
@END_15
D;JGT
@SP
A=M-1
M=0
(END_15)
D=0
        
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@891
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
@END_18
D;JGT
@SP
A=M-1
M=0
(END_18)
D=0
        
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@32766
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
@END_21
D;JLT
@SP
A=M-1
M=0
(END_21)
D=0
        
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@32767
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
@END_24
D;JLT
@SP
A=M-1
M=0
(END_24)
D=0
        
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@32766
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
@END_27
D;JLT
@SP
A=M-1
M=0
(END_27)
D=0
        
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                
@53
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
M=D+M
D=0
        
@112
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
A=M-1
M=!M
M=M+1
        
@SP
AM=M-1
D=M
M=0
A=A-1
M=D&M
D=0
        
@82
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
M=D|M
D=0
        
@SP
A=M-1
M=!M
        