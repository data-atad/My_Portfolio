from flaskapp_portfolio import create_app #import from __init__.py file

app = create_app() #create app instance. create_app() takes argument config file. here you can pass dirrerent configuration

if __name__ == '__main__':
    app.run(debug=True)
