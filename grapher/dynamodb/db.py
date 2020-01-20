import boto3

from grapher.Course import Course

timetablePath='database.csv'


def get_hot_course_data():
    '''
    This function gets all the hot course data from dynamo DB
    :return: list of results
    '''

    dynamodb_client = boto3.resource('dynamodb', region_name='us-east-1')

    my_table = dynamodb_client.Table('hot_course')

    result_item = []

    result_data = my_table.scan()

    result_item.extend(result_data['Items'])

    #rebuild the result to list of oject(course)

    result_list = []

    for item in result_item:
        code = item["code"]
        title = item["title"]
        semester = item["semester"]
        course_type = item["type"]
        category = item["category"]
        hcid = item["hcid"]
        insertion_time = item["insertion_time"]
        course = Course(code,title,semester,course_type,category,hcid,insertion_time)
        result_list.append(course)

    return result_list