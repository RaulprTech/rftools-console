import plotly.graph_objects as go 
from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt
import cmath


diccionario = {'dato0' : 3+2j, 'dato1' : 3+4j, 'dato2': 1+2j } # for test

def polar_graph(source):
    diccionario = {
        "i11": source[1],
        "i12": source[2],
        "i21": source[3],
        "i22": source[4]
        }
    vector_dict=[]
    vector_magnitud=[]
    vector_phase=[]
    vector_dict=diccionario.values()
    vector_complejo= np.array([complex(x) for x in vector_dict])
    vector_magnitud= np.array([abs(x) for x in vector_complejo])
    vector_phase= np.array([cmath.phase(x) for x in vector_complejo])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="polar")
    ax.plot(vector_magnitud,vector_complejo,color="#ffb6c1",linewidth=3)
    plt.show()

if __name__ == '__main__':
    polar_graph(diccionario)