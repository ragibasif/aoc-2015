import os
import sys

def part1(data):
    res = 0
    for i in data:
        if i == '(':
            res = res + 1
        elif i == ')':
            res = res - 1
    print(res)

if __name__ == "__main__":
    # Handle command-line arguments
    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(__file__)} <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    with open(input_file,"r") as f:
        data = f.read()

    part1("(())") # 0
    part1("()()") # 0
    part1("(((") # 3
    part1("(()(()(") # 3
    part1("))(((((") # 3
    part1("())") # -1
    part1("))(") # -1
    part1(")))") # -3
    part1(")())())") # -3
    part1(data) # 138

