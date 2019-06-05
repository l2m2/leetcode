/*
 * @File: main2.js
 * @Author: leon.li(l2m2lq@gmail.com)
 * @Date: 2019-06-05 23:51:59
 */

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
  var carry = 1;
  var curr;
  for (var i = digits.length - 1; i >= 0; i--) {
    curr = digits[i];
    digits[i] = (curr + carry) % 10;
    carry = (curr + carry) >= 10 ? 1 : 0;
    if (carry === 0) break;
  }
  if (carry === 1) digits.unshift(1);
  return digits;
};

console.log(plusOne([1, 2, 3]));
console.log(plusOne([1, 9, 9]));