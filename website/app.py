from website.create import create_app

def Exec():
    app = create_app()
    app.run(debug=True)

Exec()
