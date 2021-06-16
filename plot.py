import pandas as pd
import plotly.graph_objects as go


def build_plot(data, curr):
    resp = pd.read_json(path_or_buf=data)
    fig = go.Figure()
    fig.add_trace(go.Scatter(name="Open", x=resp['open'].keys(), y=resp['open']))
    fig.add_trace(go.Scatter(name="High", x=resp['high'].keys(), y=resp['high']))
    fig.add_trace(go.Scatter(name="Low", x=resp['low'].keys(), y=resp['low']))
    fig.add_trace(go.Scatter(name="Close", x=resp['close'].keys(), y=resp['close']))
    name = "{curr}.png".format(curr=curr)
    fig.write_image("{name}".format(name=name))
    path = "/home/rsk/PycharmProjects/exchanger/{name}".format(name=name)
    return path
