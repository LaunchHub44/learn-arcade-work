# Wrong way
#
# name = "Link"
# outfit = "Green"
# max_hit_points =50
# current_hit_points = 50
# armor_amount = 6
# max_speed = 10
#
# def display_character(name, outfit, max_hit_points, current_hit_points, armor, max_speed):
#     print(name, outfit, max_hit_points, current_hit_points)
#

class Link:
    def __init__(self, name, outfit):
        self.name = name
        self.outfit = outfit
        self.max_hit_points =50
        self.current_hit_points = 50
        self.armor_amount = 6
        self.max_speed = 10

class Zelda:
    def __init__(self, name, outfit):
        self.name = name
        self.outfit = outfit
        self.max_hit_points =1
        self.current_hit_points = 1
        self.armor_amount = 3
        self.max_speed = 3


def display_character(ch:Link):
    print(ch.name, ch.outfit, ch.max_hit_points, ch.current_hit_points, ch.armor_amount, ch.max_speed)

if __name__ == '__main__':
    link = Link("Link", "Green")
    display_character(link)

    zelda = Zelda("Zelda", "Light Blue")
    display_character(zelda)


