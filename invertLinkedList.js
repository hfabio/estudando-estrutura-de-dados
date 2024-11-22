class Node {
    data = null;
    next = null;
    constructor(data, next){
        this.data = data || null
        this.next = next || null;
    }
    toString(){
        console.log(this?.data);
        this?.next?.toString();
    }
    clone(){
        return new Node(this.data)
    }
}

let linkedList = new Node();
let currentNode = linkedList;

for(let i = 0; i < 10; i++){
    currentNode.data = `element ${i}`;
    const nextNode = new Node();
    currentNode.next = nextNode;
    currentNode = nextNode;
}
console.log('linked list:');
linkedList.toString();

let invertedLinkedList = linkedList.clone();
let travessing = linkedList.next;
while(travessing.next && travessing.data){
       const cloneNode = travessing.clone();
        cloneNode.next = invertedLinkedList;
        invertedLinkedList = cloneNode;
        travessing = travessing.next;
}
console.log('inverted linked list:')
invertedLinkedList.toString()
