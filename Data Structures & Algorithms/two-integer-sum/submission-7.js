class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    // [3,4,5,6]
    // {4: 0, }
    twoSum(nums, target) {
        const sumMap = {};
        for(let i = 0; i < nums.length; i++) {
            const res = target - nums[i];
            if (Object.hasOwn(sumMap, nums[i])) {
                return [sumMap[nums[i]], i];
            } else {
                sumMap[res] = i;
            }
        }

    }
}
