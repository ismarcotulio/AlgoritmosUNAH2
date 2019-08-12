function LinkedList(){
    this.first = null;
    this.add = LinkedListAdd;
}

    function LinkedListAdd(value){
        if(!this.first){
            this.first = new Node(value);
        }else{
            var compare = new Compare();
            if (compare.compare(this.first, value)>0){
                var stack = this.first;
                this.first = new Node(value);
                this.first.next = stack;
                return true;
            }else if(compare.compare(this.first,value)==0){
                var stack = this.first.next;
                this.first = new Node(value);
                this.first.next = stack;
                return true;
            }else{
                var 
                    previous = this.first,
                    current = this.first.next
                ;

                while (current){
                    if(compare.compare(current,value)<0){
                        previous = current;
                        current = current.next;
                        return true;
                    }else if (compare.compare(current,value)>0){
                        var stack = current;
                        previous.next = new Node(value);
                        previous.next.next = stack;
                        return true;
                    }else{
                        previous.next = new Node(value);
                        previous.next.next = current.next;
                        return true;
                    }
                }

                previous.next = new Node(value);
                return true;
            }
        }
    }