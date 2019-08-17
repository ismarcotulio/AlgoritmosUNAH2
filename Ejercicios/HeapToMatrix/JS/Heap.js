function Heap(){
	this.build = HeapBuild;
}
	function HeapBuild(list){
		var
			n = list.lenght()
			h = math.cell(math.log2(n+1)),
			mi = math.pow(2,h-1)-1,
			mf = mi * 2,
			w = mf + 1
			matrix = []
		;

		for(var i=0; i<h; i++){
			var row = [];
			for(var j=0; j<w; j++){
				row.push("&nbsp");
			}
			matrix.push(row);
		}

		//Creacion primera fila
		matrix[0][math.floor(w/2)] = list.atPosition(0);
		
		//creacion de la ultima fila
	}