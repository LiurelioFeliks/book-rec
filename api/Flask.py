from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__, template_folder='templates')

data_fix = pickle.load(open('data123.pkl', 'rb'))
data_top = pickle.load(open('TOPbooks.pkl', 'rb'))
pivot = pickle.load(open('pivot.pkl', 'rb'))
fix = pickle.load(open('fix1.pkl', 'rb'))
cos = pickle.load(open('cos.pkl', 'rb'))
cos2 = pickle.load(open('cos2.pkl', 'rb'))
list_buku = []



@app.route("/")
def hello():
    return render_template('index.html',
                           bookname=list(data_fix['Title'].values),
                           author=list(data_fix['Author'].values),
                           publisher=list(data_fix['Publisher'].values),
                           year=list(data_fix['Year'].values),
                           image=list(data_fix['Image URL'].values),
                           rating=list(data_fix['Rating'].values)
                           )


@app.route("/Top Books")
def top():
    return render_template('50books.html',
                           bookname=list(data_top['Title'].values),
                           author=list(data_top['Author'].values),
                           publisher=list(data_top['Publisher'].values),
                           year=list(data_top['Year'].values),
                           image=list(data_top['Image URL'].values),
                           rating=list(data_top['Rating'].values)
                           )
@ app.route('/Recommended', methods=['post'])


def rec_title():
    list_buku.clear()
    list_gabungan = []
    list_buku2 = []
    user_input_title = request.form.get('user_input')
    list_author = []
    list_buku1 = []
    list_pub = []
    TITLE = list(fix['Title'])
    PUB = list(fix['Publisher'])
    author = list(fix['Author'])
    print(PUB)
    if user_input_title in TITLE:
        print(user_input_title)
        idx_keyword = fix[(fix['Title'] == user_input_title)].index[0]
        list_similiarity_key = sorted(list(enumerate(cos[idx_keyword])), key=lambda x: x[1], reverse=True)
        list_similiarity_key = list_similiarity_key[0:30]
        for i in list_similiarity_key:
            buku = fix['Title'].iloc[i[0]]
            list_buku2.append(buku)
        idx_keyword1 = np.where(pivot.index == user_input_title)[0][0]
        list_similiarity_key1 = sorted(list(enumerate(cos2[idx_keyword1])), key=lambda x: x[1], reverse=True)
        list_similiarity_key1 = list_similiarity_key1[0:30]
        for i in list_similiarity_key1:
            buku = pivot.index[i[0]]
            list_buku1.append(buku)
        list_gabungan = list_buku1 + list_buku2
        print(list_gabungan)
            # print(list_gabungan)
    elif user_input_title in author:
        # idx_keyword3 = fix2[(fix2['Publisher'] == user_input_title)].index[0]
        idx_keyword = fix[(fix['Author'] == user_input_title)].index[0]
        # print(fix.head(5))
        list_similiarity_key = sorted(list(enumerate(cos[idx_keyword])), key=lambda x: x[1], reverse=True)
        list_similiarity_key = list_similiarity_key[0:30]
        for i in list_similiarity_key:
            buku = fix['Title'].iloc[i[0]]
            list_author.append(buku)
        list_gabungan = list_author
        print(list_gabungan)
    elif user_input_title in PUB:
        print(user_input_title)
        # idx_keyword3 = fix2[(fix2['Publisher'] == user_input_title)].index[0]
        idx_keyword = fix[(fix['Publisher'] == user_input_title)].index[0]
        # print(fix.head(5))
        list_similiarity_key = sorted(list(enumerate(cos[idx_keyword])), key=lambda x: x[1], reverse=True)
        list_similiarity_key = list_similiarity_key[0:30]
        for i in list_similiarity_key:
            buku = fix['Title'].iloc[i[0]]
            list_pub.append(buku)
        list_gabungan = list_pub
    for i in list_gabungan:
        item = []
        b = fix.loc[fix['Title'] == i]
        # b.astype('int')
        item.extend(list(b.drop_duplicates('Title')['Title'].values))
        item.extend(list(b.drop_duplicates('Title')['Author'].values))
        item.extend(list(b.drop_duplicates('Title')['Publisher'].values))
        item.extend(list(b.drop_duplicates('Title')['Image URL'].values))
        item.extend(list(b.drop_duplicates('Title')['Rating'].round(2).values))
        list_buku.append(item)
    list_gabungan.clear()
    return render_template('recommended.html',list_buku = list_buku)


# @app.route('/Recommended', methods=['post'])
# def rec_pub():
#     list_buku.clear()
#     user_input_pub = request.form.get('user_input')
#     list_pub = []
#     idx_keyword_pub = fix[(fix['Publisher'] == user_input_pub)].index[0]
#     # print(fix.head(5))
#     list_similiarity_key = sorted(list(enumerate(cos[idx_keyword_pub])), key=lambda x: x[1], reverse=True)
#     list_similiarity_key = list_similiarity_key[0:10]
#     for i in list_similiarity_key:
#         buku = fix['Title'].iloc[i[0]]
#         list_pub.append(buku)
#     # list_similiarity_publisher =[i[0] for i in list_similiarity_publisher]
#     # publisher = data_fix['Title'].iloc[list_similiarity_publisher]
#     print(list_pub)
#     # list_buku = []
#     for i in list_pub:
#         item = []
#         b = fix.loc[fix['Title'] == i]
#         item.extend(list(b.drop_duplicates('Title')['Title'].values))
#         item.extend(list(b.drop_duplicates('Title')['Author'].values))
#         item.extend(list(b.drop_duplicates('Title')['Publisher'].values))
#         item.extend(list(b.drop_duplicates('Title')['Image URL'].values))
#         list_buku.append(item)
#     print(list_buku)
#     # return list_buku
#     return list_buku


if __name__ == '__main__':



# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# app = Flask(__name__,template_folder='templates')
#
# data_fix = pickle.load(open('data.pkl','rb'))
# data_top = pickle.load(open('TOP50.pkl','rb'))
# pivot = pickle.load(open('pivot.pkl','rb'))
# fix = pickle.load(open('fix1.pkl','rb'))
# fix2 = pickle.load(open('fix2.pkl','rb'))
# cos = pickle.load(open('cos.pkl','rb'))
# cos2 = pickle.load(open('cos2.pkl','rb'))
# list_buku = []
# @app.route("/")
# def hello():
#     return render_template('index.html',
#                            bookname = list(data_fix['Title'].values),
#                            author = list(data_fix['Author'].values),
#                            publisher = list(data_fix['Publisher'].values),
#                            year = list(data_fix['Year'].values),
#                            image = list(data_fix['Image URL'].values),
#                            rating = list(data_fix['Rating'].values)
#                            )
#
#
# @app.route("/Top Books")
# def top():
#     return render_template('50books.html',
#                            bookname=list(data_top['Title'].values),
#                            author=list(data_top['Author'].values),
#                            publisher=list(data_top['Publisher'].values),
#                            year=list(data_top['Year'].values),
#                            image=list(data_top['Image URL'].values),
#                            rating=list(data_top['Rating'].values)
#                            )\
#
# @app.route('/Recommended', methods=['post'])
# def rec_title():
#     list_buku.clear()
#     # list_buku2=[]
#     list_author = []
#     # list_publisher = []
#     user_input_title = request.form.get('user_input')
#     list_author = []
#     list_buku2 = []
#     idx_keyword = fix[(fix['Title'] == user_input_title)].index[0]
#     # print(fix.head(5))
#     list_similiarity_key = sorted(list(enumerate(cos[idx_keyword])), key=lambda x: x[1], reverse=True)
#     list_similiarity_key = list_similiarity_key[0:10]
#     for i in list_similiarity_key:
#         buku = fix['Title'].iloc[i[0]]
#         list_buku2.append(buku)
#     list_buku1=[]
#     idx_keyword1 = np.where(pivot.index == user_input_title)[0][0]
#     list_similiarity_key1 = sorted(list(enumerate(cos2[idx_keyword1])), key=lambda x: x[1], reverse=True)
#     list_similiarity_key1 = list_similiarity_key1[0:10]
#     for i in list_similiarity_key1:
#         buku = pivot.index[i[0]]
#         list_buku1.append(buku)
#     list_gabungan = list_buku1 + list_buku2
#         # print(list_gabungan)
#
#     for i in list_gabungan:
#         item = []
#         b = fix.loc[fix['Title'] == i]
#         # b.astype('int')
#         item.extend(list(b.drop_duplicates('Title')['Title'].values))
#         item.extend(list(b.drop_duplicates('Title')['Author'].values))
#         item.extend(list(b.drop_duplicates('Title')['Publisher'].values))
#         item.extend(list(b.drop_duplicates('Title')['Image URL'].values))
#         item.extend(list(b.drop_duplicates('Title')['Rating'].round(2).values))
#         list_buku.append(item)
#     print(list_buku)
#     return list_buku
# # @app.route('/Recommended', methods=['post'])
# def rec_pub():
#     list_buku.clear()
#     user_input_pub = request.form.get('user_input')
#     list_pub = []
#     idx_keyword_pub = fix[(fix['Publisher'] == user_input_pub)].index[0]
#     # print(fix.head(5))
#     list_similiarity_key = sorted(list(enumerate(cos[idx_keyword_pub])), key=lambda x: x[1], reverse=True)
#     list_similiarity_key = list_similiarity_key[0:10]
#     for i in list_similiarity_key:
#         buku = fix['Title'].iloc[i[0]]
#         list_pub.append(buku)
#     # list_similiarity_publisher =[i[0] for i in list_similiarity_publisher]
#     # publisher = data_fix['Title'].iloc[list_similiarity_publisher]
#     print(list_pub)
#     # list_buku = []
#     for i in list_pub:
#         item = []
#         b = fix.loc[fix['Title'] == i]
#         item.extend(list(b.drop_duplicates('Title')['Title'].values))
#         item.extend(list(b.drop_duplicates('Title')['Author'].values))
#         item.extend(list(b.drop_duplicates('Title')['Publisher'].values))
#         item.extend(list(b.drop_duplicates('Title')['Image URL'].values))
#         list_buku.append(item)
#     print(list_buku)
#     # return list_buku
#     return list_buku
# if __name__ == '__main__':
#     app.run(debug=True)