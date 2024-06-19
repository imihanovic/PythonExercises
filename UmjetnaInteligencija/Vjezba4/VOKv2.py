# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:34:31 2024

@author: IvanaMihanović
"""

from queue import PriorityQueue
from copy import deepcopy
state_dictionary = {}
class Stanje:
    def __init__(self, left='VOK', boat='', right='', boat_side='L', last_unloaded = ''):
        self.left = left
        self.boat = boat
        self.right = right
        self.last_unloaded = last_unloaded
        self.boat_side = boat_side

    def __str__(self):
        left_coast = ''.join(sorted(self.left, reverse=True)) + ('B' if self.boat_side == 'L' else '')
        right_coast = ''.join(sorted(self.right, reverse=True)) + ('B' if self.boat_side == 'D' else '')
        return f"{left_coast} ~~ {right_coast}    boat: {self.boat}"
    
    def all_actions(self):
        closer_loading = []
        closer_unloading = []
        transfer_boat = ['']
        if self.boat == '':
            if self.boat_side == 'L':
                closer_loading = [obj for obj in self.left]
            else:
                closer_loading = [obj for obj in self.right]
        else:
            if len(set(self.boat))>0:
                closer_unloading = [self.boat]
            else:
                closer_unloading = []
            return closer_unloading
        return (closer_loading + transfer_boat + closer_unloading)
    
    def next_states(self):
        next_states_list = []
        if self.boat_side == 'L':
            current_coast = set(self.left)
            opposite_coast = set(self.right)
        else:
            current_coast = set(self.right)
            opposite_coast = set(self.left)
        if self.boat != '':
            new_current_side = current_coast | {self.boat}
            new_boat = ''
            if self.boat_side == 'L':
                next_states_list.append(Stanje(new_current_side, new_boat, opposite_coast, self.boat_side))
            else:
                next_states_list.append(Stanje(opposite_coast, new_boat, new_current_side, self.boat_side))
        else:
            for obj in current_coast:
                new_current_side = current_coast - {obj}
                new_coast = 'L' if self.boat_side == 'D' else 'D'
                new_boat = obj
                if self.boat_side == 'L':
                    new_state = Stanje(new_current_side, new_boat, opposite_coast, new_coast)
                else:
                    new_state = Stanje(opposite_coast, new_boat, new_current_side, new_coast)
                next_states_list.append(new_state)
            if self.boat_side == 'L':
                new_state = Stanje(current_coast, '', opposite_coast, 'L' if self.boat_side == 'D' else 'D')
            else:
                new_state = Stanje(opposite_coast, '', current_coast, 'L' if self.boat_side == 'D' else 'D')
            next_states_list.append(new_state)
        return next_states_list
    
    def is_solved(self):
        return all(st in list(self.right) for st in ['V', 'O', 'K']) and self.boat_side == 'D'
     
    def is_initial(self):
        return all(st in list(self.left) for st in ['V', 'O', 'K']) and self.boat_side == 'L'

    def is_terminal(self):
        if(self.boat_side == 'D' and self.left == "VOK"):
            return True
        if self.boat_side == 'D' and 'O' in self.left and ('V' in self.left or 'K' in self.left):
                return True
        elif self.boat_side == 'L' and 'O' in self.right and ('V' in self.right or 'K' in self.right):
                return True
        return self.is_solved()
    
    def action(self, obj):
        if obj:
            if self.boat_side == 'L':
                if obj in self.boat:
                    self.boat = ''
                    self.left += obj
                    self.last_unloaded = obj
                else: 
                    self.left = self.left.replace(obj, '')
                    self.boat = obj
                    self.last_unloaded = ''
                    self.boat_side = 'D'
            else:
                if obj in self.boat:
                    self.boat = ''
                    self.right += obj
                    self.last_unloaded = obj
                else:
                    self.right = self.right.replace(obj, '')
                    self.boat = obj
                    self.last_unloaded = ''
                    self.boat_side = 'L'
        else:
            self.boat_side = 'D' if self.boat_side == 'L' else 'L'
        return self

    def undo_action(self, obj):
        if obj:
           if self.last_unloaded == obj and self.boat == '':
               if self.boat_side == 'L':
                   self.left = self.left.replace(obj, '')
                   
               else:
                   self.right = self.right.replace(obj, '')
               self.boat = obj
               self.last_unloaded = ''
           else:
               if self.boat_side == 'L':
                   self.right += obj
                   self.boat_side = 'D'
               else:
                   self.left += obj
                   self.boat_side = 'L'
               self.boat = ''
        else:
            self.boat_side = 'D' if self.boat_side == 'L' else 'L'
        return self

    def copy(self):
        return deepcopy(self)

def generate(state):
    string_state = str(state)
    if string_state in state_dictionary:
        return
    if not (state.is_terminal() and state.boat == '' and not state.is_solved()) or (state.left == 'VOK' and state.boat_side == 'D'):
        print("STANJA", state)
        state_dictionary[string_state] = state.copy()
    for obj in state.all_actions():
        new_state = state.copy().action(obj)
        generate(new_state)
        new_state.undo_action(obj)
    return state_dictionary

def solution_bfs(node, cilj = Stanje(left = '', boat = '', right = 'VOK', boat_side='D')):
    queue = [node]
    visited = {str(node):[]}
    while queue:
        current_node = queue.pop(0)
        if str(current_node) == str(cilj):
            return visited[str(current_node)] + [str(current_node)]

        for neighbour in current_node.next_states():
            visited[str(neighbour)] = visited[str(current_node)] + [str(current_node)]
            if str(neighbour) not in visited[str(current_node)] and not neighbour.is_terminal():
                queue.append(neighbour)
                
    return visited[str(cilj)] + [str(cilj)]

def solution_dfs(node, cilj = Stanje(left = '', boat = '', right = 'VOK', boat_side='D')):
    visited = {str(node):[]}
    stack = [node]
    while stack:
        current_node = stack.pop()

        if str(current_node) == str(cilj):
            return visited[str(current_node)] + [str(current_node)]

        for next_state in current_node.next_states():
            visited[str(next_state)] = visited[str(current_node)] + [str(current_node)]
            if str(next_state) not in visited[str(current_node)] and not next_state.is_terminal():
                stack.append(next_state)

    return visited[str(cilj)] + [str(cilj)]

def best_first_search(initial_state, winning_state, states):
    queue = PriorityQueue()
    queue.put((len(states[str(initial_state)].right), str(initial_state)))
    visited = []
    while not queue.empty():
        _, current = queue.get()
        visited.append(str(current)) 
        if str(current) == str(winning_state):
            return True, visited

        for next_state in states[current].next_states():
            if str(next_state) not in visited and not (next_state.is_terminal() and not next_state.is_solved()):
                priority = (len(states[str(next_state)].right))
                queue.put((priority, str(next_state)))
    return False, visited
        
if __name__ == '__main__':
    pocetno_state = Stanje()
    pobjednicko_state = Stanje("", "","VOK","D")
    stanja = generate(pocetno_state)
    dfs = solution_dfs(pocetno_state)
    bfs = solution_bfs(pocetno_state)
    _, bestFS = best_first_search(pocetno_state, pobjednicko_state, stanja)
    print("Broj stanja: ", len(stanja))
    print("Bfs: ", bfs)
    print()
    print("Dfs: ", dfs)
    print()
    print("BestFS: ", len(bestFS),bestFS)