from todo_controller import app
from todo_model import create_connection

if __name__ == "__main__":
    app.run(debug=True)
    create_connection().close()
