""" api generator file """

import os
from fastapi import FastAPI
import {{ cookiecutter.project_slug }}.endpoints.root as root

app = FastAPI(
    title=os.getenv('FASTAPI_TITLE', '{{ cookiecutter.fastapi_title }}'),
    description=os.getenv('FASTAPI_DESC', '{{ cookiecutter.fastapi_desc }}'),
    version=os.getenv('VERSION', '{{ cookiecutter.fastapi_version }}'))
app.include_router(root.router)
