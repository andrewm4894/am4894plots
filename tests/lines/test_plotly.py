from am4894pd.utils import df_dummy_ts
from am4894plots.lines.plotly import plot_lines, plot_lines_grid

# make test data
df = df_dummy_ts(n_cols=2, freq='1min')


def test_plot_lines():
    p = plot_lines(df, out_path=None, return_p=True, show_p=False)
    assert str(type(p)) == "<class 'plotly.graph_objs._figure.Figure'>"
    assert len(p.data) == 2
    assert [p.data[c].name for c in range(len(p.data))] == ['col0', 'col1']
    assert [len(p.data[c].x) for c in range(len(p.data))] == [1342, 1342]


def test_plot_lines_grid():
    p = plot_lines_grid(df, out_path=None, return_p=True, show_p=False)
    assert str(type(p)) == "<class 'plotly.graph_objs._figure.Figure'>"
    assert len(p.data) == 2
    assert [p.data[c].name for c in range(len(p.data))] == ['col0', 'col1']
    assert [p.data[c].xaxis for c in range(len(p.data))] == ['x', 'x2']
    assert [len(p.data[c].x) for c in range(len(p.data))] == [1342, 1342]



