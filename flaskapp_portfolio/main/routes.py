from flask import render_template, Blueprint, url_for

main  = Blueprint('main', __name__)

@main.route("/", methods=['GET'])

def portfolio():

	return render_template('index.html', title='Portfolio - Giorgi K.')



