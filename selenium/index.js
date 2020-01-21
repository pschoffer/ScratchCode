
function solution(x) {
  function matches(a, b) {
    var matchItems = a.map((aItem, ix) => aItem === b[ix])
    return !matchItems.includes(false)
  }
  var sorted = x.concat().sort((a, b) => a < b ? -1 : 1)
  var reversed = x.concat().reverse()
  return matches(x, sorted) ? 1 : (matches(reversed, sorted) ? -1 : 0)
}
// report_problemsortingType( [0,-1,-100] ) = 0expected: -1

// report_problemsortingType( [-2,4,10,19] ) = 0expected: 1

// report_problemsortingType( [1,11,101] ) = 0expected: 1

// report_problemsortingType( [101,11,1] ) = 0expected: -1

// donesortingType( [14,-2,1.5] ) = 0

// donesortingType( [18,18.1,19] ) = 1

// report_problemsortingType( [0.9,0.4,-0.1,-0.12,-1] ) = 0expected: -1
// x is an array of at least 2 unique members
// return 0 if it's not sorted, 1 if it's ascending, -1 if it's descending


x = [101, 11, 1]
result = solution(x)

console.log(result)