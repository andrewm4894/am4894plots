#%%

from am4894pd.utils import df_dummy_ts
from am4894plots.dist.bokeh import plot_hists

df = df_dummy_ts(n_cols=2, freq='1min')
print(df.shape)


plot_hists(df, out_path='tmp/plot.html')

