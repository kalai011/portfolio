
from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "CRUD Blog Application",
        "description": "Secure Flask blog app with login authentication and MySQL database.",
        "tech": ["Flask", "MySQL", "Bootstrap"]
    },
    {
        "title": "Shopping Website",
        "description": "Modern shopping platform with cart and checkout system.",
        "tech": ["Flask", "JavaScript", "MySQL"]
    },
    {
        "title": "Weather App",
        "description": "Live weather dashboard using third-party API integration.",
        "tech": ["Flask", "API", "HTML/CSS"]
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
