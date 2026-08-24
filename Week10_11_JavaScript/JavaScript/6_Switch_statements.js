
// 1) Syntax

/*             
JavaScript:                     Python:

switch (val){                   match val :
    default:                        case _: -> default
        statements;                     statements
        break;
    case 1 :                        case 1 :
        statements;     ->              statements  
        break;                      
    case 2 :                        case 2:   
        statements;                     statements
        break;
}

*/

function caseInSwitch(val){
    var answer = "";

    switch (val){
        default:
            answer = "default";
            break;
        case 1 : 
            answer = "hello";
            break;
        case 2:
            answer = "beta";
            break;
        case 3:
            answer = "gamma";
            break;
        
    }
    return answer;
}

console.log(caseInSwitch(2));


// 2) Mutiple Indentical options in switch statements

function squentialSize(val){
    var answer="";
     
    switch (val){
        default:
            answer="default"
        case 1:
        case 2:
        case 3:
            answer = "low";
            break
        case 4:
        case 5:
        case 6:
            answer = "mid";
            break
        case 7:
        case 8:
        case 9:
            answer = "high";  
            break;      
    }

    return answer;

}
console.log(squentialSize(4));


