# visualize.py
import matplotlib.pyplot as plt

def plot_head_position(head_counts_child, head_counts_adult):
    """
    Plot the distribution of head-initial vs. head-final compounds for child and adult data.
    """
    positions = ['initial', 'final', 'unknown']
    child_counts = [head_counts_child.get(pos, 0) for pos in positions]
    adult_counts = [head_counts_adult.get(pos, 0) for pos in positions]

    x = range(len(positions))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar([p - width/2 for p in x], child_counts, width, label='Child')
    ax.bar([p + width/2 for p in x], adult_counts, width, label='Adult')

    ax.set_xlabel('Head Position')
    ax.set_ylabel('Frequency')
    ax.set_title('Head Position in Compounds (Child vs. Adult)')
    ax.set_xticks(x)
    ax.set_xticklabels(positions)
    ax.legend()

    plt.show()
