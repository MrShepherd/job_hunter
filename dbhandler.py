import json
import sqlite3
from datetime import datetime


class DbHandler(object):
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.flag = {"flag": "no", "today": "1990-01-01"}
        self.flag_file = "flag.json"
        self.today = datetime.now().strftime('%Y-%m-%d')

    def if_in_db(self, tmp_md5_str):
        return (tmp_md5_str,) in self.query_all_md5()

    def save_into_all(self, tmp_list):
        for tmp_dict in tmp_list:
            # print(tmp_dict)
            if not self.if_in_db(tmp_dict['md5']):
                # print(tmp_dict, '\n')
                self.cursor.execute("insert into job_info values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    tmp_dict['job_link'], tmp_dict['job'], tmp_dict['job_company'], tmp_dict['job_department'], tmp_dict['job_location'], tmp_dict['date'], tmp_dict['md5'], tmp_dict['etl_date']))
        self.conn.commit()

    def save_into_today(self, tmp_list):
        with open(self.flag_file, 'r') as fread:
            self.flag = json.load(fread)
        if self.flag['flag'] == 'no' or self.flag['today'] == self.today:
            self.initial_table('job_info_today')
            for tmp_dict in tmp_list:
                # print(tmp_dict)
                if not self.if_in_db(tmp_dict['md5']):
                    self.cursor.execute("insert into job_info_today values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        tmp_dict['job_link'], tmp_dict['job'], tmp_dict['job_company'], tmp_dict['job_department'], tmp_dict['job_location'], tmp_dict['date'], tmp_dict['md5'], tmp_dict['elt_date']))
            flag = {'flag': 'yes', 'today': self.today}
            with open(self.flag_file, 'w') as fwrite:
                json.dump(flag, fwrite)
            self.conn.commit()

    def query_all_md5(self):
        self.cursor.execute('SELECT md5 FROM job_info')
        return self.cursor.fetchall()

    def query_new(self):
        self.cursor.execute("SELECT * FROM job_info WHERE etl_date='%s'" % self.today)
        return self.cursor.fetchall()

    def query(self, date):
        self.cursor.execute("SELECT * FROM job_info WHERE etl_date='%s'" % date)
        return self.cursor.fetchall()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def initial_table(self, table_name):
        self.cursor.execute("delete  from '%s'" % table_name)
        self.conn.commit()

    def reset_flag(self):
        with open(self.flag_file, 'w') as fwrite:
            json.dump(self.flag, fwrite)

    def db_task(self, data_list):
        # print('    db connect successfully')
        self.reset_flag()
        # self.initial_table('job_info')
        # self.initial_table('job_info_today')
        # print('    initial successfully')
        # self.save_into_today(data_list)
        # print('    update today\'s job info successfully')
        self.save_into_all(data_list)
        # print('    save data into job_info successfully')
