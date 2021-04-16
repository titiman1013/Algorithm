function solution(board, moves) {
  var answer = 0;

  const stack = [];
  for (let j = 0; j < moves.length; j++) {
    let i = 0;
    let flag = false;
    while (board[i][moves[j]-1] === 0) {
      if (i + 1 < board.length) {
        i += 1;
      } else {
        flag = true;
        break;
      }
    }
    if (flag === true) {
      continue;
    }
    if (stack.length > 0) {
      if (stack[stack.length-1] === board[i][moves[j]-1]) {
        board[i][moves[j]-1] = 0;
        stack.pop();
        answer += 2;
        continue;
      }
    }
    stack.push(board[i][moves[j]-1]);
    board[i][moves[j]-1] = 0;
  }

  return answer;
}




console.log(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

// answer
// 4