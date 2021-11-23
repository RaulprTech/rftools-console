from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# diccionario = {'dato0': 3+2j, 'dato1': 3+4j, 'dato2': 1+2j}   # for test


def smith_chart(source):
    A = []
    # A = diccionario.values()
    A = source
    print(f"A = Source = {A}")
    b = np.array([complex(x) for x in A])
    print("")
    print(b)
    print(len(b))
    fig = go.Figure(go.Scattersmith(imag = b.imag, real = b.real))
    fig.show()


if __name__ == '__main__':
    # rectangular_graph(diccionario)
    pass