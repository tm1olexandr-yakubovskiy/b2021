

class Patrons(Exception):
    def __str__(self):
        return f"We cann`t go to fight with their amount patrons"
def check_patrons(amount_patrons, minimal_value):
    if minimal_value>amount_patrons:
        return f'Patrons is not enough'
    else:
        raise Patrons(minimal_value)
patrons = 300
check_patrons(patrons, 100)