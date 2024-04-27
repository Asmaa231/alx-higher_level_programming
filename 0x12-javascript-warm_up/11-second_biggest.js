#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log('0');
} else {
  let second = parseInt(args[2]);
  let third = parseInt(args[3]);
  for (let i = 2; i < args.length; i++) {
    const current = parseInt(args[i]);
    if (current > third) {
      second = third;
      third = current;
    } else if (current > second && current < third) {
        second = current;
      }
  }
  console.log(second);
}
