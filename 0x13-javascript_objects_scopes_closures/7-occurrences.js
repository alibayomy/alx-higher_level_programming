exports.nbOccurences = function (list, searchElement) {
  let sum = 0;
  for (const i of list) {
    if (i === searchElement) { sum++; }
  }
  return sum;
};
