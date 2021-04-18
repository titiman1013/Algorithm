// false

function solution(n, arr1, arr2) {
    var answer = [];

    const room1 = [];
    for (let num1 of arr1) {
        let tmp1 = num1.toString(2);
        if (n !== tmp1.length) {
            tmp1 = '0' * (n - tmp1.length) + tmp1;
        }
        room1.push(tmp1);
    }

    const room2 = [];
    for (let num2 of arr2) {
        let tmp2 = num2.toString(2);
        if (n !== tmp2.length) {
            // console.log(tmp2.length)
            tmp2 = '0' * (n - tmp2.length) + tmp2;
        }
        room2.push(tmp2);
    }

    for (let i = 0; i < n; i++) {
        let line = '';
        for (let j = 0; j < n; j++) {
            if (room1[i][j] | room2[i][j]) {
                line += '#';
            } else {
                line += ' ';
            }
        }
        answer.push(line);
    }

    // console.log(room1, room2)

    return answer;
}




console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
console.log(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

// answer
// ["#####","# # #", "### #", "# ##", "#####"]
// ["######", "### #", "## ##", " #### ", " #####", "### # "]