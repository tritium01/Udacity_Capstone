from src.main import create_app

app = create_app()
# host='0.0.0.0', port=8080, debug=True
if __name__ == '__main__':
    app.run()
