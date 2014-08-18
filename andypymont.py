from werkzeug.wsgi import DispatcherMiddleware

from app import app as app_homepage
import fantasydrafts

from flask import render_template

app = DispatcherMiddleware(app_homepage, {'/drafts': fantasydrafts.app})

@app_homepage.route('/')
def index():
	return render_template('index.html', drafts=fantasydrafts.get_latest_drafts())

if __name__ == '__main__':
	app.run()