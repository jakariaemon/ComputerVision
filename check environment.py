import sys
import tensorflow as tf
import pandas as pd
import sklearn as sk
import numpy as np
import matplotlib


print(f"Python {sys.version}")
print()
print(f"Tensorflow version: {tf.__version__}")
print(f"Keras Version: {tf.keras.__version__}")
print()
print(f"Pandas: {pd.__version__}")
print(f"Scikit-Learn: {sk.__version__}")
print(f"Numpy: {np.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print()
print("GPU is ", "available" if tf.config.list_physical_devices('GPU') else "not available")
print(f"CUDA: {tf.test.is_built_with_cuda()}")