#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.backends.backend_pdf import PdfPages 
pp = PdfPages('pot-surf.pdf')

def f(x, y):
    #return np.tan(np.sqrt(x ** 2 + y ** 2 - y))
    return np.sin(x**2) + x*np.sin(y)**3 + y*np.cos(x)**3 

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

#width = 3.5
#height = width/1.31
#f, ax1 = plt.subplots()
#f.set_size_inches(width, height)

ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, edgecolor='none')
#ax.set_title('surface');
plt.tick_params(axis='x', which='both', bottom=False, top=False, left=False, right = False, labelbottom=False) # labels along the bottom edge are off
plt.tick_params(axis='y', which='both', bottom=False, top=False, left=False, right = False, labelbottom=False) # labels along the bottom edge are off
#plt.savefig('pot-surf.eps')
#plt.show()
pp.savefig()
pp.close()
None
