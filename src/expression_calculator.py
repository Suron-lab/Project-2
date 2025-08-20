from math import pow

# --- Operator table (precedence, associativity, function) ---
OPS = {
    '+': (2, 'L', lambda a, b: a + b),
    '-': (2, 'L', lambda a, b: a - b),
    '*': (3, 'L', lambda a, b: a * b),
    '/': (3, 'L', lambda a, b: a / b),
    '^': (4, 'R', lambda a, b: pow(a, b)),
}


# === Tokenizer ===
def tokenize(expr: str):
    tokens, num = [], ''
    for c in expr:
        if c.isdigit() or c == '.':  # part of number
            num += c
        else:
            if num:
                tokens.append(num)
                num = ''
            if c in OPS or c in "()":
                tokens.append(c)
            elif c.isspace():
                continue
            else:
                raise ValueError(f"Invalid token: {c}")
    if num:
        tokens.append(num)
    return tokens


# === Infix ➜ Postfix (Shunting Yard) ===
def infix_to_postfix(tokens):
    out, stack = [], []
    for t in tokens:
        if t.replace('.', '', 1).isdigit():  # number
            out.append(t)
        elif t in OPS:
            prec, assoc, _ = OPS[t]
            while stack and stack[-1] in OPS:
                top_prec, top_assoc, _ = OPS[stack[-1]]
                if (assoc == 'L' and prec <= top_prec) or (assoc == 'R' and prec < top_prec):
                    out.append(stack.pop())
                else:
                    break
            stack.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                out.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()
    while stack:
        if stack[-1] in "()":
            raise ValueError("Mismatched parentheses")
        out.append(stack.pop())
    return out


# === Postfix Evaluation ===
def eval_postfix(tokens):
    stack = []
    for t in tokens:
        if t.replace('.', '', 1).isdigit():  # number
            stack.append(float(t))
        elif t in OPS:
            if len(stack) < 2:
                raise ValueError("Insufficient values")
            b, a = stack.pop(), stack.pop()
            stack.append(OPS[t][2](a, b))
        else:
            raise ValueError(f"Unknown token: {t}")
    if len(stack) != 1:
        raise ValueError("Too many values")
    return stack[0]


# === Calculator Interface ===
def evaluate_expression(expr: str):
    tokens = tokenize(expr)
    postfix = infix_to_postfix(tokens)
    result = eval_postfix(postfix)
    return postfix, result


# === Demo ===
if __name__ == "__main__":
    tests = [
        "3 + 4 * 2 / (1 - 5) ^ 2 ^ 3",
        "(2+3)*4 - 10/5",
        "10 + 2 * 6",
        "100 * (2 + 12) / 14"
    ]
    for expr in tests:
        postfix, res = evaluate_expression(expr)
        print(f"Infix: {expr}")
        print(f"Postfix: {' '.join(postfix)}")
        print(f"Result: {res}\n")
