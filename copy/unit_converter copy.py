def convert_units(value, from_unit, to_unit):
    # Dictionary to map all units to their categories for validation
    all_units = {}
    # ---------------- LENGTH (base: meter) ----------------
    length_factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344
    }

    # ---------------- WEIGHT / MASS (base: gram) ----------------
    weight_factors = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.3495,
        "lb": 453.592,
        "ton": 1_000_000
    }

    # ---------------- TIME (base: second) ----------------
    time_factors = {
        "ms": 0.001,
        "s": 1,
        "min": 60,
        "hr": 3600,
        "day": 86400,
        "week": 604800,
        "year": 31_536_000
    }

    # ---------------- VOLUME (base: liter) ----------------
    volume_factors = {
        "ml": 0.001,
        "l": 1,
        "m3": 1000,
        "tsp": 0.00492892,
        "tbsp": 0.0147868,
        "cup": 0.24,
        "pt": 0.473176,
        "qt": 0.946353,
        "gal": 3.78541
    }

    # ---------------- AREA (base: square meter) ----------------
    area_factors = {
        "mm2": 0.000001,
        "cm2": 0.0001,
        "m2": 1,
        "km2": 1_000_000,
        "acre": 4046.86,
        "hectare": 10_000
    }

    # ---------------- SPEED (base: m/s) ----------------
    speed_factors = {
        "m/s": 1,
        "km/h": 0.277778,
        "mph": 0.44704,
        "ft/s": 0.3048,
        "knot": 0.514444
    }

    # ---------------- ENERGY (base: joule) ----------------
    energy_factors = {
        "j": 1,
        "kj": 1000,
        "cal": 4.184,
        "kcal": 4184,
        "wh": 3600,
        "kwh": 3_600_000
    }

    # ---------------- PRESSURE (base: pascal) ----------------
    pressure_factors = {
        "pa": 1,
        "kpa": 1000,
        "bar": 100000,
        "psi": 6894.76,
        "atm": 101325
    }

    # ---------------- POWER (base: watt) ----------------
    power_factors = {
        "w": 1,
        "kw": 1000,
        "mw": 1_000_000,
        "hp": 745.7
    }

    # ---------------- DATA STORAGE (base: byte) ----------------
    data_factors = {
        "b": 1,
        "kb": 1024,
        "mb": 1024 ** 2,
        "gb": 1024 ** 3,
        "tb": 1024 ** 4
    }

    # ---------------- ANGLE (base: radian) ----------------
    angle_factors = {
        "rad": 1,
        "deg": 0.0174533,
        "grad": 0.0157079
    }

    # ---------------- FREQUENCY (base: hertz) ----------------
    frequency_factors = {
        "hz": 1,
        "khz": 1000,
        "mhz": 1_000_000,
        "ghz": 1_000_000_000
    }

    # ---------------- FORCE (base: newton) ----------------
    force_factors = {
        "n": 1,
        "kn": 1000,
        "dyn": 0.00001,
        "lbf": 4.44822,
        "kgf": 9.80665
    }

    # ---------------- ACCELERATION (base: m/s²) ----------------
    acceleration_factors = {
        "m/s2": 1,
        "cm/s2": 0.01,
        "g": 9.80665,
        "ft/s2": 0.3048
    }

    # ---------------- DENSITY (base: kg/m³) ----------------
    density_factors = {
        "kg/m3": 1,
        "g/cm3": 1000,
        "lb/ft3": 16.0185,
        "g/ml": 1000,
        "oz/in3": 1729.99
    }

    # ---------------- ELECTRIC CHARGE (base: coulomb) ----------------
    charge_factors = {
        "c": 1,
        "mc": 0.001,
        "uc": 0.000001,
        "nc": 0.000000001,
        "ah": 3600,
        "mah": 3.6
    }

    # ---------------- RESISTANCE (base: ohm) ----------------
    resistance_factors = {
        "ohm": 1,
        "kohm": 1000,
        "mohm": 1_000_000,
        "microohm": 0.000001,
        "megohm": 1_000_000
    }

    # ---------------- VISCOSITY (base: pascal-second) ----------------
    viscosity_factors = {
        "pa.s": 1,
        "cp": 0.001,
        "p": 0.1,
        "cst": 0.000001,
        "st": 0.0001
    }

    # ---------------- TORQUE (base: newton-meter) ----------------
    torque_factors = {
        "n.m": 1,
        "kn.m": 1000,
        "lb.ft": 1.35582,
        "lb.in": 0.112985,
        "dyn.cm": 0.00001,
        "kg.m": 9.80665
    }

    # ---------------- ILLUMINANCE (base: lux) ----------------
    illuminance_factors = {
        "lux": 1,
        "fc": 10.764,
        "lm/m2": 1,
        "phot": 10000,
        "cd.sr/m2": 1
    }

    # ---------------- MAGNETIC FLUX DENSITY (base: tesla) ----------------
    magnetic_factors = {
        "t": 1,
        "mt": 0.001,
        "ut": 0.000001,
        "gauss": 0.0001,
        "kg/(a.s2)": 1
    }

    # ---------------- RADIOACTIVITY (base: becquerel) ----------------
    radioactivity_factors = {
        "bq": 1,
        "kbq": 1000,
        "mbq": 1_000_000,
        "ci": 37_000_000_000,
        "mci": 37_000_000,
        "uci": 37000
    }

    # ---------------- LUMINOUS INTENSITY (base: candela) ----------------
    luminous_factors = {
        "cd": 1,
        "mcd": 0.001,
        "lm": 1,
        "flm": 0.0764555
    }

    # ---------------- ELECTRIC VOLTAGE (base: volt) ----------------
    voltage_factors = {
        "v": 1,
        "mv": 0.001,
        "kv": 1000,
        "uv": 0.000001,
        "nv": 0.000000001
    }

    # ---------------- ELECTRIC CURRENT (base: ampere) ----------------
    current_factors = {
        "a": 1,
        "ma": 0.001,
        "ua": 0.000001,
        "na": 0.000000001,
        "ka": 1000
    }

    # ---------------- CAPACITANCE (base: farad) ----------------
    capacitance_factors = {
        "f": 1,
        "mf": 0.001,
        "uf": 0.000001,
        "nf": 0.000000001,
        "pf": 0.000000000001
    }

    # ---------------- INDUCTANCE (base: henry) ----------------
    inductance_factors = {
        "h": 1,
        "mh": 0.001,
        "uh": 0.000001,
        "nh": 0.000000001
    }

    # ---------------- CONDUCTIVITY (base: siemens) ----------------
    conductivity_factors = {
        "s": 1,
        "ms": 0.001,
        "us": 0.000001,
        "ns": 0.000000001,
        "mho": 1
    }

    # ---------------- FLOW RATE (base: liter per second) ----------------
    flow_rate_factors = {
        "l/s": 1,
        "ml/s": 0.001,
        "l/min": 0.0166667,
        "l/hr": 0.000277778,
        "m3/s": 1000,
        "m3/min": 16.6667,
        "gal/s": 3.78541,
        "gal/min": 0.0630902
    }

    # ---------------- MOLARITY (base: mole per liter) ----------------
    molarity_factors = {
        "mol/l": 1,
        "mmol/l": 0.001,
        "umol/l": 0.000001,
        "mol/ml": 1000,
        "mol/m3": 1
    }

    # ---------------- ABSORBANCE (base: abs unit) ----------------
    absorbance_factors = {
        "au": 1,
        "percent": 0.01,
        "transmission": 1,
        "od": 1
    }

    # ---------------- CONCENTRATION (base: ppm) ----------------
    concentration_factors = {
        "ppm": 1,
        "ppb": 0.001,
        "ppt": 0.000001,
        "percent": 10000,
        "mg/l": 1
    }

    # ---------------- VISCOSITY KINEMATIC (base: stoke) ----------------
    kinematic_viscosity_factors = {
        "st": 1,
        "cst": 0.01,
        "m2/s": 10000,
        "cm2/s": 0.01
    }

    # ---------------- SURFACE TENSION (base: dyne per cm) ----------------
    surface_tension_factors = {
        "dyn/cm": 1,
        "n/m": 0.001,
        "erg/cm2": 1,
        "mj/m2": 0.001
    }

    # ---------------- THERMAL CONDUCTIVITY (base: watt per meter kelvin) ----------------
    thermal_conductivity_factors = {
        "w/m.k": 1,
        "w/m.c": 1,
        "btu/h.ft.f": 1.73073,
        "cal/s.cm.c": 418.4,
        "kcal/h.m.c": 1.163
    }

    # ---------------- ENTROPY (base: joule per kelvin) ----------------
    entropy_factors = {
        "j/k": 1,
        "kj/k": 1000,
        "cal/k": 0.239006,
        "kcal/k": 239.006,
        "btu/k": 0.527751
    }

    # ---------------- MOLAR MASS (base: gram per mole) ----------------
    molar_mass_factors = {
        "g/mol": 1,
        "kg/mol": 1000,
        "mg/mol": 0.001,
        "lb/mol": 453.592,
        "u": 1.66054e-24
    }

    # ---------------- TEMPERATURE (special handling) ----------------
    temperature_units = {"c", "f", "k"}

    if from_unit in temperature_units and to_unit in temperature_units:
        if from_unit == "c":
            temp_c = value
        elif from_unit == "f":
            temp_c = (value - 32) * 5 / 9
        else:  # kelvin
            temp_c = value - 273.15

        if to_unit == "c":
            return temp_c
        elif to_unit == "f":
            return (temp_c * 9 / 5) + 32
        else:
            return temp_c + 273.15

    # ---------------- GENERAL CONVERSION ----------------
    categories = [
        length_factors, weight_factors, time_factors, volume_factors,
        area_factors, speed_factors, energy_factors, pressure_factors,
        power_factors, data_factors, angle_factors, frequency_factors,
        force_factors, acceleration_factors, density_factors, charge_factors,
        resistance_factors, viscosity_factors, torque_factors, illuminance_factors,
        magnetic_factors, radioactivity_factors, luminous_factors, voltage_factors,
        current_factors, capacitance_factors, inductance_factors, conductivity_factors,
        flow_rate_factors, molarity_factors, absorbance_factors, concentration_factors,
        kinematic_viscosity_factors, surface_tension_factors, thermal_conductivity_factors,
        entropy_factors, molar_mass_factors
    ]

    for factors in categories:
        if from_unit in factors and to_unit in factors:
            base_value = value * factors[from_unit]
            return base_value / factors[to_unit]

    raise ValueError("Invalid or incompatible units.")


def get_conversion_rate(from_unit, to_unit):
    """Calculate the conversion rate (1 unit = ? other unit)"""
    try:
        rate = convert_units(1, from_unit, to_unit)
        return rate
    except:
        return None


def find_similar_units(invalid_unit, all_units_list):
    """Find units similar to the invalid one for suggestions"""
    suggestions = [u for u in all_units_list if invalid_unit.lower() in u.lower() or u.lower() in invalid_unit.lower()]
    return suggestions[:5]  # Return top 5 suggestions


def format_number(number, decimal_places=6):
    """Format a number with proper formatting"""
    if number == int(number):
        return str(int(number))
    return f"{number:.{decimal_places}f}".rstrip('0').rstrip('.')


def save_conversion_history(history, filename="conversion_history.txt"):
    """Save conversion history to a file"""
    try:
        with open(filename, 'a') as f:
            for entry in history:
                f.write(entry + "\n")
        return True
    except:
        return False


def get_all_supported_units():
    """Return a list of all supported units"""
    # This will be populated when convert_units is called
    pass



# ---------------- MAIN PROGRAM ----------------
def main():
    print("=" * 70)
    print("                  UNIVERSAL UNIT CONVERTER")
    print("=" * 70)
    print("✨ Chara Version | Supports 38 Categories | 300+ Units")
    print("=" * 70)
    print("\n📋 SUPPORTED CONVERSION CATEGORIES:")
    print("   • Length: mm, cm, m, km, in, ft, yd, mi")
    print("   • Weight/Mass: mg, g, kg, oz, lb, ton")
    print("   • Time: ms, s, min, hr, day, week, year")
    print("   • Volume: ml, l, m3, tsp, tbsp, cup, pt, qt, gal")
    print("   • Area: mm2, cm2, m2, km2, acre, hectare")
    print("   • Speed: m/s, km/h, mph, ft/s, knot")
    print("   • Energy: j, kj, cal, kcal, wh, kwh")
    print("   • Pressure: pa, kpa, bar, psi, atm")
    print("   • Power: w, kw, mw, hp")
    print("   • Data Storage: b, kb, mb, gb, tb")
    print("   • Angle: rad, deg, grad")
    print("   • Frequency: hz, khz, mhz, ghz")
    print("   • Force: n, kn, dyn, lbf, kgf")
    print("   • Acceleration: m/s2, cm/s2, g, ft/s2")
    print("   • Density: kg/m3, g/cm3, lb/ft3, g/ml, oz/in3")
    print("   • Electric Charge: c, mc, uc, nc, ah, mah")
    print("   • Resistance: ohm, kohm, mohm, microohm, megohm")
    print("   • Viscosity: pa.s, cp, p, cst, st")
    print("   • Torque: n.m, kn.m, lb.ft, lb.in, dyn.cm, kg.m")
    print("   • Illuminance: lux, fc, lm/m2, phot, cd.sr/m2")
    print("   • Magnetic Flux: t, mt, ut, gauss, kg/(a.s2)")
    print("   • Radioactivity: bq, kbq, mbq, ci, mci, uci")
    print("   • Luminous Intensity: cd, mcd, lm, flm")
    print("   • Electric Voltage: v, mv, kv, uv, nv")
    print("   • Electric Current: a, ma, ua, na, ka")
    print("   • Capacitance: f, mf, uf, nf, pf")
    print("   • Inductance: h, mh, uh, nh")
    print("   • Conductivity: s, ms, us, ns, mho")
    print("   • Flow Rate: l/s, ml/s, l/min, l/hr, m3/s, m3/min, gal/s, gal/min")
    print("   • Molarity: mol/l, mmol/l, umol/l, mol/ml, mol/m3")
    print("   • Absorbance: au, percent, transmission, od")
    print("   • Concentration: ppm, ppb, ppt, percent, mg/l")
    print("   • Kinematic Viscosity: st, cst, m2/s, cm2/s")
    print("   • Surface Tension: dyn/cm, n/m, erg/cm2, mj/m2")
    print("   • Thermal Conductivity: w/m.k, w/m.c, btu/h.ft.f, cal/s.cm.c, kcal/h.m.c")
    print("   • Entropy: j/k, kj/k, cal/k, kcal/k, btu/k")
    print("   • Molar Mass: g/mol, kg/mol, mg/mol, lb/mol, u")
    print("   • Temperature: c (Celsius), f (Fahrenheit), k (Kelvin)")
    print("\n" + "=" * 70)
    print("📝 QUICK COMMANDS:")
    print("   • Type 'help' - View common conversion examples")
    print("   • Type 'list' - Show supported units by category")
    print("   • Type 'history' - View conversion history (if enabled)")
    print("   • Type 'quit' or 'exit' - Close the program")
    print("=" * 70)
    
    conversion_history = []
    max_history = 10
    
    while True:
        try:
            print("\n")
            value_input = input("Enter the value to convert (or 'help'): ").strip()
            
            if value_input.lower() == "help":
                print("\n" + "─" * 70)
                print("UNIT CONVERSION GUIDE - Common Examples:")
                print("─" * 70)
                print("LENGTH: 1 mile = 1.609344 km | 1 foot = 0.3048 m")
                print("WEIGHT: 1 pound = 0.453592 kg | 1 ounce = 28.3495 g")
                print("TIME: 1 hour = 3600 seconds | 1 day = 86400 seconds")
                print("TEMPERATURE: 32°F = 0°C = 273.15 K | 100°C = 212°F")
                print("VOLUME: 1 gallon = 3.78541 liters | 1 cup = 0.24 liters")
                print("ENERGY: 1 kilowatt-hour = 3,600,000 joules")
                print("PRESSURE: 1 atmosphere = 101,325 pascals")
                print("─" * 70 + "\n")
                continue
            
            if value_input.lower() in ["quit", "exit", "q"]:
                print("\n" + "=" * 70)
                print("Thank you for using the Universal Unit Converter! 👋")
                if conversion_history:
                    save_option = input("Save conversion history? (yes/no): ").lower().strip()
                    if save_option in ["yes", "y"]:
                        if save_conversion_history(conversion_history):
                            print("✅ History saved to 'conversion_history.txt'")
                        else:
                            print("❌ Could not save history")
                print("=" * 70 + "\n")
                break
            
            if value_input.lower() == "history":
                if conversion_history:
                    print("\n" + "─" * 70)
                    print("📊 RECENT CONVERSIONS (Last 10):")
                    print("─" * 70)
                    for i, entry in enumerate(conversion_history, 1):
                        print(f"  {i}. {entry}")
                    print("─" * 70 + "\n")
                else:
                    print("❌ No conversion history yet.\n")
                continue
            
            value = float(value_input)
            
            if value == 0:
                print("⚠️  Warning: Converting zero value. Proceeding...\n")
            elif value < 0:
                print("⚠️  Warning: Negative value entered. Proceeding with conversion...\n")
            
            from_unit = input("Enter the unit to convert FROM (e.g., m, kg, s): ").lower().strip()
            to_unit = input("Enter the unit to convert TO (e.g., ft, lb, hr): ").lower().strip()
            
            if not from_unit or not to_unit:
                print("❌ Error: Units cannot be empty. Please try again.")
                continue
            
            if from_unit == to_unit:
                print(f"\n{'─' * 70}")
                print(f"⚠️  Notice: Converting from and to the same unit!")
                print(f"  {value} {from_unit} = {value} {to_unit}")
                print(f"{'─' * 70}\n")
                
                history_entry = f"{value} {from_unit} = {value} {to_unit}"
                conversion_history.append(history_entry)
                if len(conversion_history) > max_history:
                    conversion_history.pop(0)
            else:
                result = convert_units(value, from_unit, to_unit)
                conversion_rate = get_conversion_rate(from_unit, to_unit)
                formatted_result = format_number(result)
                
                print(f"\n{'─' * 70}")
                print(f"✅ CONVERSION RESULT:")
                print(f"  {value} {from_unit.upper()} = {formatted_result} {to_unit.upper()}")
                
                if conversion_rate:
                    rate_formatted = format_number(conversion_rate)
                    print(f"  📊 Conversion Rate: 1 {from_unit.upper()} = {rate_formatted} {to_unit.upper()}")
                
                print(f"{'─' * 70}\n")
                
                history_entry = f"{value} {from_unit} → {formatted_result} {to_unit}"
                conversion_history.append(history_entry)
                if len(conversion_history) > max_history:
                    conversion_history.pop(0)
            
            another = input("Do you want to convert another value? (yes/no): ").lower().strip()
            if another not in ["yes", "y"]:
                print("\n" + "=" * 70)
                print("Thank you for using the Universal Unit Converter! 👋")
                if conversion_history:
                    save_option = input("Save conversion history? (yes/no): ").lower().strip()
                    if save_option in ["yes", "y"]:
                        if save_conversion_history(conversion_history):
                            print("✅ History saved to 'conversion_history.txt'")
                        else:
                            print("❌ Could not save history")
                print("=" * 70 + "\n")
                break

        except ValueError as e:
            print(f"\n❌ Input Error: Invalid number entered.")
            print("   Please enter a valid numerical value.\n")
        except Exception as e:
            error_msg = str(e)
            print(f"\n❌ Conversion Error: {error_msg}")
            print("   Please check that both units are valid and compatible.\n")
            
            # Provide helpful suggestions
            if "Invalid or incompatible units" in error_msg:
                print("💡 Tip: Make sure you're converting compatible unit types (e.g., length to length)")

if __name__ == "__main__":
    main()