interface node<T> {
    next: node<T> | null;
    element: T
}

class LinkedNode<T> implements node<T> {
    element: T
    next: node<T> | null = null
    constructor(element: T, next: node<T> | null = null) {
        this.element = element
        this.next = next
    }
}

class LinkedList<T> {
    length: number = 0
    head: node<T> | null = null
    append(element: node<T>) {
        let node: node<T> = element
        if (this.head === null) {
            this.head = node
        } else {
            let current = this.head
            while (current.next) {
                current = current.next
            }
            current.next = node
        }
        this.length++
    }
}

var testLinkedList = new LinkedList<string>()
testLinkedList.append(new LinkedNode<string>('a'))
testLinkedList.append(new LinkedNode<string>('b'))
testLinkedList.append(new LinkedNode<string>('c'))

// 链表倒叙输出 c b a
// {"length":3,"head":{"next":{"next":{"next":null,"element":"c"},"element":"b"},"element":"a"}}

function printLinkedListReversing (head: node<string>): void {
    let result: string[] = []
    while(head !== null) {
        result.push(head.element)
        head = head.next
    }
    console.log(result.reverse())
}

function printLinkedListReversing_recursion(head: node<string>): void{
    if (head !== null) {
        if (head.next != null) {
            printLinkedListReversing_recursion(head.next)
        }
        console.log(head.element)
    }
}

// function printLinkedListReversing_recursion(head: node<string>, result: Array<string> = []): Array<string> {
//     if (head !== null) {
//         if (head.next != null) {
//             printLinkedListReversing(head.next, result)
//         }
//         result.push(head.element)
//     }
//     return result
// }

console.log(printLinkedListReversing(testLinkedList.head))
console.log(printLinkedListReversing_recursion(testLinkedList.head))