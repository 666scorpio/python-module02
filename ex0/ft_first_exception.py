def check_temperature(temp_str):
    try:
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            return temp
        else:
            return None
    except:
            return None
