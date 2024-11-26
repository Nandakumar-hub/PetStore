from PyTest.framework.api_requests import create_pet, get_pet, update_pet, delete_pet

#encapsulate API's to use in test
class PetStoreAPI:
    def __init__(self, pet_id, pet_name):
        #store pet id
        self.pet_id = pet_id
        #store pet name
        self.pet_name = pet_name

    def create(self):
        #calls create_pet from api_requests
        return create_pet(self.pet_id, self.pet_name)

    def get(self):
        #calls get_pet from api_requests
        return get_pet(self.pet_id)

    def update(self, new_pet_name):
        #calls update_pet from api_requests
        return update_pet(self.pet_id, new_pet_name)

    def delete(self):
        #calls delete_pet from api_requests
        return delete_pet(self.pet_id)