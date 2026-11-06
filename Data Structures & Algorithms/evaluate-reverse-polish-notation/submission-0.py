import math


class Solution:
    def evaluate(self, operand_1: int, operand_2: int, operator: str) -> int:
        match operator:
            case "+":
                return operand_1 + operand_2
            case "-":
                return operand_1 - operand_2
            case "*":
                return operand_1 * operand_2
            case "/":
                return math.trunc(operand_1 / operand_2)
            case _:
                return None

    def is_operator(self, token: str) -> bool:
        return token in ("+", "-", "*", "/")

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_operator(token):
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(self.evaluate(operand_1, operand_2, token))
            else:
                stack.append(int(token))

        return stack.pop()
