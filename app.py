from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
	data = None
	if request.method == "POST":
		city=request.form["cityName"]
		state=request.form["stateName"]
		country=request.form["countryName"]
		measurement=request.form.get("measurementName")
		if measurement == "on":
			measurement = "imperial"
		else:
			measurement = "metric"
		data = get_weather(city, state, country, measurement)
	return render_template('weather.html', data=data)

if __name__ == "__main__":
	app.run(debug=True)