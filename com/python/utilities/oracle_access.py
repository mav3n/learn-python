import cx_Oracle
import urllib3
import json


# from joblib import Parallel, delayed
# import multiprocessing


def get_col2(col1):
    api_url = 'https://api.host.com/core_col2/v1/{}?key=abcd'.format(col1)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http = urllib3.PoolManager()
    core_col2_response = http.request('GET', api_url)

    if core_col2_response.status == 200:
        response_array = json.loads(core_col2_response.data.decode('utf-8'))
        if len(response_array) is not 0 and 'col2' in response_array:
            return response_array['col2']
        else:
            return None
    else:
        print('[!] HTTP {0} calling [{1}]'.format(core_col2_response.status, api_url))
        return None


def update_col2(col2, col1):
    cursor = db_connection.cursor()
    sql_update = "update TABLE_NAME set col2 = :col2 where col1 = :col1 and col2 is null"
    cursor.execute(sql_update, col2=col2, col1=col1)
    print("Updated  col2 as {} for col1 {}".format(col2, col1))
    db_connection.commit()
    cursor.close()


def process_data(col1):
    col2 = get_col2(col1)
    if col2 is not None:
        update_col2(col2, col1)
    else:
        print('[!] col2 is NULL for col1 {}'.format(col1))


# num_cores = multiprocessing.cpu_count()
# print("No. of Cores : {} ".format(num_cores))

# dsn_tns = cx_Oracle.makedsn('host', 'port', 'sid')
dsn_tns = cx_Oracle.makedsn('xyz.db_host.com', 'port', service_name='service_name')
db_connection = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)

select_query = 'select distinct COL2 from TABLE_NAME where COL2 is null'
select_cursor = db_connection.cursor()
select_cursor.execute(select_query)

# Parallel(n_jobs=num_cores)(delayed(process_data)(row[0]) for row in select_cursor)
data = select_cursor.fetchall()
print("No. of data entries found {}".format(len(data)))

for row in data:
    process_data(row[0])

db_connection.close()
