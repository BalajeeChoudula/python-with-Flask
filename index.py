from app import create_app
from app.routes import routes
from flask import redirect
app = create_app()
@app.context_processor
def inject_menu():
    items = [route.name for route in routes]
    routesList = [{'name': item, 'url': f'/{item}'} for item in items[:len(items)-1]]
    return dict(menu=routesList)

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/pagenotfound')

if __name__ == '__main__':
    app.run(debug=True)
