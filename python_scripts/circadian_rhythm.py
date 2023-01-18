now = datetime.datetime.now()
current_time = now.time()
morning_start = datetime.time(5, 30)
day_start = datetime.time(8, 0)
evening_start = datetime.time(19, 0)
later_evening_start = datetime.time(20, 30)
night_start = datetime.time(22, 0)

# A setting is a tuple of (morning, day, evening, later_evening, night)
all_settings = {
    "light_auto_awake_kelvin_hallway": (6500, 5000, 3800, 3200, 2700),
    "light_auto_awake_brightness_hallway": (150, 255, 200, 160, 90),
    "light_auto_away_kelvin_hallway": (6500, 5000, 3800, 3200, 2700),
    "light_auto_away_brightness_hallway": (150, 255, 200, 160, 90),
    "light_auto_awake_kelvin_kitchen": (6500, 5000, 3800, 3200, 2700),
    "light_auto_awake_brightness_kitchen": (255, 255, 200, 160, 90),
    "light_auto_awake_kelvin_toilet": (6500, 5000, 3800, 3200, 2700),
    "light_auto_awake_brightness_toilet": (255, 255, 200, 160, 80),
    "light_auto_awake_kelvin_living_room": (6500, 5000, 3800, 3200, 2700),
    "light_auto_awake_brightness_living_room": (150, 255, 200, 160, 90),
    "light_auto_awake_kelvin_lr_indirect": (6500, 5000, 3800, 3200, 2700),
    "light_auto_awake_brightness_lr_indirect": (150, 255, 200, 160, 90),
    "light_auto_awake_kelvin_bedroom": (6500, 5000, 3800, 3200, 2700),
    "light_auto_awake_brightness_bedroom": (255, 255, 200, 160, 90),
}

current_position = 4  # Night (default)
if (current_time >= morning_start and current_time < day_start):
    current_position = 0  # Morning
elif (current_time >= day_start and current_time < evening_start):
    current_position = 1  # Day
elif (current_time >= evening_start and current_time < later_evening_start):
    current_position = 2  # Evening
elif (current_time >= later_evening_start and current_time < night_start):
    current_position = 3  # Later evening

# {'entity_id': 'input_number.hallway_light_default_kelvin', 'value': 6500}

for name, element in all_settings.items():
    value = element[current_position]
    payload = {
        "entity_id": f"input_number.{name}",
        "value": value,
    }
    hass.services.call('input_number', 'set_value', payload, False)
