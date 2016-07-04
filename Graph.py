# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:15:12 2016

@author: wzhao
"""

class Graph(dict):
    def __init__(self, vs = [], es = []):
        """
        create a new graph, vs: list of vertices; es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
        
        for e in es:
            self.add_edge(e)
        
    def add_vertex(self, v):
         """ add vertex v to the graph """
         self[v] = {}
         
    def add_edge(self, e):
         """ add edge e to the graph """
         v, w = e
         self[v][w] = e
         self[w][v] = e
         
    def get_edge(self, v, w):
        try:
            return self[v][w]
        except:
            return None
    
    def remove_edge(self, e):
        v, w = e
        del self[v][w]
        del self[w][v]
        
    def vertices(self):
        return self.keys()
        
    def edges(self):
        s = set()
        for d in self.itervalues():
            s.update(d.itervalues())
        return s

    def out_vertices(self, w):
        return self[v].keys()
    
    def out_edges(self, v):
        return self[v].values()
    
    def add_all_edges(self):
        vs = self.vertices()
        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if j == i:
                    break
                self.add_edge(Edge(v, w))
                
    def add_regular_edges(self, k=2):
        vs = self.vertices
        if k >= len(vs):
            raise ValueError, ("cannot build a regular graph with " +
                               "degree >= number of vertices.")
        
        if is_odd(k):
            if is_odd(len(vs)):
                raise ValueError, ("cannot build a regular graph with a odd degree and odd number of vertex")
            self.add_regular_edges_even(k-1)
            self.add_regular_edges_odd()
        else:
            self.add_regular_edges_even(k)
            
    def add_regular_edges_even(self, k = 2):
        vs = self.vertices()
        double = vs * 2
        for i, v in enumerate(vs):
            for j in range(1, k/2 + 1):
                w = double[i + j]
                self.add_edge(Edge(v, w))
                
                
    def adde_regular_edge_odd(self):
        vs = self.vertices()
        n = len(vs)
        reduplicated_list = vs * 2
        
        for i in range(n/2):
            v = reduplicated_list[i]
            w = reduplicated_list[i + n/2]
            self.add_edge(Edge(v, w))
                
        
        
                               
        
                                
def is_odd(k):
    return x % 2
         
         
class Vertex(object):
    def __init__(self, label=''):
        self.label = label
        
    def __repr__(self):
        return "vertex(%s)" % repr(self.label)
        
    __str__ = __repr__
    
    
class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))
        
    def __repr__(self):
        return "edge (%s, %s)" % (repr(self[0]), repr(self[1]))
        

#unit test
if __name__ == "__main__" :
    v = Vertex("v")
    print v    
    w = Vertex("w")
    e = Edge(v, w)
    print e
    g = Graph([v, w], [e])
    print g
    x = Vertex("x")    
    print g.get_edge(w, v)
    print g.get_edge(v, x)
    g.remove_edge(e)
    print g.get_edge(w, v)
    print g.vertices()
    
    
    g.add_edge(Edge(v, w))
    g.add_vertex(x)
    g.add_edge(Edge(w, x))
    
    print g.edges()
    print g.out_vertices(x)
    
    
            
        