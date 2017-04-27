class Person(object):
    def __init__(self, person_id, person_name, person_type):
        self.person_id = person_id
        self.person_name = person_name
        self.person_type = person_type

class Fellow(Person):
    def __init__(self, person_name):
        self.person_name = person_name
        self.person_type = "fellow"


class Staff(Person):
    def __init__(self, person_name):
        self.person_name = person_name
        self.person_type = "staff"

