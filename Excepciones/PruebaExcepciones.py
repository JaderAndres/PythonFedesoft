def div(x):
    try:
        res = 100+(x/2)
        print(res)
    # except ZeroDivisionError:
     #   print("No se permite dividir entre cero")
        # print("El programa continua")
    except Exception as err:
        print("Oops, ha ocurrido algo malo!")
        print(err)
        # raise  # Muestra el error real
    else:
        print("Final!!!")


div(10)
