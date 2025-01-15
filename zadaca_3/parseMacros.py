def _parse_macros(self):
    self._counter = 0
    self._stack = []
    
    newlines = []
    i = 0
    for (line, p, o) in self._lines:
        expanded = self._parse_macro(line, p, o)
        if not self._flag:
            break
        
        # Razbij višelinijski string u više linija
        lines_split = expanded.split('\n')
        
        for one_line in lines_split:
            one_line = one_line.strip()
            if one_line:
                newlines.append((one_line, i, o))
                i += 1
    
    self._lines = newlines

def _parse_macro(self, line, p, o):
    if len(line) == 0:
        return line
    
    if line[0] == '$':
        # Ovdje isto kao kod vas: MV, SWP, ADD, WHILE, END
        if line[1:3] == "MV":
            A = line[4]
            B = line[6]
            l = (
                "@" + A + "\n"
                "D=M\n"
                "@" + B + "\n"
                "M=D"
            )
        
        elif line[1:4] == "SWP":
            A = line[5]
            B = line[7]
            l = (
                f"@{A}\nD=M\n"
                "@15\nM=D\n"
                f"@{B}\nD=M\n"
                f"@{A}\nM=D\n"
                "@15\nD=M\n"
                f"@{B}\nM=D"
            )
        
        elif line[1:4] == "ADD":
            A_ = line[5]
            B_ = line[7]
            D_ = line[9]
            l = (
                f"@{A_}\nD=M\n"
                f"@{B_}\nD=D+M\n"
                f"@{D_}\nM=D"
            )
        
        elif len(line) >= 6 and line[1:6] == "WHILE":
            self._counter += 1
            self._stack.append(self._counter)
            A = line[7]
            l = (
                f"(WHILE{self._counter})\n"
                f"@{A}\n"
                "D=M\n"
                f"@END{self._counter}\n"
                "D;JEQ"
            )
        
        elif line[1:4] == "END":
            if not self._stack:
                self._flag = False
                self._line = o
                self._errm = "Invalid macro: $END without matching $WHILE."
                return ""
            n = self._stack.pop()
            l = (
                f"@WHILE{n}\n"
                "0;JMP\n"
                f"(END{n})"
            )
        
        else:
            self._flag = False
            self._line = o
            self._errm = "Invalid macro name."
            return ""
        
        return l
    
    else:
        # Nije makro -> vrati kako jest
        return line
