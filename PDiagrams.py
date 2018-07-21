#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:40:43 2018

@author: cx513
"""




points = np.random.random((100, 4))
f = d.fill_rips(points, 2, 1.)
p = d.homology_persistence(f)
dgms = d.init_diagrams(p, f)
d.plot.plot_diagram(dgms[1], show = True)


from scipy.spatial import distance


#distance.euclidean(u, v)

#Y = distance.pdist(X, 'euclidean')