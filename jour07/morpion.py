# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:19:46 2020

@author: straw
"""
import pygame

pygame.init()

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.box_centers = [[(round(self.width/6), round(self.height/6)), (round(self.width/3 + self.width/6), round(self.height/6)), (round((self.width/3)*2 + self.width/6), round(self.height/6))],
               [(round(self.width/6), round(self.height/3 + self.height/6)), (round(self.width/3 + self.width/6), round(self.height/3 + self.height/6)), (round((self.width/3)*2 + self.width/6), round(self.height/3 + self.height/6))],
               [(round(self.width/6), round((self.height/3)*2) + round(self.height/6)), (round(self.width/3 + self.width/6), round((self.height/3)*2 + self.height/6)), (round((self.width/3)*2 + self.width/6), round((self.height/3)*2 + self.height/6))]]

        self.window = None
        self.grid = [[None]*3, [None]*3, [None]*3]
        
    def __get_box(self):
        pos = pygame.mouse.get_pos()
        if (pos[0] <= self.width/3) and (pos[1] <= self.height/3):
            box = 'first box'
            
        if (pos[0] <= (self.width/3)*2) and (pos[0] >= (self.width/3)) and (pos[1] <= self.height/3):
            box = 'second box'
            
        if (pos[0] <= self.width) and (pos[0] >= (self.width/3)*2) and (pos[1] <= self.height/3):
            box = 'third box'
        
        if (pos[0] <= self.width/3) and (pos[1] <= (self.height/3)*2) and (pos[1] >= (self.height/3)):
            box = 'forth box'
            
        if (pos[0] <= (self.width/3)*2) and (pos[0] >= (self.width/3)) and (pos[1] <= (self.height/3)*2) and (pos[1] >= (self.height/3)):
            box = 'fifth box'
        
        if (pos[0] <= self.width) and (pos[0] >= (self.width/3)*2) and (pos[1] <= (self.height/3)*2) and (pos[1] >= (self.height/3)):
            box = 'sixth box'
            
        if (pos[0] <= self.width/3) and (pos[1] <= self.height) and (pos[1] >= (self.height/3)*2):
            box = 'seventh box'
            
        if (pos[0] <= (self.width/3)*2) and (pos[0] >= self.width/3) and (pos[1] <= self.height) and (pos[1] >= (self.height/3)*2):
            box = 'eighth box'
            
        if (pos[0] <= self.width) and (pos[0] >= (self.width/3)*2) and (pos[1] <= self.height) and (pos[1] >= (self.height/3)*2):
            box = 'nineth box'
        return box
    
    def fill_grid(self, player):
        box = self.__get_box()
        if box == 'first box':
            if self.grid[0][0] == None:
                self.grid[0][0] = player
                print(self.grid)
            
        if box == 'second box':
            if self.grid[0][1] == None:
                self.grid[0][1] = player
                print(self.grid)
            
        if box == 'third box':
            if self.grid[0][2] == None:
                self.grid[0][2] = player
                print(self.grid)
            
        if box == 'forth box':
            if self.grid[1][0] == None:
                self.grid[1][0] = player
                print(self.grid)
            
        if box == 'fifth box':
            if self.grid[1][1] == None:
                self.grid[1][1] = player
                print(self.grid)
            
        if box == 'sixth box':
            if self.grid[1][2] == None:
                self.grid[1][2] = player
                print(self.grid)
            
        if box == 'seventh box':
            if self.grid[2][0] == None:
                self.grid[2][0] = player
                print(self.grid)
            
        if box == 'eighth box':
            if self.grid[2][1] == None:
                self.grid[2][1] = player
                print(self.grid)
            
        if box == 'nineth box':
            if self.grid[2][2] == None:
                self.grid[2][2] = player
                print(self.grid)
    
    def player_switcher(self):
        for i in range(9):
            if i % 2 == 0:
                self.fill_grid(player='O')
            else:
                self.fill_grid(player='X')
    
    def get_winner(self):
        """
        Get winner from grid

        Parameters
        ----------
        grid : list
            grid tic tac toe.

        Returns
        -------
        winner : str
            tic tac toe winner.

        """
        winner = None
        o_moves = []
        x_moves = []
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 'O':
                    o_moves.append((i,j))
                if self.grid[i][j] == 'X':
                    x_moves.append((i,j))
                    
        o_moves_lines = []
        o_moves_columns = []
        x_moves_lines = []
        x_moves_columns = []
        if len(o_moves) >= 3:
            for o_line, o_column in o_moves:
                o_moves_lines.append(o_line)
                o_moves_columns.append(o_column)
                
            if (o_moves_lines.count(0) == 3) or (o_moves_lines.count(1) == 3) or (o_moves_lines.count(2) == 3):
                winner = 'O'
                
            if (o_moves_columns.count(0) == 3) or (o_moves_columns.count(1) == 3) or (o_moves_columns.count(2) == 3):
                winner = 'O'
                
            if (o_moves_lines == o_moves_columns) or (o_moves_lines == o_moves_columns[::-1]):
                winner = 'O'
                
        if len(x_moves) >= 3:
            for x_line, x_column in x_moves:
                x_moves_lines.append(x_line)
                x_moves_columns.append(x_column)
                
            if (x_moves_lines.count(0) == 3) or (x_moves_lines.count(1) == 3) or (x_moves_lines.count(2) == 3):
                winner = 'X'
                
            if (x_moves_columns.count(0) == 3) or (x_moves_columns.count(1) == 3) or (x_moves_columns.count(2) == 3):
                winner = 'X'
                
            if (x_moves_lines == x_moves_columns) or (x_moves_lines == x_moves_columns[::-1]):
                winner = 'X'
     
        return winner
                
    def __display_grid(self):
        """
        Display tic tac toe's grid

        Returns
        -------
        None.

        """
        #draw vertical lines  
        pygame.draw.line(self.window,(255,255,255),(round(self.width/3), 0),(round(self.width/3), self.height),2)
        pygame.draw.line(self.window,(255,255,255),(self.width - round(self.width/3), 0),(self.width - round(self.width/3), self.height),2)
        
        #draw horizontal lines 
        pygame.draw.line(self.window,(255,255,255),(0, round(self.height/3)),(self.width,round(self.height/3)),2)
        pygame.draw.line(self.window,(255,255,255),(0,self.height - round(self.height/3)),(self.width, self.height - round(self.height/3)),2)
    
    def __display_X_O(self, v):
        """
        Display the player's turn in tic tac toe's grid

        Parameters
        ----------
        v : str
            X or O.

        Returns
        -------
        None.

        """
        box = self.__get_box()
        if box == 'first box':
            print('First box')
            if v == 'O':
                pygame.draw.circle(self.window, (255, 255, 255), (self.box_centers[0][0][0], self.box_centers[0][0][1]), round(self.height/6)-10, 10)
            elif v == 'X':
                pygame.draw.line(self.window, (255,255,255),(0,0),(self.width/3, self.height/3),2)
                pygame.draw.line(self.window, (255,255,255),(0, self.height/3),(self.width/3, 0),2)
                        
        if box == 'fifth box':
            print('Fifth box')
            if v == 'O':
                pygame.draw.circle(self.window, (255, 255, 255), (self.box_centers[1][1][0], self.box_centers[1][1][1]), round(self.height/6)-10, 10)
            elif v == 'X':
                pygame.draw.line(self.window, (255,255,255),(self.width/3, self.height/3),((self.width/3)*2, (self.height/3)*2),2)
                pygame.draw.line(self.window, (255,255,255),((self.width/3)*2, self.height/3),(self.width/3, (self.height/3)*2),2)
                    
        if box == 'nineth box':
            print('Nineth box')
            if v == 'O':
                pygame.draw.circle(self.window, (255, 255, 255), (self.box_centers[2][2][0], self.box_centers[2][2][1]), round(self.height/6)-10, 10)
            elif v == 'X':
                pygame.draw.line(self.window, (255,255,255), ((self.width/3)*2,(self.height/3)*2), (self.width,self.height), 2)
                pygame.draw.line(self.window, (255,255,255), (self.width, (self.height/3)*2), ((self.width/3)*2, self.height), 2)
                
        #boxes in line 1
        if box == 'second box':
            print('Second box')
            if v == 'O':
                pygame.draw.circle(self.window, (255, 255, 255), (self.box_centers[0][1][0], self.box_centers[0][1][1]), round(self.height/6)-10, 10)
            elif v == 'X':
                pygame.draw.line(self.window, (255,255,255), (self.width/3,0), ((self.width/3)*2, self.height/3), 2)
                pygame.draw.line(self.window, (255,255,255), ((self.width/3)*2,0), (self.width/3, self.height/3), 2)
                    
        if box == 'third box':
            print('Third box')
            if v == 'O':
                pygame.draw.circle(self.window, (255, 255, 255), (self.box_centers[0][2][0], self.box_centers[0][2][1]), round(self.height/6)-10, 10)
            elif v == 'X':
                pygame.draw.line(self.window, (255,255,255), ((self.width/3)*2,0), (self.width, self.height/3), 2)
                pygame.draw.line(self.window, (255,255,255), (self.width,0), ((self.width/3)*2, self.height/3), 2)
        
        # boxes in line 2
        if box == 'forth box':
            print('Forth box')
            if v == 'O':
                pygame.draw.circle(self.window, (255, 255, 255), (self.box_centers[1][0][0], self.box_centers[1][0][1]), round(self.height/6)-10, 10)
            elif v == 'X':
                pygame.draw.line(self.window, (255,255,255), (0,self.height/3), (self.width/3, (self.height/3)*2), 2)
                pygame.draw.line(self.window, (255,255,255), (self.width/3,self.height/3), (0, (self.height/3)*2), 2)
        
        if box == 'sixth box':
            print('Sixth box')
            if v == 'O':
                pygame.draw.circle(self.window, (255, 255, 255), (self.box_centers[1][2][0], self.box_centers[1][2][1]), round(self.height/6)-10, 10)
            elif v == 'X':
                pygame.draw.line(self.window, (255,255,255),((self.width/3)*2,self.height/3),(self.width, (self.height/3)*2),2)
                pygame.draw.line(self.window, (255,255,255), (self.width,self.height/3), ((self.width/3)*2, (self.height/3)*2), 2)
        
        # boxes in line 3
        if box == 'seventh box':
            print('Seventh box')
            if v == 'O':
                pygame.draw.circle(self.window, (255, 255, 255), (self.box_centers[2][0][0], self.box_centers[2][0][1]), round(self.height/6)-10, 10)
            elif v == 'X':
                pygame.draw.line(self.window, (255,255,255), (0,(self.height/3)*2), (self.width/3, self.height),2)
                pygame.draw.line(self.window, (255,255,255), (self.width/3, (self.height/3)*2), (0, self.height), 2)
        
        if box == 'eighth box':
            print('Eighth box')
            if v == 'O':
                pygame.draw.circle(self.window, (255, 255, 255), (self.box_centers[2][1][0], self.box_centers[2][1][1]), round(self.height/6)-10, 10)
            elif v == 'X':
                pygame.draw.line(self.window, (255,255,255), (self.width/3,(self.height/3)*2), ((self.width/3)*2, self.height),2)
                pygame.draw.line(self.window, (255,255,255), ((self.width/3)*2,(self.height/3)*2), (self.width/3, self.height),2)

    def display_winner(self, winner):
        self.window.fill((255,255,255))
        font = pygame.font.SysFont('Lato', 40, True)
        message = font.render('The winner is player {} !'.format(winner), True, (0,0,0))
        self.window.blit(message, [200, 30, 200, 50])

    def display_all(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        counter = 0
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1,0,0):
                        if counter % 2 == 0:
                            player = 'O'
                        else:
                            player = 'X'
                        self.fill_grid(player=player)
                        self.__display_X_O(player)
                        counter = counter + 1
                        if counter >= 4:
                            winner = self.get_winner()
                            if winner != None:
                                print('The winner is player {} !'.format(winner))
                                self.display_winner(winner)
            self.__display_grid()
            pygame.display.flip()
        pygame.quit()
        

g = Game(800, 600)
g.display_all()

