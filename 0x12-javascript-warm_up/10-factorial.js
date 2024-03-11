#!/usr/bin/node
function factorial(num) {
  // Base case: Factorial of 0 and NaN is 1
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    // Recursive case: Factorial(n) = n * Factorial(n-1)
    return num * factorial(num - 1);
  }
}

// Check if there's at least one argument
if (process.argv.length > 2) {
  const firstArg = process.argv[2];

  // Implicit type coercion with `+` for potential non-numeric input
  const num = Number(firstArg);

  // Handle potential errors during type coercion
  if (isNaN(num)) {
    console.log("Invalid input: Please provide a number.");
  } else {
    // Call the factorial function with the converted number
    const result = factorial(num);
    console.log(`The factorial of ${num} is ${result}`);
  }
} else {
  console.log("Missing number: Please provide a number to compute the factorial.");
}
