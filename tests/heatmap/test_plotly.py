from am4894pd.utils import df_dummy_ts
from am4894plots.heatmap.plotly import plot_heatmap

# make test data
df = df_dummy_ts(n_cols=2, freq='1min')


def test_plot_heatmap():
    p = plot_heatmap(df, out_path=None, return_p=True, show_p=False)
    assert str(type(p)) == "<class 'plotly.graph_objs._figure.Figure'>"
    assert len(p.data[0]['x']) == 2684
    assert len(p.data[0]['y']) == 2684
    assert len(p.data[0]['z']) == 2684
    assert set(p.data[0]['y']) == {'col0', 'col1'}
