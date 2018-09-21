import datetime

import pytz


def transform_date(str_time):
    # new_str_time = str_time[0:19]
    new_date_time = datetime.datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    transformed_time = new_date_time.astimezone(pytz.timezone('GMT')).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    # print('转换后的时间为：',transformed_time)
    return transformed_time