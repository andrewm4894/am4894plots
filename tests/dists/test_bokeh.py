from am4894pd.utils import df_dummy_ts
from am4894plots.dists.bokeh import plot_hists


def test_plot_hists():
    df = df_dummy_ts(n_cols=2, freq='1min')
    p = plot_hists(df, out_path=None, return_p=True, show_p=False)
    assert str(type(p)) == "<class 'bokeh.models.layouts.GridBox'>"
    assert len(p.children) == 2
