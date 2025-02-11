def main():
    
    filtered_lines = read_file()
    symbols = load_predefined_symbols()
    load_labels(filtered_lines, symbols)
    load_variables(filtered_lines, symbols)

    machine_code = []
    for line in filtered_lines:
        if line.startswith('@'):
            machine_code.append(assemble_a(line, symbols))
        else:
            machine_code.append(assemble_c(line))
    
    print(filtered_lines)
    print(machine_code)


####################################################
#                     Helpers                      #
####################################################


def read_file():
    filtered_lines = []
   
    with open("./rectangle.txt", 'r') as file:
        # remove tabs and empty spaces
        lines = [line.strip() for line in file]

        # remove comments and empty lines
        for line in lines:
            if not (line.startswith("//") or line == ""):
                # remove inline comments
                if not ("//" in line):
                    filtered_lines.append(line)
                else:
                    filtered_lines.append(line.split("//")[0])
                    
    return filtered_lines

def load_predefined_symbols():
    symbols = {}
    VIRTUAL_MEMORY_SIZE = 16
    SCREEN_ADDRESS = 16384
    KBD_ADDRESS  = 24576
    PREDEFINED = ["SP", "LCL", "ARG", "THIS", "THAT"]

    # load predefined
    for i in range(len(PREDEFINED)):
        symbols[PREDEFINED[i]] = i

    # load virtual memory
    for i in range(VIRTUAL_MEMORY_SIZE):
        symbols[f"R{i}"] = i

    # load screen / kbd
    symbols["SCREEN"] = SCREEN_ADDRESS
    symbols["KBD"]  = KBD_ADDRESS

    return symbols

def load_labels(filtered_lines, symbols):
    # label to symbols{}
    label_counter = 0
    for i, line in enumerate(filtered_lines):
        if line.startswith("("):
            label = line.rstrip(')').lstrip('(')
            label_counter += 1
            symbols[label]= i + 1 - label_counter
    
    # remove labels from code
    for i, line in enumerate(filtered_lines):
        if line.startswith("("):
            filtered_lines.pop(i)

def load_variables(lines, symbols):
    variable_counter = 15
    for line in lines:
        if line.startswith('@'):
            possible_var = line.lstrip('@')
            if not (possible_var in symbols or possible_var.isdecimal()):
                variable_counter += 1
                symbols[possible_var] = variable_counter

def assemble_a(instruction, symbols):
    code = "0"
    value_at_areg = instruction.lstrip('@')

    if value_at_areg in symbols:
        code += bin(symbols[value_at_areg])[2:].zfill(15)
    else:
        code += bin(int(value_at_areg))[2:].zfill(15)
        
    return code

def assemble_c(instruction):

    DEST = {
        # "null" : "000",
        "M"    : "001",
        "D"    : "010",
        "MD"   : "011",
        "A"    : "100",
        "AM"   : "101",
        "AD"   : "110",
        "AMD"  : "111",
    }

    COMP = {
        "0"   : "0101010",
        "1"   : "0111111",
        "-1"  : "0111010",
        "D"   : "0001100",
        "A"   : "0110000",
        "!D"  : "0001101",
        "!A"  : "0110001",
        "-D"  : "0001111",
        "-A"  : "0110011",
        "D+1" : "0011111",
        "A+1" : "0110111",
        "D-1" : "0001110",
        "A-1" : "0110010",
        "D+A" : "0000010",
        "D-A" : "0010011",
        "A-D" : "0000111",
        "D&A" : "0000000",
        "D|A" : "0010101",
        "M"   : "1110000", 
        "!M"  : "1110001",
        "-M"  : "1110011",
        "M+1" : "1110111",
        "M-1" : "1110010",
        "D+M" : "1000010",
        "D-M" : "1010011",
        "M-D" : "1000111",
        "D&M" : "1000000",
        "D|M" : "1010101",
    }

    JUMP = {
        # "null" : "000",
        "JGT"  : "001",
        "JEQ"  : "010",
        "JGE"  : "011",
        "JLT"  : "100",
        "JNE"  : "101",
        "JLE"  : "110",
        "JMP"  : "111",
    }
    
    dest_instruction = "000"
    jump_instruction = "000"

    if "=" in instruction:
        dest = instruction.split("=")[0].strip()
        instruction = instruction.split("=")[1].strip()   
        dest_instruction = DEST[dest]
        

    if ";" in instruction:
        jump = instruction.split(";")[1].strip()
        instruction = instruction.split(";")[0].strip()
        jump_instruction = JUMP[jump]

    return "111" + COMP[instruction] + dest_instruction + jump_instruction


#############################################################
#                         Call Main                         #     
#############################################################
if __name__ == "__main__":
    main()
