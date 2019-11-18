from am4894pd.utils import df_dummy_ts
from am4894plots.lines.bk import plot_lines, plot_lines_grid


def test_plot_lines():
    df = df_dummy_ts(n_cols=2)
    p = plot_lines(df, out_path='scratchpad/plot.html', return_p=True, show_p=False)
    assert str(type(p)) == "<class 'bokeh.plotting.figure.Figure'>"
    assert p.plot_height == 300
    assert p.plot_width == 1200
    assert len(p.toolbar.__dict__.get('_property_values').get('tools')) == 5

