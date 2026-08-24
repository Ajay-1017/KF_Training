
class SpaceShuttle{
    constructor(targetplanet){
        this.targetplanet = targetplanet
    }
}

zeus = new SpaceShuttle("jupiter")
console.log(zeus.targetplanet)


// getter and setter

class Person {

    constructor(age) {
        this._age = age;
    }

    get age() {
        return this._age;
    }

    set age(value) {

        if (value < 0) {
            console.log("Age cannot be negative");
        } else {
            this._age = value;
        }
    }
}

const person = new Person(21);

console.log(person.age);

person.age = -10;

console.log(person.age);