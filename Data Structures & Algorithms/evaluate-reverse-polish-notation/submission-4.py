class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        solution = []
        for val in tokens:
            if val not in "+-*/":
                solution.append(int(val))
            else:
                b, a = solution.pop(), solution.pop()
            
                if (val == "+"):
                    solution.append(a + b)
                elif (val == "-"):
                    solution.append(a - b)
                elif (val == "*"):
                    solution.append(a * b)
                elif (val == "/"):
                    solution.append(int(a / b))
        return solution[-1]
        