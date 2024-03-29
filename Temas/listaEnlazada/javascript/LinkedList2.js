	
	function Node(item, next){
		this.item = item;
		this.next = next;

		this.getItem = getItemNodo;
		this.getNext = getNextNodo;
		this.setItem = setItemNodo;
		this.setNext = setNextNodo;

	}
		function getItemNodo(){
			return this.item;
		}
		function getNextNodo(){
			return this.next;
		}
		function setItemNodo(item){
			this.item = item;
		}
		function setNextNodo(next){
			this.next = next;
		}


	function LinkedList(contents = []){
		this.first = new Node(None, None);
		this.last = first;
		this.numItems = 0;

		this.getItem = getItemLinkedList;
		this.setItem = setItemLinkedList;
		this.add = addLinkedList;
		this.append = appendLinkedList;
		this.insert = insertLinkedList;

	}

		function getItemLinkedList(index){
			if (index >= 0 && index < this.numItems){
				cursor = this.first.getNext();
				for (var i = 0; i <= index; i++) {
					cursor = cursor.getNext();
				}
				return cursor.getItem();
			}
		}
		function setItemLinkedList(index, item){
			if (index >= 0 && index < this.numItems) {
				cursor = cursor.first.getNext();
				for (var i = 0; i <= index; i++) {
					cursor = cursor.getNext();
				}
				cursor.setItem(item);
			}
		}
		function addLinkedList(other){
			if(typeof(this) == typeof(other)){
				result = new LinkedList();
				cursor = this.first.getNext();
				while(cursor != null){
					result.append(cursor.getItem());
					cursor = cursor.getNext();
				}
				cursor = other.first.getNext();
				while(cursor != null){
					result.append(cursor.getItem());
					cursor = cursor.getNext();
				}
				return result;
			}
		}
		function appendLinkedList(item){
			node = new Node(item);
			this.last.setNext(node);
			this.last = node;
			this.numItems += 1;
		}
		function insertLinkedList(index, item){
			cursor = this.first.getNext();
			if(index < this.numItems){
				for (var i = 0; i <= index; i++) {
					cursor = cursor.getNext();
				}
				node = new Node(item, cursor.getNext());
				cursor.setNext(node);
				this.numItems += 1;
			}else{
				this.append(item);
			}
		}

