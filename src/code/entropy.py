""" 
Solution for MOD500 information entropy tutorial
"""

import numpy as np
import matplotlib.pyplot as plt


def calculate_entropy(p_distr):
    """Calculate the entropy from a probability distribution

    Input
    -----
    p : np.array
        the discrete probability distribution

    Output
    ------
    h : float
        entropy
    """
    entropy = -np.sum(p_distr[p_distr != 0]*np.log(p_distr[p_distr != 0]))
    return entropy


def create_experiments(n_points, shape='gaussian'):
    """Create experiments according to a probability distribution
    
    Input
    -----
    n_points : integer
        the number of points of the probability distribution
   
    shape : string, optional
        the type of distribution, 
        supported types: gaussian, poisson, geometrici, flat

    Output
    ------
    p : np.array
        probability distribuiton
    """
    if shape == 'gaussian':
        p = np.random.normal(loc=5, scale=0.5, size=n_points)

    elif shape == 'poisson':
        p = np.random.poisson(5, size=n_points)

    elif shape == 'geometric':
        p = np.random.geometric(p=0.35, size=n_points)

    elif shape == 'flat':
        p = np.random.rand(n_points)

    else:
        raise TypeError(f'Distribution type {shape}  not supported')

    return p


def create_prob_distribution(x, n_intervals=100, min_val=0, max_val=10):
    """From a set of measurement, create a discrete distribution

    Input
    -----
    x : np.array
        list of experiments
    n_intervals : int
        number of points in the discrete distribution
    min_val : float, optional
        the minimal value the distribution can have
    max_val : float, optional
        the maximal value the distribution can have

    Output
    ------
    y : np.array
        distribution data points

    """
    # I write this in semi-vanilla python,
    # with numpy could be much faster
    y = np.zeros(n_intervals)
    for i in list(x):
        if i > min_val:
            y[int(i/max_val*n_intervals)] += 1
    tot = np.sum(y)
    return y/tot


def plotter(x, y=None, mode='hist'):
    """Plot your distribution

    Input
    -----
    x : np.array
        list of points to plot
    y : np.array, optional
        list of y values
    mode : string, optional
        type of plot to prepare, 
        it accept: hist, xy
    """
    if mode == 'hist':
        plt.hist(x, 160, density=True)
    elif mode == 'xy':
        plt.plot(x, y)
    else:
        raise TypeError(f'{mode} plot not supported')
    plt.show()


# Here the main code
npoints = 1000
h = []
for i in range(npoints):
    experiments = create_experiments(i)
    prob = create_prob_distribution(experiments)
    h.append(calculate_entropy(prob))
    
plotter(np.arange(npoints), h, mode='xy')
