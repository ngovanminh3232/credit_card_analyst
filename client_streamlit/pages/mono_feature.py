import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib
import seaborn as sns

st.title("Phân tích đơn biến")

train_df = pd.read_csv('../../train.csv')
# train_df = train_df.head(1000)

# Function trả về giá trị và tần số tương ứng của chúng


def value_count_norm_call(df, feature):
    frt_value_count = df[feature].value_counts()
    frt_value_count_norm = df[feature].value_counts(normalize=True) * 100
    frt_value_concat = pd.concat(
        [frt_value_count, frt_value_count_norm], axis=1)
    frt_value_concat.columns = ['Count', 'Frequency (%)']
    return frt_value_concat


def get_info(df, feature):
    if feature == 'Age':
        print('Description:\n{}'.format((np.abs(df[feature])/365).describe()))
        print('*'*50)
        print('Object type:{}'.format(df[feature].dtype))
    elif feature == 'Employment length':
        # chỉ chọn ra các người còn làm việc và bỏ qua những người đã nghỉ việc
        employment_len_no_ret = train_df['Employment length'][train_df['Employment length'] < 0]
        employment_len_no_ret_yrs = np.abs(employment_len_no_ret)/365
        print('Description:\n{}'.format((employment_len_no_ret_yrs).describe()))
        print('*'*50)
        print('Object type:{}'.format(employment_len_no_ret.dtype))
    elif feature == 'Account age':
        # Thay đổi thời gian thành số dương
        print('Description:\n{}'.format((np.abs(df[feature])).describe()))
        print('*'*50)
        print('Object type:{}'.format(df[feature].dtype))
    else:
        print('Description:\n{}'.format(df[feature].describe()))
        print('*'*50)
        print('Object type:\n{}'.format(df[feature].dtype))
        value_cnt = value_count_norm_call(df, feature)
        print('Value count:\n{}'.format(value_cnt))


def create_pie_plot(df, feature):
    if feature == 'Drewlling' or 'Education level':
        ratio_size = value_count_norm_call(df, feature)
        ratio_size_len = len(ratio_size.index)
        ratio_list = []
        for i in range(ratio_size_len):
            ratio_list.append(ratio_size.iloc[i]['Frequency (%)'])
        fig, ax = plt.subplots(figsize=(8, 8))
        # 1.2f %% hiển thị số thập phân trong biểu đồ hình tròn với 2 chữ số thập phân
        plt.pie(ratio_list, startangle=90, wedgeprops={
                'edgecolor': 'black'}, autopct='%1.1f%%')
        plt.title('Pie chart of {}'.format(feature))
        plt.legend(loc='best', labels=ratio_size.index)
        plt.axis('equal')
        # return plt.show()
    else:
        ratio_size = value_count_norm_call(df, feature)
        ratio_size_len = len(ratio_size.index)
        ratio_list = []
        for i in range(ratio_size_len):
            ratio_list.append(ratio_size.iloc[i]['Frequency (%)'])
        fig, ax = plt.subplots(1, 2)
        # 1.2f %% hiển thị số thập phân trong biểu đồ hình tròn với 2 chữ số thập phân
        plt.pie(ratio_list, labels=ratio_size.index, autopct='%1.2f%%',
                startangle=90, wedgeprops={'edgecolor': 'black'})
        plt.title('Pie chart of {}'.format(feature))
        plt.legend(loc='best')
        plt.axis('equal')
        # return plt.show()
    st.pyplot(fig)

# function để tạo ra các bar chart


def create_bar_chart(df, feature):
    if feature == 'Marital status' or 'Dwelling' or 'Job title' or 'Employment status' or 'Education level':
        fig, ax = plt.subplots()
        sns.barplot(x=value_count_norm_call(df, feature).index,
                    y=value_count_norm_call(df, feature).values[:, 0])
        ax.set_xticklabels(labels=value_count_norm_call(
            df, feature).index, rotation=45, ha='right')
        plt.xlabel('{}'.format(feature))
        plt.ylabel('Count')
        plt.title('{} count'.format(feature))
        # return plt.show()
    else:
        fig, ax = plt.subplots(1, 2)
        sns.barplot(x=value_count_norm_call(df, feature).index,
                    y=value_count_norm_call(df, feature).values[:, 0])
        plt.xlabel('{}'.format(feature))
        plt.ylabel('Count')
        plt.title('{} count'.format(feature))
        # return plt.show()
    st.pyplot(fig)

# Function để tạo bar chart


def create_bar_plot(df, feature):
    if feature == 'Marital status' or 'Dwelling' or 'Job title' or 'Employment status' or 'Education level':
        fig, ax = plt.subplots(1, 2)
        sns.barplot(x=value_count_norm_call(df, feature).index,
                    y=value_count_norm_call(df, feature).values[:, 0])
        # ax.set_xticklabels(labels=value_count_norm_call(
        #     df, feature).index, rotation=45, ha='right')
        plt.xlabel('{}'.format(feature))
        plt.ylabel('Count')
        plt.title('{} count'.format(feature))
        # return plt.show()
    else:
        fig, ax = plt.subplots(1, 2)
        sns.barplot(x=value_count_norm_call(df, feature).index,
                    y=value_count_norm_call(df, feature).values[:, 0])
        plt.xlabel('{}'.format(feature))
        plt.ylabel('Count')
        plt.title('{} count'.format(feature))
        # return plt.show()
    # st.pyplot(fig)
    return fig


# Function tạo box plot


def creat_box_plot(df, feature):
    if feature == 'Age':
        fig, ax = plt.subplots()
        sns.boxplot(y=np.abs(df[feature]/365))
        plt.title('{} distribution(Boxplot)'.format(feature))
        # return plt.show()
    elif feature == 'Children count':
        fig, ax = plt.subplots(figsize=(2, 8))
        sns.boxplot(y=df[feature])
        plt.title('{} distribution(Boxplot)'.format(feature))
        plt.yticks(np.arange(0, df[feature].max(), 1))
        # return plt.show()
    elif feature == 'Employment length':
        fig, ax = plt.subplots()
        employment_len_no_ret = train_df['Employment length'][train_df['Employment length'] < 0]
        employment_len_no_ret_yrs = np.abs(employment_len_no_ret)/365.25
        sns.boxplot(y=employment_len_no_ret_yrs)
        plt.title('{} distribution(Boxplot)'.format(feature))
        plt.yticks(np.arange(0, employment_len_no_ret_yrs.max(), 2))
        # return plt.show()
    elif feature == 'Account age':
        fig, ax = plt.subplots()
        sns.boxplot(y=np.abs(df[feature]))
        plt.title('{} distribution(Boxplot)'.format(feature))
        # return plt.show()
    else:
        fig, ax = plt.subplots()
        sns.boxplot(y=df[feature])
        plt.title('{} distribution(Boxplot)'.format(feature))
        # return plt.show()
    st.pyplot(fig)


def creat_hist_plot(df, feature, thebins=50):
    if feature == 'Age':
        fig, ax = plt.subplots()
        sns.histplot(np.abs(df[feature]/365.25), bins=thebins)
        plt.title("{} distribution".format(feature))
        # return plt.show()
    elif feature == 'Income':
        fig, ax = plt.subplots()
        sns.histplot(df[feature], bins=thebins)
        ax.get_xaxis().set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ",")))
        plt.title('{} distribution'.format(feature))
        # return plt.show()
    elif feature == 'Account age':
        fig, ax = plt.subplots()
        sns.histplot(np.abs(df[feature], bins=thebins))
        plt.title("{} distribution".format(feature))
        # return plt.show()
    else:
        fig, ax = plt.subplots()
        sns.histplot(df[feature], bins=thebins)
        plt.title("{} distribution".format(feature))
        # return plt.show()
    st.pyplot(fig)


if __name__ == '__main__':
    # fig1 = plt.figure()
    create_bar_chart(train_df, "Gender")
    create_pie_plot(train_df, 'Gender')
    st.markdown('#### Nhận xét:')
    st.markdown(
        ' - Khách hàng là nam giới chiếm khoảng 33%, cụ thể là 9616 người')
    st.markdown(
        '- Khách hàng là nữ giới chiếm khoảng 67%, cụ thể là 19549 người')
    st.markdown('#### Nhận xét:')
    st.markdown(
        '- Trong tập khách hàng trên, độ tuổi chiếm số lượng lớn rơi vào từ 28 đến 42 tuổi ')
    st.markdown('- Tuổi 37 là tuổi của nhiều khách hàng nhất: 953 người')
    st.markdown('- Tuổi 21 là tuổi của ít khách hàng nhất: 8 người')
    create_pie_plot(train_df, 'Marital status')
    create_bar_chart(train_df, 'Marital status')
    st.markdown('#### Nhận xét')
    st.markdown('- Số khách hàng đã kết hôn chiếm đa số: 68.7%')

    create_bar_plot(train_df, 'Children count')
    create_pie_plot(train_df, "Dwelling")
    create_bar_chart(train_df, "Dwelling")
    st.markdown('#### Nhận xét')
    st.markdown('- Số khách hàng sống ở nhà riêng / căn hộ chiếm đa số 89.4 %')
# creat_box_plot(train_df, "Income")
    creat_hist_plot(train_df, "Income")
    st.markdown('#### Nhận xét')
    st.markdown(
        '- Mức thu nhập phổ biến của những người trong bộ dữ liệu nằm trong khoảng từ 100000 đến 200000')
# create_bar_chart(train_df, 'Employment status')
    create_pie_plot(train_df, 'Employment status')
# get_info(train_df, 'Education level')
    # create_bar_chart(train_df, 'Education level')
    create_pie_plot(train_df, 'Education level')
    create_pie_plot(train_df, 'Has a car')
    create_pie_plot(train_df, 'Has a property')
# create_bar_chart(train_df, 'Has a property')
