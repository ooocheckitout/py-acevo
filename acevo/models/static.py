from ctypes import (
    LittleEndianStructure,
    sizeof,
    c_bool,
    c_char,
    c_float,
    c_int32,
    c_uint8,
)


class StaticPage(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4

    sm_version: bytes
    ac_evo_version: bytes
    session: int
    session_name: bytes
    event_id: int
    session_id: int
    starting_grip: int
    starting_ambient_temperature_c: float
    starting_ground_temperature_c: float
    is_static_weather: bool
    is_timed_race: bool
    is_online: bool
    number_of_sessions: int
    nation: bytes
    longitude: float
    latitude: float
    track: bytes
    track_configuration: bytes
    track_length_m: float

    _fields_ = [
        ("sm_version", (c_char * 15)),
        ("ac_evo_version", (c_char * 15)),
        ("session", c_int32),
        ("session_name", (c_char * 33)),
        ("event_id", c_uint8),
        ("session_id", c_uint8),
        ("starting_grip", c_int32),
        ("starting_ambient_temperature_c", c_float),
        ("starting_ground_temperature_c", c_float),
        ("is_static_weather", c_bool),
        ("is_timed_race", c_bool),
        ("is_online", c_bool),
        ("number_of_sessions", c_int32),
        ("nation", (c_char * 33)),
        ("longitude", c_float),
        ("latitude", c_float),
        ("track", (c_char * 33)),
        ("track_configuration", (c_char * 33)),
        ("track_length_m", c_float),
    ]


assert sizeof(StaticPage) == 208, "StaticPage differs from the EVO ABI"
