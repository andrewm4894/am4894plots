#%%

import pandas as pd
from am4894pd.utils import df_dummy_ts
from am4894plots.plots import plot_lines, plot_boxes, plot_hists


df = df_dummy_ts(n_cols=10, freq='1min')
print(df.shape)

#%%

plot_lines(df)

#%%

plot_boxes(df)

#%%

plot_hists(df, out_path='tmp/plot.html')


