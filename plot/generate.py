from cluster.functions import SETTINGS, find_cluster
from db.models.entity import Sensor, Type
from db.settings.defualt import DefaultType
from plot.plots import (
    linear_plot,
    circular_plot,
    columnar_plot,
)


def generate_all_plots():
    motion = list(map(lambda x: float(x.value),
                      Sensor.select().where(Sensor.type == Type.get(Type.name == DefaultType.motion).id)))
    voltage = list(map(lambda x: float(x.value),
                       Sensor.select().where(Sensor.type == Type.get(Type.name == DefaultType.voltage).id)))
    temperature = list(map(lambda x: float(x.value),
                           Sensor.select().where(Sensor.type == Type.get(Type.name == DefaultType.temperature).id)))

    if len(temperature) > 0:
        linear_plot(
            temperature,
            "Температура",
            "График изменения температуры"
        )
    if len(voltage) > 0:
        circular_plot(
            find_cluster(voltage),
            f"Круговая диаграмма\n"
            f"кластеризации изменения\n"
            f"вольтажа с алгоритмом\n"
            f"db-scan: {SETTINGS}"
        )
    if len(motion) > 0:
        columnar_plot(
            find_cluster(motion),
            f"Столбчатая диаграмма\n"
            f"кластеризации изменения\n"
            f"движения с алгоритмом\n"
            f"db-scan: {SETTINGS}"
        )
