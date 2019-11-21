import math
import itertools
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.offline
from plotly.subplots import make_subplots


def plot_scatters(df: pd.DataFrame, cols: list = None, x: str = None, title: str = None, out_path: str = None,
                  show_p: bool = True, return_p: bool = False, h: int = None, w: int = None, marker_size: int = 4,
                  vertical_spacing: float = 0.1, horizontal_spacing: float = 0.1, theme: str = 'simple_white',
                  n_cols: int = 3, renderer: str = 'browser', show_axis: bool = False, show_titles: bool = False):
    """Plot scatters with plotly"""
    # get cols to plot
    if not cols:
        cols = df._get_numeric_data().columns
    num_plots = len(list(itertools.combinations(cols, 2)))
    n_rows = math.ceil(num_plots / n_cols)
    if show_titles:
        subplot_titles = tuple(f'{x[0]} vs {x[1]}' for x in itertools.combinations(cols, 2))
    else:
        subplot_titles = None
    p = make_subplots(rows=n_rows, cols=n_cols, vertical_spacing=vertical_spacing,
                      horizontal_spacing=horizontal_spacing, subplot_titles=subplot_titles)
    # figure out what to plot where on the subplot
    axes_dict = dict()
    i = 0
    for index, x in np.ndenumerate(np.zeros((n_cols, n_rows))):
        axes_dict[i] = index
        i += 1
    # make each plot
    for i, pair in enumerate(itertools.combinations(cols, 2)):
        x = pair[0]
        y = pair[1]
        i_row = axes_dict[i][1]+1
        i_col = axes_dict[i][0]+1
        p.add_trace(go.Scatter(x=df[x], y=df[y], name=f'{x} vs {y}', mode='markers', marker=dict(size=marker_size)),
                    row=i_row, col=i_col)
        p.update_xaxes(title_text=x, row=i_row, col=i_col, title_standoff=0,
                       showline=show_axis, linewidth=1, linecolor='grey', showticklabels=show_axis, ticks='')
        p.update_yaxes(title_text=y, row=i_row, col=i_col, title_standoff=0,
                       showline=show_axis, linewidth=1, linecolor='grey', showticklabels=show_axis, ticks='')
    p.update_layout(showlegend=False)
    if title:
        p.update_layout(title_text=title)
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
