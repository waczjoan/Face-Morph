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
    landmarks_468_points = {
        'CONTOURS' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_FACE_OVAL)).flatten())), 
        'LEFT_EYEBROWN' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LEFT_EYEBROW)).flatten())),
        'REIGHT_EYEBROWN' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_RIGHT_EYEBROW)).flatten())),
        'NOSE_POINTS' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LIPS)).flatten())), #####
        'NOSE_LINE_POINTS' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LIPS )).flatten())), #####
        'LEFT_EYE' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LEFT_EYE)).flatten())), 
        'REIGHT_EYE' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_RIGHT_EYE)).flatten())),  
        'UPPER_LIP' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LIPS)).flatten())), #####
        'BOTTOM_LIP' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LIPS)).flatten())), #####
        'TEETH' : list(set(np.array(list(mp.solutions.face_mesh.FACEMESH_LIPS)).flatten())), ########
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
    