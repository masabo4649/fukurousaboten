
def insert_fukurou_info():
    import json
    from webhook_twitter import cosmosdb

    '''
    fukurou-info.jsonを、cosmosdbに投入する。
    '''

    json_open = open('fukurou-info.json', 'r')
    json_load = json.load(json_open)

    for row in json_load:
        cosmosdb.insert_fukurou_info(row)

    insertedItems = cosmosdb.read_all_fukurou_info()
    print (f'{len(insertedItems)} have been inserted/upserted.')

if __name__ == "__main__":

    from testtools import local_settings_helper as helper

    helper.import_to_env()
    
    insert_fukurou_info()
