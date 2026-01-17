# --- MASTER DATA DICTIONARY ---
# This contains all 38 categories from your original code
UNIT_DATA = {
    "Length": {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344},
    "Weight/Mass": {"mg": 0.001, "g": 1, "kg": 1000, "oz": 28.3495, "lb": 453.592, "ton": 1_000_000},
    "Time": {"ms": 0.001, "s": 1, "min": 60, "hr": 3600, "day": 86400, "week": 604800, "year": 31_536_000},
    "Volume": {"ml": 0.001, "l": 1, "m3": 1000, "tsp": 0.00492892, "tbsp": 0.0147868, "cup": 0.24, "pt": 0.473176, "qt": 0.946353, "gal": 3.78541},
    "Area": {"mm2": 0.000001, "cm2": 0.0001, "m2": 1, "km2": 1_000_000, "acre": 4046.86, "hectare": 10_000},
    "Speed": {"m/s": 1, "km/h": 0.277778, "mph": 0.44704, "ft/s": 0.3048, "knot": 0.514444},
    "Energy": {"j": 1, "kj": 1000, "cal": 4.184, "kcal": 4184, "wh": 3600, "kwh": 3_600_000},
    "Pressure": {"pa": 1, "kpa": 1000, "bar": 100000, "psi": 6894.76, "atm": 101325},
    "Power": {"w": 1, "kw": 1000, "mw": 1_000_000, "hp": 745.7},
    "Data Storage": {"b": 1, "kb": 1024, "mb": 1024**2, "gb": 1024**3, "tb": 1024**4},
    "Angle": {"rad": 1, "deg": 0.0174533, "grad": 0.0157079},
    "Frequency": {"hz": 1, "khz": 1000, "mhz": 1_000_000, "ghz": 1_000_000_000},
    "Force": {"n": 1, "kn": 1000, "dyn": 0.00001, "lbf": 4.44822, "kgf": 9.80665},
    "Acceleration": {"m/s2": 1, "cm/s2": 0.01, "g": 9.80665, "ft/s2": 0.3048},
    "Density": {"kg/m3": 1, "g/cm3": 1000, "lb/ft3": 16.0185, "g/ml": 1000, "oz/in3": 1729.99},
    "Electric Charge": {"c": 1, "mc": 0.001, "uc": 0.000001, "nc": 0.000000001, "ah": 3600, "mah": 3.6},
    "Resistance": {"ohm": 1, "kohm": 1000, "mohm": 1_000_000, "microohm": 0.000001},
    "Viscosity": {"pa.s": 1, "cp": 0.001, "p": 0.1, "cst": 0.000001, "st": 0.0001},
    "Torque": {"n.m": 1, "kn.m": 1000, "lb.ft": 1.35582, "lb.in": 0.112985, "dyn.cm": 0.00001, "kg.m": 9.80665},
    "Illuminance": {"lux": 1, "fc": 10.764, "lm/m2": 1, "phot": 10000, "cd.sr/m2": 1},
    "Magnetic Flux": {"t": 1, "mt": 0.001, "ut": 0.000001, "gauss": 0.0001},
    "Radioactivity": {"bq": 1, "kbq": 1000, "mbq": 1_000_000, "ci": 37_000_000_000, "mci": 37_000_000, "uci": 37000},
    "Luminous Intensity": {"cd": 1, "mcd": 0.001, "lm": 1, "flm": 0.0764555},
    "Voltage": {"v": 1, "mv": 0.001, "kv": 1000, "uv": 0.000001, "nv": 0.000000001},
    "Current": {"a": 1, "ma": 0.001, "ua": 0.000001, "na": 0.000000001, "ka": 1000},
    "Capacitance": {"f": 1, "mf": 0.001, "uf": 0.000001, "nf": 0.000000001, "pf": 0.000000000001},
    "Inductance": {"h": 1, "mh": 0.001, "uh": 0.000001, "nh": 0.000000001},
    "Conductivity": {"s": 1, "ms": 0.001, "us": 0.000001, "ns": 0.000000001, "mho": 1},
    "Flow Rate": {"l/s": 1, "ml/s": 0.001, "l/min": 0.0166667, "l/hr": 0.000277778, "m3/s": 1000, "gal/min": 0.0630902},
    "Molarity": {"mol/l": 1, "mmol/l": 0.001, "umol/l": 0.000001, "mol/ml": 1000, "mol/m3": 1},
    "Absorbance": {"au": 1, "percent": 0.01, "transmission": 1, "od": 1},
    "Concentration": {"ppm": 1, "ppb": 0.001, "ppt": 0.000001, "mg/l": 1},
    "Kinematic Viscosity": {"st": 1, "cst": 0.01, "m2/s": 10000, "cm2/s": 0.01},
    "Surface Tension": {"dyn/cm": 1, "n/m": 0.001, "erg/cm2": 1, "mj/m2": 0.001},
    "Thermal Conductivity": {"w/m.k": 1, "w/m.c": 1, "btu/h.ft.f": 1.73073, "cal/s.cm.c": 418.4},
    "Entropy": {"j/k": 1, "kj/k": 1000, "cal/k": 0.239006, "kcal/k": 239.006, "btu/k": 0.527751},
    "Molar Mass": {"g/mol": 1, "kg/mol": 1000, "mg/mol": 0.001, "lb/mol": 453.592},
    "Temperature": {"c": "special", "f": "special", "k": "special"}
}

def convert_units(value, from_unit, to_unit, category):
    """Refined conversion function to work with categorized data."""
    if category == "Temperature":
        if from_unit == "c": temp_c = value
        elif from_unit == "f": temp_c = (value - 32) * 5 / 9
        else: temp_c = value - 273.15
        
        if to_unit == "c": return temp_c
        elif to_unit == "f": return (temp_c * 9 / 5) + 32
        else: return temp_c + 273.15

    # General conversion using factors
    factors = UNIT_DATA[category]
    base_value = value * factors[from_unit]
    return base_value / factors[to_unit]

def format_number(number, decimal_places=6):
    """Format a number to be clean and readable."""
    if number == int(number):
        return str(int(number))
    return f"{number:.{decimal_places}f}".rstrip('0').rstrip('.')