function Tree(){
    this.root = new LinkedList();
    this.add = TreeAdd;
}

    function TreeAdd(value, parent = this.root){
        parent.add(value);
    }