class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = ['+', '-', '*', '/']
        # if tokens[0] or tokens[1] in operand:
        #     return False

        stack = []

        for t in tokens:
            if t not in operand:
                stack.append(t)
            else:
                sp2 = stack.pop()
                sp1 = stack.pop()
                ans = str(int(eval(sp1 + t + sp2)))
                stack.append(ans)

        return eval(stack[0])



