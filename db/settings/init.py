from peewee import IntegrityError

from db.models.entity import Type, Sensor
from db.settings.connect import db
from db.settings.defualt import types


def init_db():
    with db:
        db.create_tables([Type, Sensor, ])

    try:
        Type.insert_many(types).execute()
    except IntegrityError as exception:
        if str(exception) != "UNIQUE constraint failed: type.name":
            raise exception
