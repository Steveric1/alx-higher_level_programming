#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: 1-writeme.js <file> <text>');
  process.exit(1);
}

fs.writeFile(process.argv[2], process.argv[3], 'utf8', (error) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }
  console.log('The file has been saved!');
});
