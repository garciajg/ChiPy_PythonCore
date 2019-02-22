import random
import string

# Dictionary class
# each user has a key that is the string, value that is the comfort score
# creation will be looped a number of times picked at random
# string identifier will be generated at random
# comfort score also generated at random
# after dictionary is populated with these random methods
# groups will be constructed, with a mind to make the average comfort score as close as possible

class Attendee(object):

    def __init__(self):
        """
        Initializes and Attendee with and
        identifier and a comfort score
        """
        self.idenfier = self.generate_attendee_id()
        self.comfort = self.generate_attendee_comfort_score()

    def generate_attendee_id(self):
        """
        Generates a random String ID for attendee
        """
        n = random.randint(1, 12)
        identifier = "".join(random.choice(string.ascii_letters) for i in range(n))
        return identifier

    def generate_attendee_comfort_score(self):
        """
        Generates random comfort score for attendee
        """
        n = random.randint(0, 100)
        return n


def generate_list_of_attendees():
    """
    Generates a list of Attendies
    """
    n = generate_attendee_number()
    temp_list = []
    for i in range(n):
        temp_list.append(Attendee())
    return temp_list


def generate_attendee_number():
    """
    Generates random numbers of Attendees
    that attended the event
    """
    n = random.randint(35,50)
    m = n % 4
    if m != 0:
        return n - m
    return n

number_of_attendees = generate_attendee_number()
attendees = generate_list_of_attendees()
print(len(attendees))

attendees_IDs = []