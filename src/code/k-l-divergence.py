""" 
Solution for MOD500 information entropy tutorial: KL divergence

"""

import numpy as np
import matplotlib.pyplot as plt

from entropy import calculate_entropy, create_experiments
from entropy import create_prob_distribution, plotter


def calculate_kl(p_distr, p_ref):
    """Calculate the Kullback-Leibler divergence

    Input
    -----
    p_distr : np.array
        the discrete probability distribution
    p_ref : np.array
        the reference discrete probability distribution

    Output
    ------
    kl : float
        divergence
    """
    kl = np.sum(p_distr[p_distr*p_ref != 0]*np.log(p_distr[p_distr*p_ref != 0]/
                                                   p_ref[p_distr*p_ref != 0]))
    return kl


def main():
    experiments = create_experiments(1000000)
    reference_prob = create_prob_distribution(experiments)


    npoints = 1000
    kl = []
    for i in range(npoints):
        experiments = create_experiments(i)
        prob = create_prob_distribution(experiments)
        kl.append(calculate_kl(prob, reference_prob))

    plotter(np.arange(npoints), kl, mode='xy')


if __name__ == "__main__":
    main()
