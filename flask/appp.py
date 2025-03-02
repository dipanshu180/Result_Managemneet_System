from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def home():
    # Load CSV (Spark Output)
    df = pd.read_csv('pyhton/average_marks/part-00000')
    fig = px.bar(df, x='subject', y='average', title='Average Marks')
    graph_html = fig.to_html(full_html=False)
    return render_template('dashboard.html', plot=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
