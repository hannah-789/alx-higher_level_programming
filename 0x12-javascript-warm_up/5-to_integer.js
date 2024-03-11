#!/usr/bin/node
//Checks  if the first argument can be converted to an integer
function printNumberIfValid() {
  // Check if there's at least one argument
  if (process.argv.length > 2) {
    const firstArg = process.argv[2];

    // Implicit type coercion using the `+` operator
    if (isNaN(Number(firstArg))) {
      // Not a number
      console.log("Not a number");
    } else {
      // Valid integer
      console.log(`My number: ${Number(firstArg)}`);
    }
  } else {
    // Not enough arguments
    console.log("Please provide an argument.");
  }
}
