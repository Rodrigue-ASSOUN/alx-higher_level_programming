const fs = require('fs');

// The first argument is the file path
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', function (err, data) {
  if (err) {
    // If an error occurred during the reading, print the error object
    console.error(err);
  } else {
    // The content of the file must be read in utf-8
    console.log(data);
  }
});
