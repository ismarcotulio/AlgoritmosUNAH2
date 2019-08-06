function LinkedList(){
	this.first = null;
	this.add = addLinkedList;
}

	function addLinkedList(value){
		var compare = new Compare();
		if(!this.first){
			this.first = new Node(value);
		}else{
			if(compare.compare(this.first,value)>0){
				var stack = this.first;
				this.first = new Node(value);
				this.first.next = stack;
				return true;
			}else if(compare.compare(this.first,value)==0){
				var stack = this.first.next;
				this.first = new Node(value);
				this.first.next = stack;
			}else{
				var previous = this.first;
				current = this.first.next;

				while(current){
					if(compare.compare(current, value)<0){
						previous = current;
						current = current.next;
					}else if(compare.compare(current, value)>0){
						var stack = current;
						previous.next = new Node(value);
						previous.next.next = stack;
					}else{
						var stack = current.next;
						previous.next = new Node(value);
						previous.next.next = stack;
					}
				}
				previous.next = new Node(value);
				return true;
			}
		}
	} 