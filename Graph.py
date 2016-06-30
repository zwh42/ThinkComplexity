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
    
    
            
        