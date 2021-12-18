import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

########### Define your data
df = pd.read_csv("parameters_v2.csv", delimiter = ';')'

########### Set up the figure
fig = go.Figure(data=
    go.Parcoords(
        line = dict(color = df['accuracy'],
                   colorscale = [[0,'purple'],[0.5,'lightseagreen'],[1,'gold']]),
        dimensions = list([
            dict(range = [0,5],
                label = 'Epoch', values = df['epoch']),
            dict(range = [0,0.0005],
                label = 'Learning rate', values = df['Lr']),
            dict(range = [0,18],
                label = 'Batch size', values = df['batch size']),
            dict(range = [0,100],
                label = 'Accuracy', values = df['accuracy'])
        ]),
    ),
            
)

fig.update_layout(
    plot_bgcolor = 'white',
    paper_bgcolor = 'white',
    title ="This figure shows the interaction between hyperparameters and the accuracy that was achieved."
)

########### Initiate the app
app = dash.Dash()

########### Set up the layout
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server()
