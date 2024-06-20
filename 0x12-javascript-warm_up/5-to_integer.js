#!/usr/bin/node
const firstArg = process.argv[2]; // Access the first argument (skip script name)

if (isNaN(parseInt(firstArg))) {
  console.log("Not a number");
} else {
  console.log(`My number: ${parseInt(firstArg)}`); // Use template literal
}
