from Segunda_pre_entrega_Murua.Cliente import Cliente

cliente1 = Cliente('cristian', 'murua', 'C.Pellegrini 1543', 'cristianmurua1995@gmail.com')
cliente1.compra_realizada()
cliente1.compra_realizada()
#para modificar un dato en especifico se debe pasar el resto de los parametros como cadena de texto vacia
cliente1.modificar_datos('martin', '', '', 'martinmurua@mail.com')
print(cliente1.__str__())