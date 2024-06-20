#!/usr/bin/node
const args = process.argv.slice(1); // Extract arguments (skip script name)

if (args.length === 0) {
  console.log("No argument");
} else {
  console.log(args[0]); // Print the first argument
}

