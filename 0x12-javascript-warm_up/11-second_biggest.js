#!/usr/bin/node
function findSecondBiggest(args) {
  // Handle cases with no or only one argument
  if (args.length <= 1) {
    return 0;
  }

  // Convert arguments to numbers (assuming valid integers)
  const numbers = args.slice(2).map(Number); // Skip script path and script execution path

  // Sort the numbers in descending order
  numbers.sort((a, b) => b - a);

  // Check if there's at least a second element (second biggest)
  if (numbers.length >= 2) {
    // Second biggest element is at index 1 after sorting
    return numbers[1];
  } else {
    // Only one unique element (all equal)
    return numbers[0];
  }
}
