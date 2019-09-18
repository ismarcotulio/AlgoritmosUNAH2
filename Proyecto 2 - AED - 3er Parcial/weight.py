import math

class Weight:
    def __init__(self):
        pass

    def getWeight(self, distance,bandwidth, users, traffic, conectionType):

        if conectionType == "CAT5":
            reliability = 0.98 - (math.floor(distance/50)*0.02)
        elif conectionType == "CAT6":
            reliability = 0.98 - (math.floor(distance/50)*0.01)
        elif conectionType == "Fibra-Optica":
            reliability = 0.90 - (math.floor(distance/100)*0.05)
        elif conectionType == "Wi-Fi":
            reliability = 0.70 - (math.floor(distance/6)*0.06)
        elif conectionType == "Coaxial":
            reliability = 1 - (math.floor(distance/100)*0.04)
        elif conectionType == "Par-Trenzado":
            reliability = 1 - (math.floor(distance/100)*0.01)

        weight = 100

        #Distancias
        #Basandonos en la distancia
        if distance>=50*3 and conectionType == "CAT5" or conectionType == "CAT6":
            weight-=20
        elif distance>= 100*4 and conectionType == "Fibra-Optica" or conectionType == "Coaxial" or conectionType== "Par-Trenzado":
            weight-=20
        elif distance >= 6 and conectionType == "Wi-Fi":
            weight-=20

        #Bandwidth
        #Supongamos un ancho de Banda Promedio (10mbps)
        if bandwidth<10:
            weight -= 20

        #Users
        #Tomando en cuenta el ancho de Banda
        if users>bandwidth*1.3:
            weight-=20

        #Traffic
        #Tomando en cuenta el ancho de Banda, mayor a 2/3 del ancho de banda
        if traffic>bandwidth*0.66:
            weight-=20

        #Reliability
        if reliability<0.7:
            weight-=20

        if weight == 100:
            quality = "Excelente"
        elif weight == 80:
            quality = "Muy Buena"
        elif weight == 60:
            quality = "Buena"
        elif weight == 40:
            quality = "Mala"
        elif weight == 20:
            quality = "Muy Mala"
        else:
            quality = "Pésima"

        print("La Arista tiene confiabilidad %.2f con un peso de %s y calidad %s" % (reliability,weight,quality))

v1 = Weight()
v2 = Weight()
v1.getWeight(200,25,10,10,"Coaxial")
v2.getWeight(7,10,4,2,"Wi-Fi")