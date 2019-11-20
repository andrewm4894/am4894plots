import pandas as pd
from bokeh.io import curdoc, output_notebook
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, show, output_file
from bokeh.palettes import Category20


def make_figure(h: int = 300, w: int = 1200, t_str: str = 'box_zoom,pan,hover,reset,save',
                x_type: str = 'datetime', t_loc: str = 'above', x_range=None, y_range=None):
    """Helper to make a figure object"""
    p = figure(plot_height=h, plot_width=w, x_axis_type=x_type, toolbar_location=t_loc,
               tools=t_str, x_range=x_range, y_range=y_range, active_drag='box_zoom')
    return p


def add_hover(p, cols: list = None, x_col: str = 'time'):
    """Helper function to add hovers to plot object p"""
    hover = p.select(dict(type=HoverTool))
    tooltips_list = list([("", f"@{x_col}{{%Y-%m-%d %H:%M:%S}}")])
    tooltips_list.extend([(f"{col}", f"@{col}") for col in cols])
    hover.tooltips = tooltips_list
    hover.formatters = {x_col: "datetime"}


def plot_lines(df: pd.DataFrame, cols: list = None, x: str = None, h: int = 300, w: int = 1200,
               t_str: str = 'box_zoom,pan,hover,reset,save', x_type: str = 'datetime', show_p: bool = True,
               t_loc: str = 'right', out_path: str = None, return_p: bool = False, palette: str = 'Category20',
               p_theme: str = 'light_minimal', notebook: bool = False):
    """Plot lines.
    """
    # get cols to plot
    if not cols:
        cols = df._get_numeric_data().columns
    # define x axis if needed
    if not x:
        x = df.index.name
    # define source
    source = ColumnDataSource(df)
    # define palette
    if palette == 'Category20':
        p_palette = Category20[20]
    else:
        raise NotImplementedError(f'... palette {palette} not implemented ...')
    p = make_figure(h=h, w=w, x_type=x_type, t_loc=t_loc, t_str=t_str)
    for i, col in enumerate(cols):
        p.line(x, col, source=source, name=col, color=p_palette[i])
        add_hover(p, cols)
    if out_path:
        output_file(out_path)
    curdoc().theme = p_theme
    if notebook:
        output_notebook()
    if show_p:
        show(p)
    if return_p:
        return p


def plot_lines_grid(df: pd.DataFrame, cols: list = None, x: str = None, h: int = 300, w: int = 1200,
                    t_str: str = 'box_zoom,pan,hover,reset,save', x_type: str = 'datetime', show_p: bool = True,
                    t_loc: str = 'right', out_path: str = None, return_p: bool = False, notebook: bool = False,
                    share_x: bool = True, share_y: bool = False, palette: str = 'Category20',
                    p_theme: str = 'light_minimal'):
    """Plot lines grid.
    """
    # get cols to plot
    if not cols:
        cols = df._get_numeric_data().columns
    # define x axis if needed
    if not x:
        x = df.index.name
    # define source
    source = ColumnDataSource(df)
    # define palette
    if palette == 'Category20':
        p_palette = Category20[20]
    else:
        raise NotImplementedError(f'... palette {palette} not implemented ...')
    # define some variables
    grid_list = []
    x_range = None
    y_range = None
    # loop over each col to be plotted
    for i, col in enumerate(cols):
        if i == 0:
            p0 = make_figure(h=h, w=w, x_type=x_type, t_loc=t_loc, t_str=t_str)
            p0.line(x, col, source=source, name=col, color=p_palette[i])
            if share_x:
                x_range = p0.x_range
            if share_y:
                y_range = p0.y_range
            add_hover(p0, cols)
            grid_list.append([p0])
        else:
            p = make_figure(h=h, w=w, x_type=x_type, t_loc=t_loc, t_str=t_str, x_range=x_range, y_range=y_range)
            p.line(x, col, source=source, name=col, color=p_palette[i])
            add_hover(p, cols)
            grid_list.append([p])
    p = gridplot(grid_list, toolbar_location=t_loc)
    if out_path:
        output_file(out_path)
    curdoc().theme = p_theme
    if notebook:
        output_notebook()
    if show_p:
        show(p)
    if return_p:
        return p
