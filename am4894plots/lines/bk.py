

def plot_lines(df: pd.DataFrame, cols: list = None, x: str = None, h: int = 300, w: int = 1200,
               tools: str = 'box_zoom,save,hover,reset', x_axis_type: str = 'datetime', toolbar_location: str = 'above',
               hover: bool = True, out_path: str = "scratchpad/ts.html"):
    p = figure(
        plot_height=h,
        plot_width=w,
        x_axis_type=x_axis_type,
        toolbar_location=toolbar_location,
        tools=tools)
    if not cols:
        cols = df._get_numeric_data().columns
    if not x:
        x = df.index.name
    source = ColumnDataSource(df)
    for i, col in enumerate(cols):
        p.line(x, col, source=source, name=col, color=Category20[20][i])
    if hover:
        hover = p.select(dict(type=HoverTool))
        tooltips_list = list([("Datetime", "@time{%y-%m-%d %H:%M:%S}")])
        tooltips_list.extend([(f"{col}", f"@{col}") for col in cols])
        hover.tooltips = tooltips_list
        hover.formatters = {"time": "datetime"}
    output_file(out_path)
    show(p)
