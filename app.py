import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("parameters_v2.csv", delimiter = ';')

########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='Common sense challenge!'
myheading='Common sense challenge - Group 32'
myheading2='This figure shows the interaction between hyperparameters and the accuracy that was achieved'
label1='IBU'
label2='ABV'
githublink='https://github.com/naomioe/flying-dog-beers'

########### Set up the chart
#bitterness = go.Bar(
 #   x=beers,
 #   y=ibu_values,
 #   name=label1,
 #   marker={'color':color1}
#)
#alcohol = go.Bar(
#    x=beers,
 #   y=abv_values,
 #   name=label2,
 #   marker={'color':color2}
#)

#beer_data = [bitterness, alcohol]
#beer_layout = go.Layout(
 #   barmode='group',
 #   title = mytitle
#)

beer_fig = go.Figure(data=
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


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.H2(myheading2),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    ]
)

if __name__ == '__main__':
    app.run_server()
