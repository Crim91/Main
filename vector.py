import math as m


def rotate(vector, angle):
    return [vector[0] * m.cos(angle) - vector[1] * (m.sin(angle)),
            vector[0] * m.sin(angle) + vector[1] * (m.cos(angle))]


def magnitude(vector):
    return m.sqrt(vector[0] * vector[0] + vector[1] * vector[1])


def magnitude_squared(vector):
    return vector[0] * vector[0] + vector[1] * vector[1]


def normalize(vector):
    length = magnitude(vector)
    if length > 0:
        return [vector[0] / length, vector[1] / length]
    else:
        return [0, 0]


def add(vector1, vector2):
    return [vector1[0] + vector2[0], vector1[1] + vector2[1]]


def subtract(vector1, vector2):
    return [vector1[0] - vector2[0], vector1[1] - vector2[1]]


def scale(vector, in_scale):
    return [vector[0] * in_scale, vector[1] * in_scale]


def add_scaled(vector1, vector2, in_scale):
    return [vector1[0] + (in_scale * vector2[0]), vector1[1] + (in_scale * vector2[1])]


def dot(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]


def prod(vector1, vector2):
    return [vector1[0] * vector2[0], vector1[1] * vector2[1]]


def cross2(vectora, vectorb):
    # ACTUAL MATHEMATICAL CALCULATION
    # vector1 = [vectora[0], vectora[1], 0]
    # vector2 = [vectorb[0], vectorb[1], 0]
    #
    # result = [vector1[1] * vector2[2] - vector1[2] * vector2[1],
    #           vector1[2] * vector2[0] - vector1[0] * vector2[2],
    #           vector1[0] * vector2[1] - vector1[1] * vector2[0]]
    # return result

    # EFFECTIVE RESULT IN 2D
    return vectora[0] * vectorb[1] - vectora[1] * vectorb[0]



def cross2sv(scalar, vector):
    # ACTUAL MATHEMATICAL CALCULATION
    # vector1 = [0, 0, scalar]
    # vector2 = [vector[0], vector[1], 0]
    #
    # result = [vector1[1] * vector2[2] - vector1[2] * vector2[1],
    #           vector1[2] * vector2[0] - vector1[0] * vector2[2]]
    #           vector1[0] * vector2[1] - vector1[1] * vector2[0]]

    # EFFECTIVE RESULT IN 2D
    return [- scalar * vector[1], scalar * vector[0]]
