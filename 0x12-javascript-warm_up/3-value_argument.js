#!/usr/bin/node

function printFirstArgument() {
  // Check if there are any arguments using process.argv property
  if (process.argv.length > 2) {
    // Print the first argument (index 2, as process.argv[0] is the script path and process.argv[1] is the path to the script)
    console.log(process.argv[2]);
  } else {
    // No arguments passed, print "No argument"
    console.log("No argument");
  }
}
