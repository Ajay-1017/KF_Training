let stocks = {
    Fruits : ["strawberry", "grapes", "banana", "apple"],
    liquid : ["water", "ice"],
    holder : ["cone", "cup", "stick"],
    toppings : ["chocolate", "peanuts"],
};

let is_shop_open = true;


function time(ms){
    return new Promise( (resolve,reject) => {
        if (is_shop_open){
            setTimeout(()=>{
                resolve()
            },ms)   
        }  
        else{
            reject(console.log("shop is closed"))
        }
    })
}


async function kitchen(){
    try{
    await time(2000)
    console.log(`${stocks.Fruits[0]} was selected`)
    
    await time(0)
    console.log("production has started")

    await time(2000)
    console.log(`${stocks.Fruits[0]} has been chopped`)

    await time(1000)
    console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]} was added`)
    
    await time(1000)
    console.log("machine was started")
    
    await time(2000)
    console.log(`ice cream placed on ${stocks.holder[0]}`)
    
    await time(3000)
    console.log(`${stocks.toppings[0]} was selected`)

    await time(2000)
    console.log("icecream is served") 
    
  }
  catch(error){
    console.log("customer left",error)
  }
  finally{ 
    console.log("day ended shop is closed")
  }
}
kitchen();
