import pandas as pd
import numpy as np
from bokeh.io import output_file, curdoc, output_notebook
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show


def plot_hists(df: pd.DataFrame, cols: list = None, n_bins: int = 50, n_cols: int = 3, pw: int = 400, ph: int = 400,
              out_path: str = None, return_p: bool = False, notebook: bool = False, p_theme: str = 'light_minimal',
              show_p: bool = True, density: bool = False):
    """Plot histograms"""
    # get cols to plot
    if not cols:
        cols = df._get_numeric_data().columns
    plots = []
    for i, col in enumerate(cols):
        hist, edges = np.histogram(df[col], density=density, bins=n_bins)
        p = figure(title=col, tools='', background_fill_color="#fafafa")
        p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="navy", line_color="white", alpha=0.5)
        plots.append(p)
    if out_path:
        output_file(out_path)
    curdoc().theme = p_theme
    if notebook:
        output_notebook()
    p = gridplot(plots, ncols=n_cols, plot_width=pw, plot_height=ph, toolbar_location=None)
    if show_p:
        show(p)
    if return_p:
        return p
