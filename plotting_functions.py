import pandas as pd
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource, FactorRange, Whisker


def barplot(df, datacol, title='Title', xlabel='X', ylabel='Y'):
    """
    This function plots a barplot based on a dataframe from within the 
    data_dict
    Args:
        df (DataFrame): a dataframe
    Returns:
        p: a barplot
    By:
        Mahdiye
        Jacob Menzinga
    """

    # create a list of different session types
    types = list(df['type'].unique())

    dff = df.groupby(['participant', 'type']).mean().reset_index()

    # create a list of participants
    participants = list(dff['participant'].unique())

    # create two list of reaction time regarding session types
    control_mean = list(dff[datacol][dff['type'] == 'control'])
    dehydration_mean = list(dff[datacol][dff['type'] == 'dehydration'])

    # create a dictionary of 3 keys and values and then convert into a dataframe
    data = {'participants': participants,
            'control': control_mean,
            'dehydration': dehydration_mean,
            }
    data = pd.DataFrame(data)

    palette = ["skyblue", "salmon"]  # colors

    # create a list like:
    # [ ("blue", "control"), ("Ablue", "dehydration"), ("red", "control"), ("red", "dehydration"), ... ]
    x = [(participant, test) for participant in participants for test in types]
    counts = sum(zip(data['control'], data['dehydration']), ())  # like an hstack

    source = ColumnDataSource(data=dict(x=x, counts=counts))

    # plot
    p = figure(x_range=FactorRange(*x), y_range=[0, df[datacol].max()], 
               width=600, height=400, title=title,
               y_axis_label=ylabel, x_axis_label=xlabel)

    p.vbar(x='x', top='counts', width=1, source=source, line_color="black",
           fill_color=factor_cmap('x', palette=palette,
                                  factors=types, start=1, end=2))

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None

    return p


def calculate_standard_error(df, datacol):
    """
    A function to calculate the standard error of one column within a dataframe
    Args:
        df: one of the dataframes returned in the data_dict
        datacol: the column of wich you want the SE
    Returns:
        data: returns the standard error
    By:
        Mahdiye
        Jacob Menzinga
    """
    df_mean = df.groupby(by=["participant", "type"]).agg(mean=(datacol, "mean"))
    df_se = df.groupby(by=["participant", "type"]).agg(se=(datacol, "sem"))
    upper = df_mean["mean"] + 1.96 * df_se["se"]
    lower = df_mean["mean"] - 1.96 * df_se["se"]
    data = pd.concat([upper.rename("upper"), lower.rename("lower")], axis=1)
    return data


def plot_standard_error(plot, data):
    """
    A function to add the SE as wiskers to an already existing plot
    The data is derived form the 'calculate_standard_error' function.
    Args:
        plot: an alredy existing bokeh plot object
        data: the standard error data
    Returns:
        p: the plot given as argument with added whiskers
    """

    x = list(data.index.values)
    data_map = {
        'x': x,
        'upper': data["upper"].tolist(),
        'lower': data["lower"].tolist()

        }
    source = ColumnDataSource(data=data_map)

    w = Whisker(source=source, base="x", upper="upper", lower="lower",
                line_color='black', level="overlay")
    w.upper_head.line_color = 'black'
    w.lower_head.line_color = 'black'
    w.upper_head.size = w.lower_head.size = 20
    plot.add_layout(w)
    return plot


def plot_error_bar(df, datacol, participants, title, xlabel, ylabel):
    """
    Plots a barplot with error whiskers
    Args:
        df (DataFrame): a dataframe from the data_dict
        datacol (string): the column name of the y-variable you want to plot
        participants (list): the participants wich you want to have included in
                             the plot.
        title (string): the title of the plot
        xlabel (string): the label on the x-axis
        ylabel (string): the label on the y-axis
    Returns:
        bokeh object: a bokeh barplot with error whiskers
    By:
        Mahdiye
        Jacob Menzinga
    """
    df = df[df.participant.isin(participants)]
    data_se = calculate_standard_error(df, datacol)
    p = barplot(df, datacol, title, xlabel, ylabel)
    p = plot_standard_error(p, data_se)

    return p
