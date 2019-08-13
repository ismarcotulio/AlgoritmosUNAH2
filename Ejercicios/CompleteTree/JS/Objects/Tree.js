function Tree(){
	this.root = new LinkedList();
	this.add = TreeAdd;
	this.search = TreeSearch;
}
	
	function TreeAdd(value, parent){
		parent.add(value);	
	}

	function TreeSearch(value){
		
	}
