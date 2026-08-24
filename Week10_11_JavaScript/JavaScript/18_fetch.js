

async function getAllCustomers(){
    try{
        const response = await fetch("http://127.0.0.1:8000/api/customers")

        if (!response.ok){
            throw new Error("could not fetch resource")
        }

        const data = await response.json()

        const names =  data.map( (customer) => customer.name)

        console.log(names)
    }
    catch(error){
        console.log(error)
    }
}

getAllCustomers();

async function getCustomer(id){
    try{
        const response = await fetch(`http://127.0.0.1:8000/api/customers/${id}`)

        if (!response.ok){
            throw new Error("could not fetch resource")
        }

        const data = await response.json()

        console.log(data)
    }
    catch(error){
        console.log(error)
    }
}

getCustomer(1);