#%%
import pandas as pd
from am4894pd.utils import df_dummy_ts
from am4894plots.plots import plot_heatmap


df = df_dummy_ts(n_cols=2, freq='1min')
print(df.shape)

#%%

p = plot_heatmap(df, return_p=True, show_p=False)

#%%

set(p.data[0]['y'])
