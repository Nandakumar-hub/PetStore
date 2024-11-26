import pytest
from PyTest.framework.pet_store_api import PetStoreAPI
from PyTest.framework.setup_teardown import setup, teardown
from PyTest.framework.logger import get_logger

#initialize logger
logger = get_logger()

@pytest.fixture(scope="module", autouse=True)
def setup_teardown():
    setup()
    yield
    teardown()
#TC_1 to verify pet creation using PetStoreAPI
def test_create_pet():
    pet = PetStoreAPI("9753186420", "shadow")
    response = pet.create() #call create method to create a new pet
    createPet_ID = str(response['id']) #get the id from API response and change it to string datatype. We are passing the pet_id as string
    assert createPet_ID == "9753186420"
    logger.info(f"Test_01 Passed: POST response ID - {createPet_ID} matches the expected ID - 9753186420")

#TC_2 to verify retrieving pet details using PetStoreAPI
def test_get_pet():
    pet = PetStoreAPI("9753186420", "shadow")
    response = pet.get() #call get method to retrieve pet details
    name = response['name'] #get the name from API response
    assert name == "shadow"
    logger.info(f"Test_02 Passed: Get response of Pet name - {name} matches the expected name - shadow")

#TC_3 to verify updating a pet name details using PetStoreAPI
def test_update_pet():
    pet = PetStoreAPI("9753186420", "shadow")
    response = pet.update("Micky") #update the pet name to a new value
    updatedPetName = response['name'] #get the updated name from API response
    assert updatedPetName == "Micky", f"Assertion failed: Updated Pet name - {updatedPetName} does not match the expected name - Micky"

#TC_4 to verify deleting pet using PetStoreAPI
def test_delete_pet():
    pet = PetStoreAPI("9753186420", "shadow")
    status_code = pet.delete() #call delete method to remove the pet
    assert status_code == 200
    logger.info(f"Test_04 Passed: Pet record id: 9753186420 successfully deleted from server")
