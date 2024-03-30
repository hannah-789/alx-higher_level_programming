#!/usr/bin/node
function printSquare() {
  // Check if there's at least one argument
  if (process.argv.length > 2) {
    const firstArg = process.argv[2];

    // Implicit type coercion with `+` and `isNaN` check
    if (isNaN(Number(firstArg))) {
      console.log("Missing size");
    } else {
      const size = Number(firstArg);

      // Use nested for loops for clarity and efficient row/column printing
      for (let i = 0; i < size; i++) {
        // Inner loop for printing each row (size X's)
        for (let j = 0; j < size; j++) {
          process.stdout.write("X"); // Use process.stdout.write for efficiency
        }
        console.log(); // Move to the next line after each row
      }
    }
  } else {
    console.log("Missing size");
  }
}

