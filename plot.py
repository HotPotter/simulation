import matplotlib.pyplot as plt

'''Bar Chart'''
def my_plot(x, y):
    fig, ax = plt.subplots()
    ax.bar(x, y, width=0.4, color='r')
    # ax.set_xticks([1,2,3])  # set the x ticks to be at the middle of each bar since the width of each bar is 0.8
    # ax.set_xticklabels("A", "B", "C")  #replace the name of the x ticks with your Groups name
    plt.ylabel("Number of players")
    plt.xlabel("Get the first hero")
    plt.show()