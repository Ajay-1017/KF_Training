// 1) declare a string 
var str = "hello world!";
console.log(str);


// 2) Escaping literal quotes in string 
var mystr = "I am a \"double quoted\" string inside \"double quotes\" ";
console.log(mystr);


// 3) Backticks
var mystr = `I am a "double quoted" string inside "double quotes"`;
console.log(mystr);


// 4) Escape sequence
var mystr ="Firstline\n\t\\secondline\nthirdline";
console.log(mystr);


// 5) concate string 
var mystr = "I am come First " + "I am second";
console.log(mystr);

var mystr = "Hello ";
mystr+= "world";
console.log(mystr);


// 6) length of string
var myname = "AjayBalu";
var mylength;
mylength = myname.length;
console.log(mylength);


// 7) Bracket Notation 
var myName = "AjayBalu";
console.log(myName[3]);
console.log(myName[myName.length - 1]);


// 8) Exercise for string
function worldBlanks(myNoun,myAdjective,myVerb,myAdverb){
    var result = "";
    result += "The " + myAdjective + " " + myNoun + " " + myVerb + " to the store " + myAdverb;
    return result;
}

console.log(worldBlanks("dog","big","ran","quickly"));
