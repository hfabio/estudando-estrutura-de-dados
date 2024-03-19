class Node {
    left = null;
    right = null;
    value = null
    constructor(value, left, right){
        this.value = value;
        this.left = left;
        this.right = right;
    }
}
class Tree {
    root = null
    constructor(root){
        this.root = root;
    }

    read(node = this.root){
        let values = [];
        if(!node) return [];
        if(node.left) values.push(...this.read(node.left));
        if(node.right) values.push(...this.read(node.right));
        values.push(node.value);
        return values;
    }
}
class Solution {
    constructor(){
        this.tree = new Tree();
        this.addNodes();
    }
    addNodes(){
        if(!this.tree) this.tree = new Tree();
        const left = new Node(2, new Node(1), new Node(3));
        const right = new Node(7, new Node(6), new Node(9));
        this.tree.root = new Node(4, left, right);
    }

    invert(node = this.tree.root){
        if(node){
            if(node.left) this.invert(node.left);
            if(node.right) this.invert(node.right);
            [node.left, node.right] = [node.right, node.left]
        }
    }
}

const solution = new Solution();
console.log(solution.tree.read());
solution.invert();
console.log(solution.tree.read());
