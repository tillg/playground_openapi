# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.new_pet import NewPet  # noqa: F401
from openapi_server.models.pet import Pet  # noqa: F401


def test_add_pet(client: TestClient):
    """Test case for add_pet

    
    """
    new_pet = {"name":"name","tag":"tag"}

    headers = {
    }
    response = client.request(
        "POST",
        "/pets",
        headers=headers,
        json=new_pet,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_pet(client: TestClient):
    """Test case for delete_pet

    
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/pets/{id}".format(id=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_find_pet_by_id(client: TestClient):
    """Test case for find_pet_by_id

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/pets/{id}".format(id=1),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_find_pets(client: TestClient):
    """Test case for find_pets

    
    """
    params = [("tags", ['tags_example']),     ("limit", 56)]
    headers = {
    }
    response = client.request(
        "GET",
        "/pets",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

