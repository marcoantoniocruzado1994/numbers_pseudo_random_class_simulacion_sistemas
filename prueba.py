import random
import numpy as np
from scipy import stats
import pandas as pd

np.random.seed(10)
datos = np.random.randn(5, 4) # datos normalmente distribuidos
media=datos.mean()
print(datos)
