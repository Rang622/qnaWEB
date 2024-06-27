from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM 초기화
    db.init_app(app)
    migrate.init_app(app, db)
    from . import modes

    # 모델을 애플리케이션과 함께 초기화
    from . import models

    # 블루프린트 등록
    from .views import main_views, user_views, product_views, order_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(user_views.bp, url_prefix='/user')
    app.register_blueprint(product_views.bp, url_prefix='/product')
    app.register_blueprint(order_views.bp, url_prefix='/order')

    return app
