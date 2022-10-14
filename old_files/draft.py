rate = 1.68
value_day = 40 * rate
value_night = 40 * (rate / 2)
payment = value_day + value_night
print(type(payment))

rate = 1.68
value_day = 40
value_night = 40
payment = (value_day * rate) + (value_night * (rate/2))
print(type(payment))