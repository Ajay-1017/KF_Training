

let cart_items = [
    {
        name : "keyboard",
        price : 1200,
        quantity : 10
    },
    {
        name : "mouse",
        price : 200,
        quantity : 20
    },
    {
        name : "phone",
        price : 10000,
        quantity : 5
    }
]


function shoppingCart(cart_items){

    let item_total ; 
    let discount_amount = 0 ;
    let final_amount ;

   let products = cart_items.map( product => {

        let product_name = product.name
        
        let product_price = product.price

        let product_quantity = product.quantity

        // product item_total
        item_total = product.price * product.quantity;

        // discount item_total
        discount_amount =  item_total * 0.10;


        return {
            product_name,
            product_price,
            product_quantity,
            item_total,
            discount_amount,
        }
    });
  
    // Calculate cart totals (accumulation)
    let cart_total = products.reduce((total, product) => {
        return total + product.item_total;
    }, 0);

    let total_discount = products.reduce((total, product) => {
        return total + product.discount_amount;
    }, 0);

    let final_cart_amount = cart_total - total_discount;


    return {
        product_detail: products,

        cart_detail: {
            cart_total,
            total_discount,
            final_cart_amount
        }
    };
}

console.log(shoppingCart(cart_items));

// //final amount
// final_amount = item_total - discount_amount;

// // cart_total 
// cart_total  +=  item_total