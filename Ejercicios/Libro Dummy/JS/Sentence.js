function Sentence(){
	this.random = SentenceRandom;
}

	function SentenceRandom(min=2, max=20){
		var words = [];
		var random = new Random();
		var r = random.int(min, max);
		var w = new word();

		for (var i = 0; i < r; i++) {
			words.push(w.random());
		}
		return '$(words.join())';
	}