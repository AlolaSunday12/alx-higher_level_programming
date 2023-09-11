#!/usr/bin/node
const argc = process.argv.length;

if (argc === 2) {
console.log('Argument found');
} else if (argc > 2) {
console.log('Arguments found');
} else {
console.log('NO argument');
}
