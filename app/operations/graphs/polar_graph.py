from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt


diccionario = {'dato0' : 3+2j, 'dato1' : 3+4j, 'dato2': 1+2j } # for test

def polar_graph(source):
    diccionario = {
        "i11": source[1],
        "i12": source[2],
        "i21": source[3],
        "i22": source[4]
        }
    A=[]
    A=diccionario.values()
    b= np.array([complex(x) for x in A])
    print(b)
    fig, ax=plt.subplots()
    ax.scatter(b.real,b.imag)
    ax.axis([-10,10,-10,10])

    #   Grafica de ejes
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    # Elimina los ejes superior e inferior
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_title("Gráfica de complejos en plano cartesiano ")
    plt.show()

if __name__ == '__main__':
    polar_graph(diccionario)