from time import sleep, time

from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from numpy import (
    max,
    min,
    mean,
    arange,
    linspace,
    convolve,
    ones,
)

from db.models.entity import Sensor, Type
from db.settings.defualt import DefaultType


def animate_line_plot():
    interp = 500
    window_size = 5  # Размер окна скользящей средней
    type_id = Type.get(Type.name == DefaultType.temperature)
    plt.ion()

    end_time = time() + 60 * 10
    while end_time - time() >= 0:
        data = list(map(lambda x: float(x.value), Sensor.select().where(Sensor.type == type_id)))
        if len(data) > 0:
            x = linspace(0, len(data) - 1, interp)
            f = interp1d(arange(len(data)), data)
            data_interpolated = f(linspace(0, len(data) - 1, interp))

            moving_avg = convolve(data, ones(window_size) / window_size, mode='valid')
            x_moving_avg = linspace(0, len(data) - window_size, len(moving_avg))

            plt.clf()
            plt.plot(x, data_interpolated, label="Интерполированные данные")
            plt.plot(
                x_moving_avg,
                moving_avg,
                label=f'Скользящее среднее ({window_size}-точечное окно)',
                color='orange'
            )
            plt.ylabel("Температура")
            plt.axhline(value := min(data), color='red', linestyle='--', label=f'Min: {value:.4}')
            plt.axhline(value := max(data), color='green', linestyle='--', label=f'Max: {value:.4}')
            plt.axhline(value := float(mean(data)), color='blue', linestyle='--', label=f'Mean: {value:.4}')
            plt.legend(loc='upper right')
            plt.grid()
            plt.title("График температуры")
            plt.draw()
            plt.gcf().canvas.flush_events()
        sleep(1)
        plt.pause(0.01)
    plt.ioff()
    plt.show()
