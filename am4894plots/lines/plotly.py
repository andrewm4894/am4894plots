import pandas as pd
import plotly.graph_objects as go
import plotly.offline


def plot_lines(df: pd.DataFrame, cols: list = None, x: str = None, title: str = None, slider: bool = True,
               out_path: str = None, show_p: bool = True, return_p: bool = False):
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
        p.add_trace(go.Scatter(x=x, y=df[col], name=col))
    if title:
        p.update_layout(title_text=title)
    if slider:
        p.update_layout(xaxis_rangeslider_visible=slider)
    if out_path:
        plotly.offline.plot(p, filename=out_path, auto_open=show_p)
    if show_p:
        p.show()
    if return_p:
        return p
