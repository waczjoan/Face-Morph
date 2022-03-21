import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def plot_img(image, ax = plt, title = None, alpha = 1):
    ax.imshow(image, alpha = alpha)
    ax.axis('off')
    if title is not None:
        if ax == plt:
            plt.title(title)
        else:
            ax.set_title(title)
            
            
def plot_landmarks_color(landmarks, ax = plt):
        r = landmarks.landmarks_array
        landmarks_point_info = landmarks.points_info
        ax.plot(r[landmarks_point_info['CONTOURS'],0], r[landmarks_point_info['CONTOURS'],1], 'b.')
        ax.plot(r[landmarks_point_info['LEFT_EYEBROWN'],0], r[landmarks_point_info['LEFT_EYEBROWN'],1], 'r.')
        ax.plot(r[landmarks_point_info['REIGHT_EYEBROWN'],0], r[landmarks_point_info['REIGHT_EYEBROWN'],1], 'g.')
        ax.plot(r[landmarks_point_info['NOSE_POINTS'],0], r[landmarks_point_info['NOSE_POINTS'],1], 'k.')
        ax.plot(r[landmarks_point_info['LEFT_EYE'],0], r[landmarks_point_info['LEFT_EYE'],1], '.', color =  'white')
        ax.plot(r[landmarks_point_info['REIGHT_EYE'],0], r[landmarks_point_info['REIGHT_EYE'],1], '.', color = 'purple')
        ax.plot(r[landmarks_point_info['UPPER_LIP'],0], r[landmarks_point_info['UPPER_LIP'],1], '.', color =  'pink')
        ax.plot(r[landmarks_point_info['BOTTOM_LIP'],0], r[landmarks_point_info['BOTTOM_LIP'],1], '.', color =  'orange')
        ax.plot(r[landmarks_point_info['TEETH'],0], r[landmarks_point_info['TEETH'],1], '.', color =  'yellow')
        if 'EYE' in landmarks_point_info.keys():
            ax.plot(r[landmarks_point_info['EYE'],0], r[landmarks_point_info['EYE'],1], '.', color =  'tab:blue')
            
            
def plot_corr(x, y, cmap = plt.get_cmap('RdBu'), norm = plt.Normalize(vmin=-.5, vmax=.5),**kwds):
    ax = plt.gca()
    r, _ = pearsonr(x, y)
    facecolor = cmap(norm(r))
    ax.set_facecolor(facecolor)
    lightness = (max(facecolor[:3]) + min(facecolor[:3]) ) / 2
    ax.annotate(f"r={r:.2f}", xy=(.5, .5), xycoords=ax.transAxes,
                color='white' if lightness < 0.7 else 'black', size=26, ha='center', va='center')
    
def plot_hist_with_component(component, ax = plt, label = ""):
     _ = ax.hist(component.flatten(), 
                          bins = int(len(set(component.flatten()))/2),
                          label = label, density = True, alpha = 0.7)