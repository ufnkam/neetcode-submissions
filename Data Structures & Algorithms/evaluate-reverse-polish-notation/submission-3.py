class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: return 0 
        stack = []
        operators = {"+", "-", "*", "/"}

        for i in range(len(tokens)):
            token = tokens[i]
            if token in operators and stack:
                b = stack.pop()
                a = stack.pop()
                match token:
                    case "+": stack.append(a + b)
                    case "-": stack.append(a - b)
                    case "/": stack.append(int(a / b))
                    case "*": stack.append(a * b)
                continue
            stack.append(int(token))

        return stack[0]
        