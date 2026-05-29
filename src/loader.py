from pathlib import Path
import yaml


REQUIRED_NODE_FIELDS = {"name", "sensors"}
REQUIRED_SENSOR_FIELDS = {"alias", "type", "label"}


def load_yaml(path: str | Path) -> dict:
    with open(path) as file:
        data = yaml.safe_load(file)
    return data or {}


def validate_nodes(data: dict) -> None:
    if "nodes" not in data:
        raise ValueError("nodes.yml: falta la clave 'nodes'")

    nodes = data["nodes"]
    if not isinstance(nodes, list):
        raise ValueError("nodes.yml: 'nodes' debe ser una lista")

    for i, node in enumerate(nodes):
        missing = REQUIRED_NODE_FIELDS - node.keys()
        if missing:
            raise ValueError(
                f"nodes.yml: nodo[{i}] le falta: {', '.join(sorted(missing))}"
            )

        if not isinstance(node["name"], str) or not node["name"]:
            raise ValueError(f"nodes.yml: nodo[{i}]: 'name' debe ser un texto no vacío")

        sensors = node["sensors"]
        if not isinstance(sensors, list) or not sensors:
            raise ValueError(
                f"nodes.yml: nodo '{node['name']}': 'sensors' debe ser una lista con al menos un elemento"
            )

        for j, sensor in enumerate(sensors):
            missing = REQUIRED_SENSOR_FIELDS - sensor.keys()
            if missing:
                raise ValueError(
                    f"nodes.yml: nodo '{node['name']}' sensor[{j}]: "
                    f"le falta: {', '.join(sorted(missing))}"
                )

            for key in ("alias", "type", "label"):
                if not isinstance(sensor[key], str) or not sensor[key]:
                    raise ValueError(
                        f"nodes.yml: nodo '{node['name']}' sensor[{j}]: "
                        f"'{key}' debe ser un texto no vacío"
                    )
