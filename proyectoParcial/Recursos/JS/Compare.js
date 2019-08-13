function Compare(){
    this.alphabet = "°|!#$%&/()=?¡0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ";
    this.compare = CompareCompare;
    this.greaterLength = CompareGreaterLength;
    this.lesserLength = CompareLesserLength;
}

    function CompareGreaterLength(str1,str2){
        var l =0;
        if (l<str1.length) l = str1.length;
        if (l<str2.length) l = str2.length;

        return l;
    }

    function CompareLesserLength(str1,str2){
        var l = str1.length;
        if(l=str2.length) l = str2.length;

        return l;
    }

    function CompareCompare(obj1,obj2){
        if (typeof obj1 == "object"){
            obj1 = obj1.name;
        }
        if (typeof obj1 == "number"){
            obj1 = '${obj1}';
        }

        if (typeof obj2 == "object"){
            obj1 = obj2.name;
        }
        if (typeof obj2 == "number"){
            obj2 = '${obj2}';
        }

        obj1 = obj1.trim();
        obj2 = obj2.trim();

        if (obj1 == obj2){
            return 0;
        }

        var lesser = this.lesserLength(obj1,obj2);

        for (i=0;i<lesser; i++){
            
            if ((typeof obj1[i] != "undefined" && typeof obj2[i] != "undefined") && 
                (this.alphabet.indexOf(obj1[i]) < this.alphabet.indexOf(obj2[i]))) {
                return -1;
            } else if ((typeof obj1[i] != "undefined" && typeof obj2[i] != "undefined") 
                        &&(this.alphabet.indexOf(obj1[i]) > this.alphabet.indexOf(obj2[i]))){
                        return 1;
                    }
        }

        if(obj1.length < obj2.length){
            return -1;
        }
        return 1;

    }