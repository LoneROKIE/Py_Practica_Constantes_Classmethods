class Producto:
    _cont_productos =0
    @classmethod
    def _contador_productos(cls):
        cls._cont_productos +=1
        return cls._cont_productos

    def __init__(self, nombreProducto, precio):
        self._idProducto = Producto._contador_productos()
        self._nombreProducto = nombreProducto
        self._precio = precio

    @property
    def nombreProducto(self):
        return self._nombreProducto
    @property
    def precio(self):
        return self._precio
    @property
    def idProducto(self):
        return self._idProducto

    def __str__(self):
        return f'Nombre producto: {self._nombreProducto}, precio: {self._precio}, idProducto: {self._idProducto}'


#clase Orden
class Orden(Producto):
    _cont_ordenes =0
    @classmethod
    def _contador_orden(cls):
        cls._cont_ordenes +=1
        return cls._cont_ordenes

    def __init__(self,productos):

        self.idOrdenes = Orden._contador_orden()
        self.productos = list(productos)

    def agregar_producto(self,producto):
        self.productos.append(producto)

    def precio_total(self):
        total =0
        for producto in self.productos:
            total+=producto.precio
        return total




    def __str__(self):
        productos_str = ''
        for producto in self.productos:
            productos_str += producto.__str__()+ " | "
        return f'Orden: {self.idOrdenes}, Productos {productos_str}, precio total: {self.precio_total()}'



# Prueba producto1
producto1 = Producto('Arroz',1800)
# print(producto1)
producto2 = Producto('sopa',1200)

# if producto1.idProducto ==1:
#     del producto1
# print(producto1)

orden = Orden([producto2,producto1])
print(orden)
