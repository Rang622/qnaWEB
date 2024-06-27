from flask import Blueprint, url_for
from werkzeug.utils import redirect
from ..models import Product

# Blueprint 객체 생성
bp = Blueprint('main', __name__, url_prefix='/')

# 홈페이지 라우트
@bp.route('/')
def home():
    return redirect(url_for('product.home'))


# 제품 목록 페이지 라우트
@bp.route('/products')
def products():
    # 모든 제품을 데이터베이스에서 조회
    product_list = Product.query.all()
    return redirect(url_for('product.products'))


# 제품 상세 페이지 라우트
@bp.route('/products/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return redirect(url_for(''))


