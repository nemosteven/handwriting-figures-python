import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example 1
# With function xkcd, we can achieve hand-writing
# df = pd.DataFrame({
#     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
#     'y': [4, 4, 4.5, 5, 5.5, 6, 6]
# })
#
# with plt.xkcd():
#     fig, ax = plt.subplots(figsize=(6.5, 4), dpi=100)
#     ax = df.plot.kde(color=["#BC3C28", "#0972B5"], ax=ax)
#     ax.set_ylim((0, 0.4))
#     ax.legend(frameon=False)
#     ax.set_title('Example1 of Handwriting', pad=20)
#     ax.text(.8, -.22, 'Visualization by DataCharm', transform=ax.transAxes,
#             ha='center', va='center', fontsize=10, color='black')
#     plt.show()

# Example 2
with plt.xkcd():
    fig, ax = plt.subplots(figsize=(6.5, 4), dpi=100)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim([-30, 10])
    data = np.ones(100)
    data[70:] -= np.arange(30)
    ax.annotate('The Day I Realized \n I Cound Cook Bacon \n Whenever I Wanted',
                xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

    ax.plot(data, color='#BC3C28')
    ax.set_xlabel('time')
    ax.set_ylabel('my overall health')
    ax.set_title('Example 2 of Handwriting')
    ax.text(.8, -.15, 'Visualization by DataCharm', transform=ax.transAxes,
            ha='center', va='center', fontsize=10, color='black')
    plt.show()


# # Example 3
# with plt.xkcd():
#     x = [1, 2, 3, 4]
#     y = [3, 4, 5, 6]
#     plt.plot(x, y)
#     plt.xlabel('x_label')
#     plt.ylabel('y_label')
#     plt.title('Example 3 of Handwriting')
#     plt.show()



