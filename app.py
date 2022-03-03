import time
import requests
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO, datefmt='%m/%d/%Y %H:%M:%S')

api_base_url = "http://127.0.0.1:8000"


def get_response():
    logging.info(f'Sending GET request to: {api_base_url}')
    response = requests.get(api_base_url)
    logging.info(f'Got response status code: {response.status_code}')
    logging.info(f'Got response body: {response.json()}')


def create_user():
    logging.info(f'Sending POST request')
    new_user = {"firstname": "Hugh", "lastname": "Gass", "age": "35"}

    response = requests.post(api_base_url + "/users/", json=new_user)
    logging.info(f'Got response status code: {response.status_code}')
    # logging.info(f'Got response body: {response.json()}')
#     TODO get and log response if app1 will return generated user_id


def test_fake_users():
    for id in range(1, 7):
        logging.info(f'Sending GET request')
        response = requests.get(api_base_url + "/users/" + str(id))
        logging.info(f'Got response status code: {response.status_code}')
        time.sleep(2)


if __name__ == '__main__':
    # get_response()
    # create_user()
    test_fake_users()
