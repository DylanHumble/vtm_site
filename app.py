from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

def calculate_estimate(radius,height):
        top_area = 3.14 * int(radius)**2
        side_area = 2*(3.14*(int(radius)*int(height)))
        total_inch = top_area + side_area
        total_sqft = total_inch / 144
        mat_cost = total_sqft * 25
        labor_cost = total_sqft * 15
        t_estimate = mat_cost + labor_cost
        total_estimate = "{:,.2f}".format(t_estimate)
        return total_estimate

@app.route('/estimate', methods=["GET", "POST"])
def estimate():
    if request.method == "POST":
        radius = request.form.get('radius')
        height = request.form.get('height')
        estimate = calculate_estimate(radius,height)
        return render_template('estimate.html', estimate=estimate)
    return render_template('estimate.html')



if __name__ == '__main__':
    app.run(debug=True)