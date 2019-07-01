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
  let temp = nums.reduce((prev, curr) => {
    if (typeof prev[curr] == "undefined") {
      prev[curr] = 1;
    } else {
      prev[curr] += 1;
    }
    return prev;
  }, {});
  for (let i in temp) {
    if (temp[i] === 1) {
      return i;
    }
  }
};

console.log(singleNumber([2,2,3,2]));
console.log(singleNumber([0,1,0,1,0,1,99]));