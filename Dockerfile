FROM python:3.7 as base

# Configuration
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    APP_DIR=/src

# redis-tools package is required for after deployment tests
RUN apt-get update && apt-get install -y postgresql && \
    pip install poetry
RUN mkdir -p $APP_DIR
COPY ./src $APP_DIR

# Create src dir
WORKDIR $APP_DIR
RUN chmod 777 $APP_DIR
RUN poetry install
RUN poetry run python setup.py develop

# Install dependencies
# COPY --chown=user:user src/Pipfile src/Pipfile.lock src/setup.py $APP_DIR/
# RUN pipenv install --dev --system && python setup.py develop

CMD ./start.sh

EXPOSE 8000
