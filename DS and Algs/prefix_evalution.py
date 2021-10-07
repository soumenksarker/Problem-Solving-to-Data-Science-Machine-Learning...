from Stack import Stack
def prefix_eval(prefix_expr):
    operand_stack = Stack()
    token_list = prefix_expr.split()
    for token in reversed(token_list):
       if token in "0123456789":
          operand_stack.push(int(token))
       else:
          operand1 = operand_stack.pop()
          operand2 = operand_stack.pop()
        
          result = do_math(token, operand1, operand2)
          operand_stack.push(result)
    return operand_stack.pop()
def do_math(op, op1, op2):
    if op == "**":
        return op1**op2
    elif op == "*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
print("The value of the prefix expression is ",prefix_eval(' + - * 2 3 5 / ** 2 3 4')) 
