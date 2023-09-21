try:
    sql = "INSERT INTO table_name (name, email, city) VALUES ('{}', '{}', '{}')\n"

    #Adiciona texto al archivo
    with open('Consolidado.sql', 'a') as f:
        f.write(sql)
    print("Adicionado!")
except():
    print("Ha ocurrido un error...")
finally:
    print("Fin del script")
