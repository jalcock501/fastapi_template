""" __main__.py """
import uvicorn
from {{cookiecutter.project_slug}}.api import app


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='{{cookiecutter.server_host}}',
        port={{cookiecutter.server_port}}
    )
