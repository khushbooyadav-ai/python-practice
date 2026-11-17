def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def safe_year(year):
    if  year <= 0:
        raise ValueError("year must be positive")
    return year
    