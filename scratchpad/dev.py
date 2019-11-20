#%%
import math
import seaborn as sns
import matplotlib.pyplot as plt

from am4894pd.utils import df_dummy_ts

df = df_dummy_ts(n_cols=3, freq='1min')
print(df.shape)

cols = df.columns
cols_len = len(cols)
n_cols = 2
if cols_len == n_cols:
    n_cols = n_cols - 1
n_rows = math.ceil(cols_len / n_cols)
figsize = (10, 8)
fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)

print(n_rows, n_cols)

for i, col in enumerate(cols):
    ax_row = i // n_cols
    ax_col = i % n_cols
    ax_curr = axes[ax_row, ax_col]
    sns.boxplot(y=col, data=df, ax=ax_curr)

plt.show()

#%%
