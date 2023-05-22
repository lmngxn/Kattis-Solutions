from math import ceil
def lamps(hour_day, elec_price):
    num_bulb = 1
    price_bulb = 0.0006 * elec_price * 1000 + 5
    price_lamp = 0.00011 * elec_price * 1000 + 60
    while price_bulb < price_lamp:
        num_bulb += 1
        price_bulb = (0.0006 * elec_price * 1000 + 5) * num_bulb
        price_lamp = 0.00011 * elec_price * 1000 * num_bulb + 60

    base_hours = (num_bulb - 1) * 1000
    price_diff = 60 - (5 * num_bulb) - (base_hours * 0.00049 * elec_price)
    if price_diff < 0:
        day = ceil((base_hours + 1) / hour_day)
        print(day)
    else:
        hours = ceil(price_diff / 0.00049 / elec_price) + base_hours
        day = ceil(hours/hour_day)
        print(day)
    
    day2 = ceil((num_bulb - 1) * 1000 / hour_day) + 1
    price_bulb = 0.0006 * elec_price * day2 * hour_day + 5 * num_bulb
    price_lamp = 0.00011 * elec_price * day2 * hour_day + 60
    while price_bulb < price_lamp:
        day2 += 1
        price_bulb += 0.0006 * elec_price * hour_day
        price_lamp += 0.00011 * elec_price * hour_day
    print(day2)
"""
day = ceil((num_bulb - 1) * 1000 / hour_day) + 1
price_bulb = 0.0006 * elec_price * day * hour_day + 5 * num_bulb
price_lamp = 0.00011 * elec_price * day * hour_day + 60
while price_bulb < price_lamp:
    day += 1
    price_bulb += 0.0006 * elec_price * hour_day
    price_lamp += 0.00011 * elec_price * hour_day
print(day)
"""
