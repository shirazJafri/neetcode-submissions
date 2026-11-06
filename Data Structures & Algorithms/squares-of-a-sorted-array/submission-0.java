
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] numsSquared = new int[nums.length];

        int i = numsSquared.length - 1;
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int numLeft = Math.abs(nums[left]);
            int numRight = Math.abs(nums[right]);

            if (numLeft >= numRight) {
                numsSquared[i] = numLeft * numLeft;
                left++;
            } else {
                numsSquared[i] = numRight * numRight;
                right--;
            }

            i--;
        }
        return numsSquared;
    }
}