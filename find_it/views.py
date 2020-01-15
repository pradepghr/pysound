from flask import render_template, request

from find_it import app
from find_it.forms import SearchForm


@app.route('/', methods=['GET', 'POST'])
def index():
    # print(app.config['BASE_DIR'])
    form = SearchForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            url = form.url.data
            return url
    else:
        return render_template('index.html', form=form)
