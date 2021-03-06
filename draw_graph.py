# -*- coding: utf-8 -*-
#!/usr/bin/env python

from graphviz import Digraph
import csv
from Queue import Queue

def parse_csv(csv_file):
  csv_reader = csv.reader(open(csv_file), dialect=csv.excel)
  return {unicode(key, 'utf-8'):value for [value, key] in csv_reader}

def draw_graph(centroid, graph):
  g = Digraph(centroid, engine='sfdp')
  g.attr('node', style='filled')
  g.node(centroid, color='crimson')
  for key in graph:
    g.node(key, color=('burlywood2' if key is not centroid else 'crimson'))
  large_set = Queue()
  large_set.put(centroid)
  visited_from_graph = {}
  while not large_set.empty():
    key = large_set.get()
    if key in graph and key not in visited_from_graph:
      visited_from_graph[key] = True
      for keyword in graph[key]:
        g.edge(key, keyword, penwidth=str(float(graph[key][keyword])/50.0))
        large_set.put(keyword)
  g.view()

def main():
  dataset = {
      u'biały' : parse_csv('data/bialy.csv'),
      u'godło' : parse_csv('data/godlo.csv'),
      u'orzeł' : parse_csv('data/orzel.csv'),
      u'ptak' : parse_csv('data/ptak.csv')
  }
  for key in dataset:
    draw_graph(key, dataset)


if __name__ == '__main__':
    main()
