from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import User 
from .. import db

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # 로그인 처리 로직
    if request.method == 'POST':
        # 폼 데이터로부터 사용자 이름과 비밀번호 확인
        # 사용자 인증 로직 구현
        # 성공 시 홈 페이지로 리디렉션
        return redirect(url_for('product.home'))
    return redirect(url_for('auth.login'))

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    # 회원가입 처리 로직
    if request.method == 'POST':
        # 폼 데이터 처리 및 사용자 등록
        # 성공 시 로그인 페이지로 리디렉션
        return redirect(url_for('auth.login'))
    return  redirect(url_for('auth.signup'))
