import requests

from PyTest.framework import config
from PyTest.framework.logger import get_logger

# initialize logger
logger = get_logger()


# create newpet
def create_pet(pet_id, pet_name):
    response = requests.post(config.baseurl(), json={
        "id": pet_id,
        "category": {
            "id": pet_id,
            "name": pet_name
        },
        "name": pet_name,
        "photoUrls": [pet_name],
        "tags": [{
            "id": pet_id,
            "name": pet_name
        }],
        "status": "available"
    }, headers={"Content-Type": "application/json"}, auth=(config.authkey(), config.password()))
    # raise HTTPError if response code is 4xx/5xx series
    response.raise_for_status()
    return response.json()


# get the details of pet using its ID
def get_pet(pet_id):
    response = requests.get(config.baseurl() + pet_id, auth=(config.authkey(), config.password()))
    response.raise_for_status()
    return response.json()


# update an existing pet's details
def update_pet(pet_id, new_pet_name):
    response = requests.put(config.baseurl(), json={
        "id": pet_id,
        "category": {
            "id": pet_id,
            "name": new_pet_name
        },
        "name": new_pet_name,
        "photoUrls": [new_pet_name],
        "tags": [{
            "id": pet_id,
            "name": new_pet_name
        }],
        "status": "available"
    }, headers={"Content-Type": "application/json"}, auth=(config.authkey(), config.password()))

    response.raise_for_status()
    return response.json()


# delete a pet using its ID
def delete_pet(pet_id):
    response = requests.delete(config.baseurl() + pet_id, auth=(config.authkey(), config.password()))
    response.raise_for_status()
    return response.status_code
