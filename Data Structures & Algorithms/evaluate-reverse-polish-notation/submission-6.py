class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
                continue
            
            if token == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
                continue
            elif token == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
                continue
            elif token == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
                continue
            elif token == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
                continue
            
        return stack[0]