
cadenaestado1 = '__servidor1' 
cadenaestados2 = '3servidor '


def AFD(entradas):
    estado = 0

    for i in range(len(entradas)):
        if estado == 0:
            if entradas[i] == '_':
                estado = 1
            elif entradas[i] == 'A':
                estado = 2
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return
        elif estado == 1:
            if entradas[i] == '_':
                estado = 1
            elif entradas[i] == 'A':
                estado = 3
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return
        elif estado == 2:
            if entradas[i] == '1':
                estado = 4
            elif entradas[i] == 'A':
                estado = 2
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return 
        elif estado == 3:
            if entradas[i] == '1':
                estado = 4
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return
        elif estado == 4:
            if entradas[i] == '1':
                estado = 4
            elif entradas[i] == '1':
                estado = 4
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return

    print ("CADENA CORRECTA !!!")

AFD(cadenaestado1)
AFD(cadenaestados2)
