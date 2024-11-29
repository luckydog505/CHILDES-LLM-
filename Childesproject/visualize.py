import matplotlib.pyplot as plt

def plot_head_position(head_counts):
    """
    Plot the distribution of head-initial vs. head-final compounds.
    """
    plt.bar(head_counts.keys(), head_counts.values())
    plt.xlabel("Head Position")
    plt.ylabel("Frequency")
    plt.title("Head Position in Compounds")
    plt.show()
