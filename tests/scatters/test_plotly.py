import itertools
from am4894pd.utils import df_dummy_ts
from am4894plots.scatters.plotly import plot_scatters

# make test data
df = df_dummy_ts(n_cols=4, freq='1min')


def test_plot_scatters():
    p = plot_scatters(df, out_path=None, return_p=True, show_p=False)
    assert str(type(p)) == "<class 'plotly.graph_objs._figure.Figure'>"
    assert len(list(itertools.combinations(df.columns, 2))) == 6
    assert [p.data[c].name for c in range(len(p.data))] == [f'{x[0]} vs {x[1]}' for x in itertools.combinations(df.columns, 2)]
