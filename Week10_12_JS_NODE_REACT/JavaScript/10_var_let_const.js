/*
// 1) 'var' vs 'let' vs 'const'

function sampleFunc(){

    const CONSTANTVAR = "constant";
    // CONSTANTVAR = "trying to the change it"; // refrenceError -> Assignment to constant Variable

    if (true){
    var x = 50;  // it works outside the block because 'var' -> function scoped
    let y = 50;  // it does not work outside block because 'let' -> block scoped
}

    console.log(x); // works 
    console.log(y); // referenceError
}

console.log(sampleFunc())

*/

let i = 0;
while (i < 5){
    console.log(i);
    i++;
}

// 2) Mutate a array declared with constant 

const ARR = [5,6,7]

function mutateArr(){

    // ARR = [1,2,3]; // TypeError: Assignment to constant variable.

    // we can mutate constant variable
    ARR[0] = 1;
    ARR[1] = 2;
    ARR[2] = 3;

    return ARR
}

console.log(mutateArr())


// prevent object mutation

function freezeObject(){
    "use strict";
    const constants = {
        PI : 3.14
    };

    Object.freeze(constants); // prevent data mutation

    try{
        constants.PI = 99;
    }
    catch (ex){
        console.log(ex)
    } 

    return constants.PI

}

const PI = freezeObject()

console.log(PI)