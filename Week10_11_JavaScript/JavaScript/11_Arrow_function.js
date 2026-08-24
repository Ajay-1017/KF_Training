
/*
syntax :

Python      → lambda parameters : expression
JavaScript  → (parameters) => expression

Example:
Python      → lambda x: x * 2
JavaScript  → (x) => x * 2

*/

// -------------------------------------------------------
// 1) Arrow functions to write concise anonymous functions
// -------------------------------------------------------


// anonymous function
var magic1 = function(){
    return new Date();
}
console.log(magic1())

// arrow function
const magic2 =  () => new Date();
console.log(magic2())


// -------------------------------------------------------
// 2) Arrow functions with parameters
// -------------------------------------------------------

// anonymous function
var myConcat1 = function(arr1,arr2){
    return arr1.concat(arr2);
}
console.log(myConcat1([1,2],[3,4,5]));

// arrow function
const myConcat2 = (arr1,arr2) => arr1.concat(arr2);
console.log(myConcat2([0,9,8,7],[6,5]))


// -------------------------------------------------------
// 3) Higher order arrow function
// -------------------------------------------------------


// filter → Which elements do I want?  (SELECT)
// map    → What should each element become? (TRANSFORM)
// reduce → How do I combine everything into one result? (COMBINE)


// flow chart of below function

// [4, 5.6, -9.8, 3.14, 42, 6, 8.34, -2]
//                     ↓
//                   filter
//                     ↓
//                 [4, 42, 6]
//                     ↓
//                    map
//                     ↓
//              [16, 1764, 36]
//                     ↓
//                  reduce
//                     ↓
//                   1816


realNumberArray = [4, 5.6, -9.8, 3.14, 42, 6, 8.34, -2];

const squareOfSum = (arr) => {
    const squaredSum = arr
    .filter(num => Number.isInteger(num) && num > 0)
    .map(num => num * num)
    .reduce((total , num) => total + num , 0)
    return squaredSum
}

console.log(squareOfSum(realNumberArray))

