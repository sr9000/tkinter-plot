from matplotlib import pyplot as plt


def plot(name, values):
    fig, ax = plt.subplots()
    ax.plot(values)

    ax.set(xlabel='days', ylabel='infected', title=name)
    ax.grid()

    plt.show()
