from app.database import db, ma


class Neibour(db.Model):
    __tablename__ = 'neibour'

    id = db.Column(db.Integer, primary_key=True)
    dx = db.Column(db.Integer, unique=True)
    dy = db.Column(db.Integer, unique=True)
    echo = db.Column(db.String)

    def __init__(self, dx, dy, echo):
        self.dx = dx
        self.dy = dy
        self.echo = echo

    def __str__(self):
        return self.id

    def __repr__(self):
        return f'<Neibour {self.id}> at {self.dx}x{self.dy}'


class NeibourSchema(ma.Schema):
    class Meta:
        fields = ('dx', 'dy', 'echo')
