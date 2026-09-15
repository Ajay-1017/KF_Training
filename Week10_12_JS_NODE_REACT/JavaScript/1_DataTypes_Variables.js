
// ============================================================================
// 1) Comment
// ============================================================================

// in-line comment

/* this is a
multi line comment */



// ============================================================================
// 2) DataTypes and variables
// ============================================================================

/*
    1. undefined -> something hasn't been defined 
    2. null -> Nothing
    3. boolean -> True / False
    4. string -> text
    5. symbol -> immutable primitive value thats is unique
    6. number -> integer
    7. object -> key value pair
*/


var myName = "Ajay";     // used in whole program
let ourName = "youtube"; // only be used within the scopes of where you declare that
const pi = 3.14; // variable should never change -> if change gets error


// 2.a) variables

var a;      // declaration
console.log(a);
a = 2;      // assignment

var b = 5;  // declaration + initialization

a = b;
console.log(a);

// 2.b) case sensitive

// "use strict"  // -> UnComment to get case sensitive refrence error
var cAseSenSitive = 20;
casesensitive = 100; // gets error because variables are case sensitive
console.log(casesensitive);


// ============================================================================
// 3) Basic Math
// ============================================================================

var sum = 10 + 10;
console.log(sum);

var substraction = 10 -2;
console.log(substraction);

var multiply = 10 * 2;
console.log(multiply);

var remainder = 10 % 3;
console.log(remainder);

// incrementing and decrementing a number
var num1 = 1;
num1++; // num1--
console.log(num1); 


