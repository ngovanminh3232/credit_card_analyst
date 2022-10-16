import math
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
print("Setup Complete")
# Cách dùng:
# pip install streamlit
# run file: tại termial, chạy lệnh streamlit run client_streamlit.py

st.title("Project")

train_df = pd.read_csv('../../train.csv')
train_df = train_df.head(1000)


def get_sum_people_by_item(df, item, age):
    sum = 0
    for i in range(len(df)):
        if df["Age"].iloc[i] // -365.25 == age and df[item].iloc[i] == 'Y':
            sum += 1
    return sum


list_age = (train_df["Age"].to_numpy() // -365.25).tolist()
list_age_unique = np.unique(list_age)
list_age_unique = list(map(int, list_age_unique))

# plot age and cars
sum = [get_sum_people_by_item(train_df, "Has a car", i)
       for i in list_age_unique]


def age_and_cars_plot():
    fig = plt.figure(figsize=(16, 6))
    plt.title("Độ tuổi sở hữu xe hơi", fontsize=14)
    plt.xlabel("Tuổi", fontsize=14)
    plt.ylabel("Số người sở hữu xe hơi", fontsize=14)
    sns.barplot(x=list_age_unique, y=sum)
    st.pyplot(fig)


# plot age and property
sum = [get_sum_people_by_item(train_df, "Has a property", i)
       for i in list_age_unique]

# plot


def age_and_property():
    fig = plt.figure(figsize=(16, 6))
    plt.title("Độ tuổi sở hữu tài sản", fontsize=14)
    plt.xlabel("Tuổi", fontsize=14)
    plt.ylabel("Số người sở hữu tài sản", fontsize=14)
    sns.barplot(x=list_age_unique, y=sum)
    st.pyplot(fig)

# age and income


def get_average_income_by_age(df, age):
    sum = 0
    count = 0
    for i in range(len(df)):
        if df["Age"].iloc[i] // -365.25 == age:
            sum += df["Income"].iloc[i]
            # print(df.loc[i, "Income"])
            count += 1
    return sum / count


sum = [get_average_income_by_age(train_df, i) for i in list_age_unique]
# plot


def age_and_income():

    fig = plt.figure(figsize=(16, 6))
    plt.title("Độ tuổi và thu nhập", fontsize=14)
    plt.xlabel("Tuổi", fontsize=14)
    plt.ylabel("Mức thu nhập trung bình", fontsize=14)
    sns.barplot(x=list_age_unique, y=sum)
    st.pyplot(fig)

# job and income


# def get_average_income_by_job(df, job):
#     sum = 0
#     count = 0
#     for i in range(len(df)):
#         if df["Job title"].iloc[i] == job:
#             sum += df["Income"].iloc[i]
#             # print(df.loc[i, "Income"])
#             count += 1
#     # print(sum)
#     # # print(count)
#     return sum / count


# job_title = train_df.groupby(["Job title"])["Job title"].size()
# print(job_title.index)
# sum = [get_average_income_by_job(train_df, i) for i in job_title.index]
# # plot


# def jobs_and_income():
#     fig = plt.figure(figsize=(16, 6))
#     plt.title("Ngành nghề và thu nhập")
#     plt.xlabel("Ngành nghề")
#     plt.ylabel("Mức thu nhập trung bình")
#     chart = sns.barplot(x=job_title.index, y=sum)
#     chart.set_xticklabels(chart.get_xticklabels(),
#                           rotation=45, horizontalalignment='right')
#     st.pyplot(fig)

# Scatter plot
def scatter_gender_income():
    fig = plt.figure(figsize=(16, 6))
    plt.title("Phân bố thu nhập theo độ tuổi, giới tính")
    plt.xlabel("Tuổi")
    plt.ylabel("Mức thu nhập")
    sns.scatterplot(x=list_age, y=train_df.Income, hue=train_df.Gender)
    st.pyplot(fig)

# scatter age and education


def scatter_age_edu_income():
    fig = plt.figure(figsize=(10, 6))
    plt.title("Phân bố thu nhập theo độ tuổi, học vấn")
    plt.xlabel("Tuổi")
    plt.ylabel("Mức thu nhập trung bình")
    sns.scatterplot(x=list_age, y=train_df.Income,
                    hue=train_df["Education level"])
    st.pyplot(fig)
# scatter age, marital, income


def scatter_age_marita_income():
    fig = plt.figure(figsize=(10, 6))
    plt.title("Phân bố thu nhập theo độ tuổi, tình trang hôn nhân")
    plt.xlabel("Tuổi")
    plt.ylabel("Mức thu nhập trung bình")
    sns.scatterplot(x=list_age, y=train_df.Income,
                    hue=train_df["Marital status"])
    st.pyplot(fig)


# income and experience
new_data = train_df.copy()
new_data_satisfy = new_data[new_data["Employment length"] != 365243]
list_employment_length = (
    new_data_satisfy["Employment length"].to_numpy() // -365.25).tolist()


def scatter_income_exp():
    fig = plt.figure(figsize=(10, 6))
    plt.title("Phân bố thu nhập theo số năm làm việc")
    plt.xlabel("Số năm làm việc")
    plt.ylabel("Mức thu nhập trung bình")
    sns.scatterplot(x=list_employment_length, y=new_data_satisfy.Income)
    st.pyplot(fig)

# children and family member


def scatter_children():
    fig = plt.figure(figsize=(10, 6))
    plt.title("Tương quan giữa số con và số thành viên trong gia đình")
    plt.xlabel("Số con")
    plt.ylabel("Số thành viên trong gia đình")
    sns.regplot(x='Children count', y='Family member count',
                data=train_df, line_kws={'color': 'red'})
    st.pyplot(fig)


# corelation
new_data = train_df.copy()
new_data.drop(["Has a mobile phone", "STATUS", "dep_value",
              "Is high risk"], axis=1, inplace=True)


def relation():
    fig = plt.figure(figsize=(14, 8))
    sns.set_theme(style="white")
    corr = new_data.corr()
    heatmap = sns.heatmap(corr, annot=True, cmap="Blues", fmt='.1g')
    st.pyplot(fig)


if __name__ == '__main__':
    # age_and_cars_plot()
    # age_and_property()
    # age_and_income()
    # jobs_and_income()
    # scatter_gender_income()
    # scatter_age_edu_income()
    # scatter_age_marita_income()
    # scatter_income_exp()
    # scatter_children()
    relation()
