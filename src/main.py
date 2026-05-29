import logging
import os
from dotenv import load_dotenv
from builder import build_readings
from core import run_loop
from loader import load_yaml

load_dotenv()


def main() -> None:
    nodes = load_yaml("nodes.yml")["nodes"]
    config = load_yaml("config.yml")

    log_config = config.get("logging", {})
    logging.basicConfig(
        level=getattr(logging, log_config.get("level", "INFO")),
        format=log_config.get("format", "%(asctime)s | %(levelname)-5s | %(message)s"),
        datefmt=log_config.get("datefmt"),
    )

    readings = build_readings(
        nodes,
        broker=os.environ["MQTT_BROKER"],
        port=int(os.environ["MQTT_PORT"]),
        topic_prefix=os.environ["MQTT_TOPIC_PREFIX"],
    )

    run_loop(readings, interval=config.get("interval", 1.0))


if __name__ == "__main__":
    main()
