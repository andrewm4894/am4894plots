import numpy as np
import pandas as pd
import plotly
import math
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_boxes(df: pd.DataFrame, cols: list = None, out_path: str = None, show_p: bool = True, return_p: bool = False,
               h: int = None, w: int = None, spacing: float = 0.05, theme: str = 'simple_white',
               renderer: str = 'browser', n_cols: int = 3, shared_yaxes: bool = True):
    """plot box plots"""
    # get cols to plot
    if not cols:
        cols = df._get_numeric_data().columns
    n_rows = math.ceil(len(cols) / n_cols)
    p = make_subplots(rows=n_rows, cols=n_cols, shared_yaxes=shared_yaxes, vertical_spacing=spacing, horizontal_spacing=spacing)
    # figure out what to plot where on the subplot
    axes_dict = dict()
    i = 0
    for index, x in np.ndenumerate(np.zeros((n_cols, n_rows))):
        axes_dict[i] = index
        i += 1
    # make each plot
    for i, col in enumerate(cols):
        p.add_trace(go.Box(name=col, y=df[col]), row=axes_dict[i][1]+1, col=axes_dict[i][0]+1)
    if h:
        p.update_layout(height=h)
    if w:
        p.update_layout(width=w)
    p.update_layout(template=theme)
    if out_path:
        plotly.offline.plot(p, filename=out_path, auto_open=False)
    if show_p:
        p.show(renderer=renderer)
    if return_p:
        return p
