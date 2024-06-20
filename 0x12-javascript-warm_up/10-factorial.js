#!/usr/bin/node
function factorial(num) {
  if (isNaN(num)) {
    return 1; // Factorial of NaN is 1 (as specified)
  } else if (num === 0) {
    return 1; // Base case: factorial of 0 is 1
  } else {
    return num * factorial(num - 1); // Recursive call
  }
}

const number = parseInt(process.argv[2]); // Get and convert first argument

console.log(factorial(number)); // Call the factorial function

