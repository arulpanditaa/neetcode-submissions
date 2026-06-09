class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tkn in tokens:
            if tkn == "+":
                pop1 = stack.pop()
                pop2 = stack.pop()
                stack.append(pop2 + pop1)
            elif tkn == "-":
                pop1 = stack.pop()
                pop2 = stack.pop()
                stack.append(pop2 - pop1)
            elif tkn == "*":
                pop1 = stack.pop()
                pop2 = stack.pop()
                stack.append(pop2 * pop1)
            elif tkn == "/":
                pop1 = stack.pop()
                pop2 = stack.pop()
                stack.append(int(pop2 / pop1))
            else:
                stack.append(int(tkn))
        return stack[0]
            


        