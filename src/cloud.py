import json
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

from models import Valor
from sensor import Sensor


class MQTTClient:
    def __init__(
        self,
        node: str,
        broker: str,
        port: int,
        topic_prefix: str,
    ) -> None:
        self.client = mqtt.Client()
        self.client.connect(broker, port)
        self.topic_prefix = topic_prefix
        self.node = node

    def send(self, sensor: Sensor, valor: Valor) -> None:
        payload = {
            "sensor": sensor.name.lower(),
            "type": sensor.data_type,
            "value": valor.value,
            "unit": valor.unit,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        topic = f"{self.topic_prefix}/{self.node}/{sensor.name.lower()}"
        self.client.publish(topic, json.dumps(payload, ensure_ascii=False))
