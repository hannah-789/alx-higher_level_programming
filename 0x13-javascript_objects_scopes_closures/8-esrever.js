#!/usr/bin/node

exports.esrever = function (list) {
  // Check if the input is an array
  if (!Array.isArray(list)) {
    throw new Error('Input is not an array.');
  }

  const reversedList = [];
  
  // Iterate over the original list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};

