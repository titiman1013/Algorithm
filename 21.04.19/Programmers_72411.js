function combination(answer, source, target, n, r, count) {
  if (r === 0) answer.push(target);
  else if (n === 0 || n < r) return;
  else {
    target += source[count];
    combination(source, Object.assign('', target), n - 1, r - 1, count + 1);
    target = target.slice(0, -1);
    combination(source, Object.assign('', target), n - 1, r, count + 1);
  }
}


function solution(orders, course) {
  var answer = [];

  const orderedCount = new Map();
  for (let i = 0; i < course.length; i++) {
    combination(answer, orders, '', orders.length, course[i], 0);
  }
  
  answer.sort();

  return answer;
}




console.log(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
console.log(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
console.log(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

// answer
// ["AC", "ACDE", "BCFG", "CDE"]
// ["ACD", "AD", "ADE", "CD", "XYZ"]
// ["WX", "XY"]