import os
import time
from pathlib import Path
from dotenv import load_dotenv
from cloud import MQTTClient
from sensor import Sensor
from sensor_types import (
    calidad_aire,
    co2,
    humedad,
    luz,
    presion,
    ruido,
    temperatura,
)


def main() -> None:
    load_dotenv(Path(__file__).parent.parent / ".env")
    mqtt_broker = os.environ.get("MQTT_BROKER", "localhost")
    mqtt_port = int(os.environ.get("MQTT_PORT", "1883"))
    mqtt_prefix = os.environ.get("MQTT_TOPIC_PREFIX", "casa")

    cloud_1 = MQTTClient(
        node="nodo_1",
        broker=mqtt_broker,
        port=mqtt_port,
        topic_prefix=mqtt_prefix,
    )
    cloud_2 = MQTTClient(
        node="nodo_2",
        broker=mqtt_broker,
        port=mqtt_port,
        topic_prefix=mqtt_prefix,
    )

    readings = [
        (cloud_1, Sensor("TempSensor", "Temperatura", temperatura)),
        (cloud_1, Sensor("HumeSensor", "Humedad", humedad)),
        (cloud_1, Sensor("LightSensor", "Luz", luz)),
        (cloud_1, Sensor("AQISensor", "Calidad de Aire", calidad_aire)),
        (cloud_2, Sensor("PressSensor", "Presión", presion)),
        (cloud_2, Sensor("NoiseSensor", "Ruido", ruido)),
        (cloud_2, Sensor("CO2Sensor", "CO2", co2)),
    ]

    try:
        while True:
            print("- Sensores ", "-" * 38)
            batch = []

            for cloud, sensor in readings:
                valor = sensor.get_data()
                batch.append((cloud, sensor, valor))
                print(
                    f"{cloud.node} | {sensor.name} - SENSOR_{sensor.node_number} | {sensor.data_type}: {valor}"
                )

            print("-" * 50)

            for cloud, sensor, valor in batch:
                cloud.send(sensor, valor)

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSaliendo...")
    finally:
        print("Programa detenido con éxito")


if __name__ == "__main__":
    main()
