import nnumpy as np
def get_random_subset_of_naturals_up_to_20():
    mask = np.random.randint(0,2, size=20)
    naturals = np.arange(1,21)
    subset= naturals [mask == 1]
    return subset

