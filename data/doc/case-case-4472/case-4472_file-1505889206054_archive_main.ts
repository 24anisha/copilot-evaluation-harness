import { MustHaveCoffee } from './src/coffee/getcoffee'

function f(input:boolean) {
    let a = 100
    if(input){
        let b = a + 10012
        return b;
    }
    return a;
}

console.log(f(true))
console.log(f(false))

let coffee = new MustHaveCoffee()