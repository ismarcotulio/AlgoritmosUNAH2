import * as ll from "../../../Temas/listaEnlazada/javascript/LinkedList2.js";

function Persona(nombre, cuenta){
	this.nombre = nombre;
	this.cuenta = cuenta;
}

var persona1 = new Persona("Juan", 1);
var persona2 = new Persona("Daniel", 2);
var persona3 = new Persona("Jona", 3);
var persona4 = new Persona("Fer", 4);



listaEnlazada = new ll LinkedList(null);
console.log("hola");

listaEnlazada.append(persona1);

