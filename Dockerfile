FROM python:3.10.12-slim
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
WORKDIR /nova-test
COPY poetry.lock pyproject.toml /mir-govorit/
RUN pip install --upgrade --no-cache-dir pip==23.1.2 && \
    pip install -U --no-cache-dir poetry==1.7.1 && \
    poetry config --local virtualenvs.in-project true && \
    poetry install
RUN poetry check
COPY . .
