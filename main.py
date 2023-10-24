from multiprocessing import Process

from db.models.entity import Sensor
from db.settings.connect import db
from db.settings.init import init_db
from mqtt.client import parse_values
from plot.animate import animate_line_plot
from plot.generate import generate_all_plots
import matplotlib

matplotlib.use('TkAgg')


def main():
    with db:
        mqtt_client = Process(target=parse_values)
        animate_plot = Process(target=animate_line_plot)
        mqtt_client.start()
        animate_plot.start()
        mqtt_client.join()
        animate_plot.join()
        generate_all_plots()


if __name__ == '__main__':
    Sensor.drop_table()
    try:
        init_db()
        main()
    except KeyboardInterrupt:
        pass

