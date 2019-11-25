import pandas as pd
import plotly
import plotly.graph_objects as go


def plot_heatmap(df: pd.DataFrame, cols: list = None, id_vars: list = None, out_path: str = None, show_p: bool = True,
                 return_p: bool = False, h: int = None, w: int = None, theme: str = 'plotly_white',
                 renderer: str = 'browser', colorscale: str = 'RdBu', showscale: bool = False):
    """plot heatmap"""
    # get cols to plot
    if not cols:
        cols = df._get_numeric_data().columns
    if not id_vars:
        id_vars = list(df.index.names)
    df = pd.melt(df.reset_index(), id_vars=id_vars, value_vars=cols)
    p = go.Figure(data=go.Heatmap(z=df['value'], x=df[','.join(id_vars)], y=df['variable'], colorscale=colorscale,
                                  showscale=showscale))
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
