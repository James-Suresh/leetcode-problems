/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
        let newarr = []
        for (let i = 0; i < nums.length; i++) {
            if (newarr.includes(nums[i]))
            {   
                return true
            }
                newarr.push(nums[i])          
        }
        return false
    
    };