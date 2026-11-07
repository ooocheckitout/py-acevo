from ctypes import (
    LittleEndianStructure,
    sizeof,
    c_bool,
    c_char,
    c_float,
    c_int16,
    c_int32,
    c_int8,
    c_uint16,
    c_uint32,
    c_uint64,
    c_uint8,
)
from collections.abc import Sequence


FloatArray = Sequence[float]
FloatMatrix = Sequence[FloatArray]


class TyreState(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4
    slip: float
    lock: bool
    tyre_pressure: float
    tyre_temperature_c: float
    brake_temperature_c: float
    brake_pressure: float
    tyre_temperature_left: float
    tyre_temperature_center: float
    tyre_temperature_right: float
    tyre_compound_front: bytes
    tyre_compound_rear: bytes
    tyre_normalized_pressure: float
    tyre_normalized_temperature_left: float
    tyre_normalized_temperature_center: float
    tyre_normalized_temperature_right: float
    brake_normalized_temperature: float
    tyre_normalized_temperature_core: float
    _fields_ = [
        ("slip", c_float),
        ("lock", c_bool),
        ("tyre_pressure", c_float),
        ("tyre_temperature_c", c_float),
        ("brake_temperature_c", c_float),
        ("brake_pressure", c_float),
        ("tyre_temperature_left", c_float),
        ("tyre_temperature_center", c_float),
        ("tyre_temperature_right", c_float),
        ("tyre_compound_front", (c_char * 33)),
        ("tyre_compound_rear", (c_char * 33)),
        ("tyre_normalized_pressure", c_float),
        ("tyre_normalized_temperature_left", c_float),
        ("tyre_normalized_temperature_center", c_float),
        ("tyre_normalized_temperature_right", c_float),
        ("brake_normalized_temperature", c_float),
        ("tyre_normalized_temperature_core", c_float),
        ("placeholder", (c_char * 128)),
    ]


class DamageState(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4
    damage_front: float
    damage_rear: float
    damage_left: float
    damage_right: float
    damage_center: float
    damage_suspension_lf: float
    damage_suspension_rf: float
    damage_suspension_lr: float
    damage_suspension_rr: float
    _fields_ = [
        ("damage_front", c_float),
        ("damage_rear", c_float),
        ("damage_left", c_float),
        ("damage_right", c_float),
        ("damage_center", c_float),
        ("damage_suspension_lf", c_float),
        ("damage_suspension_rf", c_float),
        ("damage_suspension_lr", c_float),
        ("damage_suspension_rr", c_float),
        ("placeholder", (c_char * 92)),
    ]


class PitInfo(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4
    damage: int
    fuel: int
    tyres_lf: int
    tyres_rf: int
    tyres_lr: int
    tyres_rr: int
    _fields_ = [
        ("damage", c_int8),
        ("fuel", c_int8),
        ("tyres_lf", c_int8),
        ("tyres_rf", c_int8),
        ("tyres_lr", c_int8),
        ("tyres_rr", c_int8),
        ("placeholder", (c_char * 58)),
    ]


class Electronics(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4
    tc_level: int
    tc_cut_level: int
    abs_level: int
    esc_level: int
    ebb_level: int
    brake_bias: float
    engine_map_level: int
    turbo_level: float
    ers_deployment_map: int
    ers_recharge_map: float
    is_ers_heat_charging_on: bool
    is_ers_overtake_mode_on: bool
    is_drs_open: bool
    diff_power_level: int
    diff_coast_level: int
    front_bump_damper_level: int
    front_rebound_damper_level: int
    rear_bump_damper_level: int
    rear_rebound_damper_level: int
    is_ignition_on: bool
    is_pit_limiter_on: bool
    active_performance_mode: int
    _fields_ = [
        ("tc_level", c_int8),
        ("tc_cut_level", c_int8),
        ("abs_level", c_int8),
        ("esc_level", c_int8),
        ("ebb_level", c_int8),
        ("brake_bias", c_float),
        ("engine_map_level", c_int8),
        ("turbo_level", c_float),
        ("ers_deployment_map", c_int8),
        ("ers_recharge_map", c_float),
        ("is_ers_heat_charging_on", c_bool),
        ("is_ers_overtake_mode_on", c_bool),
        ("is_drs_open", c_bool),
        ("diff_power_level", c_int8),
        ("diff_coast_level", c_int8),
        ("front_bump_damper_level", c_int8),
        ("front_rebound_damper_level", c_int8),
        ("rear_bump_damper_level", c_int8),
        ("rear_rebound_damper_level", c_int8),
        ("is_ignition_on", c_bool),
        ("is_pit_limiter_on", c_bool),
        ("active_performance_mode", c_int8),
        ("placeholder", (c_char * 88)),
    ]


class Instrumentation(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4
    main_light_stage: int
    special_light_stage: int
    cockpit_light_stage: int
    wiper_level: int
    rain_lights: bool
    direction_light_left: bool
    direction_light_right: bool
    flashing_lights: bool
    warning_lights: bool
    selected_display_index: int
    display_current_page_index: Sequence[int]
    are_headlights_visible: bool
    _fields_ = [
        ("main_light_stage", c_int8),
        ("special_light_stage", c_int8),
        ("cockpit_light_stage", c_int8),
        ("wiper_level", c_int8),
        ("rain_lights", c_bool),
        ("direction_light_left", c_bool),
        ("direction_light_right", c_bool),
        ("flashing_lights", c_bool),
        ("warning_lights", c_bool),
        ("selected_display_index", c_int8),
        ("display_current_page_index", (c_int8 * 16)),
        ("are_headlights_visible", c_bool),
        ("placeholder", (c_char * 101)),
    ]


class SessionState(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4
    phase_name: bytes
    time_left: bytes
    time_left_ms: int
    wait_time: bytes
    total_laps: int
    current_lap: int
    lights_on: int
    lights_mode: int
    lap_length_km: float
    end_session_flag: int
    time_to_next_session: bytes
    disconnected_from_server: bool
    restart_season_enabled: bool
    ui_enable_drive: bool
    ui_enable_setup: bool
    is_ready_to_next_blinking: bool
    show_waiting_for_players: bool
    _fields_ = [
        ("phase_name", (c_char * 33)),
        ("time_left", (c_char * 15)),
        ("time_left_ms", c_int32),
        ("wait_time", (c_char * 15)),
        ("total_laps", c_int32),
        ("current_lap", c_int32),
        ("lights_on", c_int32),
        ("lights_mode", c_int32),
        ("lap_length_km", c_float),
        ("end_session_flag", c_int32),
        ("time_to_next_session", (c_char * 15)),
        ("disconnected_from_server", c_bool),
        ("restart_season_enabled", c_bool),
        ("ui_enable_drive", c_bool),
        ("ui_enable_setup", c_bool),
        ("is_ready_to_next_blinking", c_bool),
        ("show_waiting_for_players", c_bool),
        ("placeholder", (c_char * 140)),
    ]


class TimingState(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4
    current_lap_time: bytes
    delta_current: bytes
    delta_current_p: int
    last_lap_time: bytes
    delta_last: bytes
    delta_last_p: int
    best_lap_time: bytes
    ideal_lap_time: bytes
    total_time: bytes
    is_invalid: bool
    _fields_ = [
        ("current_lap_time", (c_char * 15)),
        ("delta_current", (c_char * 15)),
        ("delta_current_p", c_int32),
        ("last_lap_time", (c_char * 15)),
        ("delta_last", (c_char * 15)),
        ("delta_last_p", c_int32),
        ("best_lap_time", (c_char * 15)),
        ("ideal_lap_time", (c_char * 15)),
        ("total_time", (c_char * 15)),
        ("is_invalid", c_bool),
        ("placeholder", (c_char * 137)),
    ]


class AssistsState(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4
    auto_gear: int
    auto_blip: int
    auto_clutch: int
    auto_clutch_on_start: int
    manual_ignition_e_start: int
    auto_pit_limiter: int
    standing_start_assist: int
    auto_steer: float
    arcade_stability_control: float
    _fields_ = [
        ("auto_gear", c_uint8),
        ("auto_blip", c_uint8),
        ("auto_clutch", c_uint8),
        ("auto_clutch_on_start", c_uint8),
        ("manual_ignition_e_start", c_uint8),
        ("auto_pit_limiter", c_uint8),
        ("standing_start_assist", c_uint8),
        ("auto_steer", c_float),
        ("arcade_stability_control", c_float),
        ("placeholder", (c_char * 48)),
    ]


class GraphicsPage(LittleEndianStructure):
    _layout_ = "ms"
    _pack_ = 4

    packet_id: int
    status: int
    focused_car_id_a: int
    focused_car_id_b: int
    player_car_id_a: int
    player_car_id_b: int
    rpm: int
    is_rpm_limiter_on: bool
    is_change_up_rpm: bool
    is_change_down_rpm: bool
    tc_active: bool
    abs_active: bool
    esc_active: bool
    launch_active: bool
    is_ignition_on: bool
    is_engine_running: bool
    kers_is_charging: bool
    is_wrong_way: bool
    is_drs_available: bool
    battery_is_charging: bool
    is_max_kj_per_lap_reached: bool
    is_max_charge_kj_per_lap_reached: bool
    display_speed_kmh: int
    display_speed_mph: int
    display_speed_ms: int
    pit_speeding_delta: float
    gear_int: int
    rpm_percent: float
    gas_percent: float
    brake_percent: float
    handbrake_percent: float
    clutch_percent: float
    steering_percent: float
    ffb_strength: float
    car_ffb_multiplier: float
    water_temperature_percent: float
    water_pressure_bar: float
    fuel_pressure_bar: float
    water_temperature_c: int
    air_temperature_c: int
    oil_temperature_c: float
    oil_pressure_bar: float
    exhaust_temperature_c: float
    g_forces_x: float
    g_forces_y: float
    g_forces_z: float
    turbo_boost: float
    turbo_boost_level: float
    turbo_boost_perc: float
    steer_degrees: int
    current_km: float
    total_km: int
    total_driving_time_s: int
    time_of_day_hours: int
    time_of_day_minutes: int
    time_of_day_seconds: int
    delta_time_ms: int
    current_lap_time_ms: int
    predicted_lap_time_ms: int
    fuel_liter_current_quantity: float
    fuel_liter_current_quantity_percent: float
    fuel_liter_per_km: float
    km_per_fuel_liter: float
    current_torque: float
    current_bhp: int
    tyre_lf: TyreState
    tyre_rf: TyreState
    tyre_lr: TyreState
    tyre_rr: TyreState
    npos: float
    kers_charge_perc: float
    kers_current_perc: float
    control_lock_time: float
    car_damage: DamageState
    car_location: int
    pit_info: PitInfo
    fuel_liter_used: float
    fuel_liter_per_lap: float
    laps_possible_with_fuel: float
    battery_temperature: float
    battery_voltage: float
    instantaneous_fuel_liter_per_km: float
    instantaneous_km_per_fuel_liter: float
    gear_rpm_window: float
    instrumentation: Instrumentation
    instrumentation_min_limit: Instrumentation
    instrumentation_max_limit: Instrumentation
    electronics: Electronics
    electronics_min_limit: Electronics
    electronics_max_limit: Electronics
    electronics_is_modifiable: Electronics
    total_lap_count: int
    current_pos: int
    total_drivers: int
    last_lap_time_ms: int
    best_lap_time_ms: int
    flag: int
    global_flag: int
    max_gears: int
    engine_type: int
    has_kers: bool
    is_last_lap: bool
    performance_mode_name: bytes
    diff_coast_raw_value: float
    diff_power_raw_value: float
    race_cut_gained_time_ms: int
    distance_to_deadline: int
    race_cut_current_delta: float
    session_state: SessionState
    timing_state: TimingState
    player_ping: int
    player_latency: int
    player_cpu_usage: int
    player_cpu_usage_avg: int
    player_qos: int
    player_qos_avg: int
    player_fps: int
    player_fps_avg: int
    driver_name: bytes
    driver_surname: bytes
    car_model: bytes
    is_in_pit_box: bool
    is_in_pit_lane: bool
    is_valid_lap: bool
    car_coordinates: FloatMatrix
    gap_ahead: float
    gap_behind: float
    active_cars: int
    fuel_per_lap: float
    fuel_estimated_laps: float
    assists_state: AssistsState
    max_fuel: float
    max_turbo_boost: float
    use_single_compound: bool
    car_ids: Sequence[Sequence[int]]

    _fields_ = [
        ("packet_id", c_int32),
        ("status", c_int32),
        ("focused_car_id_a", c_uint64),
        ("focused_car_id_b", c_uint64),
        ("player_car_id_a", c_uint64),
        ("player_car_id_b", c_uint64),
        ("rpm", c_uint16),
        ("is_rpm_limiter_on", c_bool),
        ("is_change_up_rpm", c_bool),
        ("is_change_down_rpm", c_bool),
        ("tc_active", c_bool),
        ("abs_active", c_bool),
        ("esc_active", c_bool),
        ("launch_active", c_bool),
        ("is_ignition_on", c_bool),
        ("is_engine_running", c_bool),
        ("kers_is_charging", c_bool),
        ("is_wrong_way", c_bool),
        ("is_drs_available", c_bool),
        ("battery_is_charging", c_bool),
        ("is_max_kj_per_lap_reached", c_bool),
        ("is_max_charge_kj_per_lap_reached", c_bool),
        ("display_speed_kmh", c_int16),
        ("display_speed_mph", c_int16),
        ("display_speed_ms", c_int16),
        ("pit_speeding_delta", c_float),
        ("gear_int", c_int16),
        ("rpm_percent", c_float),
        ("gas_percent", c_float),
        ("brake_percent", c_float),
        ("handbrake_percent", c_float),
        ("clutch_percent", c_float),
        ("steering_percent", c_float),
        ("ffb_strength", c_float),
        ("car_ffb_multiplier", c_float),
        ("water_temperature_percent", c_float),
        ("water_pressure_bar", c_float),
        ("fuel_pressure_bar", c_float),
        ("water_temperature_c", c_int8),
        ("air_temperature_c", c_int8),
        ("oil_temperature_c", c_float),
        ("oil_pressure_bar", c_float),
        ("exhaust_temperature_c", c_float),
        ("g_forces_x", c_float),
        ("g_forces_y", c_float),
        ("g_forces_z", c_float),
        ("turbo_boost", c_float),
        ("turbo_boost_level", c_float),
        ("turbo_boost_perc", c_float),
        ("steer_degrees", c_int32),
        ("current_km", c_float),
        ("total_km", c_uint32),
        ("total_driving_time_s", c_uint32),
        ("time_of_day_hours", c_int32),
        ("time_of_day_minutes", c_int32),
        ("time_of_day_seconds", c_int32),
        ("delta_time_ms", c_int32),
        ("current_lap_time_ms", c_int32),
        ("predicted_lap_time_ms", c_int32),
        ("fuel_liter_current_quantity", c_float),
        ("fuel_liter_current_quantity_percent", c_float),
        ("fuel_liter_per_km", c_float),
        ("km_per_fuel_liter", c_float),
        ("current_torque", c_float),
        ("current_bhp", c_int32),
        ("tyre_lf", TyreState),
        ("tyre_rf", TyreState),
        ("tyre_lr", TyreState),
        ("tyre_rr", TyreState),
        ("npos", c_float),
        ("kers_charge_perc", c_float),
        ("kers_current_perc", c_float),
        ("control_lock_time", c_float),
        ("car_damage", DamageState),
        ("car_location", c_int32),
        ("pit_info", PitInfo),
        ("fuel_liter_used", c_float),
        ("fuel_liter_per_lap", c_float),
        ("laps_possible_with_fuel", c_float),
        ("battery_temperature", c_float),
        ("battery_voltage", c_float),
        ("instantaneous_fuel_liter_per_km", c_float),
        ("instantaneous_km_per_fuel_liter", c_float),
        ("gear_rpm_window", c_float),
        ("instrumentation", Instrumentation),
        ("instrumentation_min_limit", Instrumentation),
        ("instrumentation_max_limit", Instrumentation),
        ("electronics", Electronics),
        ("electronics_min_limit", Electronics),
        ("electronics_max_limit", Electronics),
        ("electronics_is_modifiable", Electronics),
        ("total_lap_count", c_int32),
        ("current_pos", c_uint32),
        ("total_drivers", c_uint32),
        ("last_lap_time_ms", c_int32),
        ("best_lap_time_ms", c_int32),
        ("flag", c_int32),
        ("global_flag", c_int32),
        ("max_gears", c_uint32),
        ("engine_type", c_int32),
        ("has_kers", c_bool),
        ("is_last_lap", c_bool),
        ("performance_mode_name", (c_char * 33)),
        ("diff_coast_raw_value", c_float),
        ("diff_power_raw_value", c_float),
        ("race_cut_gained_time_ms", c_int32),
        ("distance_to_deadline", c_int32),
        ("race_cut_current_delta", c_float),
        ("session_state", SessionState),
        ("timing_state", TimingState),
        ("player_ping", c_int32),
        ("player_latency", c_int32),
        ("player_cpu_usage", c_int32),
        ("player_cpu_usage_avg", c_int32),
        ("player_qos", c_int32),
        ("player_qos_avg", c_int32),
        ("player_fps", c_int32),
        ("player_fps_avg", c_int32),
        ("driver_name", (c_char * 33)),
        ("driver_surname", (c_char * 33)),
        ("car_model", (c_char * 33)),
        ("is_in_pit_box", c_bool),
        ("is_in_pit_lane", c_bool),
        ("is_valid_lap", c_bool),
        ("car_coordinates", ((c_float * 3) * 60)),
        ("gap_ahead", c_float),
        ("gap_behind", c_float),
        ("active_cars", c_uint8),
        ("fuel_per_lap", c_float),
        ("fuel_estimated_laps", c_float),
        ("assists_state", AssistsState),
        ("max_fuel", c_float),
        ("max_turbo_boost", c_float),
        ("use_single_compound", c_bool),
        ("car_ids", ((c_uint64 * 2) * 60)),
    ]


assert sizeof(TyreState) == 256, "TyreState differs from the EVO ABI"
assert sizeof(DamageState) == 128, "DamageState differs from the EVO ABI"
assert sizeof(PitInfo) == 64, "PitInfo differs from the EVO ABI"
assert sizeof(Electronics) == 128, "Electronics differs from the EVO ABI"
assert sizeof(Instrumentation) == 128, "Instrumentation differs from the EVO ABI"
assert sizeof(SessionState) == 256, "SessionState differs from the EVO ABI"
assert sizeof(TimingState) == 256, "TimingState differs from the EVO ABI"
assert sizeof(AssistsState) == 64, "AssistsState differs from the EVO ABI"
assert sizeof(GraphicsPage) == 4900, "GraphicsPage differs from the EVO ABI"
