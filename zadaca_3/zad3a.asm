@R1
D=M
@R0
D=D-M        // D = R1 - R0
@NOSWAP
D;JGE        // ako R1 >= R0 => NOSWAP
// inace swap
$SWP(R0,R1)

(NOSWAP)

@R1
D=M
@R0
D=D-M        // D = (R1 - R0)
@R1
M=D+1        // R1 = (R1 - R0) + 1

@R2
M=0

$WHILE(R1)

    // R2 = R2 + R0
    $ADD(R2, R0, R2)

    // R0++
    @R0
    M=M+1

    // R1--
    @R1
    M=M-1

$END
