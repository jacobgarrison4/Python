#====================================
# P2_View.py
# Created by Jacob Garrison
# CIS 211 Spring 2016
# Project 3
#====================================

class View:

    def create(self, world_size):
        self.__world_size = world_size

    def draw(self):
        rows = world_size
        columns = world_size
        for i in range(rows):
            for j in range(columns):
                if j == 0:
                    print(ij, end=' ')
                if j == 5:
                    print(ij, end=' ')
                print('.', end=' ')
                
