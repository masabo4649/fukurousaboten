
def test_():

    import webhook_twitter.twitter_crc_response as crc
    
    crc_token = "dummy"
    response = crc.get_response(crc_token)
    print(f"twitter_crc_response is executed. Response: {response}")

if __name__ == "__main__":
    from testtools import local_settings_helper as helper

    helper.import_to_env()
    
    test_()

    