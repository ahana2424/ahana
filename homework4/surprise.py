# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def starname(x):
    for star in x:
        print(star)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def star_spectral_type(x):
    for star, type in x.items():
        print(star, type["Spectral Type"])
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def findstars(x):
    for star, type in x.items():
        if type["Magnitude"] > 0.1:
            print(star, type["Magnitude"])
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Procyon"] = {
    "RA": "07h 39m 18.1s",
    "Dec": "+05° 13′ 30″",
    "Magnitude": 0.34,
    "Spectral Type": "F5IV-V"
}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def find_bright_star(x):
    bright_star = None
    min_diff = float('inf')
    
    for star, type in x.items():
        dec_str = type["Dec"].replace("−", "-").replace("+", "")
        deg_part = dec_str.split("°")[0]
        deg_value = float(deg_part)
        
        diff = abs(deg_value - 20.0)
        
        if diff < min_diff:
            min_diff = diff
            bright_star = star
        elif diff == min_diff:
            if x[star]["Magnitude"] < x[bright_star]["Magnitude"]:
                bright_star = star

# 6) What is your favorite constellation?
print("My favorite constellation is the Big Dipper")
starname(targets)
star_spectral_type(targets)
findstars(targets)
find_bright_star(targets)