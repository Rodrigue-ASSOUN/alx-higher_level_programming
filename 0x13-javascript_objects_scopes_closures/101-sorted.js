#!/usr/bin/node
const { mainDict } = require('./101-data');

const emptyDict = {};

for (const key in mainDict) {
  const value = mainDict[key];

  if (!(value in emptyDict)) {
    emptyDict[value] = [key];
  } else {
    emptyDict[value].push(key);
  }
}
console.log(emptyDict);
