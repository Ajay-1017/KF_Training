
// 1) Math.random(); -> returns random number between 0 to 1

function randomFraction(){
    return Math.random(); // returns random number between 0 to 1
}
console.log(randomFraction());


// 2) Random whole numbers

function randomWhole(){
    randomNumBetween0and19 = Math.floor(Math.random() * 20); 
    return randomNumBetween0and19 
}
console.log(randomWhole());

// 3) Random whole numbers within a range

function ourRandomRange(myMin , myMax){
    return Math.floor(Math.random() * (myMax - myMin + 1)) + myMin;
}
console.log(ourRandomRange(1,9))