#!/usr/bin/node
const size = parseInt(process.argv[2]); // Get and convert first argument

if (isNaN(size)) {
  console.log("Missing size");
} else {
  for (let i = 0; i < size; i++) {
    let row = ""; // Initialize empty string for each row
    for (let j = 0; j < size; j++) {
      row += "X"; // Add "X" to the current row
    }
    console.log(row); // Print the completed row
  }
}

