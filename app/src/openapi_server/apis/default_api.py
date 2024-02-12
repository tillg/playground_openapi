# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.error import Error
from openapi_server.models.new_pet import NewPet
from openapi_server.models.pet import Pet


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/pets",
    responses={
        200: {"model": Pet, "description": "pet response"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def add_pet(
    new_pet: NewPet = Body(None, description="Pet to add to the store"),
) -> Pet:
    """Creates a new pet in the store.  Duplicates are allowed"""
    return BaseDefaultApi.subclasses[0]().add_pet(new_pet)


@router.delete(
    "/pets/{id}",
    responses={
        204: {"description": "pet deleted"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def delete_pet(
    id: int = Path(None, description="ID of pet to delete"),
) -> None:
    """deletes a single pet based on the ID supplied"""
    return BaseDefaultApi.subclasses[0]().delete_pet(id)


@router.get(
    "/pets/{id}",
    responses={
        200: {"model": Pet, "description": "pet response"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def find_pet_by_id(
    id: int = Path(None, description="ID of pet to fetch"),
) -> Pet:
    """Returns a user based on a single ID, if the user does not have access to the pet"""
    return BaseDefaultApi.subclasses[0]().find_pet_by_id(id)


@router.get(
    "/pets",
    responses={
        200: {"model": List[Pet], "description": "pet response"},
        200: {"model": Error, "description": "unexpected error"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def find_pets(
    tags: List[str] = Query(None, description="tags to filter by", alias="tags"),
    limit: int = Query(None, description="maximum number of results to return", alias="limit"),
) -> List[Pet]:
    """Returns all pets from the system that the user has access to """
    return BaseDefaultApi.subclasses[0]().find_pets(tags, limit)
