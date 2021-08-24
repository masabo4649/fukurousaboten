import logging
import base64
import hashlib
import hmac
import os
import json

def get_response(crc_token):
    logging.info('Python HTTP trigger function processed webhook_twitter CRC Check.')
    TWITTER_CONSUMER_SECRET = os.environ["TWITTER_CONSUMER_API_SECRET"]

    # creates HMAC SHA-256 hash from incomming token and your consumer secret

    byte_crc_token = bytearray(crc_token,"ASCII")
    byte_secret = bytearray(TWITTER_CONSUMER_SECRET, "ASCII")
    hmac_crc = hmac.new(byte_secret, msg=byte_crc_token, digestmod=hashlib.sha256)
    sha256_hash_digest = hmac_crc.digest()
    sha256_hash_base64 = base64.b64encode(sha256_hash_digest)
    sha256_hash_base64_decode = sha256_hash_base64.decode()

      # construct response data with base64 encoded hash
    response_json = {
        'response_token': 'sha256=' + sha256_hash_base64_decode
    }
    response_str = json.dumps(response_json)
    return response_str


