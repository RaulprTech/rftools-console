

def decoder_s2p(route):
    parametros = []
    archivo = open(route, "rt", encoding="utf8")

    letras = "!"
    while(letras=="!"):
        first = archivo.readline()
        letras = first[0]

    lineas = archivo.readlines()
    # print(f"lineas {lineas}")
    for linea in lineas:
        parametros.append(linea.replace("\n", "").replace("\t", " ").split(" "))
        # print(parametros)
    
    archivo.close()
    return parametros

# param 2 y 3 estan inversos en el archivo, por lo que aqui se corrige
def params_complex_destructure(parameters_list):
    # print(f"parameter_list {parameters_list}")
    frec = parameters_list[0]
    
    param1 = complex(parameters_list[1]) + complex(parameters_list[2] + "j")
    param3 = complex(parameters_list[3]) + complex(parameters_list[4] + "j")
    param2 = complex(parameters_list[5]) + complex(parameters_list[6] + "j")
    param4 = complex(parameters_list[7]) + complex(parameters_list[8] + "j")
    return frec, param1, param2, param3, param4

# param 2 y 3 estan inversos en el archivo, por lo que aqui se corrige
def params_complex_destructure_output(parameters_list):
    params =[]        
    for p in parameters_list:
        p.pop(0)
        params += p
    
    param_float = [float(x) for x in params]
    # frec = parameters_list[0]
    # param1 = float(parameters_list[1])
    # param3 = float(parameters_list[2])
    # param2 = float(parameters_list[3])
    # param4 = float(parameters_list[4])
    # param_float = [float(x) for x in parameters_list]

    return param_float


if __name__ == '__main__':
    parameters_list = decoder_s2p("./input/s.s2p")
    # print(parameters_list)
    params = params_complex_destructure(parameters_list[0])  # usando un for es posible acceder a cada linea para operarla
    print(params)
    