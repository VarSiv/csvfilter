import unittest
# Importamos el codigo a testear.
from departamento import Departamento

####################################################################

class TestDepartamento(unittest.TestCase):

    def test_atributos(self):
        dep1:Departamento = Departamento('Pje Cnel J F Bogado 4561',17,54900,3513600,3229,206682,1,64,'SEGUNDO','ALMAGRO',5)
        self.assertEqual(dep1.direccion, 'Pje Cnel J F Bogado 4561')
        self.assertAlmostEqual(dep1.metros_cuadrados, 17)
        self.assertEqual(dep1.precio_en_dolares, 54900)
        self.assertEqual(dep1.precio_en_pesos, 3513600)
        self.assertEqual(dep1.m2_en_dolares, 3229)
        self.assertEqual(dep1.m2_en_pesos, 206682)
        self.assertEqual(dep1.ambientes, 1)
        self.assertEqual(dep1.cotizacion, 64)
        self.assertEqual(dep1.trimestre, 'SEGUNDO')
        self.assertEqual(dep1.barrio, 'ALMAGRO')
        self.assertEqual(dep1.comuna, 5)
        
        dep2:Departamento = Departamento('G De Helguera 2424',38,105000,7056000,2763,185684,2,64, 'TERCERO','VILLA DEL PARQUE',11)
        self.assertEqual(dep2.direccion, 'G De Helguera 2424')
        self.assertAlmostEqual(dep2.metros_cuadrados, 38)
        self.assertEqual(dep2.precio_en_dolares, 105000)
        self.assertEqual(dep2.precio_en_pesos, 7056000)
        self.assertEqual(dep2.m2_en_dolares, 2763)
        self.assertEqual(dep2.m2_en_pesos, 185684)
        self.assertEqual(dep2.ambientes, 2)
        self.assertEqual(dep2.cotizacion, 64)
        self.assertEqual(dep2.trimestre, 'TERCERO')
        self.assertEqual(dep2.barrio, 'VILLA DEL PARQUE')
        self.assertEqual(dep2.comuna, 11)
        
        dep3:Departamento = Departamento('',0,0,0,0,0,0,0,'','',0)
        self.assertEqual(dep3.direccion, '')
        self.assertAlmostEqual(dep3.metros_cuadrados, 0)
        self.assertEqual(dep3.precio_en_dolares, 0)
        self.assertEqual(dep3.precio_en_pesos, 0)
        self.assertEqual(dep3.m2_en_dolares, 0)
        self.assertEqual(dep3.m2_en_pesos, 0)
        self.assertEqual(dep3.ambientes, 0)
        self.assertEqual(dep3.cotizacion, 0)
        self.assertEqual(dep3.trimestre, '')
        self.assertEqual(dep3.barrio, '')
        self.assertEqual(dep3.comuna, 0)
        
    def test_menor(self):
        dep1:Departamento = Departamento('Pje Cnel J F Bogado 4561',17,54900,3513600,3229,206682,1,64,'SEGUNDO','ALMAGRO',5)
        dep2:Departamento = Departamento('G De Helguera 2424',38,105000,7056000,2763,185684,2,64,'SEGUNDO','VILLA DEL PARQUE',11)
        dep3:Departamento = Departamento('Artigas 1300',72,197000,13691500,2736,190160,3,64,'SEGUNDO','VILLA GRAL. MITRE',15)
        dep4:Departamento = Departamento('Mahatma Gandhi 300',40,197000,6116000,2200,152900,2,64,'SEGUNDO','VILLA CRESPO',11) 
        dep5:Departamento = Departamento('Mahatma Gandhi 300',40,197000,6116000,2200,152900,3,64,'SEGUNDO','ALMAGRO',5) 
        #caso basico
        self.assertTrue(dep1<dep2)
        #test de que tambien funciona el signo mayor
        self.assertTrue(dep2 > dep1)
        #test caso falso
        self.assertFalse(dep4 < dep2)
        #2 precios iguales deben respetar orden alfabetico
        self.assertFalse(dep4 < dep3)
        self.assertTrue(dep3 < dep4)
        
        #en caso de que tanto direccion como precio usd sean iguales deben dar falso los 2
        self.assertFalse(dep4 < dep5)
        self.assertFalse(dep5 < dep4)


    def test_repr(self):
        dep1:Departamento = Departamento('Pje Cnel J F Bogado 4561',17,54900,3513600,3229,206682,1,64,'SEGUNDO','ALMAGRO',5)
        dep2:Departamento = Departamento('G De Helguera 2424',38,105000,7056000,2763,185684,2,64,'SEGUNDO','VILLA DEL PARQUE',11)
        dep3:Departamento = Departamento('',0,0,0,0,0,0,0,'','',0)
        #casos genericos
        self.assertEqual(str(dep1), '<17M2@ALMAGRO>')        
        self.assertEqual(str(dep2), '<38M2@VILLA DEL PARQUE>')   
        #test de formato no convencional
        self.assertEqual(str(dep3), '<0M2@>')   
    
    def test_eq(self):
        dep1:Departamento = Departamento('Pje Cnel J F Bogado 4561',17,54900,3513600,3229,206682,1,64,'SEGUNDO','ALMAGRO',5)
        dep2:Departamento = Departamento('Pje Cnel J F Bogado 4561',17,54900,3513600,3229,206682,1,64,'SEGUNDO','ALMAGRO',5)
        #dos departamentos completamente iguales
        self.assertEqual(dep1==dep2, True)
        #test que funciona el trunc de metros_cuadrados
        dep3:Departamento = Departamento('Pje Cnel J F Bogado 4561',17.002,54900,3513600,3229,206682,1,64,'SEGUNDO','ALMAGRO',5)
        self.assertEqual(dep1==dep3, True)
        #test con 1 atributo distinto (2 vs 1 ambientes)
        dep4:Departamento = Departamento('Pje Cnel J F Bogado 4561',17,54900,3513600,3229,206682,2,64,'SEGUNDO','ALMAGRO',5)
        self.assertEqual(dep1==dep4, False)
        #test con metros_cuadrados distinto
        dep5:Departamento = Departamento('Pje Cnel J F Bogado 4561',20,54900,3513600,3229,206682,2,64,'SEGUNDO','ALMAGRO',5)
        self.assertEqual(dep1==dep5, False)
        #test con todos los atributos distintos
        dep6:Departamento = Departamento('G De Helguera 2424',38,105000,7056000,2763,185684,2,65,'PRIMERO','VILLA DEL PARQUE',11)
        self.assertEqual(dep1==dep6, False)
####################################################################

unittest.main()

