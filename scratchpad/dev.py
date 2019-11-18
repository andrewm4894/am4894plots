#%%

from am4894pd.utils import df_dummy_ts
from am4894plots.lines.bk import plot_lines, plot_lines_grid

#%%

df = df_dummy_ts(n_cols=5, smooth_n=5000)
print(df.shape)

#%%

p = plot_lines(df, out_path='scratchpad/plot.html', return_p=True, show_p=False)

#%%

print(type(p))

#%%

print(type(p))
'bokeh.plotting.figure.Figure'
print(p.plot_height)
300
print(p.plot_width)
1200
print(len(p.toolbar.__dict__.get('_property_values').get('tools')))
5

#%%

print(p.l)


#%%

#plot_lines_grid(df, h=200, out_path='scratchpad/plot.html')
