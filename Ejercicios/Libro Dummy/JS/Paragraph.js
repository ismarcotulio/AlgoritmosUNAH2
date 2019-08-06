function Paragraph(){
	this.random = ParagraphRandom;
}
	
	function ParagraphRandom(min=2, max=20){
		var paragraph = [];
		var random = new Random();
		var r = random.int(min, max);
		var s = new Sentence();

		for (var i = 0; i < r; i++) {
			paragraph.push(s.random());
		}
		return paragraph.join("")
	}