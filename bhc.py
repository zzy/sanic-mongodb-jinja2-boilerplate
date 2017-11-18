from sanic import Sanic
from sanic.response import json

<<<<<<< HEAD
template = SanicJinja2(app)

@app.route('/')
async def index(request):
    return template.render('index.html', request, greetings='BudsHome.com will be coming soon ...')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
=======
app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
>>>>>>> 0a1102b5d09c5ed33a4833a64b634e11624894e4
