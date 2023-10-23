from peewee import PrimaryKeyField, Model

from db.settings.connect import db


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'
