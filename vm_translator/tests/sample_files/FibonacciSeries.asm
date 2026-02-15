
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
@4
M=D
                    
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
@THAT
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
@13
M=D
@THAT
D=M
@1
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
                
(FibonacciSeries.LOOP)
            
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
@FibonacciSeries.COMPUTE_ELEMENT
D;JNE

@FibonacciSeries.END
0;JMP
        
(FibonacciSeries.COMPUTE_ELEMENT)
            
@THAT
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
                
@THAT
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
AM=M-1
D=M
M=0
@13
M=D
@THAT
D=M
@2
D=D+A
@14
M=D
@13
D=M
@14
A=M
M=D
                
@4
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
M=D+M
D=0
        
@SP
AM=M-1
D=M
M=0
@4
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
                
@FibonacciSeries.LOOP
0;JMP
        
(FibonacciSeries.END)
            