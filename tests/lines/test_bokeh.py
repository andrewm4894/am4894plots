from am4894pd.utils import df_dummy_ts
from am4894plots.lines.bokeh import plot_lines, plot_lines_grid


def test_plot_lines():
    df = df_dummy_ts(n_cols=2)
    p = plot_lines(df, out_path='tmp/test_plot.html', return_p=True, show_p=False)
    assert str(type(p)) == "<class 'bokeh.plotting.figure.Figure'>"
    assert p.plot_height == 300
    assert p.plot_width == 1200
    assert len(p.toolbar.__dict__.get('_property_values').get('tools')) == 5


def test_plot_lines_grid():
    df = df_dummy_ts(n_cols=2)
    p = plot_lines_grid(df, out_path='tmp/test_plot.html', return_p=True, show_p=False)
    assert str(type(p)) == "<class 'bokeh.models.layouts.Row'>"
    assert len(p.children[0].to_json(include_defaults=True)['children']) == 2
    assert p.children[0].to_json(include_defaults=True)['children'][0][0]['type'] == 'Plot'



