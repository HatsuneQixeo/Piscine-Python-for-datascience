import numpy as np
import statistics as st

print(np.quantile((1, 42, 360, 11, 64), [0.25, .5, 0.75]))
print(st.quantiles((1, 42, 360, 11, 64)))
print(np.percentile((1, 42, 360, 11, 64), [25, 50, 75]))
