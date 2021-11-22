import glob

################################        Modules             ################################
#   import and read documents
from app.doc_process.decoder_s2p import decoder_s2p as decode
from app.doc_process.decoder_s2p import params_complex_destructure as fracc
from app.doc_process.decoder_s2p import params_complex_destructure_output as fracc_out

#   export documents
from app.doc_process.doc_out import doc_out
#   converter function
from app.operations.param_converter import converter

#   graphs
from app.operations.graphs.rect_graph import rectangular_graph
from app.operations.graphs.polar_graph import polar_graph
from app.operations.graphs.smith_graph import Smith


lines = []

def select_file():
    print("Estos archivos estan disponibles para leer")
    files = glob.glob(f"input/" + "*.s2p") 
    print(f"""          {files}""")
    name_file = input(f"""Selecciona el archivo que deseas usar (coloca el nombre y ruta del archivo aqui) : """)
    return "./" + str(name_file).replace("\'", "")


def params_for_graph(route, structure):
    frecs = []
    parameters_list = decode(route)
    print("Estos son los parametros disponibles para graficar")
    for parameter in parameters_list:
        line_params = structure(parameter)
        frecs.append(line_params[0])
    print(frecs)
    frec_graph = input("Escribe la frecuencia de los parametros que deseas graficar: ")
    for parameter in parameters_list:
        line_params = structure(parameter)
        if(frec_graph == line_params[0]):
            return line_params

    print("Lo siento no fueron medidos parametros en esa frecuencia")
    reset = input("Deseas intentar con otro valor [s/n] ")
    if reset == 's':
        params_for_graph()
    else:
        print("Adios")


def plot_menu(mode, route_file):
    if mode == '1':
        print("¡Genial Empecemos!")
        route_file = select_file()
        p = params_for_graph(route_file, fracc)
    elif mode == '2':
        p = params_for_graph(route_file, fracc_out)
    plot_type = input("¿Como quieres graficar? [1 = Rectangular, 2 = Polar, 3 = Carta de Smith] ")
    if plot_type == '1':
        print("Preparando para graficar en forma Rectangular ...")
        rectangular_graph(p)
    elif plot_type == '2':
        print("Preparando para graficar en forma Polar ...")
        polar_graph(p)
    elif plot_type == '3':
        print("Preparando para graficar en forma de Carta de Smith ...")
        smith = Smith()
        smith.markZ(p[1], text='Z1')
        smith.markZ(p[2], text='Z2')
        smith.markZ(p[3], text='Z3')
        smith.markZ(p[4], text='Z4')
        # smith.drawZList([0, 50j, 10000j, -50j, 0])
        print("graficando")
        smith.show()
    else: 
        print("*******************************************************************************")
        print("Creo que te confundiste, intentemos de nuevo ")
        plot_menu()
    
    reset = input("¿Quieres graficar algo mas? [s/n] ")
    if reset == 's':
        plot_menu(mode, route_file)
    elif reset == 'n':
        print("Oh esta bien, hasta luego")
    else: 
        print("*******************************************************************************")
        print("Upps creo que te equivocaste de tecla, intentemos de nuevo")
        plot_menu(mode, route_file)




def converter_menu():
    route = select_file()
    parameters_list = decode(route)
    entrada = input(f"¿Que tipo de parametro contiene el archivo? (z, y, abcd, s o t) ")
    salida = input(f"¿En que tipo de parametro quieres que se convierta? (z, y, abcd, s o t) ")

    lines.append(f"!Nueva Lista de parametros {salida.upper()} \n")
    lines.append("# frec param1 param2  param3  param4 \n")

    for parameter in parameters_list:
        line_params = fracc(parameter)
        # print(params) 
        array_params = [[line_params[1], line_params[2]], [line_params[3], line_params[4]]]
        results =  converter(entrada, salida, array_params)
        lines.append(line_params[0] + " \t")
        lines.append(str(results).replace("(", "\t").replace(")", "").replace(",", "\t").replace("\'", ""))
        lines.append("\n")
    name_route_out = route.replace("./input/", "./output/")
    doc_out(name_route_out, lines)
    print("El archivo de resultados ya esta disponible en la carpeta output")
    print("Tambien puedes graficar tus nuevos parametros")
    a = input("¿Deseas graficar? [s/n] ")
    if a == 's':
        plot_menu('2', name_route_out)
    elif a == 'n':
        print("OK, Adios")
    
    
    

    

    

    # if(results == 0):
    #     print("Por favor inserte un valor valido ")
    #     main_menu()
    # else:
    #     print(results)
    #     a = input("Seguimos haciendo convirtiendo [s/n] ")
    #     if a == "s":
    #         main_menu() 
    #     elif a == "n":
    #         print("Adios")
    
def main_menu():
    print(f"""
    ******************************************************************************************************************
                                
                                **** Bienvenido a nuestra herramienta para RF ****

    ******************************************************************************************************************
    """)
    inicio = input("¿Que deseas hacer? [1 = Graficar, 2 = Convertir Parametros] ")
    if inicio == '1':
        plot_menu('1', None)
    elif inicio == '2':
        converter_menu()
    else:
        print("*******************************************************************************")
        print("             ¡Volvamos a intentarlo!           ")
        main_menu()




if __name__ == '__main__':
    main_menu()



    #     array_params = [[line_params[1], line_params[2]], [line_params[3], line_params[4]]]
    #     results =  converter(entrada, salida, array_params)