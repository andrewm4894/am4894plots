import pandas as pd
import plotly.graph_objects as go
import plotly.offline
from plotly.subplots import make_subplots


def plot_lines(df: pd.DataFrame, cols: list = None, x: str = None, title: str = None, slider: bool = True,
               out_path: str = None, show_p: bool = True, return_p: bool = False, h: int = None, w: int = None,
               theme: str = 'simple_white', lw: int = 1, renderer: str = 'browser'):
    """Plot lines with plotly"""
    p = go.Figure()
    # get cols to plot
    if not cols:
        cols = df._get_numeric_data().columns
    # define x axis if needed
    if not x:
        x = df.index
    else:
        x = df[x]
    for i, col in enumerate(cols):
        p.add_trace(go.Scatter(x=x, y=df[col], name=col, line=dict(width=lw)))
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
        plotly.offline.plot(p, filename=out_path, auto_open=False)
    if show_p:
        p.show(renderer=renderer)
    if return_p:
        return p
