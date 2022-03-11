#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()
moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
Moscow_London = ((moscow[0]-london[0])**2+(moscow[1]+london[1])**2)**.5
Moscow_Paris = ((moscow[0]-paris[0])**2+(moscow[1]+paris[1]**2))**.5
London_Paris = ((london[0]-paris[0])**2+(london[1]+paris[1])**2)**.5
# TODO здесь заполнение словаря

distances ['Moscow'] = {}
distances ['Moscow']['London'] = Moscow_London
distances ['Moscow']['Paris'] = Moscow_Paris

distances ['London'] = {}
distances ['London']['Moscow'] = Moscow_London
distances ['London']['Paris'] = London_Paris

distances ['Paris'] = {}
distances ['Paris']['Moscow'] = Moscow_London
distances ['Paris']['London'] = London_Paris
pprint(distances)




