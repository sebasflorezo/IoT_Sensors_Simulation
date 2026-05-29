from cloud import MQTTClient
from sensor import Sensor
from sensor_types import SENSOR_TYPES


def build_readings(
    nodes_config: list[dict],
    broker: str,
    port: int,
    topic_prefix: str,
) -> list[tuple[MQTTClient, Sensor]]:
    readings: list[tuple[MQTTClient, Sensor]] = []

    for node_cfg in nodes_config:
        cloud = MQTTClient(
            node=node_cfg["name"],
            broker=broker,
            port=port,
            topic_prefix=topic_prefix,
        )

        for sensor_cfg in node_cfg["sensors"]:
            sensor_type = SENSOR_TYPES[sensor_cfg["type"]]
            sensor = Sensor(sensor_cfg["alias"], sensor_type.label, sensor_type.fn)
            readings.append((cloud, sensor))

    return readings
