import * as $ from "jquery";

import { MustHaveCoffee } from './coffee/getcoffee'

class ReallyCoffee extends MustHaveCoffee {
   // coffeeType = 'Bulletproof'
    constructor(){ super() }
    f(input:boolean) {
        let a = 100
        if(input){
            let b = a + 10012
            return b;
        }
        return a;
    }
    setCoffeeType(name:string){
        super.setCoffeeType(name)
        console.log("hello there " + this.coffeeType)
        $("body").css('background-color', 'red')
        $("body").html("<h1>" + this.coffeeType + "</h1>")
    }
}

let newCoffee = new ReallyCoffee()
newCoffee.f(true)
newCoffee.setCoffeeType("I'm just a Regular coffee")

let oldCoffee = new MustHaveCoffee()