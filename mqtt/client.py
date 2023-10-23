# TODO delete here for prod version
import random
from copy import deepcopy
from pickle import load

from db.models.entity import Type, Sensor

from time import sleep


def parse_values():
    types = {
        item.name: item.id
        for item in list(Type.select())
    }
    data = load(open("data/file.bin", "rb"))
    for items in data:
        items = deepcopy(items)
        items.pop("stand_number")
        time = items.pop("time")
        for key in items:
            Sensor.create(
                # TODO delete here for prod version
                value=float(items[key]) + random.uniform(0, 10),
                type=types[key],
                date=time
            )
        sleep(1)


if __name__ == '__main__':
    parse_values()
