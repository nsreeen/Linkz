from app import db


class ListTable(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(128))
    links = db.relationship('LinkTable', backref='list')

    def __repr__(self):
        return '<List {}>'.format(self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class LinkTable(db.Model):
    __tablename__ = 'link'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    url = db.Column(db.String(128))
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))

    def __repr__(self):
        return '<Link {}>'.format(self.name)


class AssociationTable(db.Model):
    __tablename__ = 'association'
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))
    link_id = db.Column(db.Integer, db.ForeignKey('link.id'))


class List:
    def __init__(self, list_name):
        list_row = ListTable.query.filter_by(name=list_name).first()
        # todo error handling
        self.name = list_row.name
        self.description = list_row.description
        associations = AssociationTable.query.filter_by(list_id=list_row.id)
        self.links = [Link(a.link_id) for a in associations]

    def as_dict(self):
        return {'name': self.name,
                'description': self.description,
                'links': {link.name: link.url for link in self.links}}


class Link:
    def __init__(self, link_id):
        link_row = LinkTable.query.filter_by(id=link_id).first()
        self.name = link_row.name
        self.url = link_row.url
