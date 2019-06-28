
function Node(item, next = null){
	this.item = item;
	this.next = next;

	this.getItem = NodeGetItem;
	this.getNext = NodeGetNext;
	this.setItem = NodeSetItem;
	this.setNext = NodeSetNext;
}
	function NodeGetItem(){
		return this.item;
	}
	function NodeGetNext(){
		return this.next;
	}
	function NodeSetItem(item){
		this.item = item;
	}
	function NodeSetNext(next){
		this.next = next;
	}

function LinkedList(){
	this.first = new Node(null);
	this.last = null;
	this.numItems = 0;

	this.getItem = LinkedListGetItem;
	this.setItem = LinkedListSetItem;
	this.add = LinkedListAdd;
	this.append = LinkedListAppend;
	this.insert = LinkedListInsert;
	this.print = LinkedListPrint;
}
	function LinkedListSetItem(index){}
	function LinkedListGetItem(index, item){}
	function LinkedListAdd(other){
		ll = new LinkedList();
		cursor = this.first.getNext();
		while(cursor != null){
			ll.append(cursor.getItem());
			cursor = cursor.getNext();
		}
		cursor = other.first.getNext();
		while(cursor != null){
			if(cursor.item){
				ll.append(cursor.getItem());
			}
			cursor = cursor.getNext();
		}
		return ll;
	}
	function LinkedListAppend(item){
		cursor = this.first;
		if(cursor.getNext() != null){
			while(cursor.getNext() != null){
				cursor = cursor.getNext();
			}
			node = new Node(item);
			cursor.setNext(node);
			this.numItems += 1;
		}else{
			node = new Node(item);
			cursor.setNext(node);
			this.numItems += 1;
		}
	}
	function LinkedListInsert(index, item){
		if(index < this.numItems){
			cursor = this.first;
			for (var i = 0; i < index; i++) {
				cursor = cursor.getNext();
			}
			node = new Node(item, cursor.getNext());
			cursor.setNext(node);
			this.numItems += 1;
		}else{
			this.append(item);
		}
	}
	function LinkedListPrint(){
		cursor = this.first;
		console.log(" ");
		while(cursor != null){
			if(cursor.item){
				console.log(cursor.item.identity);
			}
			cursor = cursor.getNext();
		}
	}

function Person(identity, name){
	this.identity = identity;
	this.name = name;
}

function main(){
	Person1 = new Person(1, "Juan");
	Person2 = new Person(2, "Daniel");
	Person3 = new Person(3, "Oscar");
	Person4 = new Person(4, "Ricardo");
	Person5 = new Person(5, "David");
	Person6 = new Person(6, "Feo");
	Person7 = new Person(7, "Hassel");
	Person8 = new Person(8, "Sahid");

	Persons = new LinkedList();

	Persons.append(Person2);
	Persons.append(Person4);
	Persons.insert(0, Person1);
	Persons.insert(2, Person3);

	Persons.print();

	Persons2 = new LinkedList();

	Persons2.append(Person6);
	Persons2.append(Person8);
	Persons2.insert(0, Person5);
	Persons2.insert(2, Person7);

	Persons2.print();

	GroupPersons = Persons.add(Persons2);

	GroupPersons.print();
}

main();