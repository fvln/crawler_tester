FROM python:3-slim-bookworm

RUN pip install --no-cache-dir 'poetry'

# Copy only pyproject so thath the following stage is kept in cache event if we modify the source code
COPY ./pyproject.toml ./poetry.lock ./

# Create virtualenv at /venv in the project instead of ~/.cache/
# See https://stackoverflow.com/questions/68683913/docker-image-deploys-locally-but-fails-on-google-cloud-run
RUN poetry config virtualenvs.path /venv && \
    poetry install --no-cache --no-root -vv && \
    rm -rf /root/.cache/pypoetry/artifacts/*

COPY . .

ENTRYPOINT ["/bin/sh", "-c"]
CMD [ "poetry config virtualenvs.path /venv; poetry run gunicorn 'crawler_tester:create_app()'" ]
