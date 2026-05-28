import time

from cloud import MQTTClient
from sensor import Sensor, humedad, presion, temperatura


def main() -> None:
    sensor_temp = Sensor("TempSensor", "Temperatura", temperatura)
    sensor_hum = Sensor("HumeSensor", "Humedad", humedad)
    sensor_press = Sensor("PressSensor", "Presión", presion)

    cloud_1 = MQTTClient(node="nodo_1")
    cloud_2 = MQTTClient(node="nodo_2")

    try:
        while True:
            print("- Sensores ", "-" * 38)
            print(sensor_temp)
            print(sensor_hum)
            print(sensor_press)
            print("-" * 50)

            cloud_1.send(sensor_temp, sensor_temp.get_data())
            cloud_1.send(sensor_hum, sensor_hum.get_data())
            cloud_2.send(sensor_press, sensor_press.get_data())

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSaliendo...")
    finally:
        print("Programa detenido con éxito")


if __name__ == "__main__":
    main()
