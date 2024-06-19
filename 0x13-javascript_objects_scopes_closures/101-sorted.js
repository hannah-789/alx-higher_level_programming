#!/usr/bin/node

const { dict } = require('./101-data'); // Adjust the file name accordingly

// Function to flip the dictionary and group user ids by occurrence
function flipDictionary(originalDict) {
  const flippedDict = {};

  for (const userId in originalDict) {
    const occurrences = originalDict[userId];

    if (!flippedDict[occurrences]) {
      flippedDict[occurrences] = [];
    }

    flippedDict[occurrences].push(userId);
  }

  return flippedDict;
}

// Use the flipDictionary function to create a new dictionary
const newUserDict = flipDictionary(dict);

// Print the new dictionary
console.log(newUserDict);
