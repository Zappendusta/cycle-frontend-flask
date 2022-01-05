from app import app, db
from app.models import CycleEntry

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'CycleEntry': CycleEntry}

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=80, debug=False)
    app.run(debug=True)