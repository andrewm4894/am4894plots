import numpy as np
import pandas as pd
import plotly
import math

from am4894plots.utils import get_cols_like
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_boxes(df: pd.DataFrame, cols: list = None, out_path: str = None, show_p: bool = True, return_p: bool = False,
               h: int = None, w: int = None, spacing: float = 0.05, theme: str = 'simple_white',
               renderer: str = 'browser', n_cols: int = 3, shared_yaxes: bool = True, cols_like: list = None):
    """plot box plots"""
    # get cols to plot
    if not cols:
        if cols_like:
            cols = get_cols_like(df, cols_like)
        else:
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


def plot_hists(df: pd.DataFrame, cols: list = None, out_path: str = None, show_p: bool = True, return_p: bool = False,
               h: int = None, w: int = None, spacing: float = 0.05, theme: str = 'simple_white',
               renderer: str = 'browser', n_cols: int = 3, shared_yaxes: bool = True, cols_like: list = None,
               cumulative: bool = False, dim: str = None):
    """plot histogram"""
    # get cols to plot
    if not cols:
        if cols_like:
            cols = get_cols_like(df, cols_like)
        else:
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
        if dim:
            for dim_value in df[dim].unique():
                p.add_trace(
                    go.Histogram(
                        name=f'{col} - {dim_value}',
                        x=df[df[dim] == dim_value][col],
                        cumulative_enabled=cumulative,
                        bingroup=1,
                        histnorm='probability density'
                    ),
                    row=axes_dict[i][1]+1,
                    col=axes_dict[i][0]+1
                )
            p.update_layout(barmode='overlay')
            p.update_traces(opacity=0.5)
        else:
            p.add_trace(
                go.Histogram(
                    name=col, x=df[col], cumulative_enabled=cumulative
                ),
                row=axes_dict[i][1] + 1,
                col=axes_dict[i][0] + 1
            )

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
