import math
import sys
from collections import defaultdict

def interpret_assembly(program_lines):
    commands = []
    labels = {}
    jumps = []
    
    for line_num, line in enumerate(program_lines):
        line = line.rstrip('\n')
        if not line:
            continue
        
        line = line.lstrip()
        if not line:
            continue
        
        label = None
        if ':' in line:
            parts = line.split(':', 1)
            label = parts[0].strip()
            line = parts[1].strip()
        
        if not line:
            continue
        
        parts = line.split()
        if not parts:
            continue
        
        op = parts[0]
        
        valid = False
        if op == 'stop' and len(parts) == 1:
            valid = True
        elif op == 'store' and len(parts) == 3:
            valid = True
        elif op in {'add', 'sub', 'div', 'mul'} and len(parts) == 4:
            valid = True
        elif op in {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'} and len(parts) == 4:
            valid = True
        elif op == 'out' and len(parts) == 2:
            valid = True
        
        if valid:
            if label:
                labels[label] = len(commands)
            commands.append(parts)
            if parts[0] in {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'}:
                jumps.append((len(commands) - 1, parts[3]))
    
    # Проверяем все переходы
    for cmd_idx, label in jumps:
        if label not in labels:
            return
    
    variables = defaultdict(float)
    pc = 0
    
    while pc < len(commands):
        cmd = commands[pc]
        op = cmd[0]
        
        if op == 'stop':
            break
        
        elif op == 'store':
            try:
                value = float(cmd[1])
            except ValueError:
                value = 0.0
            variables[cmd[2]] = value
            pc += 1
        
        elif op in {'add', 'sub', 'div', 'mul'}:
            src = variables[cmd[1]]
            opnd = variables[cmd[2]]
            dst = cmd[3]
            
            if op == 'add':
                result = src + opnd
            elif op == 'sub':
                result = src - opnd
            elif op == 'mul':
                result = src * opnd
            else:  # div
                if opnd == 0:
                    result = math.inf
                else:
                    result = src / opnd
            
            variables[dst] = result
            pc += 1
        
        elif op in {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'}:
            src = variables[cmd[1]]
            opnd = variables[cmd[2]]
            label = cmd[3]
            
            condition = False
            if op == 'ifeq':
                condition = src == opnd
            elif op == 'ifne':
                condition = src != opnd
            elif op == 'ifgt':
                condition = src > opnd
            elif op == 'ifge':
                condition = src >= opnd
            elif op == 'iflt':
                condition = src < opnd
            elif op == 'ifle':
                condition = src <= opnd
            
            if condition:
                pc = labels[label]
            else:
                pc += 1
        
        elif op == 'out':
            print(variables[cmd[1]])
            pc += 1

def main():
    program_lines = sys.stdin.readlines()
    interpret_assembly(program_lines)

if __name__ == "__main__":
    main()

exec(sys.stdin.read())
