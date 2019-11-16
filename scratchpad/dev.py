#%%
import pandas as pd
import numpy as np
from am4894pd.utils import df_dummy_ts
import bokeh
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, show, output_file
from bokeh.palettes import Category20

#%%

df = df_dummy_ts(n_cols=2)
print(df.shape)

#%%


def plot_lines(df: pd.DataFrame, cols: list = None, x: str = None, h: int = 300, w: int = 1200,
               tools: str = 'box_zoom,save,hover,reset', x_axis_type: str = 'datetime', toolbar_location: str = 'above',
               hover: bool = True, out_path: str = "scratchpad/ts.html"):
    p = figure(
        plot_height=h,
        plot_width=w,
        x_axis_type=x_axis_type,
        toolbar_location=toolbar_location,
        tools=tools)
    if hover:
        hover = p.select(dict(type=HoverTool))
        hover.tooltips = [("Datetime", "@time{%y-%m-%d %H:%M:%S}"), ("Series", "$name"), ("Value", "@$name")]
        hover.formatters = {"time": "datetime"}
    if not cols:
        cols = df._get_numeric_data().columns
    if not x:
        x = df.index.name
    source = ColumnDataSource(df)
    for i, col in enumerate(cols):
        p.line(x, col, source=source, name=col, color=Category20[20][i])
    output_file(out_path)
    show(p)


#%%

plot_lines(df, x='time')


#%%

print(df)
