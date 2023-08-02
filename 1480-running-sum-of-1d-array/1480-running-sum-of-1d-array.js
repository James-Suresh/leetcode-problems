/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let nums_output = []
    for(let i=0; i<nums.length;i++)
        {
            nums_output[i]=0
            for(let j=0; j<=i;j++)
                {   
                    nums_output[i] += nums[j]
                }
        }   
    return nums_output
};