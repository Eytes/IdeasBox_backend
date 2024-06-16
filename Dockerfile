ARG PYTHON_VERSION=3.12
ARG _PACKAGE_NAME=backend
ARG _USERNAME=ideabox_backend
ARG _SOURCE_CODE_PATH=./src


FROM python:$PYTHON_VERSION-slim as builder
ARG _PACKAGE_NAME
ARG _SOURCE_CODE_PATH
ENV PACKAGE_NAME=$_PACKAGE_NAME
ENV SOURCE_CODE_PATH=$_SOURCE_CODE_PATH

WORKDIR /$PACKAGE_NAME
RUN pip install --no-cache-dir --upgrade poetry
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt


FROM python:$PYTHON_VERSION-slim
ARG _PACKAGE_NAME
ARG _SOURCE_CODE_PATH
ARG _USERNAME
ENV PACKAGE_NAME=$_PACKAGE_NAME
ENV SOURCE_CODE_PATH=$_SOURCE_CODE_PATH
ENV USERNAME=$_USERNAME

RUN useradd -s /bin/bash $USERNAME
WORKDIR /$PACKAGE_NAME
COPY --from=builder /$PACKAGE_NAME/requirements.txt /$PACKAGE_NAME/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY $SOURCE_CODE_PATH/ ./
USER $USERNAME
EXPOSE 8000
CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0", "--proxy-headers"]
