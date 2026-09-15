// 1) function 
function sampleFunction(){ // function definition 
    console.log("Hello world");
}
sampleFunction(); //function calling



// 2) Passing values to the function with arguments
function funcWithArgs(a,b) { // (a,b) -> parameters
    console.log(a+b);
}

funcWithArgs(5,10); // (5,10) -> arguments 



// 3) global variables and scopes
var myGlobal = 10;

function func1(){
    oopsGlobal = 5; // without var keyword it automatically becomes var keyword
}

function func2(){
    if (typeof myGlobal != undefined){
        console.log("Global :",myGlobal);
    }

    if (typeof oopsGlobal != undefined){
        console.log("oopsGlobal :",oopsGlobal);
    }
}

func1();
func2();



// 4) local scope
function funcWithLocalScope(){
    var myvar = "hello World"; // this variable visible only to this function not outside the function
    console.log(myvar);
}

funcWithLocalScope();
//console.log(myvar); // It gives Reference Error because it try to access the function variable outside the function



// 5) Global vs local scope
var myvar = "global"

function myfunc(){
    var myvar = "local"; // local variable take over the precedence
                         // (priority to handle first) of global variable
    console.log(myvar);
}

myfunc();
console.log(myvar);



// 6) return 
function returnFunc(message){
    return {"message" : message};
}

console.log(returnFunc("Hello World"));


// 7) StandInLine Exercise

function nextInline(arr,item){
    arr.push(item);
    return arr.shift();
}

arr = [1,2,3,4,5];
console.log("Before :",JSON.stringify(arr));
console.log(nextInline(arr,6));
console.log("After :",JSON.stringify(arr));


// 8) Boolean values

function booleanFunc(val){
    if (val > 20){
    return true;
    } else {
        return false;
    }
}
console.log(booleanFunc(21));

// alternative simple method
function booleanFunc(val){
    return val > 20;
}
console.log(booleanFunc(21));



// 9) square root of (sum of squares)function
function root_squares(a,b){
    return Math.round(
        Math.sqrt(
            (Math.pow(a,2) + Math.pow(b,2))
        )
    );
}
console.log(root_squares(2,3))


// 10) ParseInt function -> convert string to integer

function convertStrToInt(str){
    return parseInt(str)
}
console.log(convertStrToInt("56"))
console.log(convertStrToInt("aeiou"))
console.log(convertStrToInt(56))


// 10.a) ParseInt function with radix

function convertStrToInt(str){
    return parseInt(str,2)
}
console.log(convertStrToInt("10"))
