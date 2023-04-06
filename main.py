import design
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_unit, y_unit, header, path = design.gui()


data = pd.read_csv(path)
xpoints = np.array(data['X axis'])
ypoints = np.array(data['Y axis'])

if x_unit != None and y_unit != None and header != None:
    plt.title(header)
    plt.plot(xpoints, ypoints,'o')
    plt.plot(xpoints, ypoints,)
    plt.xlabel(x_unit)
    plt.ylabel(y_unit)
    plt.show()

