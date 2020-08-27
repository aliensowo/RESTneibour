from app import db


class Neibour(db.Model):
    __tablename__ = 'neibours-neibour'
    id = db.Column(db.Integer, primary_key=True)
    dx = db.Column(db.Integer, unique=True)
    dy = db.Column(db.Integer, unique=True)
    echo = db.Column(db.Boolean, unique=True)

    def __init__(self, dx=None, dy=None, echo=None):
        self.dx = dx
        self.dy = dy
        self.echo = echo

    def __repr__(self):
        return f'<Neibour {self.id}> at {self.dx}x{self.dy}'
