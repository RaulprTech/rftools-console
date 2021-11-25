from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.type_check import imag
import plotly.graph_objects as go

# diccionario = {'dato0': 3+2j, 'dato1': 3+4j, 'dato2': 1+2j}   # for test
# datos = [16.647560691949394 , 51.00518622052178, 16.543482155245705, 49.63442530408304, 16.65115482800946 48.26563338568729]

def smith_chart(source):
    # print(source)

    b = np.array([complex(x) for x in source])
    # params = [float(x) for x in source]
    real = b.real
    imag = b.imag
    real_n = [x/50 for x in real]
    imag_n = [x/50 for x in imag]
    print(f"real =  {real_n}")
    print(f"imag =  {imag_n}")

    fig = go.Figure(go.Scattersmith(imag = imag_n, real = real_n))
    fig.show()


if __name__ == '__main__':
    # smith_chart(datos)
    pass