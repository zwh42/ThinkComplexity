# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 14:34:59 2016

@author: wzhao
"""

class LinearMap(object):
    
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v
        raise KeyError

class BetterMap(object):
    
    def __init__(self, n = 100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())
    
    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]
        
    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)
        
    def get(self, k):
        m = self.find_map(k)
        return m.get(k)
        
        
class HashMap(object):
    
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0
    
    def get(self, k):
        return self.maps.get(k)
    
    def add(self, k, v):
        if self.num == len(self.maps.maps):
            self.resize()
        self.maps.add(k, v)
        self.num += 1
    
    def resize(self):
        new_maps = BetterMap(self.num * 2)
        for m in self.maps.maps:
            for k, v in m.items:
                new_maps.add(k, v)
             
        

if __name__ == "__main__" :
    test_map = LinearMap()
    test_map.add("a",2)
    test_map.add(2, 3)
    print test_map.get(2)
    
    test_map2 = BetterMap()
    test_map2.add("a",2)
    test_map2.add(2, 3)
    print test_map2.get("a")    
    
    print "test hashmap"
    test_hash = HashMap()
    test_hash.add("2",5)
    test_hash.add("343",1)
    test_hash.add("143",1)
    test_hash.add("34",1)
    print test_hash.get("2")
    
    
    
    
    
    
    
    
    
    
    