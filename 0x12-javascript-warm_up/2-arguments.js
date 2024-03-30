#!/usr/bin/node
// Prints a message based on the  number of arguments passed

if (process.argv.length === 0) {
  console.log('No argument');
} else if (process.argv.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
