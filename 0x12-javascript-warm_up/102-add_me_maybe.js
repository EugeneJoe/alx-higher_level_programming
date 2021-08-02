#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  let nb = parseInt(number) + 1;
  theFunction(nb);
}
