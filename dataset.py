from departamento import Departamento
from typing import TextIO, List, Set, Dict
import csv
class DataSetInmobiliario:
    
    def __init__(self, nombre_archivo:str):
        ''' inicializa una coleccion de Departamentos cargando datos de 
        nombre_archivo
        requiere: nombre_archivo es de tipo CSV en el cual estan las columnas
        Direccion, Propiedades, Dolares, Pesos, DolaresM2, PesosM2, Cotizacion, Trimestre, Ambientes, 
        Barrio, Comunas en ese orden'''
        #self.archivo=nombre_archivo
        self.departamentos:List=self.lista_de_departamentos(nombre_archivo)
        self.archivo:str=nombre_archivo
        
    def lista_de_departamentos(self, archivo:str)->List[Departamento]:
        ''' Requiere: archivo debe ser un archivo csv valido que 
        respete el formato de las columnas indicado
        Devuelve: Una lista de Departamentos a partir de los datos de archivo'''
        departamentos:List[Departamento]=[]
        f:TextIO=open(archivo)
        for linea in csv.DictReader(f):
            dire:str=linea['Direccion']
            sup:float=float(linea['PropiedadS'])
            usd:int=int(linea['Dolares'])
            ars:int=int(linea['Pesos'])
            usdm:int=int(linea['DolaresM2'])
            arsm:int=int(linea['PesosM2'])
            cot:int=int(linea['Cotizacion'])
            trim:str=linea['Trimestre']
            amb:int=int(linea['Ambientes'])
            bar:str=linea['Barrio']
            com:int=int(linea['Comunas'])
            dep:Departamento=Departamento(dire, sup, usd, ars, usdm, arsm, amb,cot,trim, bar, com)
            departamentos.append(dep)
        f.close()
        #usando el metodo __lt__ de Departamento lo ordena para tener una lista ordenada desde el comienzo
        departamentos.sort()
        return departamentos
    
    def departamentos_del_barrio(self, bar:str)->List[Departamento]:
        '''devuelve una lista de Departamentos con todos los departamentos del dataset
        que estan en barrio bar'''
        
        vr:List[Departamento]=[]
        for dep in self.departamentos:
            if dep.barrio==bar:
                vr.append(dep)
                
        return vr

    def tamano(self)->int:
        '''devuelve la cantidad de departamentos que hay en self.departamentos'''
        return len(self.departamentos)
        
    def barrios(self)->Set[str]:
        '''devuelve un conjunto con todos los barrios de self.departamentos'''
        vr:Set[str]=set()
        for i in self.departamentos:
            vr.add(i.barrio)
        return vr
    
    #no nos permitio poner Dict[str:int] pero ese va a ser el formato del Dict de retorno
    def oferta_por_barrio(self, amb:int)->Dict:
        '''devuelve un diccionario que representa cuantos 
        departamentos con ambientes amb hay en cada barrio'''
        vr:Dict[str:int]=dict()
        for i in self.barrios():
            cantidad_departamentos:int=0
            departamentos_en_i:List[Departamento]=self.departamentos_del_barrio(i)
            for j in departamentos_en_i:
                if j.ambientes==amb:
                    cantidad_departamentos=cantidad_departamentos+1
            vr[i]=cantidad_departamentos
        return vr
    
    
    def filtrar (self, pmin:int, pmax:int, conj_barrios:Set[str]):
        '''Modifica self.departamentos de tal forma que solo deja aquellos
        Departamento que cumplen (d.precio_en_dolares<=pmax y d.precio_en_dolares>=pmin y d.barrio in conj_barrios'''
        filtro_final:List[Departamento]=[]
        for d in self.departamentos:
            #si el departamento cumple con todas las condiciones es agregado a filtro_final
            if (d.barrio in conj_barrios) and d.precio_en_dolares>=pmin and d.precio_en_dolares<=pmax:
                filtro_final.append(d)
        #no devolvemos nada, modificamos self.departamento para que solo queden los depts que cumplen las condiciones
        self.departamentos=filtro_final
            
    def exportar(self, archivo_csv:str):
        '''Requiere: archivo_csv ser una direccion csv valida
        genera un archivo csv en la direccion archivo_csv
        con las mismas columnas que self.archivo y los mismos datos que
        self.departamentos'''
        #los f.write('/n') son para asegurar que cada departamento tenga su propia linea
        f:TextIO=open(archivo_csv, "w")
        f.write('Direccion,PropiedadS,Dolares,Pesos,DolaresM2,PesosM2,Ambientes,Cotizacion,Trimestre,Barrio,Comunas')
        f.write("\n")
        for d in self.departamentos:
            di:str=d.direccion
            m2:float=d.metros_cuadrados
            pusd:int=d.precio_en_dolares
            pars:int=d.precio_en_pesos
            m2usd:int=d.m2_en_dolares
            m2ars:int=d.m2_en_pesos
            amb:int=d.ambientes
            cot:int=d.cotizacion
            tri:str=d.trimestre
            bar:str=d.barrio
            com:int=d.comuna
            dep_str:str=','.join([di,str(m2),str(pusd),str(pars),str(m2usd),str(m2ars),str(amb),str(cot),tri,bar,str(com)])
            f.write(dep_str)
            f.write("\n")
        f.close()

