import numpy as np
import matplotlib.pyplot as plt


data_x_1 = [0.0, [0.32,-0.17],[0.086,-0.13],[0.36,-0.24]]
data_x_2 = [0.037, [-0.23,-0.52],[-0.209,-0.39],[-0.308,-0.19],[-0.19,-0.55]]
data_x_3 = [0.018, [0.0107,-0.25],[-0.075,-0.25],[0.23,-0.49],[-0.09,-0.17]]
data_x_4 = [0.0095, [-0.016,-0.25],[0.175,-0.5],[0.225,-0.65],[-0.0065,-0.2]]
data_x_5 = [0.025, [-0.025,-0.37],[-0.1,-0.319],[-0.18,-0.32],[0.38,-0.73]]
data_x_6 = [0.03, [-0.053,-0.36],[0.085,-0.55],[0.18,-0.25],[-0.03,-0.45],[0.058,-0.458]]

data_y_1 = [0.032, [0.69,-0.4],[0.5, -0.39],[0.45, -0.42],[0.34, -0.38],[0.32, -0.35]]
data_y_2 = [0.02, [0.5,-0.3],[0.45,-0.34],[0.7,-0.15],[0.27,-0.29],[0.32,-0.3]]
data_y_3 = [0.025, [0.508,-0.33],[0.5,-0.28],[0.5,-0.32],[0.73,-0.22]]
data_y_4 = [0.01, [0.3, -0.17],[0.28,-0.2],[0.38,-0.09],[0.25,-0.23]]
data_y_5 = [0.04, [0.83,-0.5],[0.42,-0.5],[0.23,-0.41],[0.725,-0.45]]

data_x = [data_x_1, data_x_2, data_x_3, data_x_4, data_x_5, data_x_6]
data_y = [data_y_1, data_y_2, data_y_3, data_y_4, data_y_5]

data_x.sort(key=lambda x: x[0])
data_y.sort(key=lambda x: x[0])

def sample_error(x, mu=0.05, sigma=0.01):
    N = len(x)
    return np.random.normal(mu, sigma, N)

def scatter_plot(dataset, func, x_range = [0, 0.9], y_range = [0, -0.6], color_range=[-0.02, 0.06]):
    ax = plt.gca()
    fig = plt.gcf()
    contour(fig, ax, func, x_range=x_range, y_range=y_range, color_range=color_range)
    cmap = plt.get_cmap("GnBu")
    cmap_errorbar = plt.get_cmap("YlGnBu")
    norm = plt.Normalize(color_range[0], color_range[1])
    norm_errorbar = plt.Normalize(color_range[0]*1.5, color_range[1]*1.2)
    for data in dataset:
        x = []
        y = []
        color = []
        label = data[0]
        val = data[1:]
        c = label
        for i in range(len(val)):
            x.append(val[i][0])
            y.append(val[i][1])
            color.append(c)
        
        # plot the error bar
        area = (10 * np.random.rand(len(x)) + 20)**2
        plt.scatter(x, y, s=area, c=cmap_errorbar(norm_errorbar(color)), alpha=0.5)
        plt.scatter(x, y, marker='o', c=cmap(norm(color)), label=label, edgecolors='k', vmin=color_range[0], vmax=color_range[1])
    # fig.suptitle('test title')
    # plt.xlabel('xlabel')
    # plt.ylabel('ylabel')
    plt.show()

def gaussian2Dcoeff(sigma):
    return 1/(2*np.pi*sigma[0]*sigma[1])

def gaussian2Dpower(x, mu, sigma):
    return (x - mu)**2/(2*sigma**2)

def gaussian2D(x, y, mu, sigma):
    return -0.1*gaussian2Dcoeff(sigma)*np.exp(-(gaussian2Dpower(x, mu[0], sigma[0]) + gaussian2Dpower(y, mu[1], sigma[1])))

def fy(y, z):
    return gaussian2D(y, z, [0, 0], [0.8, 0.4]) + 0.05

def fx(x, z, norm=[0.44589632, 0.54879547, 12]):
    return -(norm[0] * x + norm[1] * z) / norm[2]

def contour(fig, ax, func, x_range = [0, 0.9], y_range = [0, -0.6], color_range=[-0.02, 0.06]):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    cntr1 = ax.contourf(X, Y, Z, cmap="GnBu", vmin=color_range[0], vmax=color_range[1])
    cbar = fig.colorbar(cntr1, ax=ax)
    cbar.ax.set_ylabel('offset (m)')

x_range = [-0.5, 0.5]
y_range = [0, -0.8]

# scatter_plot(data_x, fx, x_range, y_range)
# scatter_plot(data_y, fy)






def plot_bar(y, objects, err=None, yscale="linear"):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(y))
    bar_graph = None
    if err is not None:
        bar_graph = ax.bar(y_pos, y, align='center', yerr=err, color=[[91/255.0,186/255.0,207/255.0]])
    else:
        bar_graph = ax.bar(y_pos, y, align='center', color=[[91,186,207]])
    ax.set_xticks(y_pos)
    ax.set_xticklabels(objects)
    ax.set_yscale(yscale)
    return ax, bar_graph

def plot_two_bars(men_means, men_std, women_means, women_std, men_label, women_label):
    ind = np.arange(len(men_means))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    fig.set_size_inches(9,6)
    rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
                    label=men_label, color=[[91/255.0,186/255.0,207/255.0]])
    rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
                    label=women_label, color=[[186/255.0,228/255.0,189/255.0]])

    ax.set_xticks(ind)
    return ax, rects1, rects2

def autolabel(ax, rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(np.around(height, 3)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

def plot_time(time_data, time_err):
    ax, bar_graph = plot_bar(time_data, ('Manual', 'Controller', 'Vuforia', 'ICP', 'Ours'), time_err, "log")
    autolabel(ax, bar_graph, "left")
    plt.ylabel("Registration time")
    plt.title("Average Registration Time of Various Registration Methods")
    plt.show()

def plot_avg_acc(acc_data, acc_err):
    ax, bar_graph = plot_bar(acc_data, ('ICP', 'Vuforia', 'Ours'), acc_err, "linear")
    autolabel(ax, bar_graph, "left")
    plt.ylabel("Average registration accuracy (cm)")
    plt.title("Average Registration Accuracy of Various Registration Methods")
    plt.show()

def plot_acc(icp_acc_data, icp_acc_err, our_acc_data, our_acc_err):
    ax, bar1, bar2 = plot_two_bars(icp_acc_data, icp_acc_err, our_acc_data, our_acc_err, "ICP", "Ours")
    ax.set_xticklabels(np.arange(4,11))
    leg = ax.legend(loc='upper right')
    leg._legend_box.align = "left"
    autolabel(ax, bar1, "left")
    autolabel(ax, bar2, "right")
    plt.xlabel("Number of Detected Markers")
    plt.ylabel("Registration accuracy (cm)")
    plt.title("Registration Accuracy vs. Number of Detected Markers")
    plt.show()

def plot_corrections(icp_corr, our_corr, our_corr_err):
    ax, bar1, bar2 = plot_two_bars(icp_corr, None, our_corr, our_corr_err, "ICP", "Ours")
    ax.set_xticklabels(np.arange(4,11))
    leg = ax.legend(loc='upper left')
    leg._legend_box.align = "left"
    autolabel(ax, bar1, "left")
    autolabel(ax, bar2, "right")
    plt.show()

def plot_dist(v_dist, v_dist_err, ours_dist, ours_dist_err, dist_data):
    ax, bar1, bar2 = plot_two_bars(v_dist, v_dist_err, ours_dist, ours_dist_err, "Vuforia", "Ours")
    ax.set_xticklabels(dist_data)
    leg = ax.legend(loc='upper right')
    leg._legend_box.align = "left"
    autolabel(ax, bar1, "left")
    autolabel(ax, bar2, "right")
    plt.xlabel("Distance from marker (cm)")
    plt.ylabel("Registration accuracy (cm)")
    plt.title("Registration Accuracy vs. Distance From Marker")
    plt.show()

def find_dist(dist):
    return np.around(np.sqrt(np.square(dist) + 45**2),1)

time_data, time_err = [142, 54, 6, 1, 0.9], [55, 24, 3, 0.5, 0.5]
avg_acc_data, avg_acc_err = [3.2, 0.3, 0.5], [0.2, 0.2, 0.2] # 27.7
our_acc_data, our_acc_err = [0.5, 0.5, 0.7, 0.2, 0.2, 0.3, 0.2], [0.2, 0.2, 0.1, 0.2, 0.2, 0.2, 0.2]
icp_acc_data, icp_acc_err = [0.379, 0.306, 0.339, 0.195, 0.3174, 0.36865, 0.312], [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
icp_acc_data = 10 * np.array(icp_acc_data)
icp_corr = [3,3,3,3,3,3,3]
our_corr, our_corr_err = [0,0,0,1,2,1,3], [0,0,0,0.5,0.5,0.5,1]

dist_data = [35, 30, 25, 20, 15, 10]
dist_data = find_dist(np.array(dist_data))
v_dist, v_dist_err = [1.3, 1.3, 1.1, 0.35, 0.4, 0.2], [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
ours_dist, ours_dist_err = [1.2, 0.8, 0.7, 0.5, 0.8, 1.2], [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

# print(sum(our_acc_data) / len(our_acc_data))
# print(sum(icp_acc_data) / len(icp_acc_err))

print("dist_data: \n", dist_data)

plot_time(time_data, time_err)
# plot_avg_acc(avg_acc_data, avg_acc_err)
# plot_acc(icp_acc_data, icp_acc_err, our_acc_data, our_acc_err)
# plot_corrections(icp_corr, our_corr, our_corr_err)
plot_dist(v_dist, v_dist_err, ours_dist, ours_dist_err, dist_data)