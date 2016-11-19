import crawlermain
import dbhandler
import json

if __name__ == '__main__':
    # print('\nmission craw start...')
    obj_crawler = crawlermain.CrawlerMain()
    data_today = obj_crawler.craw()
    # print('    data crawed:\n    ', data_today)
    # print('mission craw end...\n')
    # print('mission db start...')
    obj_db = dbhandler.DbHandler()
    obj_db.db_task(data_today)
    info_today = obj_db.query_new()
    info_query = obj_db.query('2019-10-26')
    obj_db.close_db()
    # print('mission db end...')
    print('*' * 16, 'job info unread:', '*' * 16)
    for item in info_today:
        # print("%-20s%-100s%100s" % (item[2],item[1], item[0]))
        print('{:<20}{:<40}{:>100}'.format(item[2], item[1], item[0]))
    print('*' * 16, 'have a nice day ', '*' * 16)
    # print('=' * 50)
    # print('=' * 50)
    # print('=' * 50)
    # print('*' * 16, 'job info queried:', '*' * 16)
    # for item in info_query:
    #     # print("%-20s%-100s%100s" % (item[2],item[1], item[0]))
    #     print('{:<20}{:<40}{:>100}'.format(item[2], item[1], item[0]))
    # print('*' * 16, 'have a nice day ', '*' * 16)
