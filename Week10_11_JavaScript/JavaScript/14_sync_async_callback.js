// Refer this link to understand this : https://www.freecodecamp.org/news/javascript-async-await-tutorial-learn-callbacks-promises-async-await-by-making-icecream/

/*
// sychronous

console.log(" I ");

console.log(" eat ");

console.log(" Ice Cream ");


// Asychronous

console.log(" I ");

setTimeout(() =>{
console.log(" Ice Cream ");
},2000);

console.log(" eat ");

*/

// call back 

// backend
let stocks = {
    Fruits : ["strawberry", "grapes", "banana", "apple"],
    liquid : ["water", "ice"],
    holder : ["cone", "cup", "stick"],
    toppings : ["chocolate", "peanuts"],
 };


const order = (fruit_name , call_production) => {
    setTimeout(() =>{
        console.log(`${stocks.Fruits[fruit_name]} was selected`)
        call_production();
    },2000)
   
};

// callback hell
const production = () => {
        setTimeout(() =>{
            console.log("production has started")   

            setTimeout(()=>{
                console.log("fruit has been chopped") 

                setTimeout(()=>{
                    console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]} was added`) 

                    setTimeout(()=>{
                        console.log("machine was started")  

                        setTimeout(()=>{
                            console.log(`${stocks.holder[0]}`) 

                            setTimeout(()=>{
                                console.log(`${stocks.toppings[0]}`) 

                                setTimeout(()=>{
                                    console.log("icecream is served") 
                        },2000)
                    },3000)
                },2000)
            },1000)
        },1000)
    },2000)
},0)
};

order(0,production);