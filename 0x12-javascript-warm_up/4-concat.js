#!/usr/bin/node
const args = process.argv;

if  (args.length === 4) {
    const result = args[2] + ' is ' + args[3];
    console.log(result);
}
