import matplotlib.pyplot as plt

'''
fig,ax = plt.subplots()

ax.bar([1,4,5,7], [4,5,8,2], width=0.4, color='r')
#ax.set_xticks([1,2,3])  # set the x ticks to be at the middle of each bar since the width of each bar is 0.8
#ax.set_xticklabels("A", "B", "C")  #replace the name of the x ticks with your Groups name

plt.ylabel("YYYY")
plt.xlabel("boxes")
plt.show()
'''

def my_plot(X, Y):
    fig, ax = plt.subplots()

    ax.bar(X, Y, width=0.4, color='r')
    # ax.set_xticks([1,2,3])  # set the x ticks to be at the middle of each bar since the width of each bar is 0.8
    # ax.set_xticklabels("A", "B", "C")  #replace the name of the x ticks with your Groups name

    plt.ylabel("YYYY")
    plt.xlabel("boxes")
    plt.show()