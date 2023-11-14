#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dic = {};
for (const key in dict) {
  if (dic[dict[key]] === undefined) {
    dic[dict[key]] = [key];
  } else {
    dic[dict[key]].push(key);
  }
}
console.log(dic);
