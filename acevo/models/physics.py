from ctypes import (
    LittleEndianStructure,
    sizeof,
    c_float,
    c_int32,
)
from collections.abc import Sequence


FloatArray = Sequence[float]
FloatMatrix = Sequence[FloatArray]


class PhysicsPage(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4

    packet_id: int
    gas: float
    brake: float
    fuel: float
    gear: int
    rpms: int
    steer_angle: float
    speed_kmh: float
    velocity: FloatArray
    acc_g: FloatArray
    wheel_slip: FloatArray
    wheel_load: FloatArray
    wheel_pressure: FloatArray
    wheel_angular_speed: FloatArray
    tyre_wear: FloatArray
    tyre_dirt_level: FloatArray
    tyre_core_temperature: FloatArray
    camber_rad: FloatArray
    suspension_travel: FloatArray
    drs: float
    tc: float
    heading: float
    pitch: float
    roll: float
    cg_height: float
    car_damage: FloatArray
    number_of_tyres_out: int
    pit_limiter_on: int
    abs: float
    kers_charge: float
    kers_input: float
    auto_shifter_on: int
    ride_height: FloatArray
    turbo_boost: float
    ballast: float
    air_density: float
    air_temp: float
    road_temp: float
    local_angular_vel: FloatArray
    final_ff: float
    performance_meter: float
    engine_brake: int
    ers_recovery_level: int
    ers_power_level: int
    ers_heat_charging: int
    ers_is_charging: int
    kers_current_kj: float
    drs_available: int
    drs_enabled: int
    brake_temp: FloatArray
    clutch: float
    tyre_temp_i: FloatArray
    tyre_temp_m: FloatArray
    tyre_temp_o: FloatArray
    is_ai_controlled: int
    tyre_contact_point: FloatMatrix
    tyre_contact_normal: FloatMatrix
    tyre_contact_heading: FloatMatrix
    brake_bias: float
    local_velocity: FloatArray
    p2p_activations: int
    p2p_status: int
    current_max_rpm: int
    mz: FloatArray
    fx: FloatArray
    fy: FloatArray
    slip_ratio: FloatArray
    slip_angle: FloatArray
    tc_in_action: int
    abs_in_action: int
    suspension_damage: FloatArray
    tyre_temp: FloatArray
    water_temp: float
    brake_torque: FloatArray
    front_brake_compound: int
    rear_brake_compound: int
    pad_life: FloatArray
    disc_life: FloatArray
    ignition_on: int
    starter_engine_on: int
    is_engine_running: int
    kerb_vibration: float
    slip_vibrations: float
    road_vibrations: float
    abs_vibrations: float

    _fields_ = [
        ("packet_id", c_int32),
        ("gas", c_float),
        ("brake", c_float),
        ("fuel", c_float),
        ("gear", c_int32),
        ("rpms", c_int32),
        ("steer_angle", c_float),
        ("speed_kmh", c_float),
        ("velocity", (c_float * 3)),
        ("acc_g", (c_float * 3)),
        ("wheel_slip", (c_float * 4)),
        ("wheel_load", (c_float * 4)),
        ("wheel_pressure", (c_float * 4)),
        ("wheel_angular_speed", (c_float * 4)),
        ("tyre_wear", (c_float * 4)),
        ("tyre_dirt_level", (c_float * 4)),
        ("tyre_core_temperature", (c_float * 4)),
        ("camber_rad", (c_float * 4)),
        ("suspension_travel", (c_float * 4)),
        ("drs", c_float),
        ("tc", c_float),
        ("heading", c_float),
        ("pitch", c_float),
        ("roll", c_float),
        ("cg_height", c_float),
        ("car_damage", (c_float * 5)),
        ("number_of_tyres_out", c_int32),
        ("pit_limiter_on", c_int32),
        ("abs", c_float),
        ("kers_charge", c_float),
        ("kers_input", c_float),
        ("auto_shifter_on", c_int32),
        ("ride_height", (c_float * 2)),
        ("turbo_boost", c_float),
        ("ballast", c_float),
        ("air_density", c_float),
        ("air_temp", c_float),
        ("road_temp", c_float),
        ("local_angular_vel", (c_float * 3)),
        ("final_ff", c_float),
        ("performance_meter", c_float),
        ("engine_brake", c_int32),
        ("ers_recovery_level", c_int32),
        ("ers_power_level", c_int32),
        ("ers_heat_charging", c_int32),
        ("ers_is_charging", c_int32),
        ("kers_current_kj", c_float),
        ("drs_available", c_int32),
        ("drs_enabled", c_int32),
        ("brake_temp", (c_float * 4)),
        ("clutch", c_float),
        ("tyre_temp_i", (c_float * 4)),
        ("tyre_temp_m", (c_float * 4)),
        ("tyre_temp_o", (c_float * 4)),
        ("is_ai_controlled", c_int32),
        ("tyre_contact_point", ((c_float * 3) * 4)),
        ("tyre_contact_normal", ((c_float * 3) * 4)),
        ("tyre_contact_heading", ((c_float * 3) * 4)),
        ("brake_bias", c_float),
        ("local_velocity", (c_float * 3)),
        ("p2p_activations", c_int32),
        ("p2p_status", c_int32),
        ("current_max_rpm", c_int32),
        ("mz", (c_float * 4)),
        ("fx", (c_float * 4)),
        ("fy", (c_float * 4)),
        ("slip_ratio", (c_float * 4)),
        ("slip_angle", (c_float * 4)),
        ("tc_in_action", c_int32),
        ("abs_in_action", c_int32),
        ("suspension_damage", (c_float * 4)),
        ("tyre_temp", (c_float * 4)),
        ("water_temp", c_float),
        ("brake_torque", (c_float * 4)),
        ("front_brake_compound", c_int32),
        ("rear_brake_compound", c_int32),
        ("pad_life", (c_float * 4)),
        ("disc_life", (c_float * 4)),
        ("ignition_on", c_int32),
        ("starter_engine_on", c_int32),
        ("is_engine_running", c_int32),
        ("kerb_vibration", c_float),
        ("slip_vibrations", c_float),
        ("road_vibrations", c_float),
        ("abs_vibrations", c_float),
    ]


assert sizeof(PhysicsPage) == 800, "PhysicsPage differs from the EVO ABI"
