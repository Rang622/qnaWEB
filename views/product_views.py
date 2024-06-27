from flask import Blueprint, render_template
from ..models import Product

bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/')
def product_list():
    products = Product.query.all()
    return redirect(url_for('product.products'), product=product)


@bp.route('/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return redirect(url_for('product.product_detail'), product=product)
