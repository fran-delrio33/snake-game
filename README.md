# Snake Game

Implementación clásica del juego Snake en Python usando [Pygame](https://www.pygame.org/).

Proyecto de portfolio — Franco del Río, estudiante de Ingeniería en Sistemas (UTN).

## Estado del proyecto

En desarrollo, por etapas:

- [x] Etapa 1: Ventana del juego y loop principal
- [x] Etapa 2: Serpiente (dibujo y movimiento)
- [x] Etapa 3: Comida (aparición aleatoria y colisión)
- [x] Etapa 4: Crecimiento de la serpiente
- [x] Etapa 5: Detección de choque (game over)
- [x] Etapa 6: Puntaje en pantalla
- [x] Etapa 7: Pantalla de inicio y reinicio
- [x] Etapa 8: Mejoras opcionales (niveles, sonido, high score)
- [x] Etapa 9: Grilla de fondo
- [x] Etapa 10: Empaquetado como aplicación de escritorio (.exe)

## Requisitos

- Python 3.10+
- Pygame

## Instalación

```bash
git clone https://github.com/fran-delrio33/snake-game.git
cd snake-game
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Generar el ejecutable (.exe)

El juego se puede empaquetar como una aplicación de escritorio standalone con [PyInstaller](https://pyinstaller.org/), sin necesidad de tener Python instalado para correrlo:

```bash
pip install -r requirements-dev.txt
pyinstaller --onefile --windowed --name Snake --add-data "assets;assets" main.py
```

El ejecutable queda en `dist/Snake.exe`. El high score se guarda en un `highscore.txt` junto al `.exe`.
