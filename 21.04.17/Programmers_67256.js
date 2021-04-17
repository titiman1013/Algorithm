function solution(numbers, hand) {
  var answer = '';

  // const arr = new Array()
  const dial = {
    1: [0, 0], 2: [0, 1], 3: [0, 2],
    4: [1, 0], 5: [1, 1], 6: [1, 2],
    7: [2, 0], 8: [2, 1], 9: [2, 2],
    '*': [3, 0], 0: [3, 1], '#': [3, 2],
  };
  let left_thumb = dial['*'];
  let right_thumb = dial['#'];
  for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] === 1 | numbers[i] === 4 | numbers[i] === 7) {
      left_thumb = dial[numbers[i]]
      answer += 'L';
    } else if (numbers[i] === 3 | numbers[i] === 6 | numbers[i] === 9) {
      right_thumb = dial[numbers[i]]
      answer += 'R';
    } else {
      if (Math.abs(left_thumb[0] - dial[numbers[i]][0]) + (Math.abs(left_thumb[1] - dial[numbers[i]][1])) < (Math.abs(right_thumb[0] - dial[numbers[i]][0])) + (Math.abs(right_thumb[1] - dial[numbers[i]][1]))) {
        left_thumb = dial[numbers[i]]
        answer += 'L';
      } else if (Math.abs(left_thumb[0] - dial[numbers[i]][0]) + (Math.abs(left_thumb[1] - dial[numbers[i]][1])) > (Math.abs(right_thumb[0] - dial[numbers[i]][0])) + (Math.abs(right_thumb[1] - dial[numbers[i]][1]))) {
        right_thumb = dial[numbers[i]]
        answer += 'R';
      } else {
        if (hand === 'left') {
          left_thumb = dial[numbers[i]]
          answer += 'L';
        } else {
          right_thumb = dial[numbers[i]]
          answer += 'R';
        }
      }
    }
  }

  return answer;
}




console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))

// answer
// "LRLLLRLLRRL"
// "LRLLRRLLLRR"
// "LLRLLRLLRL"