// objects

var myDog = {
    "name" : "Julie", // "name" -> property , "Julie" -> property value
    "legs" : 4,
    "tails": 1,
    "friends" : ["me","mom"]
};

console.log(myDog);

// 1) Accessing object properties using "dot notation"

var nameValue = myDog.name;
var legsValue = myDog.legs;

console.log(nameValue + " has " + legsValue + " legs ");



// 2) Acessing Object Properties using "Bracket Notation"

var friendsValue = myDog["friends"][0];
console.log(friendsValue);


// 3) Accessing Object Properties with variables
// Use bracket notation when the property name is stored inside a variable.
// Known property name -> dot notation or bracket notation

/*

Fixed, valid property name
        ↓
    obj.name
        ↓
   Dot notation


Dynamic ("The property I want can change depending on a variable/value.") /  unusual property name 
        ↓
    obj[key]
        ↓
 Bracket notation

*/

var players  = {
    7 : "ajay",
    10 : "eniyan",
    11 : "anirudh"
}

var jerseyNumber = 7;
console.log(players[jerseyNumber]);


// 4) updating , adding , deleting the object properties

var myDog = {
    "name" : "Julie", // "name" -> property , "Julie" -> property value
    "legs" : 4,
    "tails": 1,
    "friends" : ["me","mom"]
};

myDog.name = "shaggy"; // updating a property
myDog.bark = "bow-bow"; // adding a property
delete myDog.tails; // deleting a property
console.log(myDog);


// 5) hasOwnProperty method -> check the value is property or not 

myObj = {
    gift : "pony",
    pet : "kitten",
    bed : "sleigh"
};

function checkPropery(propName){
    if ( myObj.hasOwnProperty(propName) ) {
        return myObj[propName];
    }
    return "Not Found";
}

console.log(checkPropery("gift"));
console.log(checkPropery("hello"));


// 6) Manipulating complex objects

// 6.a) array of objects
var myMusic = [
                        
    {
        "artist": "Billy Joel",
        "title": "Piano Man",
        "release_year": 1973,
        "formats": [
            "CD",
            "8T",
            "LP"
        ],
        "gold": true
    },
    {
    "artist": "Michael Jackson",
    "title": "Thriller",
    "release_year": 1982,
    "formats": [
        "CD",
        "Cassette",
        "LP"
    ],
    "gold": true
}
]

MichaelJacksonFormatsFirst= myMusic[1].formats[0];
console.log(MichaelJacksonFormatsFirst);


// 6.b) nested objects
var myStorage = {
    "car": {
        "inside": {
            "glove box": "maps",
            "passenger seat": "crumbs"
        },
        "outside": {
            "trunk": "jack"
        }
    }
};

passengeSeatValue = myStorage.car.inside["passenger seat"];
console.log(passengeSeatValue);


// Exercise -> Record Collection 

collection ={

    "1245": {
    "album": "Blue",
    "artist": "LeAnn Rimes",
    "tracks": [
        "Blue",
        "How Do I Live"
    ]
},


"5439": {
    "album": "The Dark Side of the Moon",
    "artist": "Pink Floyd",
    "tracks": []
},


"6789": {
    "album": "Thriller",
    "artist": "Michael Jackson",
    "tracks": [
        "Beat It",
        "Billie Jean",
        "Thriller"
    ]
},


"9012": {
    "album": "Back in Black",
    "artist": "AC/DC",
    "tracks": [
        "Hells Bells",
        "Shoot to Thrill"
    ]
},

"3456": {
    "album": "Abbey Road",
    "artist": "The Beatles",
    "tracks": [
        "Come Together",
        "Something",
        "Here Comes the Sun"
    ]
}

}

copyCollection = JSON.parse(JSON.stringify(collection))


function updateRecords(id , prop , value){

    if (value === "") {
    delete collection[id][prop];
    } else if (prop === "tracks") {
    collection[id][prop] = collection[id][prop] || [];
    collection[id][prop].push(value);
    }
    else{
         collection[id][prop] = value;
    }
    return collection;
}

updateRecords(5439 , "tracks" , "test track");
updateRecords(5439 , "album" , "ajay's album");

console.log(collection["5439"]);