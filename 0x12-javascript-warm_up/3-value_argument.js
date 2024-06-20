#!/usr/bin/node
// Extract arguments (skip script name and first args[0] || "No argument");
const args = process.argv.slice(1); 

if (args.length === 0) {
  console.log("No argument");
} else {
  console.log(args[0]); 
}

