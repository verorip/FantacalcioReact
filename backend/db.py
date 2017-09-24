from main import app, db

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
        return data


calciatore = compravendita('Messi', 'Bassi', 'Real Madrid', 'A', 12)
if decode_auth_token(token):
    db.session.add(calciatore)
    db.session.commit()
    return calciatori = compravendita.query.all()
