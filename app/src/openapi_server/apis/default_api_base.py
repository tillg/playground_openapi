# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.error import Error
from openapi_server.models.new_pet import NewPet
from openapi_server.models.pet import Pet


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    def add_pet(
        self,
        new_pet: NewPet,
    ) -> Pet:
        """Creates a new pet in the store.  Duplicates are allowed"""
        ...


    def delete_pet(
        self,
        id: int,
    ) -> None:
        """deletes a single pet based on the ID supplied"""
        ...


    def find_pet_by_id(
        self,
        id: int,
    ) -> Pet:
        """Returns a user based on a single ID, if the user does not have access to the pet"""
        ...


    def find_pets(
        self,
        tags: List[str],
        limit: int,
    ) -> List[Pet]:
        """Returns all pets from the system that the user has access to """
        ...
