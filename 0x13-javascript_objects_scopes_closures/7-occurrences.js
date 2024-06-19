#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  // Use the reduce function to count occurrences
  return list.reduce(function (count, currentElement) {
    // Check if the current element is equal to the search element
    if (currentElement === searchElement) {
      // Increment the count
      count++;
    }
    return count;
  }, 0);
};
