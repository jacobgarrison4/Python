DIG_VAL = { "0": 0, "1":1, "2":2, "3":3, "4":4,
"5":5, "6":6, "7":7, "8":8, "9":9 }

def phone(ph):
    result = 0
    for d in ph:
        if d in DIG_VAL:
            result = result * 10
            result += DIG_VAL[d]
    return result

