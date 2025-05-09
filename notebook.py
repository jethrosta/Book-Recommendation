#!/usr/bin/env python
# coding: utf-8

# # Import Library

# In[91]:


# Import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import accuracy


# # Import Dataset

# In[2]:


# Import dataset
df_books = pd.read_csv('Book_Dataset/Books.csv')
df_ratings = pd.read_csv('Book_Dataset/Ratings.csv')
df_users = pd.read_csv('Book_Dataset/Users.csv')


# In[3]:


df_books.head()


# In[4]:


df_users.head()


# In[ ]:


print(df_books.shape)
print(df_ratings.shape)
print(df_users.shape)


# Dataset tersebut memiliki ukuran yang berbeda-beda :
# - df_books memiliki 271.360 dengan 8 kolom
# - df_ratings memiliki 1.149.780 dengan 3 kolom
# - df_users memiliki 278858 dengan 3 kolom

# # Exploratory Data Analysis
# 
# Pada bagian ini kita akan melihat karakteristik dan bentuk data yang sudah kita import sebelumnya. Setelah dianalisa, kita bisa melakukan beberapa tahapan, seperti :
# 1. Menghilangkan `duplicated data`
# 2. Membuang `features` yang tidak penting (images pada df_books)
# 3. Mengatasi `Missing Values`
# 4. dan membandingkan `Unique Values`

# In[6]:


# Menghapus data yang mengalami duplikasi
df_books = df_books.drop_duplicates()
df_ratings = df_ratings.drop_duplicates()
df_users = df_users.drop_duplicates()


# ## `df_books`

# In[7]:


df_books.info()


# Pada df_books terdapat `features` yang kurang penting, seperti Image-URL-S/M/L. Hal ini tidak akan digunakan dalam sistem rekomendasi, lebih baik kita drop saja.

# In[8]:


df_books_dropped = df_books.drop(['Image-URL-S', 'Image-URL-M', 'Image-URL-L'], axis=1)
df_books_dropped.info()


# Terdapat data yang hilang sehingga kita dapat menghilangkan **missing values** pada `Book-Author` dan `Publisher` karena jumlah dataset yang masih terlampau banyak sehingga penghapusan beberapa data kosong tidak akan mempengaruhui data kita.

# In[9]:


df_books_dropped[df_books_dropped.isnull().any(axis=1)]


# In[10]:


df_books_nan = df_books_dropped.dropna()
df_books_nan.info()


# In[11]:


df_books_nan.head(10)


# Kita perlu mengubah bentuk judul `features` **Book-Title**, **Book-Author**, dan **Year-Of-Publication** pada dataframe agar lebih mudah dilihat

# In[12]:


df_books_renamed = df_books_nan.rename(columns={'Book-Title':'book_title','Book-Author':'book_author','Year-Of-Publication':'YoP'})
df_books_renamed.head(10)


# In[13]:


print('Jumlah data ISBN: ', len(df_books_renamed.ISBN.unique()))
print('Jumlah data Judul Buku: ', len(df_books_renamed.book_title.unique()))
print('Jumlah data Penulis Buku: ', len(df_books_renamed.book_author.unique()))
print('Jumlah data Tahun Terbit Buku ', len(df_books_renamed.YoP.unique()))


# In[14]:


df_books_renamed.info()


# In[15]:


# Hitung kemunculan setiap book_title
title_counts = df_books_renamed['book_title'].value_counts()

# Tampilkan hanya yang muncul lebih dari 1 kali
duplicated_titles = title_counts[title_counts > 1]
print(duplicated_titles)


# In[16]:


df_books_renamed.query('book_title == "Selected Poems"')


# In[17]:


# Pertama kita group berdasarkan 'book_title'
grouped = df_books_renamed.groupby('book_title')

# Lalu kita cek berapa banyak ISBN unik untuk setiap book_title
isbn_check = grouped['ISBN'].nunique()

# Tampilkan book_title yang hanya punya 1 ISBN unik
same_isbn = isbn_check[isbn_check == 1]
print("Book titles dengan 1 ISBN:")
same_isbn.count()


# In[18]:


# Tampilkan book_title yang punya lebih dari 1 ISBN unik
different_isbn = isbn_check[isbn_check > 1]
print("\nBook titles dengan ISBN yang berbeda:")
different_isbn.head()


# In[19]:


# Melihat detail ISBN untuk setiap book_title
isbn_details = grouped['ISBN'].unique()

# Menampilkan book_title dengan lebih dari 1 ISBN
isbn_details = isbn_details[isbn_details.apply(lambda x: len(x) > 1)]
print("\nDetail ISBN untuk book_title yang sama:")
isbn_details.head(10)


# In[20]:


df_books_renamed[df_books_renamed['book_title'] == '!%@ (A Nutshell handbook)']


# In[21]:


df_books_renamed[df_books_renamed['book_title'] == "'Salem's Lot"]


# Ternyata tidak terdapat duplicated data karena ISBN berbeda, penulis berbeda, tahun berbeda, dan publisher yang berbeda tidak dikategorikan sebagai duplicated data. Buku dengan judul yang sama tetapi dutulis oleh orang yang berbeda sudah pasti memiliki isi yang berbeda, begitu juga dengan tahun terbit yang berbeda, tetapi untuk ISBN yang sama maka itu perlu diinvestigasi lebih lanjut

# ## `df_ratings`

# In[22]:


df_ratings.info()


# tidak terdapat missing values. Sekarang mari kita lihat apakah terdapat duplicated values, tetapi kita perlu mengganti judul dari kolom agar tidak terjadi error ketika melihat unique values

# In[23]:


df_ratings_renamed = df_ratings.rename(columns={'User-ID':'user_id', 'Book-Rating':'book_rating'})
df_ratings_renamed.head()


# In[24]:


print('Jumlah unique value user ID: ', len(df_ratings_renamed.user_id.unique()))
print('Jumlah unique value ISBN: ', len(df_ratings_renamed.ISBN.unique()))
print('Jumlah unique value Rating: ', len(df_ratings_renamed.book_rating.unique()))


# In[ ]:


df_ratings_renamed.shape


# Terlihat bahwa dari data 1.149.780, ternyata hanya ada 105.283 ID. Akan tetapi, ISBN hanya 340.556? Mari kita lihat lebih lanjut. Terdapat 2 kemungkinan :
# 1. User yang sama memberikan rating ke beberapa buku atau beberapa user memberikan rating ke satu buku yang sama
# 2. User melakukan rating ke buku yang sama lebih dari sekali dan disimpan berulang. 

# In[26]:


# Cek apakah ada baris yang persis sama (semua kolom user_id, ISBN, rating)
duplicated_rows = df_ratings_renamed.duplicated()

# Berapa banyak duplicated rows?
print("Jumlah duplicated baris:", duplicated_rows.sum())


# In[27]:


# Cek duplikat berdasarkan kombinasi user_id dan ISBN saja
duplicated_user_isbn = df_ratings_renamed.duplicated(subset=['user_id', 'ISBN'])

print("Jumlah duplicated berdasarkan (user_id, ISBN):", duplicated_user_isbn.sum())


# Ternyata data ini cukup bersih :
# 1. Tidak ada `missing values`
# 2. Tidak ada `duplicated data`
# 3. Tidak ada features yang tidak penting

# ## `df_users`

# In[28]:


df_users.info()


# In[29]:


df_users.isnull().sum()


# Terdapat missing values pada data Age

# In[30]:


df_users[df_users.isnull().any(axis=1)]


# Karena jumlah data umur yang memiliki NaN values sangat banyak, alangkah baiknya kita mengisinya terlebih dahulu dengan metode Group-by Location dimana kita mengisi NaN values semirip mungkin dengan data aslinya agar sistem rekomendasi dapat berjalan akurat. Kemudian usia orang di satu lokasi biasanya mirip-mirip.

# In[31]:


for loc in df_users['Location'].unique():
    print(loc)


# Kita menemukan masalah lain, terdapat data lokasi yang sama tetapi memiliki struktur yang berbeda, seperti USA/US/United States of America/United States/United Stated/United Staes. Kemudian terdapat lokasi detail yang sepertinya tidak terlalu berpengaruh signifikan dan justru memberikan data jadi kotor dan terlalu variatif

# In[32]:


df_users_modified = df_users
df_users_modified['Location'] = df_users_modified['Location'].apply(lambda x: ', '.join(x.split(', ')[3:]) 
                                                  if len(x.split(', ')) > 3 
                                                  else x)

df_users_modified.head()


# Sepertinya masih terdapat lokasi yang tidak diisi dengan benar dan kita harus mevalidasi lokasi tersebut berdasarkan negara yang ada. Kita akan menggunakan library pycountry untuk memudahkan kita melihat negara mana saja yang ada dan melihat daata mana saja yang bisa diperbaiki lokasinya.

# In[33]:


global_median = df_users['Age'].median()

df_users['Age'] = df_users.groupby('Location')['Age'].transform(
    lambda x: x.fillna(x.median())
)

df_users['Age'].fillna(global_median, inplace=True)

print("Sisa NaN di Age: ", df_users["Age"].isna().sum())


# Melihat bentuk data yang diisi tidak seragam lebih baik feature Location tidak perlu digunakan dalam sistem rekomendasi

# In[34]:


df_users.info()


# In[35]:


df_users_renamed = df_users.rename(columns={"User-ID":"user_id"})
df_users_renamed.head()


# In[36]:


print('Jumlah unique value user ID: ', len(df_users_renamed.user_id.unique()))
print('Jumlah unique value Lokasi: ', len(df_users_renamed.Location.unique()))
print('Jumlah unique value Rating: ', len(df_users_renamed.Age.unique()))


# ## Top 10 Most Rated Books
# 
# Melakukan analisa dan visualisasi terhadap buku-buku yang paling sering diulas oleh users

# In[37]:


most_rated_books = df_ratings_renamed.groupby('ISBN')["book_rating"].count().sort_values(ascending=False).head(10)
most_rated_books = pd.DataFrame(most_rated_books)
most_rated_books


# In[38]:


most_rated_books = df_ratings_renamed["ISBN"].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x = most_rated_books.values, y = most_rated_books.index, palette='coolwarm')
plt.title("Top 10 Most Rated Books")
plt.xlabel("Number of Rating")
plt.ylabel("ISBN")
plt.show()


# ## Top 10 Prolific Authors
# 
# Melihat 10 penulis paling produktif

# In[39]:


top_authors = df_books_renamed["book_author"].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_authors.values, y=top_authors.index, palette='coolwarm')
plt.title("Top 10 Most Prolific Authors")
plt.xlabel("Number of Books")
plt.ylabel("Author")
plt.show()


# ## Top 10 Publisher
# 
# Melihat 10 Publisher paling produktif mempublish

# In[40]:


top_publisher = df_books_renamed["Publisher"].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_publisher.values, y=top_publisher.index, palette='coolwarm')
plt.title("Top 10 Most Prolific Authors")
plt.xlabel("Number of Books")
plt.ylabel("Author")
plt.show()


# ## Distribution of Year of Publication
# 
# Melihat distribusi terbitan buku berdasarkan tahun terbit

# In[41]:


df_books_renamed.info()


# In[42]:


# Convert Year-Of-Publication to numeric (if not already) and handle errors
df_books_renamed['YoP'] = pd.to_numeric(df_books_renamed['YoP'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.histplot(df_books_renamed['YoP'].dropna(), bins=30, kde=True, color='coral')
plt.title("Distribution of Year of Publication")
plt.xlabel("Year of Publication")
plt.ylabel("Count")
plt.show()


# In[43]:


df_books_renamed[df_books_renamed['YoP'] < 1900].count()


# Ternyata terdapat tahun yang tidak ada alias bernilai 0. Terdapat 4622, karena jumlahnya tidak terlalu besar, kita hapus saja.

# In[44]:


df_books_cleaned = df_books_renamed[df_books_renamed['YoP'] >= 1900]
df_books_cleaned[df_books_cleaned['YoP'] < 1900].count()


# In[45]:


# Convert Year-Of-Publication to numeric (if not already) and handle errors
df_books_cleaned['YoP'] = pd.to_numeric(df_books_cleaned['YoP'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.histplot(df_books_cleaned['YoP'].dropna(), bins=30, kde=True, color='coral')
plt.title("Distribution of Year of Publication")
plt.xlabel("Year of Publication")
plt.ylabel("Count")
plt.show()


# Mayoritas tahun terbitan buku ada pada rentang 1990an - 2000an

# ## Distribution of Book Ratings

# In[46]:


df_ratings_renamed["book_rating"].hist(bins=10)


# In[47]:


df_ratings_cek = df_ratings_renamed[df_ratings_renamed.book_rating != 0]
df_ratings_cek.count()


# Terdapat data rating yang bernilai 0. Hal ini bukan berarti buku tersebut dinilai jelek, tetapi terkadang karakteristik user lupa untuk memberi ulasan sehingga default value dari rating akan menghasilkan nilai 0.

# In[48]:


df_ratings_renamed = df_ratings_renamed.drop(df_ratings_renamed[df_ratings_renamed.book_rating == 0].index)
df_ratings_renamed["book_rating"].hist(bins=10)


# # Data Preprocessing
# 
# karena jumlah datanya mencapai 1 juta yang mengakibatkan terpenuhnya memori, maka sampling dilakukan pada 10.000 data pertama saja untuk book_dataset dan 5000 untuk rating_dataset

# In[49]:


book_dataset = df_books_renamed[:10000]
rating_dataset = df_ratings_renamed[:10000]


# In[50]:


book_dataset.head(3)


# In[51]:


rating_dataset.head(3)


# In[52]:


all_df = pd.merge(book_dataset, rating_dataset[['ISBN']], on='ISBN', how='left')
all_df


# In[53]:


book_ISBN = all_df['ISBN'].tolist()

book_title = all_df['book_title'].tolist()

book_author = all_df['book_author'].tolist()

book_year_of_publication = all_df['YoP'].tolist()


# In[54]:


book = pd.DataFrame({
    'book_ISBN': book_ISBN,
    'book_title': book_title,
    'book_author': book_author,
    'book_year_of_publication': book_year_of_publication
})
book


# # Model Development dengan Content Based Filtering
# Content based filtering menggunakan kesamaan konten atau produk yang ada dengan kesamaan item dengan preferensi pengguna. Pada kasus kita kali ini kita menggunakan TF-IDF untuk membangun sistem rekomendasi berdasarkan penulis buku.

# ## TF-IDF Vectorizer

# In[55]:


tf = TfidfVectorizer()
 
tf.fit(book['book_author']) 
 
tf.get_feature_names_out() 


# In[56]:


tfidf_matrix = tf.fit_transform(book['book_author']) 
 
tfidf_matrix.shape 


# In[57]:


tfidf_matrix.todense()


# In[58]:


pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names_out(),
    index=book.book_title
).sample(10, axis=1,replace=True).sample(10, axis=0)


# In[59]:


tfidf_matrix.todense()


# ## Cosine Similarity

# In[60]:


cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim


# In[61]:


cosine_sim_df = pd.DataFrame(cosine_sim, index=book['book_title'], columns=book['book_title'])


# In[62]:


cosine_sim_df.head()


# ## Mendapatkan Rekomendasi
# Di sini, kita membuat fungsi author_recommendations dengan beberapa parameter sebagai berikut:
# 
# - Penulis Buku : (index kemiripan dataframe).
# - Similarity_data : Dataframe mengenai similarity yang telah kita definisikan sebelumnya.
# - Items : Nama dan fitur yang digunakan untuk mendefinisikan kemiripan, dalam hal ini adalah ‘book_title’ dan ‘book_author’.
# - k : Banyak rekomendasi yang ingin diberikan.

# In[66]:


def author_recommendations(penulis, similarity_data=cosine_sim_df, items=book[['book_title', 'book_author']], k=10):
    """
    Rekomendasi Resto berdasarkan kemiripan dataframe

    Parameter:
    ---
    penulis : tipe data string (str)
                Nama Penulis (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame(object)
                      Kesamaan dataframe, simetrik, dengan penulis sebagai 
                      indeks dan kolom
    items : tipe data pd.DataFrame(object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        banyak jumlah rekomendasi yang diberikan
    ---

    Pada index ini, kita mengambil k dengan nilai similarity terbesar
    pada index matrix yang diberikan (i)
    """

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe dibuah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:, penulis].to_numpy().argpartition(range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(penulis, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)


# In[ ]:


# Nama buku yang pernah dibaca
books_that_have_been_read = "The Diaries of Adam and Eve"
book[book.book_title.eq(books_that_have_been_read)]


# In[68]:


author_recommendations(books_that_have_been_read)


# ## Evaluation

# In[74]:


# Ambil data rekomendasi penulis
recommendations = author_recommendations(
    books_that_have_been_read, 
    cosine_sim_df, 
    book[['book_title', 'book_author']],
    k=10
)

# Ambil penulis dari buku yang dibaca
target_author = book[book.book_title == books_that_have_been_read].iloc[0]['book_author']

# Hitung berapa rekomendasi yang memiliki penulis yang sama
true_positives = recommendations[recommendations['book_author'] == target_author].shape[0]

# --- Precision ---
# Hitung berapa rekomendasi yang benar-benar ditulis oleh penulis yang sama
true_positives = recommendations[recommendations['book_author'] == target_author].shape[0]
total_recommended = recommendations.shape[0]
precision = true_positives / total_recommended

# --- Recall ---
# Total jumlah buku dalam dataset yang ditulis oleh penulis tersebut (kecuali buku yang dibaca)
total_relevant = book[(book['book_author'] == target_author) & (book['book_title'] != books_that_have_been_read)].shape[0]

# Untuk menghindari pembagian dengan nol
recall = true_positives / total_relevant if total_relevant > 0 else 0

# --- F1-score ---
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Cetak hasil evaluasi
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-score: {f1_score:.2%}")


# Dari hasil ini, dapat disimpulkan bahwa model memiliki performa yang cukup baik dalam memberikan rekomendasi yang relevan.

# # Model Development dengan Collaborative Filtering
# 
# Collaborative Filtering adalah sistem rekomendasi dimana menganalisis user lain yang memiliki pola perilaku serupa, lalu merekomendasikan item yang mereka sukai. Fokus ke "apa yang orang seperti kamu sukai"

# ## Data Preparation

# In[75]:


# Mengencode user ID
user_ids = rating_dataset['user_id'].unique().tolist()
print("list User ID: ", user_ids)

user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print("Encoded User ID: ", user_to_user_encoded)

user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print("Encoded angka ke User ID: ", user_encoded_to_user)


# In[76]:


# Mengencode book id
book_ids = rating_dataset['ISBN'].unique().tolist()
book_to_book_encoded = {x: i for i, x in enumerate(book_ids)}
book_encoded_to_book = {i: x for i, x in enumerate(book_ids)}

rating_dataset['user'] = rating_dataset['user_id'].map(user_to_user_encoded)
rating_dataset['book'] = rating_dataset['ISBN'].map(book_to_book_encoded)


# In[77]:


num_users = len(user_encoded_to_user)
print(num_users)
num_book = len(book_encoded_to_book)
print(num_book)
rating_dataset['book_rating'] = rating_dataset['book_rating'].values.astype(np.float32)

min_rating = min(rating_dataset['book_rating'])
max_rating = max(rating_dataset['book_rating'])
 
print('Number of User: {}, Number of Book: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_book, min_rating, max_rating
))


# ## Data Spliting

# In[78]:


rating_dataset = rating_dataset.sample(frac=1, random_state=42)
rating_dataset


# In[79]:


x = rating_dataset[['user', 'book']].values
 
y = rating_dataset['book_rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values
 
train_indices = int(0.70 * rating_dataset.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)
 
print(x, y)


# ## Creating Model

# In[ ]:


class RecommenderNet(tf.keras.Model):
 
  def __init__(self, num_users, num_resto, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_resto = num_resto
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding(
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1)
    self.resto_embedding = layers.Embedding( 
        num_resto,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.resto_bias = layers.Embedding(num_resto, 1) 
 
  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0])
    user_bias = self.user_bias(inputs[:, 0])
    resto_vector = self.resto_embedding(inputs[:, 1])
    resto_bias = self.resto_bias(inputs[:, 1]) 
 
    dot_user_resto = tf.tensordot(user_vector, resto_vector, 2) 
 
    x = dot_user_resto + user_bias + resto_bias
    
    return tf.nn.sigmoid(x) 


# In[100]:


model = RecommenderNet(num_users, num_book, 20)

model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.003),
    metrics=[tf.keras.metrics.RootMeanSquaredError(), tf.keras.metrics.MeanAbsoluteError()]
)


# In[101]:


history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 5,
    epochs = 20,
    validation_data = (x_val, y_val)
)


# In[104]:


plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epochs')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
rmse_train = history.history['root_mean_squared_error'][-1]  # Nilai RMSE untuk data pelatihan
rmse_val = history.history['val_root_mean_squared_error'][-1]  # Nilai RMSE untuk data validasi

print(f'RMSE (Training): {rmse_train}')
print(f'RMSE (Validation): {rmse_val}')

# Jika Anda juga memiliki MAE, Anda bisa mencetaknya dengan cara yang sama
mae_train = history.history['mean_absolute_error'][-1]  # Nilai MAE untuk data pelatihan
mae_val = history.history['val_mean_absolute_error'][-1]  # Nilai MAE untuk data validasi

print(f'MAE (Training): {mae_train}')
print(f'MAE (Validation): {mae_val}')


# ## Mendapatkan Rekomendasi

# In[105]:


book_dataset =  book
rating_dataset = rating_dataset[rating_dataset['book_rating'] > 5]


# In[106]:


# Mengambil sample user
user_id = rating_dataset.user_id.sample(8).iloc[0]
books_have_been_read_by_user = rating_dataset[rating_dataset.user_id == user_id]
 
books_have_not_been_read_by_user = book_dataset[~book_dataset['book_ISBN'].isin(books_have_been_read_by_user.ISBN.values)]['book_ISBN'] 
books_have_not_been_read_by_user = list(
    set(books_have_not_been_read_by_user).intersection(set(book_to_book_encoded.keys()))
)
 
books_have_not_been_read_by_user = [[book_to_book_encoded.get(x)] for x in books_have_not_been_read_by_user]
user_encoder = user_to_user_encoded.get(user_id)
user_book_array = np.hstack(
    ([[user_encoder]] * len(books_have_not_been_read_by_user), books_have_not_been_read_by_user)
)


# In[107]:


ratings = model.predict(user_book_array).flatten()
 
top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_book_ids = [
    book_encoded_to_book.get(books_have_not_been_read_by_user[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Author with high ratings from user')
print('===' * 8) 

top_books_recommended = (
    books_have_been_read_by_user.sort_values(
        by = 'book_rating',
        ascending=False
    )
    .head(5)
    .ISBN.values
)
 
books_row = book_dataset[book_dataset['book_ISBN'].isin(top_books_recommended)]
for row in books_row.itertuples():
    print(row.book_author, ':', row.book_title)
 
print('----' * 8)
print('Top 10 Book Recommendation for user: {}'.format(user_id))
print('----' * 8)
 
recommended_books = book_dataset[book_dataset['book_ISBN'].isin(recommended_book_ids)].drop_duplicates()
#for row in recommended_books.itertuples():
#    print(row.book_author, ':', row.book_title)
for index, row in enumerate(recommended_books.itertuples(), start=1):
    print(f"{index}. {row.book_author} : {row.book_title}")


# In[ ]:




