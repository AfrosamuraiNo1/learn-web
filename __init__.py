from flask import Flask, render_template



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        title = "Новости Python"
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = News.query.order_by(News.published.desc()).all()
        return render_template('index.html',page_title=title, weather=weather, news_list=news)
    
    return app
