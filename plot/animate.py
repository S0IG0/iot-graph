from time import sleep, time

from matplotlib import pyplot as plt
from numpy import (
    max,
    min,
    mean,
)

from db.models.entity import Sensor, Type
from db.settings.defualt import DefaultType


def animate_line_plot():
    type_id = Type.get(Type.name == DefaultType.temperature)
    plt.ion()

    end_time = time() + 60 * 10
    while end_time - time() >= 0:
        data = list(map(lambda x: float(x.value), Sensor.select().where(Sensor.type == type_id)))
        plt.clf()
        plt.plot(data)
        plt.ylabel("Температура")
        plt.axhline(value := min(data), color='red', linestyle='--', label=f'Min: {value:.4}')
        plt.axhline(value := max(data), color='green', linestyle='--', label=f'Max: {value:.4}')
        plt.axhline(value := float(mean(data)), color='blue', linestyle='--', label=f'Mean: {value:.4}')
        plt.legend()
        plt.title("График температуры")
        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(1)
    plt.ioff()
    plt.show()
