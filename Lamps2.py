from math import ceil
def lamps(hour_day, elec_price):
    num_bulb = 1
    price_bulb = 0.0006 * elec_price * 1000 + 5
    price_lamp = 0.00011 * elec_price * 1000 + 60
    while price_bulb < price_lamp:
        num_bulb += 1
        price_bulb = (0.0006 * elec_price * 1000 + 5) * num_bulb
        price_lamp = 0.00011 * elec_price * 1000 * num_bulb + 60

    price_diff = 60 - 5 * num_bulb
    hours = ceil(price_diff / (0.00049 * elec_price)) + 1
    day = ceil(hours/hour_day)
    
    
    day2 = ceil((num_bulb - 1) * 1000 / hour_day) + 1
    price_bulb = 0.0006 * elec_price * day2 * hour_day + 5 * num_bulb
    price_lamp = 0.00011 * elec_price * day2 * hour_day + 60
    while price_bulb < price_lamp:
        day2 += 1
        price_bulb += 0.0006 * elec_price * hour_day
        price_lamp += 0.00011 * elec_price * hour_day
    if day != day2 and num_bulb <= 8:
        print(f'hour_day:{hour_day}, elec_price:{elec_price}')

if __name__ == '__main__':
    for i in range (1, 25):
        for j in range (1, 201):
            lamps(i, j)
