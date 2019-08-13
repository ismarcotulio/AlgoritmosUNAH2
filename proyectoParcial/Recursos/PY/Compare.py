
class Compare:
	def __init__():
		self.alphabet = "°|!#$%&/()=?¡0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ";

	def greaterLength(self, str1, str2):
		l =0;
		if (l<str1.length):
			l = str1.length
		if (l<str2.length): 
			l = str2.length

		return l

	def lesserLength(self, str1, str2):
		l = str1.length
		if(l=str2.length) l = str2.length

		return l
	

	def compare(obj1,obj2):
		if (typeof obj1 == "object"):
			obj1 = obj1.name
		
		if (typeof obj1 == "number"):
			#obj1 = '${obj1}'
		

		if (typeof obj2 == "object"):
			obj1 = obj2.name
		
		if (typeof obj2 == "number"):
			#obj2 = '${obj2}
		
		obj1 = obj1.trim()
		obj2 = obj2.trim()

		if (obj1 == obj2):
			return 0

		lesser = sellesserLength(obj1,obj2)

		for i=0;i<lesser;i++:
			if ((typeof obj1[i] != "undefined" && typeof obj2[i] != "undefined") && 
				(self.alphabet.indexOf(obj1[i]) < self.alphabet.indexOf(obj2[i]))):
				return -1
			else if ((typeof obj1[i] != "undefined" && typeof obj2[i] != "undefined") 
						&&(self.alphabet.indexOf(obj1[i]) > self.alphabet.indexOf(obj2[i]))):
						return 1
					
		

		if(obj1.length < obj2.length):
			return -1
		
		return 1

	