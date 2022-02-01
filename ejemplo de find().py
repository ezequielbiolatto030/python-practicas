#busca en una lista los nombres que empiezan con la letra ingresada
nombres= ["pablo", "gaston","ana","elisabet","ariel","jose","juan","carolina","celeste"]
letra=input("ingrese una letra:")
for i in nombres:
    if i.find(letra,0,1)== 0:
        print (i)
