# src/__init__.py
import os
from flask import Flask  # new
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()


# new
def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    # set up extensions
    db.init_app(app)
    # register blueprints
    from src.api.ping import ping_blueprint

    app.register_blueprint(ping_blueprint)
    from src.api.users import users_blueprint

    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app


# PUT
def test_update_user(test_app, test_database):
    # create user
    user = add_user("John", "john@test.com")

    # update user
    resp = client.put(
        f"/users/{user.id}",
        data=json.dumps({"username": "Johnny"}),
        content_type="application/json",
    )

    # assert response
    updated_user = User.query.get(user.id)
    assert updated_user.username == "Johnny"


# DELETE
def test_delete_user(test_app, test_database):
    user = add_user("John", "john@test.com")

    resp = client.delete(f"/users/{user.id}")

    assert resp.status_code == 204
    assert User.query.get(user.id) is None
