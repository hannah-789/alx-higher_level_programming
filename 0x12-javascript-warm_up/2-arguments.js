#!/usr/bin/node
// prints a specific message based on the number of arguments

const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
