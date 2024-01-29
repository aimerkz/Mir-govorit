FROM python:3.10.12-slim
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
WORKDIR /mir-govorit
COPY poetry.lock pyproject.toml /mir-govorit/
RUN pip install --upgrade --no-cache-dir pip==23.1.2 && \
    pip install -U --no-cache-dir poetry==1.7.1 && \
    poetry config --local virtualenvs.create false && \
    poetry install
COPY . /mir-govorit/
RUN chmod a+x /mir-govorit/docker-entrypoint.sh
ENTRYPOINT ["/mir-govorit/docker-entrypoint.sh"]
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000" ]
