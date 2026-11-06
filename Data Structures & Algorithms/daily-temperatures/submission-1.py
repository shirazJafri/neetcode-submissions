class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)

        # Brute Force: O(n^2) time and O(n) space
        # for i in range(len(temperatures)):
        #    for j in range(i + 1, len(temperatures)):
        #        if temperatures[j] > temperatures[i]:
        #            answer[i] = j - i
        #            break

        # Monotonic Decreasing Stack Approach: O(n) time and O(n) space
        stack = []  # [(index, temperature)]
        for index, temperature in enumerate(temperatures):
            # Stack is not empty and current temperature is larger than top of stack
            while stack and temperature > self.top(stack)[1]:
                index_stack, _ = stack.pop()
                answer[index_stack] = index - index_stack
            stack.append((index, temperature))

        return answer

    def top(self, stack: list(tuple(int, int))) -> tuple(int, int):
        """
        """
        return stack[-1]
