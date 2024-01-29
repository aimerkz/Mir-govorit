#!/bin/bash -x

python3 manage.py migrate --noinput || exit 1
python3 manage.py collectstatic --noinput || exit 1

python3 manage.py loaddata fixtures/users.json && \
python3 manage.py loaddata fixtures/products.json && \
python3 manage.py loaddata fixtures/recipes.json && \
python3 manage.py loaddata fixtures/recipe_product.json || exit 1

exec "$@"
