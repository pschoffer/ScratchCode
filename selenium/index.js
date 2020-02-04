
function solution(x) {
  if (x.length == 0) return true;
  var sum = x.reduce((sum, el) => sum += el, 0)
  var runningSum = 0
  for (var el of x) { if (runningSum == sum - runningSum) { return true; } else runningSum += el; };
  return false
}
// x is an array of numbers. return whether there is an index where the sum
// before (excluding) it is equal to the sum after (including) it.

x = [1, 1]
result = solution(x)

console.log(result)