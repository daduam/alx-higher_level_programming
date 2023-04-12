#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let biggest = -Infinity;
  let secondBiggest = -Infinity;
  for (let i = 2; i < process.argv.length; i++) {
    const num = Number(process.argv[i]);
    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest) {
      secondBiggest = num;
    }
  }
  console.log(secondBiggest);
}
