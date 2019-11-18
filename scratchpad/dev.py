#%%

from am4894pd.utils import df_dummy_ts
from am4894plots.lines.bk import plot_lines, plot_lines_grid

#%%

df = df_dummy_ts(n_cols=2)
print(df.shape)

#%%

p = plot_lines_grid(df, out_path='scratchpad/plot.html', return_p=True, show_p=False)

#%%

print(type(p))

#%%

#dir(p)
#len(p.children[0].to_json(include_defaults=True)['children'])
p.children[0].to_json(include_defaults=True)['children'][0][0]['type']


#%%

print(p.l)


#%%

#plot_lines_grid(df, h=200, out_path='scratchpad/plot.html')
