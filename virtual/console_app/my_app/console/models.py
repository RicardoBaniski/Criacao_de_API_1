from my_app import db


class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tituloSerie = db.Column(db.String(100))
    genero = db.Column(db.String(50))
    tlTemporadas = db.Column(db.Integer)
    mediaIMDB = db.Column(db.Float)
    ativa = db.Column(db.String(1))

    def __init__(self, tituloSerie, genero, tlTemporadas, mediaIMDB, ativa):
        self.tituloSerie = tituloSerie
        self.genero = genero
        self.tlTemporadas = tlTemporadas
        self.mediaIMDB = mediaIMDB
        self.ativa = ativa

    def __repr__(self):
        return 'Console {0}'.format(self.id)
