#%%

import pandas as pd
from am4894pd.utils import df_dummy_ts
from am4894plots.lines.plotly import plot_lines, plot_lines_grid

df = df_dummy_ts(n_cols=5, freq='1min')
print(df.shape)

#%%

plot_lines(df, out_path='tmp/plot.html')

#%%

plot_lines_grid(df, out_path='tmp/plot.html')


