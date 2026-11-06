class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []  # pairs (idx, temp)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_idx, stack_temp = stack.pop()
                answer[stack_idx] = idx - stack_idx
            stack.append((idx, temp))

        return answer
