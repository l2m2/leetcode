/**
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  return +nums.sort().join('_').replace(/(\-?\d+_){2,}/, '');
};

console.log(singleNumber([2,2,3,2]));
console.log(singleNumber([0,1,0,1,0,1,99]));
console.log(singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]));