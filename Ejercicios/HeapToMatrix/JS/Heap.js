function Heap(list){
	this.list = list;
	this.n = this.list.length
	this.h = Math.ceil(Math.log2(this.n+1)),
	this.mi = Math.pow(2,this.h-1)-1,
	this.mf = this.mi * 2,
	this.w = this.mf + 1

	this.matrix = [];
	this.build = HeapBuild;
	this.fill = HeapFill;
	this.table = MatrixToHTML;
	this.AtPosition = MatrixAtPosition;
}


	function HeapBuild(){

		for(var i=0; i<this.h; i++){
			var row = [];
			for(var j=0; j<this.w; j++){
				row.push("&nbsp");
			}
			this.matrix.push(row);
		}

		
		this.fill(this.n, this.h);
		html = this.table(this.w, this.h);

		return html;
	}


	function HeapFill(n, h, fila = 0, nodo=0, position=0){
		if(nodo>=n){
			
		}else{
			if(fila==0){
				var blanks = Math.pow(2,h-1-fila)-1;				
			}else{
				var blanks = Math.pow(2,h-1-fila);
				position = this.AtPosition(Math.floor((nodo-1)/2), this.w, this.h);
			}
					

			if(nodo%2==0){
				var newPosition = position + blanks ;
			}else{
				var newPosition = position - blanks ;
			}

			this.matrix[fila][newPosition] = this.list[nodo]; 

			this.fill(n, h,Math.floor(Math.log2(nodo+2)), nodo+1);
			
		}
	}

	function MatrixToHTML(w, h, border = 1){

		var html = "";

		html += `<table border=${border}>`;

		for (i=0; i<h; i++){
			html += "<tr>";
			for(j=0; j<w; j++){
				html += `<td>${this.matrix[i][j]}</td>`;
			}
			html += "</tr>";
		}

		html += "</table>";

		return html;

	}

	function MatrixAtPosition(value, w, h){
		for(i=0; i<h;i++){
			for(j=0;j<w;j++){
				if(this.matrix[i][j]==value){
					return j;
				}
			}
		}
	}

	list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30];
	heap = new Heap(list);	
	document.write(heap.build(list));
