import mediapipe as mp
import numpy as np


def get_info_68_points():
    landmarks_68_points = {
        'CONTOURS' : list(range(17)),
        'LEFT_EYEBROWN' : list(range(17,22)),
        'REIGHT_EYEBROWN' : list(range(22,27)),
        'NOSE_POINTS' : list(range(27,36)),
        'NOSE_LINE_POINTS' : list(range(27,31)),
        'LEFT_EYE' : list(range(36,42)),
        'REIGHT_EYE' : list(range(42,48)),
        'UPPER_LIP' : list(range(48,55)),
        'BOTTOM_LIP' : list(range(55,61)),
        'TEETH' : list(range(61,68)),
    }
    LEFT_FACE_SIDE, REIGHT_FACE_SIDE = left_face_side_68_points(landmarks_68_points)
    landmarks_68_points['LEFT_FACE_SIDE'] = LEFT_FACE_SIDE
    landmarks_68_points['REIGHT_FACE_SIDE'] = REIGHT_FACE_SIDE
    symmetry = {}
    return landmarks_68_points, symmetry
    

def get_info_106_points():
    landmarks_106_points = {
        'CONTOURS' : list(range(33)),
        'LEFT_EYEBROWN' : list(range(33,42)),
        'REIGHT_EYEBROWN' : list(range(42,51)),
        'NOSE_POINTS' : list(range(51,66)),
        'NOSE_LINE_POINTS' : list(range(51,55)),
        'LEFT_EYE' : list(range(66,75)),
        'REIGHT_EYE' : list(range(75,84)),
        'UPPER_LIP' : list(range(84,91)),
        'BOTTOM_LIP' : list(range(91,96)),
        'TEETH' : list(range(96,104)),
        'EYE' : list(range(104,106)),
    }
    LEFT_FACE_SIDE, REIGHT_FACE_SIDE = left_face_side_106_points(landmarks_106_points)
    landmarks_106_points['LEFT_FACE_SIDE'] = LEFT_FACE_SIDE
    landmarks_106_points['REIGHT_FACE_SIDE'] = REIGHT_FACE_SIDE
    symmetry = landmarks_106_symmetry(landmarks_106_points)
    return landmarks_106_points, symmetry


def get_info_468_points():
    
    
    lips = np.array(list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LIPS)).flatten())))
    up = lips[[0,1,2, 10, 12, 13, 14, 15,  26,22]]
    down = lips[[6, 8, 39, 9, 18, 23, 28, 34, 37]]
    teeth = lips[[4, 5, 7, 16, 19,17, 20, 21, 24, 25, 27, 29, 30, 33, 35, 36, 38 , 31, 32,11]]
    
    nose_line = [1,2,4,5, 6, 19, 195, 197, 94]
    nose_R = [196, 174, 217, 3, 236, 51, 134, 198, 126, 209, 131, 45, 220,
              115, 49, 102, 48, 44, 238, 20, 241, 242, 125, 141, 239, 237, 218]
    nose_L = [419, 399, 437, 248, 456, 281, 363 , 420, 355, 429, 360, 275, 440, 
              344, 279, 278, 294, 274, 458, 250, 461, 462, 354, 370, 459, 309, 438]
    
    landmarks_468_points = {
        'CONTOURS' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_FACE_OVAL)).flatten())), 
        'LEFT_EYEBROWN' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LEFT_EYEBROW)).flatten())),
        'REIGHT_EYEBROWN' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_RIGHT_EYEBROW)).flatten())),
        'NOSE_POINTS' : nose_R  + nose_L + nose_line, 
        'NOSE_LINE_POINTS' : nose_line, 
        'LEFT_EYE' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LEFT_EYE)).flatten())), 
        'REIGHT_EYE' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_RIGHT_EYE)).flatten())),  
        'UPPER_LIP' : up, 
        'BOTTOM_LIP' : down, 
        'TEETH' : teeth, 
    }
    #LEFT_FACE_SIDE, REIGHT_FACE_SIDE = left_face_side_106_points(landmarks_106_points)
    #landmarks_468_points['LEFT_FACE_SIDE'] = LEFT_FACE_SIDE
    #landmarks_468_points['REIGHT_FACE_SIDE'] = REIGHT_FACE_SIDE
    symmetry = {}
    return landmarks_468_points, symmetry
                         

def add_to_sym(symmetry, temp_reight, temp_left, reverse = True):
    temp = list(temp_reight)
    if reverse:
        temp.reverse()
    temp_left = temp_left
    for i in range(len(temp_left)):
        symmetry[temp_left[i]] = temp[i]
        symmetry[temp[i]] = temp_left[i]
    return symmetry

def left_face_side_106_points(landmarks): 
    LEFT_FACE_SIDE =  landmarks['LEFT_EYEBROWN'] +\
        landmarks['CONTOURS'][:int(len(landmarks['CONTOURS'])/2)+1] +\
        landmarks['TEETH'][int(len(landmarks['TEETH'])*3/4):] + \
        landmarks['TEETH'][:int(len(landmarks['TEETH'])*1/4 + 1)] +\
        landmarks['UPPER_LIP'][:int(len(landmarks['UPPER_LIP'])*1/2 + 1)] + \
        landmarks['BOTTOM_LIP'][int(len(landmarks['BOTTOM_LIP'])*1/2):] + \
        landmarks['LEFT_EYE'] + [landmarks['EYE'][0]] +  landmarks['NOSE_POINTS'][:int(len(landmarks['NOSE_POINTS'])/2)+3]
    
    REIGHT_FACE_SIDE =  landmarks['REIGHT_EYEBROWN'] +\
        landmarks['CONTOURS'][int(len(landmarks['CONTOURS'])/2):] +\
        landmarks['TEETH'][int(len(landmarks['TEETH'])*1/4):int(len(landmarks['TEETH'])*3/4)+1] + \
        landmarks['UPPER_LIP'][int(len(landmarks['UPPER_LIP'])*1/2):] + \
        landmarks['BOTTOM_LIP'][:int(len(landmarks['BOTTOM_LIP'])*1/2)+1] + \
        landmarks['REIGHT_EYE'] + [landmarks['EYE'][1]] + landmarks['NOSE_LINE_POINTS'] + \
        landmarks['NOSE_POINTS'][int(len(landmarks['NOSE_POINTS'])/2)+2:]
    return LEFT_FACE_SIDE, REIGHT_FACE_SIDE


def left_face_side_68_points(landmarks): 
    LEFT_FACE_SIDE =  landmarks['LEFT_EYEBROWN'] +\
        landmarks['CONTOURS'][:int(len(landmarks['CONTOURS'])/2)+1] +\
        landmarks['TEETH'][int(len(landmarks['TEETH'])*3/4):] + \
        landmarks['TEETH'][:int(len(landmarks['TEETH'])*1/4 + 1)] +\
        landmarks['UPPER_LIP'][:int(len(landmarks['UPPER_LIP'])*1/2 + 1)] + \
        landmarks['BOTTOM_LIP'][int(len(landmarks['BOTTOM_LIP'])*1/2):] + \
        landmarks['LEFT_EYE'] +  landmarks['NOSE_POINTS'][:int(len(landmarks['NOSE_POINTS'])/2)+3]
    
    REIGHT_FACE_SIDE =  landmarks['REIGHT_EYEBROWN'] +\
        landmarks['CONTOURS'][int(len(landmarks['CONTOURS'])/2):] +\
        landmarks['TEETH'][int(len(landmarks['TEETH'])*1/4):int(len(landmarks['TEETH'])*3/4)+1] + \
        landmarks['UPPER_LIP'][int(len(landmarks['UPPER_LIP'])*1/2):] + \
        landmarks['BOTTOM_LIP'][:int(len(landmarks['BOTTOM_LIP'])*1/2)+1] + \
        landmarks['REIGHT_EYE'] + landmarks['NOSE_LINE_POINTS'] + \
        landmarks['NOSE_POINTS'][int(len(landmarks['NOSE_POINTS'])/2)+2:]
    return LEFT_FACE_SIDE, REIGHT_FACE_SIDE

def left_face_side_408_points(landmarks): 
    sym_line = [0,1,2,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19]



def landmarks_106_symmetry(landmarks):
    symmetry = {}
    for i in range(int(len(landmarks['CONTOURS'])/2)+1):
        symmetry[landmarks['CONTOURS'][i]] = landmarks['CONTOURS'][-i-1]
        symmetry[landmarks['CONTOURS'][-i-1]] = landmarks['CONTOURS'][i]


    symmetry = add_to_sym(symmetry, landmarks['REIGHT_EYEBROWN'][:5], landmarks['LEFT_EYEBROWN'][:5])
    symmetry = add_to_sym(symmetry, landmarks['REIGHT_EYEBROWN'][5:], landmarks['LEFT_EYEBROWN'][5:])
    symmetry = add_to_sym(symmetry, landmarks['REIGHT_EYE'][:5], landmarks['LEFT_EYE'][:5])
    symmetry = add_to_sym(symmetry, landmarks['REIGHT_EYE'][5:8], landmarks['LEFT_EYE'][5:8])
    symmetry = add_to_sym(symmetry, landmarks['NOSE_POINTS'][4:9], landmarks['NOSE_POINTS'][10:])
    symmetry = add_to_sym(symmetry, landmarks['NOSE_POINTS'][:4] + landmarks['NOSE_POINTS'][9:10], landmarks['NOSE_POINTS'][:4] + \
                          landmarks['NOSE_POINTS'][9:10], False)
    symmetry = add_to_sym(symmetry, landmarks['UPPER_LIP'][:3], landmarks['UPPER_LIP'][4:])
    symmetry = add_to_sym(symmetry, landmarks['BOTTOM_LIP'][:2], landmarks['BOTTOM_LIP'][3:])
    symmetry = add_to_sym(symmetry, landmarks['TEETH'][:2], landmarks['TEETH'][3:5])
    symmetry = add_to_sym(symmetry, landmarks['TEETH'][5:7], landmarks['TEETH'][6:])
    symmetry[landmarks['TEETH'][2]] = landmarks['TEETH'][2]
    symmetry[landmarks['BOTTOM_LIP'][2]] = landmarks['BOTTOM_LIP'][2]
    symmetry[landmarks['UPPER_LIP'][3]] = landmarks['UPPER_LIP'][3]
    symmetry[landmarks['LEFT_EYE'][8]] = landmarks['REIGHT_EYE'][8]
    symmetry[landmarks['REIGHT_EYE'][8]] = landmarks['LEFT_EYE'][8]
    symmetry[landmarks['EYE'][0]] = landmarks['EYE'][1]
    symmetry[landmarks['EYE'][1]] = landmarks['EYE'][0]
    
    return symmetry

class Landmarks():
    
    def __init__(self, landmarks_array):
        self.landmarks_array = landmarks_array
        self.base_information()
        
    
    def base_information(self):
        if len(self.landmarks_array) == 106:
            self.points_info, self.symmetry = get_info_106_points()
            self.symmetry_line = [i for i in self.symmetry.keys() if i == self.symmetry[i]]
        elif len(self.landmarks_array) == 68:
            self.points_info, self.symmetry = get_info_68_points()
        elif len(self.landmarks_array) == 468:
            self.points_info, self.symmetry = get_info_468_points()

    def __call__(self):
        return self.landmarks_array
    