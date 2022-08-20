import numpy as np
from numpy import cos,sin,pi,arccos

# def quaternion_rotate(v, axis, theta):
def quaternion_rotate(v, qu):
    """
    Args:
        v: 回転させるベクトル np.ndarray(3,1)
        qu: quaternion
    Returns:
        回転後のベクトル np.ndarray(3,1)
    """
    if qu[0] == 1: # u = (0,0,0)
        return v
    theta = 2*arccos(qu[0])
    axis = qu[1:]
    axis_norm = np.linalg.norm(axis)
    u = axis / axis_norm
    uv = np.dot(u, v)
    uxv = np.cross(u, v)
    return v*cos(theta) + (1 - cos(theta))*uv*u + sin(theta)*uxv

def to_quaternion(axis, angle):
    qu = np.zeros(4)
    qu[0] = cos(angle/2)
    u = axis/np.linalg.norm(axis)
    qu[1:] = u*np.sin(angle/2)
    return qu
