// ====================================================
// 1) if
// ====================================================

function trueOrFalse(isItTrue){
    if (isItTrue){
        return true;
    }
    return false;
}
console.log(trueOrFalse(true));

// ----------------------------------------------------
// 1.a)Equality vs strict Equality operator
// ----------------------------------------------------

// equality operator 
function testEqual(value){
    if (value == 12){
        return "equal";
    }
    return "not equal";
}
console.log(testEqual('12')); // do the type conversion of str -> int while checking and condition becomes true

  
// strict equality operator 
function testStrict(value){
    if (value === 12){
        return "equal";
    }
    return "not equal";
}
console.log(testStrict('12')); // does not do the type conversion for checking values and condition becomes false


// ----------------------------------------------------
// 1.b)InEquality vs strict InEquality operator
// ----------------------------------------------------

// InEquality  operator 
function testNotEqual(value){
    if (value != 12){
        return "not equal";
    }
    return "equal";
}
console.log(testNotEqual('12')); // do the type conversion of str -> int while checking and condition becomes true

  
// strict InEquality operator 
function testStrictNotEqual(value){
    if (value !== 12){
        return "not equal";
    }
    return "equal";
}
console.log(testStrictNotEqual('12')); // does not do the type conversion for checking values and condition becomes false


// ====================================================
// 2) else and else if 
// ====================================================

/* 
if (condition){statements}
else if {statements}
else{statements}
*/ 


// ====================================================
// 3) logical operators 
// ====================================================

/*

    python -> javaScript
    and -> &&
    or -> ||

    >= , > , <= , < -> same as python 
*/

// ====================================================
// 4) Excerise
// ====================================================

var names = ["hole-in-one", "eagle", "birdie","par","bogey","double bogey","go home!"];

function golfScore(par,strokes){
    if (strokes == 1){
        return names[0];
    } else if(strokes<=par-2) {
        return names[1];
    } else if(strokes<=par-1) {
        return names[2];
    } else if(strokes == par) {
        return names[3];
    } else if(strokes == p+1) {
        return names[4];
    } else if(strokes == par+2) {
        return names[5];
    } else if(strokes >= par+3) {
        return names[6];
    } else {                
        return "change me"
    }
}

console.log(golfScore(3,2));


// 5) ternary operator -> one line if else Expression

/*
condition ? statement-if-true : statement-if-false
*/

function checkEqual(a,b){
    return a===b ? true : false;
}
console.log(checkEqual(1,2))

function checkSign(a){
    return a>0 ? "positive" : a<0 ? "negative" : "zero";
}
console.log(checkSign(90))