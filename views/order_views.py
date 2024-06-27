from flask import Blueprint, render_template, session
from ..models import Order  # 가정: 주문 모델이 정의되어 있음

bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/')
def order_list():
    # 사용자의 주문 목록을 조회하는 로직
    # orders = Order.query.filter_by(user_id=session['user_id']).all()
    return redirect(url_for('carts.index'))

