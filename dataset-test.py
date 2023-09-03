import unittest

# Importamos el codigo a testear.
from dataset import DataSetInmobiliario
from departamento import Departamento
from typing import List
import os

####################################################################

class TestDataSetInmobiliario(unittest.TestCase):
    #el archivo 1-barrio.csv contiene 3 depts de almagro
    #el archivo solo-encabezado.csv contiene solo el heading requerido del formato y nada mas
    #el archivo 1-departamento.csv contiene un unico dep en parque chascomus
    #el archivo precios-varios.csv tiene varios precios repetidos (fue pensado para testear filtrar mas que nada)
    #el archivo test-variado.csv es mezclado, con distintos datos en muchos atributos. 
    #este es el que mas se aproxima a un dataset real
    
    
    def test_lista_de_departamentos(self):
        #esta mas o menos testeada en el init pero esto es un test mas a fondo
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-barrio.csv')
        dataset2:DataSetInmobiliario=DataSetInmobiliario('solo-encabezado.csv')
        dataset3:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        dataset4:DataSetInmobiliario=DataSetInmobiliario('precios-varios.csv')
        
        dep1:Departamento=Departamento('Capital 0', 26, 63000, 4032000, 2864, 183273, 1,64,'SEGUNDO', 'ALMAGRO',5)
        dep2:Departamento=Departamento('COLOMBRES 43',22,48000,3072000,2182,139636,1,64,'SEGUNDO','ALMAGRO',5)
        dep3:Departamento=Departamento('Rawson 200 0',22,64000,4096000,2909,186182,1,64,'SEGUNDO','ALMAGRO',5)
        self.assertEqual(dataset1.lista_de_departamentos(dataset1.archivo), [dep2,dep1,dep3])
        
        self.assertEqual(dataset2.lista_de_departamentos(dataset2.archivo), [])
        
        dep4:Departamento=Departamento('SALGUERO 873', 22, 59900, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'PARQUE CHASCOMUS',5)
        self.assertEqual(dataset3.lista_de_departamentos(dataset3.archivo), [dep4])
        
        dep1:Departamento=Departamento('Capital 10', 26, 30000, 4032000, 2864, 183273, 1,64,'SEGUNDO', 'PALERMO',5)
        dep2:Departamento=Departamento('COLOMBRES 43',20,35000,3072000,2182,139636,1,64,'SEGUNDO','ALMAGRO',5)
        dep3:Departamento=Departamento('Rawson 200 0',22,35000,4096000,2909,186182,3,64,'SEGUNDO','ALMAGRO',5)
        dep4:Departamento=Departamento('SALGUERO 873', 22, 40000, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'PARQUE CHASCOMUS',5)
        dep5:Departamento=Departamento('Armenia 200 0', 22, 45000, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'PARQUE CHASCOMUS',5)
        dep6:Departamento=Departamento('Charcas 200 0', 22, 45000, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'ALMAGRO',5)
        dep7:Departamento=Departamento('Cabildo 1800', 22, 50000, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'ALMAGRO',5)
        self.assertEqual(dataset4.lista_de_departamentos(dataset4.archivo), [dep1,dep2,dep3,dep4,dep5,dep6,dep7])
        
    
    def test_init(self):
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-barrio.csv')
        dataset2:DataSetInmobiliario=DataSetInmobiliario('solo-encabezado.csv')
        dataset3:DataSetInmobiliario=DataSetInmobiliario('test-variado.csv')
        dataset4:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        
        self.assertEqual(dataset1.archivo, '1-barrio.csv')
        self.assertEqual(dataset2.archivo, 'solo-encabezado.csv')
        self.assertEqual(dataset3.archivo, 'test-variado.csv')
        self.assertEqual(dataset4.archivo, '1-departamento.csv')
        
        dep1:Departamento=Departamento('Capital 0', 26, 63000, 4032000, 2864, 183273, 1,64,'SEGUNDO', 'ALMAGRO',5)
        dep2:Departamento=Departamento('COLOMBRES 43',22,48000,3072000,2182,139636,1,64,'SEGUNDO','ALMAGRO',5)
        dep3:Departamento=Departamento('Rawson 200 0',22,64000,4096000,2909,186182,1,64,'SEGUNDO','ALMAGRO',5)
        self.assertEqual(dataset1.departamentos, [dep2, dep1, dep3])
        
        self.assertEqual(dataset2.departamentos, [])
        
        dep4:Departamento=Departamento('SALGUERO 873', 22, 59900, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'PARQUE CHASCOMUS',5)
        self.assertEqual(dataset4.departamentos, [dep4])
        

    def test_departamentos_del_barrio(self):
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-barrio.csv')
        dataset2:DataSetInmobiliario=DataSetInmobiliario('solo-encabezado.csv')
        dataset3:DataSetInmobiliario=DataSetInmobiliario('test-variado.csv')
        dataset4:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        
        alm:str = 'ALMAGRO'
        bel:str='BELGRANO'
        chas:str='PARQUE CHASCOMUS'
        cogh='COGHLAN'
        dep1:Departamento=Departamento('Capital 0', 26, 63000, 4032000, 2864, 183273, 1, 64,'SEGUNDO','ALMAGRO',5)
        dep2:Departamento=Departamento('COLOMBRES 43',22,48000,3072000,2182,139636,1,64,'SEGUNDO','ALMAGRO',5)
        dep3:Departamento=Departamento('Rawson 200 0',22,64000,4096000,2909,186182,1,64,'SEGUNDO','ALMAGRO',5)
        dep4:Departamento=Departamento('SALGUERO 873', 22, 59900, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'PARQUE CHASCOMUS',5)
        #poniendo dep1 dep2 y dep3 en un orden particular permite no solo testear el
        #contenido de departamentos_del_barrio(bar) sino tambien que esta efectivamente
        #ordenado de menor a mayor
        self.assertEqual(dataset1.departamentos_del_barrio(alm), [dep2, dep1, dep3])
        self.assertEqual(dataset1.departamentos_del_barrio(bel), [])
        #caso csv vacio
        self.assertEqual(dataset2.departamentos_del_barrio(alm), [])
        #caso csv con 1 solo departamento
        self.assertEqual(dataset4.departamentos_del_barrio(alm), [])
        self.assertEqual(dataset4.departamentos_del_barrio(chas), [dep4])
        #caso variado
        self.assertEqual(dataset3.departamentos_del_barrio(cogh), [])
        self.assertEqual(dataset3.departamentos_del_barrio(chas), [dep4])
        

    def test_tamano(self):
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-barrio.csv')
        dataset2:DataSetInmobiliario=DataSetInmobiliario('solo-encabezado.csv')
        dataset3:DataSetInmobiliario=DataSetInmobiliario('test-variado.csv')
        dataset4:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        
        self.assertEqual(dataset1.tamano(), 3)
        self.assertEqual(dataset2.tamano(), 0)
        self.assertEqual(dataset3.tamano(), 15)
        self.assertEqual(dataset4.tamano(), 1)
        
        #probamos que funciona luego de un filtrar
        dataset1.filtrar(10, 20, {'ALMAGRO'})
        self.assertEqual(dataset1.tamano(), 0)
        
        dataset2.filtrar(10, 20, {'ALMAGRO'})
        self.assertEqual(dataset2.tamano(), 0)
        
        dataset3.filtrar(50000, 80000, {'BELGRANO','SAAVEDRA'})
        self.assertEqual(dataset3.tamano(), 2)
    
    def test_barrios(self):
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-barrio.csv')
        dataset2:DataSetInmobiliario=DataSetInmobiliario('solo-encabezado.csv')
        dataset3:DataSetInmobiliario=DataSetInmobiliario('test-variado.csv')
        dataset4:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        alm:str = 'ALMAGRO'
        bel:str = 'BELGRANO'
        sav:str = 'SAAVEDRA'
        chas:str='PARQUE CHASCOMUS'
        self.assertEqual(dataset1.barrios(), {alm})
        self.assertEqual(dataset2.barrios(), set())
        self.assertEqual(dataset3.barrios(), {alm, bel, sav, chas})
        self.assertEqual(dataset4.barrios(), {chas})
        
        #testeamos que funciona luego de un filtrar
        dataset3.filtrar(10, 10000000, {alm,bel,chas})
        self.assertEqual(dataset3.barrios(), {alm, bel, chas})
        
        dataset4.filtrar(10000, 20000, {alm,bel,chas})
        self.assertEqual(dataset4.barrios(), set())
    def test_oferta_por_barrio(self):
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-barrio.csv')
        dataset2:DataSetInmobiliario=DataSetInmobiliario('solo-encabezado.csv')
        dataset3:DataSetInmobiliario=DataSetInmobiliario('test-variado.csv')
        dataset4:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        
        alm:str = 'ALMAGRO'
        bel:str = 'BELGRANO'
        sav:str = 'SAAVEDRA'
        chas:str='PARQUE CHASCOMUS'
        
        self.assertEqual(dataset1.oferta_por_barrio(1), {alm:3})
        self.assertEqual(dataset2.oferta_por_barrio(1), dict())
        self.assertEqual(dataset3.oferta_por_barrio(2), {alm:6, chas:0, sav:0, bel:2})
        self.assertEqual(dataset4.oferta_por_barrio(3), {chas:1})
    
        #testeamos que funciona luego de un filtrar
        dataset1.filtrar(10, 10000000, {bel,chas})
        self.assertEqual(dataset1.oferta_por_barrio(1), dict())
        
        dataset3.filtrar(10, 10000000, {bel,chas,sav})
        self.assertEqual(dataset3.oferta_por_barrio(2), { chas:0, sav:0, bel:2})
        
        dataset3:DataSetInmobiliario=DataSetInmobiliario('test-variado.csv')
        dataset3.filtrar(50000, 10000000, {bel})
        self.assertEqual(dataset3.oferta_por_barrio(2), {bel:1})
    def test_filtrar(self):
        alm:str = 'ALMAGRO'
        bel:str = 'BELGRANO'
        sav:str = 'SAAVEDRA'
        chas:str='PARQUE CHASCOMUS'
        pal:str ='PALERMO'
        
        #filtrar archivo vacio
        dataset2:DataSetInmobiliario=DataSetInmobiliario('solo-encabezado.csv')
        dataset2.filtrar(10000, 20000, {alm,bel,sav,chas})
        self.assertEqual(dataset2.departamentos, [])
        
        #filtrar 1 dep.csv por fuera de rango (precios chicos)
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        dataset1.filtrar(10000, 20000, {chas})
        self.assertEqual(dataset1.departamentos, [])
        #filtrar 1 dep.csv por fuera de rango (precios grandes)
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        dataset1.filtrar(80000, 90000, {chas})
        self.assertEqual(dataset1.departamentos, [])
        #filtrar 1 dep.csv por conjunto de barrios
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        dataset1.filtrar(50000, 60000, {alm, bel})
        self.assertEqual(dataset1.departamentos, [])
        #1 dep.csv tal que se respeten los rangos/barrio de ese dep
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        dataset1.filtrar(50000, 60000, {chas})
        dep1:Departamento=Departamento('SALGUERO 873', 22, 59900, 3833600, 2723, 174255, 3, 64, 'SEGUNDO', 'PARQUE CHASCOMUS', 5)
        self.assertEqual(dataset1.departamentos, [dep1])
        #fuera de rango de precios y fuera de barrios
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        dataset1.filtrar(5, 10, {'este-barrio-no existe'})
        self.assertEqual(dataset1.departamentos, [])
        
        #tests de precios varios.csv para testear que los pmax y pmin son inclusives
        #y tambien ver que funcionan varios criterios a la vez
        dep1:Departamento=Departamento('Capital 10', 26, 30000, 4032000, 2864, 183273, 1,64,'SEGUNDO', 'PALERMO',5)
        dep2:Departamento=Departamento('COLOMBRES 43',20,35000,3072000,2182,139636,1,64,'SEGUNDO','ALMAGRO',5)
        dep3:Departamento=Departamento('Rawson 200 0',22,35000,4096000,2909,186182,3,64,'SEGUNDO','ALMAGRO',5)
        dep4:Departamento=Departamento('SALGUERO 873', 22, 40000, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'PARQUE CHASCOMUS',5)
        dep5:Departamento=Departamento('Armenia 200 0', 22, 45000, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'PARQUE CHASCOMUS',5)
        dep6:Departamento=Departamento('Charcas 200 0', 22, 45000, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'ALMAGRO',5)
        dep7:Departamento=Departamento('Cabildo 1800', 22, 50000, 3833600, 2723, 174255, 3,64,'SEGUNDO', 'ALMAGRO',5)
        
        #testeamos que pmin y pmax sean inclusives
        #tambien que podemos agregar barrios que no estan al set de barrios y no afecte nada(bel en este caso)
        dataset3:DataSetInmobiliario=DataSetInmobiliario('precios-varios.csv')
        dataset3.filtrar(30000, 50000, {pal, chas, alm, bel})
        #esto tmb testea que se conserva el orden de menor a mayor 
        self.assertEqual(dataset3.departamentos, [dep1, dep2, dep3, dep4, dep5, dep6, dep7])
        
        #doble filtro
        dataset3:DataSetInmobiliario=DataSetInmobiliario('precios-varios.csv')
        #sacamos aquellos que esten en chas
        dataset3.filtrar(30000, 50000, {pal, alm, bel})
        #filtramos por precio
        dataset3.filtrar(35000, 45000, {pal, alm, bel, chas})
        self.assertEqual(dataset3.departamentos, [ dep2, dep3, dep6])
        
    def test_exportar(self):
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-barrio.csv')
        dataset2:DataSetInmobiliario=DataSetInmobiliario('solo-encabezado.csv')
        dataset3:DataSetInmobiliario=DataSetInmobiliario('test-variado.csv')
        dataset4:DataSetInmobiliario=DataSetInmobiliario('1-departamento.csv')
        
        dataset1.exportar('1-barrio-copia.csv')
        dataset2.exportar('solo-encabezado-copia.csv')
        dataset3.exportar('test-variado-copia.csv')
        dataset4.exportar('1-departamento-copia.csv')
        
        #para pasar los tests los depts de la copia deben estar en el mismo orden que el original
        #a pesar de que la consigna especifica que pueden estar en cualquier orden
        #sin embargo por como esta implementado (copiar cada dep en el orden que esta)
        #podemos asegurarnos que el orden no va a ser un problema
        self.assertEqual(dataset1.departamentos, DataSetInmobiliario('1-barrio-copia.csv').departamentos)
        self.assertEqual(dataset2.departamentos,DataSetInmobiliario('solo-encabezado-copia.csv').departamentos)
        self.assertEqual(dataset3.departamentos, DataSetInmobiliario('test-variado-copia.csv').departamentos)
        self.assertEqual(dataset4.departamentos, DataSetInmobiliario('1-departamento-copia.csv').departamentos)
        
        #testeamos que luego de filtrar() el exportar sigue funcionando
        #filtrar que elimina todo
        dataset1:DataSetInmobiliario=DataSetInmobiliario('1-barrio.csv')
        dataset1.filtrar(10, 20, {'ALMAGRO'})
        dataset1.exportar('1-barrio-copia2.csv')
        self.assertEqual(dataset1.departamentos, DataSetInmobiliario('1-barrio-copia2.csv').departamentos)
        
        #filtrar que nada sea eliminado
        dataset3:DataSetInmobiliario=DataSetInmobiliario('test-variado.csv')
        dataset3.filtrar(10, 100000, {'ALMAGRO', 'BELGRANO','PARQUE CHASCOMUS', 'SAAVEDRA'})
        dataset3.exportar('test-variado-copia2.csv')
        self.assertEqual(dataset3.departamentos, DataSetInmobiliario('test-variado-copia2.csv').departamentos)
        
        #filtar que elimina algunos
        dataset3:DataSetInmobiliario=DataSetInmobiliario('test-variado.csv')
        dataset3.filtrar(50000, 70000, {'ALMAGRO', 'PARQUE CHASCOMUS', 'SAAVEDRA'})
        dataset3.exportar('test-variado-copia3.csv')
        self.assertEqual(dataset3.departamentos, DataSetInmobiliario('test-variado-copia3.csv').departamentos)
        
        #filtar sobre un archivo vacio
        dataset2:DataSetInmobiliario=DataSetInmobiliario('solo-encabezado.csv')
        dataset2.filtrar(50000, 60000, {'ALMAGRO', 'PARQUE CHASCOMUS', 'SAAVEDRA'})
        dataset2.exportar('solo-encabezado-copia2.csv')
        self.assertEqual(dataset2.departamentos, DataSetInmobiliario('solo-encabezado-copia2.csv').departamentos)
        
        #elimina las copias
        os.remove('1-barrio-copia.csv')
        os.remove('1-barrio-copia2.csv')
        os.remove('solo-encabezado-copia.csv')
        os.remove('solo-encabezado-copia2.csv')
        os.remove('test-variado-copia.csv')
        os.remove('test-variado-copia2.csv')
        os.remove('test-variado-copia3.csv')
        os.remove('1-departamento-copia.csv')
unittest.main()
