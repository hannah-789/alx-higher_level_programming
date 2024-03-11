#!/usr/bin/node
function add(a, b) {
  // Implicit type coercion with `+` to handle potential non-numeric inputs
  const sum = Number(a) + Number(b);

  // Print the sum using console.log
  console.log(sum);
}

// Check if there are at least two arguments
if (process.argv.length > 2) {
  // Extract the first two arguments (excluding script path and script execution path)
  const firstArg = process.argv[2];
  const secondArg = process.argv[3];

  // Call the add function with the extracted arguments
  add(firstArg, secondArg);
} else {
  // Not enough arguments, print an informative message
  console.log("Please provide two numbers to add.");
}
