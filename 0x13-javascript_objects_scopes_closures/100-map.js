#!/usr/bin/node

const { list } = require('./100-data'); // Adjust the file name accordingly

// Use the map function to create a new array with values multiplied by their index
const newList = list.map((value, index) => value * index);

// Print the initial list
console.log('Initial List:', list);

// Print the new list
console.log('New List:', newList);
