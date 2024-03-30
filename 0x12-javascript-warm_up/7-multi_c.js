#!/usr/bin/node
function printCFun() {
  // Check if there's at least one argument
  if (process.argv.length > 2) {
    const firstArg = process.argv[2];

    // Implicit type coercion with `+` and `isNaN` check
    if (isNaN(Number(firstArg))) {
      console.log("Missing number of occurrences");
    } else {
      const numOccurrences = Number(firstArg);

      // Use a for loop for clarity and efficiency
      for (let i = 0; i < numOccurrences; i++) {
        console.log("C is fun");
      }
    }
  } else {
    console.log("Missing number of occurrences");
  }
}
