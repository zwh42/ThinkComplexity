# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 11:23:19 2016

@author: wzhao
"""

from Graph import *
import random


class RandomGraph(Graph):
    
    def add_random_edges(self, p=0.5):
        vs = self.vertices()        
        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if j <= i : 
                    continue
                if random.random() > p:
                    continue
                self.add_edge(Edge(v, w))
                

if __name__ == "__main__":
    v = Vertex("v")
    w = Vertex("w")
    x = Vertex("x")    
    g = RandomGraph([v, w, x])
    g.add_random_edges(0.5)
    print g.edges()
    