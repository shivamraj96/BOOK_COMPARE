import flask
from views.books import books_api

app = flask.Flask(__name__)
app.config["DEBUG"] = True


app.register_blueprint(books_api , url_prefix='/books')


@app.route('/', methods=['GET'])
def welcome():
    
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


app.run()