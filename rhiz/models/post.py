from rhiz.models import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), default='Change Me')
    
    def _repr_(self):
        return '<Post {}>'.format(self.content[:16])
