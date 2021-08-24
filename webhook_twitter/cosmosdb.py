from azure.cosmos import CosmosClient, exceptions
import logging
import os

url = os.environ['COSMOS_ACCOUNT_URI']
key = os.environ['COSMOS_ACCOUNT_KEY']
client = CosmosClient(url, credential=key)

'''
参考: 
https://docs.microsoft.com/en-us/python/api/overview/azure/cosmos-readme?view=azure-python
https://docs.microsoft.com/en-us/python/api/azure-cosmos/azure.cosmos?preserve-view=true&view=azure-python

'''

def list_databases(client):
    logging.info("\n4. List all Databases on an account")

    logging.info('Databases:')

    databases = list(client.list_databases())

    if not databases:
        return

    for database in databases:
        logging.info(database['id'])

def list_Containers(db):
    logging.info("\n5. List all Container in a Database")

    logging.info('Containers:')

    containers = list(db.list_containers())

    if not containers:
        return

    for container in containers:
        logging.info(container['id'])

def get_database(client, id):
    logging.info("Get a Database by id")
    try:
        database = client.get_database_client(id)
        logging.info('Database with id \'{0}\' was found, it\'s link is {1}'.format(id, database.database_link))
        return database

    except exceptions.CosmosResourceNotFoundError:
        logging.info('A database with id \'{0}\' does not exist'.format(id))

def get_Container(db, id):
    logging.info("Get a Container by id")
    try:
        container = db.get_container_client(id)
        logging.info('Container with id \'{0}\' was found, it\'s link is {1}'.format(container.id, container.container_link))
        return container

    except exceptions.CosmosResourceNotFoundError:
        logging.info('A container with id \'{0}\' does not exist'.format(id))


def create_items(container, body):
    logging.info('Creating Items')
    container.create_item(body=body)

def upsert_items(container, body):
    logging.info('Creating Items')
    container.upsert_item(body=body)


def read_allItems(container):
    logging.info('Reading all items')
    items = container.read_all_items(max_item_count=50)
    list_items = list(items)
    logging.info(f'{len(list_items)} items have been found.' )
    return list_items


def query_items(container, doc_id):
    logging.info('\n1.4 Querying for an  Item by Id\n')

    # enable_cross_partition_query should be set to True as the container is partitioned
    items = list(container.query_items(
        query="SELECT * FROM r WHERE r.id=@id",
        parameters=[
            { "name":"@id", "value": doc_id }
        ],
        enable_cross_partition_query=True
    ))
    logging.info('Item queried by Id {0}'.format(items[0].get("id")))
    return items

def insert_tweet(tweet):
    '''
    tweet: tweet in json format
    '''
    db = get_database(client, "fukurousaboten")
    tweet_container = get_Container(db, "tweet")
    if tweet['tweet_create_events']:
        tweet['id'] = str(tweet['tweet_create_events'][0]['id'])
        logging.info ('Tweet ID {} is being stored in DB'.format(tweet['id']))
        create_items(tweet_container, tweet)
        logging.info ('Tweet ID {} has been stored in DB'.format(tweet['id']))

def insert_fukurou_info(row):
    '''
    tweet: tweet in json format
    '''
    db = get_database(client, "fukurousaboten")
    fukurou_container = get_Container(db, "fukurou-info")
    if row['id']:
        logging.info ('fukurou ID {} is being stored in DB'.format(row['id']))
        upsert_items(fukurou_container, row)
        logging.info ('Tweet ID {} has been stored in DB'.format(row['id']))
    
def read_all_fukurou_info():
    db = get_database(client, "fukurousaboten")
    fukurou_container = get_Container(db, "fukurou-info")
    return read_allItems(fukurou_container)

def get_fukuro_info(id):
    db = get_database(client, "fukurousaboten")
    fukurou_container = get_Container(db, "fukurou-info")
    items = query_items(fukurou_container, id)
    if len(items) == 1:
        return items[0]
    else:
        return None
    

def get_fukuro_info(id):
    db = get_database(client, "fukurousaboten")
    fukurou_container = get_Container(db, "fukurou-info")
    items = query_items(fukurou_container, id)
    if len(items) == 1:
        return items[0]
    else:
        return None

def get_tweet(id):
    db = get_database(client, "fukurousaboten")
    tweet_container = get_Container(db, "tweet")
    items = query_items(tweet_container, id)
    if len(items) == 1:
        return items[0]
    else:
        return None
