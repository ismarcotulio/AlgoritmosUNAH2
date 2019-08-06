
function Word(){
	this.random = WordRandom
}
	function WordRandom(min=2, max = 8){
		var random = Random();
		var r = random(min,max);
		var letters = [];
		var l = random(0,this.alphabet.lenght);
		for (var i = 0; i >= r; i++) {
			letters.push(this.alphabet[]);
		}
	}