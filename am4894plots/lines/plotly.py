import os

import pandas as pd
import plotly.graph_objects as go
import plotly.offline
from ndpd.utils import get_cols_like
from plotly.subplots import make_subplots


def plot_lines(df: pd.DataFrame, cols: list = None, cols_like: list = None, x: str = None, title: str = None,
               slider: bool = True, out_path: str = None, show_p: bool = True, return_p: bool = False, h: int = None,
               w: int = None, theme: str = 'simple_white', lw: int = 1, renderer: str = 'browser',
               stacked: bool = False, filltozero: bool = False, shade_regions: list = None,
               shade_color: str = 'Yellow', shade_opacity: float = 0.2, shade_line_width: int = 0,
               marker_list: list = None, marker_mode: str = "text+markers", marker_position: str = "bottom middle",
               marker_color: str = 'Red', marker_size: int = 5):
    """Plot lines with plotly"""

    # set stackedgroup if stacked flag set
    if stacked:
        stackgroup = 'one'
    else:
        stackgroup = None
    if filltozero:
        fill = 'tozeroy'
    else:
        fill = None

    # create figure object
    p = go.Figure()

    # get cols to plot
    if not cols:
        if cols_like:
            cols = get_cols_like(df, cols_like)
        else:
            cols = df._get_numeric_data().columns
    # define x axis if needed
    if not x:
        # if looks like int6e then convert to datetime
        if str(df.index.dtype) == 'int64':
            x = pd.to_datetime(df.index, unit='s')
        else:
            x = df.index
    else:
        x = df[x]
    for i, col in enumerate(cols):
        p.add_trace(go.Scatter(x=x, y=df[col], name=col, line=dict(width=lw), fill=fill, stackgroup=stackgroup))
    if title:
        p.update_layout(title_text=title)
    if slider:
        p.update_layout(xaxis_rangeslider_visible=slider)
    if h:
        p.update_layout(height=h)
    if w:
        p.update_layout(width=w)

    # add any shaded regions
    if shade_regions:
        shapes_to_add = []
        for x_from, x_to in shade_regions:
            # check if region is in the data to be plotted and only plot if is
            if x_from >= x.min() and x_to <= x.max():
                shapes_to_add.append(
                    dict(type="rect", xref="x", yref="paper", x0=x_from, y0=0, x1=x_to, y1=1, fillcolor=shade_color,
                        opacity=shade_opacity, layer="below", line_width=shade_line_width)
                )
        # now add relevant shapes
        p.update_layout(shapes=shapes_to_add)

    # add any markers
    if marker_list:
        for x_at, marker_label in marker_list:
            # check if region is in the data to be plotted and only plot if is
            if x_at >= x.min() and x_at <= x.max():
                p.add_trace(go.Scatter(
                    x=[x_at], y=[0], mode=marker_mode, text=[marker_label], textposition=marker_position,
                    marker=dict(color=marker_color, size=marker_size), showlegend=False)
                )

    p.update_layout(template=theme)

    if out_path:
        out_dir = '/'.join(out_path.split('/')[0:-1])
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        plotly.offline.plot(p, filename=out_path, auto_open=False)
    if show_p:
        p.show(renderer=renderer)
    if return_p:
        return p


def plot_lines_grid(df: pd.DataFrame, cols: list = None, x: str = None, title: str = None, slider: bool = False,
                    out_path: str = None, show_p: bool = True, return_p: bool = False, h: int = None, w: int = None,
                    vertical_spacing: float = 0.002, theme: str = 'simple_white', lw: int = 1,
                    renderer: str = 'browser'):
    """Plot lines with plotly"""
    # get cols to plot
    if not cols:
        cols = df._get_numeric_data().columns
    # define x axis if needed
    if not x:
        x = df.index
    else:
        x = df[x]
    p = make_subplots(rows=len(cols), cols=1, shared_xaxes=True, vertical_spacing=vertical_spacing)
    for i, col in enumerate(cols):
        p.add_trace(go.Scatter(x=x, y=df[col], name=col, line=dict(width=lw)), row=(1+i), col=1)
    if title:
        p.update_layout(title_text=title)
    if slider:
        p.update_layout(xaxis_rangeslider_visible=slider)
    if h:
        p.update_layout(height=h)
    if w:
        p.update_layout(width=w)
    p.update_layout(template=theme)
    if out_path:
        out_dir = '/'.join(out_path.split('/')[0:-1])
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        plotly.offline.plot(p, filename=out_path, auto_open=False)
    if show_p:
        p.show(renderer=renderer)
    if return_p:
        return p
