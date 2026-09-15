// 1) while loop

var arr = [];
var i = 0;

while (i < 5){
    arr.push(i+1);
    i++;
}

console.log(arr) // o/p -> [1,2,3,4,5]




// 2) for loop 

var arr=[];

for (var i = 0 ; i<5; i+=2 ){
    arr.push(i);
}
console.log(arr); // o/p -> [0,2,4]


// 2.a) count backwards

var arr = [];

for (var i =10  ; i > 0 ; i-=2){
    arr.push(i);
}
console.log(arr);

// 2.b) adding arr items

var arr = [2,4,6,8];
var total  = 0;
for ( var  i = 0 ; i < arr.length ; i++){
    total += arr[i];
}
console.log(total)



// 3) nested forloop

function MutiplyAll(arr){
    var product = 1;
    for (var i = 0 ; i < arr.length ; i++){
        for (var j = 0 ; j< arr[i].length ; j++)
        {
            product*= arr[i][j];
        }
    }
    return product;
}

var arr = [[1,2],[3,4,5],[6,7]];
console.log(MutiplyAll(arr));


// 4) do while loop
 
var arr = [];
var  i = 10;

do {
    arr.push(i);
    i++;
} while (i<5)

console.log(i,arr);



