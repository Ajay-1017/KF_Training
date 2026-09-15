let stocks = {
    Fruits : ["strawberry", "grapes", "banana", "apple"],
    liquid : ["water", "ice"],
    holder : ["cone", "cup", "stick"],
    toppings : ["chocolate", "peanuts"],
};

let is_shop_open = true;


let toppings_choice = () => {
    return new Promise((resolve,reject) =>{
        if (is_shop_open){
            setTimeout( () => {
                resolve(
                console.log("which topping would you have?")
                )
            },3000)
            
        }
        else{
            reject()
         }
    })
}


async function kitchen(){
    console.log(" A ")
    console.log(" B ")
    console.log(" C ")
    await toppings_choice()
    console.log(" D ")
    console.log(" E ")
}

kitchen();
console.log(" cleaning the dishes ");
console.log(" cleaning the tables ");
console.log(" taking orders ");