from random import choice

print("hello python")

class Caves(object):
    def __init__(self, number_of_caves):
        self.number_of_caves = number_of_caves
        self.cave_list = range(number_of_caves)
        self.unvisited = range(number_of_caves)[1:]
        self.visited = [0]
        self.caves = []
        self.setup_saves(number_of_caves)
        self.link_caves()
    
    def setup_caves(self, cave_number):
        """ Create the start list of caves"""
        for cave in range(cave_numbers):
            self.caves.append([])

    def link_caves(self):
        """ Make sure all of the caves are connected
        with two-way tunnels """
        while self.unvisited != []:
            this_cave = self.choose_cave(self.visited)
            next_cave = self.choose_cave(self.unvisited)
            self.create_tunnel(this_cave, next_cave)
            self.visit_cave(next_cave)

    def create_tunnel(self, cave_from, cave_to):
        """ Create a tunnel between cave_from
        and cave_to """
        self.caves[cave_from].append(cave_to)
        self.caves[cave_to].append(cave_from)



