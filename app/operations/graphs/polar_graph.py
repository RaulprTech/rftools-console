import plotly.graph_objects as go 
from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt
import cmath



diccionario = {'dato0' : 3+2j, 'dato1' : 3+4j, 'dato2': 1+2j } # for test

parametros = [[0.5281465564433748-114.76267752352298j, 0.38130221324468555-124.756766900855j, 0.40854369412256986-124.8977529006257j, 0.40854369412256986-124.8977529006257j],
[0.2456893893139781-121.82873960875816j, 0.261188585427646-122.06259740941981j, 0.4282730177446238-111.55903226314516j, 0.4282730177446238-111.55903226314516j],
[0.5281465564433748-114.76267752352298j, 0.38130221324468555-124.756766900855j, 0.40854369412256986-124.8977529006257j, 0.40854369412256986-124.8977529006257j],
[0.1579171491556553-119.42971744592087j, 0.3427811779491401-108.79551103899622j, 0.42059235603205847-106.14193560479306j, 0.3427811779491401-108.79551103899622j]
]



def polar_graph(source):
    # diccionario = {
    #     "i11": source[1],
    #     "i12": source[2],
    #     "i21": source[3],
    #     "i22": source[4]
    #     }
    vector_dict=[]
    vector_complejo = []
    vector_magnitud=[]
    vector_phase=[]
    # for params in source:
        # vector_dict=diccionario.values()
    vector_dict = source
    print(f"Parametros de entrada : \n {vector_dict}")
    vector_complejo = np.array([complex(x) for x in vector_dict])
    print(f"vector complejo {vector_complejo}")
    vector_magnitud = np.array([abs(x) for x in vector_complejo])
    print(f"vector magnitud {vector_magnitud}")
    vector_phase = np.array([cmath.phase(x) for x in vector_complejo])
    print(f"vector phase {vector_phase}")
    # fig = plt.figure()
    fig = go.Figure(data=go.Scatterpolar( 
        r=vector_magnitud, 
        theta=vector_phase, 
        mode='markers', #  or lines or +
        )) 
    fig.show()
    # ax = fig.add_subplot(111, projection="polar")
    # ax.plot(vector_magnitud,vector_phase,color="#ffb6c1",linewidth=3)
    print(f"Graficando vector complejo {len(vector_complejo)}")
    print(f"Graficando vector magnitud {len(vector_magnitud)}")
    print(f"Graficando vector phase {len(vector_phase)}")
    # plt.show()



if __name__ == '__main__':
    polar_graph(parametros)


