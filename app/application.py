from app import app, db
from app.database import ListTable, LinkTable, AssociationTable, List

def get_lists():
    lists = ListTable.query.all()
    for list in lists:
        print(list.name, list.description)
    return {list.name: list.as_dict() for list in lists}


def get_list(list_name):
    list = List(list_name)
    return list.as_dict()


def create_list(list_name, list_description):
    new_list = ListTable(name=list_name, description=list_description)
    db.session.add(new_list)
    db.session.commit()
    return "success"


def add_link(list_name, link_name, link_url):
    list = ListTable.query.filter_by(name=list_name).first()
    new_link = LinkTable(name=link_name, url=link_url, list_id=list.id)
    db.session.add(new_link)

    # todo collisions
    new_link_id = LinkTable.query.filter_by(name=link_name).first().id

    new_association = AssociationTable(list_id=list.id, link_id= new_link_id)
    db.session.add(new_association)
    db.session.commit()
    return "success"
