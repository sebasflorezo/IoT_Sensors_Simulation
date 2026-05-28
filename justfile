host := env_var_or_default("MQTT_BROKER", "localhost")

# Mostrar comandos disponibles
default:
    @just --list

# Ejecutar el programa IoT
run:
    uv run python3 -u src/main.py

# Leer todos los topics del broker
all:
    mosquitto_sub -h {{host}} -t "#" -v

# Leer todos los topics bajo casa/
casa:
    mosquitto_sub -h {{host}} -t "casa/#" -v

# Leer solo los topics de un nodo específico
node n:
    mosquitto_sub -h {{host}} -t "casa/{{n}}/#" -v

# Leer un sensor específico de cualquier nodo
sensor s:
    mosquitto_sub -h {{host}} -t "casa/+/{{s}}" -v
