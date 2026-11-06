class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l_mult, r_mult = 1, 1
        l_arr, r_arr = [0] * n, [0] * n

        for i in range(n):
            l_arr[i] = l_mult
            l_mult *= nums[i]

            j = -i - 1
            r_arr[j] = r_mult
            r_mult *= nums[j]

        return [l * r for l, r in zip(l_arr, r_arr)]
