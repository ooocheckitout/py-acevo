# py-acevo

## Install

```bash
pip install py-acevo
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
