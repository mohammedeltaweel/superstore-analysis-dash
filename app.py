from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("https://github.com/mohammedeltaweel/superstore-analysis-dash/files/12381114/raw-data.csv", encoding="windows-1252")
print(df.head())
app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Super Store Analysis', style={'textAlign':'center'}),

])

if __name__ == '__main__':
    app.run(debug=True)
