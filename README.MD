# py-assettocorsa-evo

The Python library to read shared memory of Assetto Corsa Evo.

## Install

```bash
pip install py-assettocorsa-evo
```

## Example

```python
from acevo import ACEvoSharedMemory

try:
    with ACEvoSharedMemory() as memory:
        static, physics, graphics = memory.read_snapshot()
        print(static.session_name, static.track)
        print(physics.speed_kmh, physics.gas, physics.brake)
        print(graphics.current_lap_time_ms, graphics.car_coordinates)
except FileNotFoundError as error:
    print("The AC Evo shared memory is unavailable. Start a driving session.")
```

## Available Models

| Model | Description |
| --- | --- |
| [Static](https://github.com/ooocheckitout/py-assettocorsa-evo/blob/main/acevo/models/static.py) | Session, track, and game information. |
| [Physics](https://github.com/ooocheckitout/py-assettocorsa-evo/blob/main/acevo/models/physics.py) | Speed, controls, engine, and wheel telemetry. |
| [Graphics](https://github.com/ooocheckitout/py-assettocorsa-evo/blob/main/acevo/models/graphics.py) | Timing, positions, tyres, damage, and pit information. |
| [Enums](https://github.com/ooocheckitout/py-assettocorsa-evo/blob/main/acevo/models/enums.py) | Named status, session, and flag values. |
