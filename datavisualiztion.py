import bar_chart_race as bcr
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('yearly_subject_uptake.csv')


bcr.bar_chart_race(
    df=df,
    filename='subject_uptake_anim.mp4',
    orientation='h',
    sort='desc',
    n_bars=15,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=60,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    perpendicular_bar_func='median',
    period_length=2000,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12',
    title='Year Subject Uptake (2019-2022)',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family' : 'calibri', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=True
    )  