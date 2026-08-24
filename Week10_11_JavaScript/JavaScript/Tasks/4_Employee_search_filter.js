// Employee Search & Filter

const readline = require("readline")

const rl = readline.createInterface(
    {
        input : process.stdin,
        output : process.stdout
    }
)

function ask(question){
    return new Promise( resolve => {
        rl.question(question , resolve)
    });
}


let employees = [

    {
        id : 101,
        name : "Ajay",
        age : 21,
        department : "ECE",
        salary : 21000
    },
    {
        id : 102,
        name : "eniyan",
        age : 22,
        department : "BRS",
        salary : 50000
    },
    {
        id : 103,
        name : "balaji",
        age : 23,
        department : "AIDS",
        salary : 100000
    },
    {
        id : 104,
        name : "Aswin",
        age : 21,
        department : "ECE",
        salary : 21000
    },
    {
        id : 105,
        name : "Adarsh",
        age : 21,
        department : "ECE",
        salary : 21000
    },

]

async function searchFilter(employees , choice){

    switch (choice){
        case 1: // search employee details by name
            let name = await ask("Enter the name : ");
            console.log(employees.find(emp => emp.name === name));
            break;
        case 2: // filter employees by department
            let department = await ask("Enter the department : ");
            console.log(employees.filter(emp => emp.department === department ));
            break;
        case 3: // filter employees by salary
            let salary = await ask("Enter the Salary : ");
            salary = Number(salary);
            console.log(employees.filter(emp => emp.salary === salary ));
            break;
        case 4: // filter employees by age
            let age = await ask("Enter the age: ");
            age = Number(age);
            console.log(employees.filter(emp => emp.age === age ));
            break;
    }          
}

searchFilter(employees,3)