import streamlit as st
import pandas as pd
import numpy as np

# Cách dùng:
# pip install streamlit
# run file: tại termial, chạy lệnh streamlit run client_streamlit.py

st.title("Welcome, Streamlit")


def get_input_user():
    # Gender
    gender = st.radio(
        "Giới tính",
        ("M", "F")
    )
    # Age
    age = st.number_input(
        "Tuổi", min_value=18, max_value=100, value=18, step=1
    )
    # Education level
    edu = st.selectbox(
        "Trình độ học vấn",
        ('Higher education', 'Incomplete higher', 'Lower secondary',
         'Secondary / secondary special')
    )
    # employment status
    employment_status = st.selectbox(
        "Tình trạng công việc",
        ('Commercial associate', 'Pensioner', 'State servant', 'Working')
    )

    employment_length = st.number_input(
        "Số năm làm việc", min_value=0.0, max_value=70.0, step=0.5, value=0.0
    )
    # Income
    income = st.number_input(
        "Thu nhập", min_value=0.0, max_value=1000000.0, step=1.0, value=0.0
    )
    job_title = st.selectbox(
        "Tên công việc",
        ('Accountants', 'Cleaning staff', 'Cooking staff', 'Core staff',
         'Drivers', 'HR staff', 'High skill tech staff', 'IT staff', 'Laborers',
         'Low-skill Laborers', 'Managers', 'Medicine staff',
         'Private service staff', 'Sales staff', 'Secretaries', 'Security staff',
         'Waiters/barmen staff')
    )

    # Marital status
    marital_status = st.selectbox(
        "Tình trạng hôn nhân",
        ('Civil marriage', 'Married', 'Separated', 'Single / not married',
         'Widow')
    )
    # Children count
    child_count = st.number_input(
        "Số con: ", min_value=0, max_value=20, step=1, value=0
    )
    # Member of family
    family_mem = st.number_input(
        "Số thành viên trong gia đình",
        min_value=0, max_value=30, value=2, step=1
    )
    # Dwelling
    dwelling = st.selectbox(
        "Nhà ở",
        ('House / apartment', 'Municipal apartment', 'Office apartment',
         'Rented apartment', 'With parents')
    )
    # has feature
    # has_car = get_has_feature("Có 1 xe ô tô")
    has_car = st.radio("Có 1 xe ô tô", (1, 0))
    has_property = st.radio("Có 1 tài sản", (1, 0))
    has_mobile = st.radio("Có 1 điện thoại di động", (1, 0))
    has_working_phone = st.radio("Có 1 điện thoại làm việc", (1, 0))
    has_phone = st.radio("Có 1 điện thoại", (1, 0))
    has_email = st.radio("Có 1 email", (1, 0))
    # Account age
    account_age = st.number_input(
        "Số năm tài khoản", min_value=0, max_value=70, step=1, value=0
    )
    user_information = {
        'gender': gender,
        'age': age,
        'education': edu,
        'employment status': employment_status,
        'employment length': employment_length,
        'Job title': job_title,
        'income': income,
        'marital status': marital_status,
        'children count': child_count,
        'family members': family_mem,
        'Dwelling': dwelling,
        'has car': has_car,
        'has property': has_property,
        'has mobile': has_mobile,
        'has working_phone': has_working_phone,
        'has phone': has_phone,
        'has email': has_email
    }
    if st.button('Dự đoán'):
        st.write(user_information)
        return user_information


get_input_user()
