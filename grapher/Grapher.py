import io

import boto3
import numpy as np
import matplotlib.pyplot as plt

from grapher.dynamodb.db import get_hot_course_data
from grapher.s3.S3Helper import store_file

hot_course_img_name = "pop_course.png"

def get_hot_courses():
    return get_hot_course_data()

def make_dict_for_draw(courses):
    '''
    This function gets the course lists from dynamoDB and convert them to dictionary for statistical analysis
    :courses: course list
    :return: dictionary
    '''
    # sorted(courses, key=lambda x: x.count, reverse=True)
    dict = {}
    for c in courses:
        # sum(p.code == "F" for p in courses)
        if c.code in dict:
            dict[c.code] = dict[c.code] + 1
        else:
            dict[c.code] = 1 # start with 1
    return dict

def draw(dictionary):
    '''
    This function impliments numpy to generate the statistical result and generate a result diagram with
    '''
    dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
    dictionary = dict(list(dictionary.items())[0: 12])
    y_pos = np.arange(len(dictionary))
    plt.figure()
    plt.barh(y_pos, dictionary.values())
    plt.gca().invert_yaxis()
    plt.yticks(y_pos, dictionary.keys())
    plt.ylim(len(dictionary), -1)
    index = 0
    for a in dictionary:
        plt.annotate(dictionary[a], xy=(dictionary[a] + 0.01, y_pos[index] + 0.01))
        index += 1
    plt.xlabel("Searched Frequency")
    plt.ylabel("Course Code")
    plt.rc('xtick')
    plt.rc('ytick')
    # plt.title("Most Popular Courses Searched in the Past 48 hours", color='b')

    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    return img_data


def main():
    courses = get_hot_courses()
    dict = make_dict_for_draw(courses)
    print(dict)
    img = draw(dict)
    store_file(hot_course_img_name, img)

main()
