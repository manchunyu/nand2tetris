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
            # machine_code.append(assemble_c(line, symbols))
            pass
    
    print(symbols)
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
                filtered_lines.append(line)
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
                print(line)
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
    code = "111"
    DEST = {
        "null": "000",
        "M"   : "001",
        "D"   : "010",
        "MD"  : "011",
        "A"   : "100",
        "AM"  : "101",
        "AD"  : "110",
        "AMD" : "111",
    }
    COMP = {
                                                
    }


#############################################################
#                         Call Main                         #     
#############################################################
if __name__ == "__main__":
    main()


