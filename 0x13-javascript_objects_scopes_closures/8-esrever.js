#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let i = 0; i < list.length; i++) {
    newlist.unshift(list[i]);
  }
  return newlist;
};
