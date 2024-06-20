#!/usr/bin/node
function findSecondBiggest(args) {
  if (args.length <= 1) {
    return 0; // No arguments or only one argument
  }

  const numbers = args.map(num => parseInt(num)); // Convert arguments to integers
  numbers.sort((a, b) => b - a); // Sort in descending order

  return numbers[1] || 0; // Second element (or 0 if only one unique value)
}

const argumentsList = process.argv.slice(2); // Get arguments (skip script name and first arg)

console.log(findSecondBiggest(argumentsList)); // Call the function and print result

