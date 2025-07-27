from app import create_app
from app.routes import routes
app = create_app()
@app.context_processor
def inject_menu():
    items = [route.name for route in routes]
    routesList = [{'name': item, 'url': f'/{item}'} for item in items]
    return dict(menu=routesList)

if __name__ == '__main__':
    app.run(debug=True)
