import matplotlib.pyplot as plt

def plot_img(image, ax = plt, title = None):
    ax.imshow(image)
    ax.axis('off')
    if title is not None:
        if ax == plt:
            plt.title(title)
        else:
            ax.set_title(title)
            
            
def plot_landmarks_color(landmarks):
        r = landmarks.landmarks_array
        landmarks_point_info = landmarks.points_info
        plt.plot(r[landmarks_point_info['CONTOURS'],0], r[landmarks_point_info['CONTOURS'],1], 'b.')
        plt.plot(r[landmarks_point_info['LEFT_EYEBROWN'],0], r[landmarks_point_info['LEFT_EYEBROWN'],1], 'r.')
        plt.plot(r[landmarks_point_info['REIGHT_EYEBROWN'],0], r[landmarks_point_info['REIGHT_EYEBROWN'],1], 'g.')
        plt.plot(r[landmarks_point_info['NOSE_POINTS'],0], r[landmarks_point_info['NOSE_POINTS'],1], 'k.')
        plt.plot(r[landmarks_point_info['LEFT_EYE'],0], r[landmarks_point_info['LEFT_EYE'],1], '.', color =  'white')
        plt.plot(r[landmarks_point_info['REIGHT_EYE'],0], r[landmarks_point_info['REIGHT_EYE'],1], '.', color = 'purple')
        plt.plot(r[landmarks_point_info['UPPER_LIP'],0], r[landmarks_point_info['UPPER_LIP'],1], '.', color =  'pink')
        plt.plot(r[landmarks_point_info['BOTTOM_LIP'],0], r[landmarks_point_info['BOTTOM_LIP'],1], '.', color =  'orange')
        plt.plot(r[landmarks_point_info['TEETH'],0], r[landmarks_point_info['TEETH'],1], '.', color =  'yellow')
        if 'EYE' in landmarks_point_info.keys():
            plt.plot(r[landmarks_point_info['EYE'],0], r[landmarks_point_info['EYE'],1], '.', color =  'tab:blue')