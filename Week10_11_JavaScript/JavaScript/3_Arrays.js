// 1) Array
var arr = ["hello",7];
console.log(arr);


// 2) Nested Array
var nestedArr = [["hello",1],["world",2]];
console.log(nestedArr);


// 3) Acessing element from an array
myArrData = arr[0];
console.log(myArrData);

myNestedArrData = nestedArr[1][1];
console.log(myNestedArrData);


// 4) Modify the existing array
arr[1] = "world";
console.log(arr);
nestedArr[0][1] = 7;
console.log(nestedArr);


//=================================================
// 5) Array Methods 
//=================================================

// 5.a) push() -> add element to the 'end' of the array
arr.push("push -> end");
console.log(arr);


// 5.b) unshift() -> add element to the 'beginning' of the array
arr.unshift('unshift -> beginning');
console.log(arr);


// 5.c) pop() -> delete the 'last' element from the arr
arr.pop();
console.log(arr);


// 5.d) shift() -> delete the 'first' element of the arr 
arr.shift();
console.log(arr);




