#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = {rest: i for i, rest in enumerate(list1)}
        intersect = {rest: i+d1[rest] for i, rest in enumerate(list2) if rest in d1}
        return [rest for rest, ct in intersect.items() if ct==min(intersect.values())]

