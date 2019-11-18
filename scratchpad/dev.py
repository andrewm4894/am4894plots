#%%

from am4894pd.utils import df_dummy_ts
from am4894plots.lines.bk import plot_lines, plot_lines_grid

#%%

df = df_dummy_ts(n_cols=5)
print(df.shape)

#%%

plot_lines(df, out_path='scratchpad/plot.html')

#%%

plot_lines_grid(df, h=200, out_path='scratchpad/plot.html')
