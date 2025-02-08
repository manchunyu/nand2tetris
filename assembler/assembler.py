filtered_lines = []
with open("./rectangle.txt", 'r') as file:
    lines = [line.strip() for line in file]
    for line in lines:
        if not (line.startswith("//") or line == ""):
            filtered_lines.append(line)

print(filtered_lines)

symbols = {}

def load_predefined_symbols():
    VIRTUAL_MEMORY_SIZE = 16
    SCREEN_ADDRESS = 16384
    KBD_ADDRESS  = 24576
    PREDEFINED = ["SP", "LCL", "ARG", "THIS", "THAT"]

    for i in range(len(PREDEFINED)):
        symbols[PREDEFINED[i]] = i

    for i in range(VIRTUAL_MEMORY_SIZE):
        symbols[f"R{i}"] = i
    symbols["SCREEN"] = SCREEN_ADDRESS
    symbols["KBD"]  = KBD_ADDRESS

def load_labels():
    label_counter = 0
    for i, line in enumerate(filtered_lines):
        if line.startswith("("):
            label = line.rstrip(')').lstrip('(')
            label_counter += 1
            symbols[label]= i + 1 - label_counter


load_predefined_symbols()
load_labels()
print(symbols)


