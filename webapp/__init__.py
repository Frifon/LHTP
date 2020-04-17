from flask import Flask, render_template, flash, redirect, url_for
from webapp.model import db

from webapp.forms import SpanishForm


def create_app():
	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	db.init_app(app)
    
	@app.route('/')
	def index():
		spanish_form = SpanishForm()
		return render_template('index.html', page_title="gogo!", form=spanish_form)


	@app.route('/', methods=['POST'])
	def process_spanish():
		form = SpanishForm()
		if form.validate_on_submit():
			spanish_word = form.spanish_word.data
			english_words = form.english_words.data
			flash(spanish_word + english_words)
			return redirect(url_for('index'))
		flash('wrong data :(')
		return redirect(url_for('index'))

	return app


