from flask import Flask, render_template, request
from imdb import IMDb
from pprint import pprint
from utils import search_result, detail_result

app = Flask(__name__)
ia = IMDb()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    q = request.args['search']
    query_set = search_result(ia=ia, movie=q)
    return render_template('search-results.html', query_set=query_set)


@app.route('/detail', methods=['GET'])
def detail():
    q = request.args['id']
    query = detail_result(ia=ia, id=q)
    return render_template('detail.html', query_set=query)


if __name__ == '__main__':
    app.run(debug=False)
