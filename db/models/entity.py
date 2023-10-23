from peewee import (
    CharField,
    DecimalField,
    DateTimeField,
    ForeignKeyField,
)

from db.models.base import BaseModel


class Type(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'type'


class Sensor(BaseModel):
    value = DecimalField()
    date = DateTimeField()
    type = ForeignKeyField(Type)

    class Meta:
        db_table = 'sensor'
