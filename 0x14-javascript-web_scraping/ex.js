#!/usr/bin/node
const array = [1, 2, 3, 4, 5];

array.forEach(function(element, index, arr) {
    console.log(`Element: ${element}, Index: ${index}, Array: ${arr}`);
});

array.forEach((element) => {
    const n = element * 2;
    console.log(n);
})

const number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumber = number.filter(n => n % 2 === 0);
console.log(evenNumber);