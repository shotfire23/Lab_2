import matplotlib.pyplot as plt
import numpy as np

# Вхідні дані
x = [5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000]
y = [0.0049, 0.0099, 0.0249, 0.0495, 0.019, 0.1, 0.25, 0.4, 0.4807, 0.495, 0.498, 0.4987, 0.49995]

#log_x = np.log10(x) 


plt.figure(figsize=(10, 6))
plt.semilogx(x, y, 'bo-', linewidth=2) 
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('Grafik') 
plt.grid(True)
plt.show()
