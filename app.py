from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from all_web import data_address

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))


    def __repr__(self):
        return f'Place: {self.name}'


@app.route('/')
def fill_db():
    places = data_address()

    for name, address in places.items():
        query = db.select(Place).filter_by(name=name)
        exists = db.session.execute(query).first()

        if not exists:
            new_place = Place(name=name, address=address)
            db.session.add(new_place)

    db.session.commit()    

    return 'database filled'      


if __name__ == '__main__':
    app.run(debug=True)              