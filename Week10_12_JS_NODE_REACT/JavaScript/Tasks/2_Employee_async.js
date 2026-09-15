// 2. Employee Management using Arrays & Objects

// require("readline") -> module given by node.js
const readline = require("readline"); 

// createInterface() ->  creates an interface for communicating with the terminal.
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
}) 


function ask(question){
    return new Promise((resolve) => {
        rl.question(question,resolve);
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


async function employeeManagement(employees,choice){

    switch (choice){
        case 1 :  // display all employees
            employees.forEach(
                (emp) => {console.log(emp)}
            );
            break;
        

        case 2 : // add employee
            let new_employee_obj = {};
            let emp_keys = Object.keys(employees[0]);

            for (let info of emp_keys){
                    let detail = await ask(" Enter the " + info +" : ");
                    if (info === "id" || info === "age" || info === "salary") {
                      detail = Number(detail);
                }
                    new_employee_obj[info] = detail 
            }
            

            employees.push(new_employee_obj);

            console.log(employees);

            break;
        

        case 3 : // total salary
            let total_salary = 0;

            employees.forEach( 
                (emp) => {
                total_salary += emp.salary; 
            });
            console.log(total_salary);

            break;
        

        case 4: // highest salary employee
            let max_salary = 0;
            let max_Salary_employee = null;

            employees.forEach((emp)=> {
            if (emp.salary > max_salary){
                max_salary = emp.salary
                max_Salary_employee = emp
            }
            });
            console.log(max_Salary_employee)
            break;
        

        case 5: // employees from particular department 

            let emp_depart = await ask("Enter the department in captial : ");
            let employee_names = [];
            for(let emp of employees){
                if (emp.department === emp_depart){
                    employee_names.push(emp.name)
                }
            }   

            console.log(employee_names)
    }
}

employeeManagement(employees,4) // Testing here