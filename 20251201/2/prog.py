import sys, math

text = sys.stdin.read().splitlines()

cmds = []
labels = {}

for line in text:
    s = line.lstrip()
    if not s:
        continue
    parts = s.split()
    if not parts:
        continue

    if parts[0].endswith(":"):
        lb = parts[0][:-1]
        if lb:
            labels[lb] = len(cmds)
        parts = parts[1:]
        if not parts:
            continue

    op = parts[0].lower()

    if op == "stop" and len(parts) == 1:
        cmds.append(("stop",))
        continue

    if op == "store" and len(parts) == 3:
        num_s = parts[1]
        var = parts[2]
        try:
            val = float(num_s)
        except Exception:
            val = 0.0
        cmds.append(("store", val, var))
        continue

    if op in ("add", "sub", "mul", "div") and len(parts) == 4:
        src, oper, dst = parts[1], parts[2], parts[3]
        cmds.append(("op", op, src, oper, dst))
        continue

    if op in ("ifeq", "ifne", "ifgt", "ifge", "iflt", "ifle") and len(parts) == 4:
        src, oper, lab = parts[1], parts[2], parts[3]
        cmds.append(("cmp", op, src, oper, lab))
        continue

    if op == "out" and len(parts) == 2:
        src = parts[1]
        cmds.append(("out", src))
        continue

for c in cmds:
    if c[0] == "cmp":
        lab = c[4]
        if lab not in labels:
            sys.exit(0)

vars = {}
pc = 0

while 0 <= pc < len(cmds):
    cmd = cmds[pc]
    kind = cmd[0]

    if kind == "cmp":
        _, cop, sname, oname, lab = cmd
        a = vars.get(sname, 0.0)
        b = vars.get(oname, 0.0)
        ok = False
        if cop == "ifeq":
            ok = a == b
        elif cop == "ifne":
            ok = a != b
        elif cop == "ifgt":
            ok = a > b
        elif cop == "ifge":
            ok = a >= b
        elif cop == "iflt":
            ok = a < b
        elif cop == "ifle":
            ok = a <= b
        if ok:
            pc = labels[lab]
        else:
            pc += 1

    elif kind == "out":
        _, name = cmd
        print(vars.get(name, 0.0))
        pc += 1

    elif kind == "store":
        _, val, name = cmd
        vars[name] = val
        pc += 1

    elif kind == "op":
        _, op, sname, oname, dest = cmd
        a = vars.get(sname, 0.0)
        b = vars.get(oname, 0.0)
        try:
            if op == "add":
                r = a + b
            elif op == "sub":
                r = a - b
            elif op == "mul":
                r = a * b
            elif op == "div":
                r = a / b
            else:
                r = 0.0
        except Exception:
            r = math.inf
        vars[dest] = r
        pc += 1

    elif kind == "stop":
        break

    else:
        pc += 1
