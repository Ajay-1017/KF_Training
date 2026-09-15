
//=====================================================
// 1) Rest and spread operator
//=====================================================


// Rest Operator with function parameters  (collect / pack the elements)

const sum = (...args) => {
    return args.reduce( (total,num) => total + num , 0 )
} 

console.log(sum(1,2,3,4,5));


// use spread operator to evaluate the arrays in place (... expands/unpacks the elements.)

const arr1 = ['JAN', 'FEB' , 'MAR', 'APR','MAY']
let arr2;

(function(){
    arr2 = [...arr1] // spreads the elements of arr1 into the new array instead of just pointing to same array
    arr1[0] = "potato"
})();

console.log(arr1)
console.log(arr2)


//=====================================================
// 2) destructuring assignment  
/*
    syntax:
    const { originalName: newVariableName } = object;
*/
//=====================================================


// normal way to assign a variables from object

/*

let temperatures = {today : 35 , tommorow : 37 , dayAfterTommorow : 38 };

let today = temperatures.today;
let tommorow = temperatures.tommorow;
let dayAfterTommorow = temperatures.dayAfterTommorow;

console.log(today , tommorow , dayAfterTommorow)


*/


// 2.a) Assign variables from 'objects' using destructuring assignment 
let temps = {today : 35 , tommorow : 37 , dayAfterTommorow : 38 };

const {today : tdy , tommorow : tmwr , dayAfterTommorow : dayAfterTmwr } = temps;

console.log(tdy , tmwr , dayAfterTmwr)


// 2.b) Assign variables from 'nest objects' using destructuring assignment 
let temp = {today : {max :35 , min : 27} , tommorow : {max :37 , min : 23} , dayAfterTommorow : {max :38, min : 30} };

const {tommorow : {max : tmwrMax}} = temp

console.log(tmwrMax)


// 2.c) Assign variables from 'array' using destructuring assignment 

const [x,y,,,z] = [1,2,3,4,5,6];
console.log(x,y,z)  // x = 1 , y = 2 , z = 3

let a = 5 , b = 6;

( () =>{
    [a,b] = [b,a]
})();

console.log(a);
console.log(b);


// 2.d) Assign variables from 'rest operator' using destructuring assignment 

const source = [1,2,3,4,5,6,7,8,9,10];

function removeFirstTwo(list){
    const [, ,...arr] = list;
    return arr
}

const arr = removeFirstTwo(source);

console.log(arr);
console.log(source);



// 2.e) pass an object as an function's parameters using destructuring assignment 

const stats = {
    max: 56.78,
    standard_deviation: 4.34,
    median: 34.54,
    mode: 23.87,
    min: -0.75,
    average: 35.85
};

const half = (function() {

    return function half({ max, min }) {
        return (max + min) / 2.0;
    };

})();

console.log(stats);
console.log(half(stats));



//=====================================================
// 3) Template literals 
//=====================================================

const person = {
    name : 'Ajay',
    age : 21
}


const greetings = (
`hello, my name is "${person.name}!".
I am ${person.age} years old.`
)

console.log(greetings)



//=====================================================
// 3) Simple Fields
//=====================================================

const createPerson = (name , age , gender) => {

    // unwanted repeatition in fields thats y we use simple fields here
    return {
        name : name,
        age : age,
        gender : gender
    }
}

console.log(createPerson("Ajay",21,"Male"))

// simple fields
const simplefieldPerson = (name , age , gender) => ( { name , age, gender })
console.log(createPerson("priyanka",28,"Female"))

//=====================================================
// 4) declarative functions
//=====================================================

const bicycle = {
    gear : 2,
    setgear(newGear){
        this.gear = newGear
    }
}

bicycle.setgear(3);
console.log(bicycle.gear);