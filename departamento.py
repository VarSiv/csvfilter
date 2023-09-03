from typing import List
class Departamento:
    
    def __init__(self, dire:str, sup:float, usd:int, ars:int, usdm:int, arsm:int, amb:int, cot:int, trim:str,bar:str, com:int):
        '''inicializa un objeto de clase departamento con direccion,
        superficie, precio en dolares, precio en pesos, precio usd por metro cuadrado,
        precio ars por metro cuadrado, ambientes y barrio
        '''
        self.direccion:str=dire
        self.metros_cuadrados:float=sup
        self.precio_en_dolares:int=usd
        self.precio_en_pesos:int=ars
        self.m2_en_dolares:int=usdm
        self.m2_en_pesos:int=arsm
        self.ambientes:int=amb
        self.barrio:str=bar
        
        #la consigna no pide crear estos atributos, pero se van a usar para la funcion exportar
        self.cotizacion:int=cot
        self.trimestre:str=trim
        self.comuna:int=com
        
    def __lt__(self, other)->bool:
        '''devuelve True si el precio en dolares de other es mayor al precio
        en dolares de self, y False en lo contrario'''
        if self.precio_en_dolares!=other.precio_en_dolares:
            return self.precio_en_dolares<other.precio_en_dolares
        else:
            #en caso de que el precio es el mismo, sorteamos por orden alfabetico de la direccion
            #esto ayuda prevenir ambiguedades en el testing en el caso de departamentos con el mismo precio
            return self.direccion<other.direccion
    
    def __eq__(self, other)->bool:
        '''devuelve True si todos los atributos entre self y other son iguales
        (excepto metros_cuadrados que puede ser casi igual). False en los contrario'''
        a:bool=(self.direccion==other.direccion)
        b:bool=(int(self.metros_cuadrados)==int(other.metros_cuadrados))

        c:bool=(self.precio_en_dolares==other.precio_en_dolares)
        d:bool=(self.precio_en_pesos==other.precio_en_pesos)
        e:bool=(self.m2_en_dolares==other.m2_en_dolares)
        f:bool=(self.m2_en_pesos==other.m2_en_pesos)
        g:bool=(self.ambientes==other.ambientes)
        h:bool=(self.cotizacion==other.cotizacion)
        i:bool=(self.trimestre==other.trimestre)
        j:bool=(self.barrio==other.barrio)
        k:bool=(self.comuna==other.comuna)
        comp:List[bool]=[a,b,c,d,e,f,g,h,i,j,k]
        
        return not(False in comp)

    def __repr__(self) -> str:
        '''devuelve un str con los metros cuadrados y 
        el barrio del departamento'''
        return '<'+str(round(self.metros_cuadrados))+'M2@'+self.barrio+'>'
        

  