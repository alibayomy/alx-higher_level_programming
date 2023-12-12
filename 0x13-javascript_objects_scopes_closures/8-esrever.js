#!/usr/bin/node
exports.esrever = function (list) {
    let newLst = [];
    for (let i = list.length -1; i >=0; i--)
        newLst.push(list[i]);
    return newLst
}
