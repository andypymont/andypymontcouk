from werkzeug.wsgi import DispatcherMiddleware

from app import app as app_homepage
import fantasydrafts
import fantasypl

from flask import render_template
from flask_sslify import SSLify

sslify_fantasydrafts = SSLify(fantasydrafts.app)
sslify_fantasypl = SSLify(fantasypl.app)
sslify_homepage = SSLify(app_homepage)

app = DispatcherMiddleware(app_homepage, {'/drafts': fantasydrafts.app,
										  '/fantasypl': fantasypl.app})

@app_homepage.route('/')
def index():
	return render_template('index.html',
						   drafts=[{'name': 'Necessary Roughness 2014', 'url': '/drafts/necessary-roughness-2014'},
								   {'name': 'Fantasy Premier League 2014-15', 'url': '/drafts/fantasy-premier-league-2014-15'}])

if __name__ == '__main__':
	app.run()