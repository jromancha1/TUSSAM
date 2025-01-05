# -*- coding: utf-8 -*-
from suds.client import Client
from lxml import etree
print "Utilización de API web con SOAP || TUSSAM"
print ""

cliente = Client('https://reddelineas.tussam.es/API/infotus-ui/buses/'
	, retxml=True)

numero = int(raw_input("Introduce el número de línea: "))
respuesta = cliente.service.GetStatusLinea(numero)
cadena = etree.fromstring(respuesta)
subcadena = cadena[0][0]

pre = "{http://tempuri.org/}"
activos = subcadena.find(pre+"GetStatusLineaResult/"+pre+"activos")
frec_bien = subcadena.find(pre+"GetStatusLineaResult/"+pre+"frec_bien")
graves = subcadena.find(pre+"GetStatusLineaResult/"+pre+"graves")

print "DATOS DE LA LINEA %s DE TUSSAM \n\n%s coches activos \n%s coches con \
frecuencia correcta \n%s incidencias graves" % (numero,activos.text,
	frec_bien.text,graves.text)
