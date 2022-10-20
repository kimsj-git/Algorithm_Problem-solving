const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// 입력 받는 부분 -> line으로 입력이 들어옴
let N   // 입력 받은 값 저장
rl.on("line", (line) => {
  N = Number(line);
  rl.close();
});

// 별찍기 함수
function stars (n) {
  for (let i = 0; i < n; i++) {
    console.log(' '.repeat(i) + '*'.repeat((n - i) * 2 - 1))
  }
  for (let i = 2; i < n + 1; i ++) {
    console.log(' '.repeat(n - i) + '*'.repeat(2 * i - 1))
  }
}

// 출력하는 부분
rl.on('close', () => {
  // 출력은 여기서!
  stars(N)
  process.exit();
})