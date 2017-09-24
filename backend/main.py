import json

from flask import Flask
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import render_template


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class compravendita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_gioc = db.Column(db.String(80), unique=True)
    nome_comp = db.Column(db.String(80), unique=False)
    team = db.Column(db.String(80), unique=False)
    ruolo = db.Column(db.String(1), unique=False)
    prezzo = db.Column(db.Integer)

    def __init__(self, nome_gioc, nome_comp, team, ruolo, prezzo):
        self.nome_gioc = nome_gioc
        self.nome_comp = nome_comp
        self.team = team
        self.ruolo = ruolo
        self.prezzo = prezzo

    def __repr__(self):
        data = {
            'nome_gioc': self.nome_gioc,
            'nome_comp': self.nome_comp,
            'team': self.team,
            'ruolo': self.ruolo,
            'prezzo': self.prezzo,
        }
        return json.dumps(data)
db.create_all()

@app.route("/api/full")
def full():
    full = compravendita.query.all()
    calciatori = []
    for calciatore in full:
        temp = {'nome_gioc': calciatore.nome_gioc,
               'nome_comp': calciatore.nome_comp,
               'team': calciatore.team,
               'ruolo': calciatore.ruolo,
               'prezzo': calciatore.prezzo}
        calciatori.append(temp)
    data = {'calciatori': calciatori}
    return Response(json.dumps(data), mimetype='text/json')

@app.route("/api/single/<id>")
def single(id):
    if int(id) > 0:
        calciatore = compravendita.query.filter_by(id=int(id)).first()
        temp = {'nome_gioc': calciatore.nome_gioc,
               'nome_comp': calciatore.nome_comp,
               'team': calciatore.team,
               'ruolo': calciatore.ruolo,
               'prezzo': calciatore.prezzo}
        data = {'calciatore': temp}
        return Response(json.dumps(data), mimetype='text/json')
    else:
        data = {'calciatore': None}
        return Response(json.dumps(data), mimetype='text/json')

@app.route("/api/new", methods=['POST'])
def new():
    try:
        calciatore = request.values.to_dict()
        print(calciatore)
        new_calciatore = compravendita(calciatore['nome_gioc'],
                                       calciatore['nome_comp'],
                                       calciatore['team'],
                                       calciatore['ruolo'],
                                       calciatore['prezzo'])
        db.session.add(new_calciatore)
        db.session.commit()
        status = {'status': True, 'action': 'NEW_CALCIATORE'}
        return Response(json.dumps(status), mimetype='text/json')
    except Exception as e:
        status = {'status': False, 'action': 'NEW_CALCIATORE', 'error': str(e)}
        return Response(json.dumps(status), mimetype='text/json')


app.run(port=8880)
