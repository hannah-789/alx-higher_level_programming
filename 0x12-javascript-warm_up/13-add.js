#!/usr/bin/node
function add(a, b) {
  // Implicit type coercion with `+` for potential non-numeric inputs
  return Number(a) + Number(b);
}

// This makes the function accessible outside the current scope (module)
module.exports = add;
