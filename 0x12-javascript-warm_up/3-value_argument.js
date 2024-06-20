#!/usr/bin/node
// Extract arguments (skip script name and first arg)
const args = process.argv.slice(2)
// Use optional chaining or default value
console.log(args[0] || "No argument");
