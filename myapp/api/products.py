# -*- coding: utf-8 -*-
"""
    myapp.api.products
    ~~~~~~~~~~~~~~~~~~~~~

    Product endpoints
"""

from flask import Blueprint, request

from ..services import products
from . import route

bp = Blueprint('products', __name__, url_prefix='/products')


@route(bp, '/')
def list():
    """Returns a list of product instances."""
    return products.all()


@route(bp, '/', methods=['POST'])
def create():
    """Creates a new product. Returns the new product instance."""
    return products.create(**request.json)


@route(bp, '/<product_id>')
def show(product_id):
    """Returns a product instance."""
    return products.get_or_404(product_id)


@route(bp, '/<product_id>', methods=['PUT'])
def update(product_id):
    """Updates a product. Returns the updated product instance."""
    return products.update(products.get_or_404(product_id), **request.json)


@route(bp, '/<product_id>', methods=['DELETE'])
def delete(product_id):
    """Deletes a product. Returns a 204 response."""
    products.delete(products.get_or_404(product_id))
    return None, 204
