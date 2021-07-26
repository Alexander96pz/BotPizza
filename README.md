# Server Bot
Este sera el servidor encargado de receptar los commandos, mensajes y botones de Telegram a traves del Bot.

Ademas este sera la conexion con la API que contiene la ontología
[Repositorio de la API](https://github.com/Alexander96pz/OntoPizza.git)

Se tiene que disenar POST o GET en /rutas

## Requerimentos
* Python 3
* Pip
## Install
Descargar 
```
https://github.com/Alexander96pz/BotPizza.git
```
Antes de instalar , asegura de tener installado pip
```
pip install -r requirements.txt
```
### Nota: Es mejor contar con un entorno virtual a la hora in instalar python

## Bot de Telegram
Telegram nos ofrece una UI a traves de Telegram, llamada [@BotFather](https://telegram.me/BotFather)

Puedes ver la documentacion de creaccion del bot en la pagina oficial de Telegram Bot
* [Pagina Oficial de Telegram API](https://core.telegram.org/bots#6-botfather)

El token proporcionado debes color en api.key 

## Ejecucion
```
python main.py
```