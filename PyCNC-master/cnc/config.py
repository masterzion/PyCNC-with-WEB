import configparser

configFilePath = '/etc/pycnc.conf'


configParser = configparser.RawConfigParser()
configParser.read(configFilePath)


# -----------------------------------------------------------------------------
# Hardware config.

# Maximum velocity for each axis in millimeter per minute.
#funcionou com 1600 na diagonal y50z50
MAX_VELOCITY_MM_PER_MIN_X = 1500
MAX_VELOCITY_MM_PER_MIN_Y = 1500
MAX_VELOCITY_MM_PER_MIN_Z = 1500
MAX_VELOCITY_MM_PER_MIN_E = 1500
MIN_VELOCITY_MM_PER_MIN = 1
# Average velocity for endstop calibration procedure
CALIBRATION_VELOCITY_MM_PER_MIN = 300

# DM860A
# SW5 SW6 SW7 SW8   pulses/rev
# OFF OFF ON  ON    3200

# Fuso
# 5mm/rev


# Stepper motors steps per millimeter for each axis.
STEPPER_PULSES_PER_MM_X = 640
STEPPER_PULSES_PER_MM_Y = 640   #6400 #int(3200/5)*10 -> mm
STEPPER_PULSES_PER_MM_Z = 640   #int(3200/5)
STEPPER_PULSES_PER_MM_E = 640

# Invert axises direction, by default(False) high level means increase of
# position. For inverted(True) axis, high level means decrease of position.
STEPPER_INVERTED_X = True
STEPPER_INVERTED_Y = True
STEPPER_INVERTED_Z = True
STEPPER_INVERTED_E = True

# Invert zero end stops switches. By default(False) low level on input pin
# means that axis in zero position. For inverted(True) end stops, high level
# means zero position.
ENDSTOP_INVERTED_X = True
ENDSTOP_INVERTED_Y = False
ENDSTOP_INVERTED_Z = True  # Auto leveler

# Workplace physical size.
TABLE_SIZE_X_MM = 200
TABLE_SIZE_Y_MM = 300
TABLE_SIZE_Z_MM = 200

# Mixed settings.
STEPPER_PULSE_LENGTH_US = 55 #2  >55us
STEPPER_MAX_ACCELERATION_MM_PER_S2 = 2000 #3000  # for all axis, mm per sec^2
SPINDLE_MAX_RPM = 10000
EXTRUDER_MAX_TEMPERATURE = 250
BED_MAX_TEMPERATURE = 100
MIN_TEMPERATURE = 40
EXTRUDER_PID = {"P": 0.059161177519,
                "I": 0.00206217171374,
                "D": 0.206217171374}
BED_PID = {"P": 0.226740848076,
           "I": 0.00323956215053,
           "D": 0.323956215053}

# -----------------------------------------------------------------------------
# Pins configuration.

# Enable pin for all steppers, low level is enabled.
STEPPERS_ENABLE_PIN = configParser.getint('CONTROL', 'STEPPERS_ENABLE_PIN')

STEPPER_STEP_PIN_X  = configParser.getint('AXIS', 'STEPPER_STEP_PIN_X')
STEPPER_DIR_PIN_X   = configParser.getint('AXIS', 'STEPPER_DIR_PIN_X')
ENDSTOP_PIN_X       = configParser.getint('AXIS', 'ENDSTOP_PIN_X')

STEPPER_STEP_PIN_Y  = configParser.getint('AXIS', 'STEPPER_STEP_PIN_Y')
STEPPER_DIR_PIN_Y   = configParser.getint('AXIS', 'STEPPER_DIR_PIN_Y')
ENDSTOP_PIN_Y       = configParser.getint('AXIS', 'ENDSTOP_PIN_Y')

STEPPER_STEP_PIN_Z  = configParser.getint('AXIS', 'STEPPER_STEP_PIN_Z')
STEPPER_DIR_PIN_Z   = configParser.getint('AXIS', 'STEPPER_DIR_PIN_Z')
ENDSTOP_PIN_Z       = configParser.getint('AXIS', 'ENDSTOP_PIN_Z')

STEPPER_STEP_PIN_E  = configParser.getint('AXIS', 'STEPPER_STEP_PIN_E')
STEPPER_DIR_PIN_E   = configParser.getint('AXIS', 'STEPPER_DIR_PIN_E')

SPINDLE_PWM_PIN     = configParser.getint('CONTROL', 'SPINDLE_PWM_PIN')
FAN_PIN             = configParser.getint('CONTROL', 'FAN_PIN')
EXTRUDER_HEATER_PIN = configParser.getint('CONTROL', 'EXTRUDER_HEATER_PIN')
BED_HEATER_PIN      = configParser.getint('CONTROL', 'BED_HEATER_PIN')

EXTRUDER_TEMPERATURE_SENSOR_CHANNEL = configParser.getint('CONTROL', 'EXTRUDER_TEMPERATURE_SENSOR_CHANNEL')
BED_TEMPERATURE_SENSOR_CHANNEL = configParser.getint('CONTROL', 'BED_TEMPERATURE_SENSOR_CHANNEL')


# -----------------------------------------------------------------------------
#  Behavior config

# Run command immediately after receiving and stream new pulses, otherwise
# buffer will be prepared firstly and then command will run.
# Before enabling this feature, please make sure that board performance is
# enough for streaming pulses(faster then real time).
INSTANT_RUN = True

# If this parameter is False, error will be raised on command with velocity
# more than maximum velocity specified here. If this parameter is True,
# velocity would be decreased(proportional for all axises) to fit the maximum
# velocity.
AUTO_VELOCITY_ADJUSTMENT = True

# Automatically turn on fan when extruder is heating, boolean value.
AUTO_FAN_ON = True
