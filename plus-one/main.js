/*
 * @File: main.js
 * @Author: leon.li(l2m2lq@gmail.com)
 * @Date: 2019-06-05 04:23:41
 */

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
  var carry = 1;
  var result = digits.reduceRight((acc, curr) => {
    acc.unshift((curr + carry) % 10);
    carry = (curr + carry) >= 10 ? 1 : 0;
    return acc;
  }, []);
  if (carry > 0) result.unshift(1);
  return result;
};

console.log(plusOne([1, 2, 3]));
console.log(plusOne([1, 9, 9]));