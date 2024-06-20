#!/usr/bin/node
function add(a, b) {
  return a + b; // Return the sum of a and b
}

const firstNum = parseInt(process.argv[2]); // Get and convert first argument
const secondNum = parseInt(process.argv[3]); // Get and convert second argument

if (isNaN(firstNum) || isNaN(secondNum)) {
  console.log("Error: Not a number"); // Handle invalid arguments
} else {
  const sum = add(firstNum, secondNum); // Call the add function
  console.log(sum); // Print the sum
}

