from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
from simulation import run_simulation, rule_30, generate_automaton
import plotly.graph_objects as go
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    initial_state = np.random.randint(2, size=100)
    steps = 50

    # Generate the cellular automaton
    automaton = generate_automaton(initial_state, steps)

    # Create the Plotly figure
    fig = go.Figure(data=go.Heatmap(z=automaton, colorscale='Viridis'))
    fig.update_layout(
        width=800,  # Adjust the width
        height=600  # Adjust the height
    )
    plot_html = fig.to_html(full_html=False)
    return render_template('index.html', plot_html=plot_html)

# @app.route('/simulate')
# def simulate():
#     result = session.evaluate(wlexpr('RandomInteger[{1, 100}, 10]'))
#     plt.figure()
#     plt.plot(result)
#     img = io.BytesIO()
#     plt.savefig(img, format='png')
#     img.seek(0)
#     plot_url = base64.b64encode(img.getvalue()).decode()
#     return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
