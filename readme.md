# playground-openapi

Trying to generate code based on oepnAPI definbitions.

## 2024-02-12 Experimenting 

* [Generate Python FastAPI Server from OpenApi file - Medium, Oct 2023](https://medium.com/@georgedimitropulos/generate-python-fastapi-server-from-openapi-file-099bfa944d3b)
* Using the [PetSHop Example](https://github.com/GeorgeDimi/FastAPI_OpenAPI/tree/main/open_api)

Could not fix error with an experimental sring handling switch:

```bash
TypeError: __init__() got an unexpected keyword argument 'experimental_string_processing'
```

* Switched over to read thru [Must Read! OpenAPI Generator Tutorial (Practical) - ApiDog Blog](https://apidog.com/blog/openapi-generator-tutorial/) and tried to run 

```bash
openapi-generator generate -i pet_shop_api.json -g python-fastapi -o app
```

This generated code, but I failed to install the reqiurements of the generated code: `Getting requirements to build wheel ... error`

This tip solved it: [Getting requirements to build wheel did not run successfully exit code: 1](https://discuss.python.org/t/getting-requirements-to-build-wheel-did-not-run-successfully-exit-code-1/30365):
* `echo "Cython<3" > cython_constraint.txt`
* ` PIP_CONSTRAINT=cython_constraint.txt pip3 install -r requirements.txt`
* I have no clue what it does, but it builds

⚡️ Running the project doesn't work:
```bash
> uvicorn main:app --host 0.0.0.0 --port 8080
ERROR:    Error loading ASGI app. Could not import module "main".
```
