#!/usr/bin/node
// prints the arg passed first to it here

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
