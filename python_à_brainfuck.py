import sys

def brainfuck_to_python(bf_code: str) -> str:
    valid_chars = set("+-<>[],.")
    bf_code = "".join([c for c in bf_code if c in valid_chars])

    py_code = [
        "import sys\n",
        "tape = [0] * 30000",
        "ptr = 0\n"
    ]
    
    indent_level = 0
    
    for char in bf_code:
        indent = "    " * indent_level
        
        if char == '>':
            py_code.append(f"{indent}ptr = (ptr + 1) % 30000")
        elif char == '<':
            py_code.append(f"{indent}ptr = (ptr - 1) % 30000")
        elif char == '+':
            py_code.append(f"{indent}tape[ptr] = (tape[ptr] + 1) % 256")
        elif char == '-':
            py_code.append(f"{indent}tape[ptr] = (tape[ptr] - 1) % 256")
        elif char == '.':
            py_code.append(f"{indent}sys.stdout.write(chr(tape[ptr]))")
        elif char == ',':
            py_code.append(f"{indent}tape[ptr] = ord(sys.stdin.read(1) or '\\0') % 256")
        elif char == '[':
            py_code.append(f"{indent}while tape[ptr] != 0:")
            indent_level += 1
        elif char == ']':
            indent_level -= 1
            if indent_level < 0:
                raise SyntaxError("Unmatched closing bracket ']' in Brainfuck code.")
                
    if indent_level != 0:
        raise SyntaxError("Unmatched opening bracket '[' in Brainfuck code.")

    return "\n".join(py_code)


if __name__ == "__main__":
    hello_bf = "++++++++++[>+++++++>++++++++++<<-]>+.>++."
    
    python_script = brainfuck_to_python(hello_bf)
    
    print("--- Generated Python Code ---")
    print(python_script)
    print("\n--- Execution Output ---")
    exec(python_script)
