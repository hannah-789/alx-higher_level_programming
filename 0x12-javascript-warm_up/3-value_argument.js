#!/usr/bin/node
// Extract arguments (skip script name and first args[0] || "No argument");
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
