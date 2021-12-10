class Queue {
  
  constructor(...props){
    this.queue = [];
    this.first = undefined;
    this.last = undefined;
    this.size = 0;
    if(props){
      this.first = props[0];
      this.last = props[props.length -1];
      for (const value of props) {
        this.add(value);
      }
    }
  }

  add(...values){
    this.last = values[values.length -1]
    for (const value of values) {
      this.queue.push(value);
      this.size += 1;
    }
  }

  remove(){
    this.first = this.queue[1];
    this.size -=1;
    return this.queue.shift();
  }

  toString(){
    return `Queue -> [${this.queue.join(', ')}] (size = ${this.size})`
  }
}

const queue = new Queue(1, 2, 3, 4, 5, 0);
queue.add(1,2)
console.log(queue.first)
console.log(queue.last)
console.log(queue.size)
console.log(queue.toString())
console.log('-----')
console.log(queue.remove())
console.log('-----')
console.log(queue.first)
console.log(queue.last)
console.log(queue.size)
console.log(queue.toString())