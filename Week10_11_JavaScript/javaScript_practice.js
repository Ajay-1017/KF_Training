
const readline = require("readline");


const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});

// question("question", callback func)
rl.question("Enter you Name : ",(answer) => console.log(answer))

// flow : 
            // rl.question()
            //        ↓
            // "Enter your name:"
            //        ↓
            // program waits for user
            //        ↓
            // user enters "Ajay"
            //        ↓
            // callback function runs
            //        ↓
            // answer = "Ajay"


function ask(question){
    return new Promise((resolve) => {
        rl.question(question,resolve)
    });
}