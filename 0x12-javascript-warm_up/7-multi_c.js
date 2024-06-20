#!/usr/bin/node
const numOccurrences = parseInt(process.argv[2]); // Get and convert first argument

if (isNaN(numOccurrences)) {
  console.log("Missing number of occurrences"); // Invalid argument
} else {
  for (let i = 0; i < numOccurrences; i++) {
    console.log("C is fun");
  }
}

