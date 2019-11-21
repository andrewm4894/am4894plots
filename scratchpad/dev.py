#%%
import itertools
import pandas as pd
from am4894pd.utils import df_dummy_ts
from am4894plots.scatters.plotly import plot_scatters

df = df_dummy_ts(n_cols=4, freq='1min')
print(df.shape)

plot_scatters(df)
