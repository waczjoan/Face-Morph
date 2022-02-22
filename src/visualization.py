import matplotlib.pyplot as plt

def plot_img(image, ax = plt, title = None):
    ax.imshow(image)
    ax.axis('off')
    if title is not None:
        if ax == plt:
            plt.title(title)
        else:
            ax.set_title(title)