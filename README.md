# Machine Learning Project Report - Feivel Jethro Ezhekiel

![Book Image](Assets/Gambar_buku/vecteezy_whimsical-book-stack-with-hot-air-balloons_51064729.jpg)

## Project Overview

This project is an Artificial Intelligence-based Recommendation System focused on authors, utilizing data that includes information about book titles, authors, publication years, ISBNs, and user ratings. Readers/users are provided with 10 recommendations using 2 approaches: `Content Based Filtering` and `Collaborative Filtering`. `Content Based Filtering` provides recommendations based on the similarity of content or products with items that match user preferences, while `Collaborative Filtering` uses the behavior patterns of other users who have similar preferences based on the content/products they like.

**Additional Notes**:
- Research from the Yale School of Public Health found that those who spend 30 minutes reading books each day for a year live 2 years longer than those who never read. According to Specktor (2018), reading makes individuals better by fostering empathy and emotional intelligence. Erasmus (2018) also states that reading can reduce stress and enhance intelligence in the long term by stimulating the brain and improving memory function.
- A study by Tulgan (2018) explains that Gen-Z has poor *critical thinking* skills due to their dependence on gadgets as sources of information, leading to a lack of independent thinking because answers are quickly provided by the internet rather than through their own experiences in seeking answers with **depth of thought** to solve problems.
- PISA (Programme for International Student Assessment) is an international study that measures the abilities of students worldwide at the age of 15, reflecting the Human Resources (HR) of the respective countries. The test is organized by the Organisation for Economic Co-operation and Development (OECD), which consists of developed and developing countries aiming to improve economic and social welfare. The PISA test is conducted every 3 years and covers three main categories:
  - Mathematics: Tests students' ability to apply mathematical concepts to solve everyday problems.
  - Reading: Assesses students' ability to understand and use information from written texts in various contexts.
  - Science: Measures students' understanding of scientific concepts and their ability to apply knowledge in real-life situations.
- Where does Indonesia's PISA score stand? According to an article from Detik.com, Indonesia's PISA score has been categorized as low since the study began in 2000. Indonesia's score in 2022 was 359, with a mathematics score of 366 and a science score of 396. This result places Indonesia at 69th out of 80 participating countries.


<div style="display: flex; justify-content: center;"> 
  <img src="https://cdn.gnfi.net/goodstats/uploads/images/15189/September/s__Pisa.png">
</div>


**References**:
- [EXPLORING READING ISSUES AMONG MILLENNIALS AND GENZ](https://www.researchgate.net/publication/329814876_EXPLORING_READING_ISSUES_AMONG_MILLENNIALS_AND_GENZ) 
- [Indonesia's PISA Score Targeted to Match OECD Countries, RI Diaspora Suggests This Learning](https://www.detik.com/edu/sekolah/d-7695294/skor-pisa-indonesia-ditarget-setara-negara-oecd-diaspora-ri-usul-belajar-ini)
- [PISA Scores: A Reference for National HR Quality](https://s1pbing.fbs.unesa.ac.id/post/skor-pisa-acuan-kualitas-sdm-negara)
- [Indonesia's Position in PISA 2022, Ready for 2025?](https://goodstats.id/article/posisi-indonesia-di-pisa-2022-siapkah-untuk-2025-6RLyK)
- [Narrative of Indonesia's PISA Score Should Not Seem Like an Achievement](https://www.kompas.id/baca/humaniora/2023/12/06/narasi-skor-pisa-indonesia-jangan-seolah-olah-prestasi)

## Business Understanding

The reading ability of Indonesia's youth is below the global average, as reflected in our low PISA scores in mathematics, reading, and science. What can PISA scores reflect? According to an article from Surabaya State University, PISA scores are used by countries as indicators of national HR quality. PISA scores are often referenced for several reasons:
1. Essential Indicator
2. Comparative Between Countries
3. Predictor of Future HR
4. Basis for Educational Policy Making

Therefore, the low reading interest among Indonesia's youth contributes to the low PISA scores compared to other Southeast Asian countries.

### Problem Statements

The continuously evolving technology and gadgets, which are always in the hands of Indonesia's youth, known as smartphones, are not smart enough to increase their reading interest. Some causes of the lack of reading interest among Indonesia's youth include:
- Books not matching the interests/needs of readers 
- Lack of personalization in the presentation of literacy content

### Goals

![Teen Reading a Book](https://newsone.com/wp-content/uploads/sites/22/2022/08/16600434609052.jpg?strip=all&quality=80)

The above problems can be addressed with one AI technology aimed at:
- **Increasing reading interest and engagement among Indonesia's youth**
This can be achieved by creating a system that can recognize and personalize each child's interests through their respective smart devices, known as a Recommendation System.
- **Developing a Book Recommendation System**
This recommendation system is built to enhance personalization and book recommendations based on young people's interactions with books they have read and with other users.

**Additional Notes**:

![Recommendation System Method Illustration](https://lh4.googleusercontent.com/0NoiKF9NDEM0_daE0Wwfmyq9Z5sRCMIoNM0Fst-JJr9Hi0dG7PSSZeUM_Xok3lW762UbDYit8bCz_p8vZ7rJO9XuSKbRyUPFk_gTIgA2G2i_PmknJUc8l91nB-Stx77z1tMxtFsxIOpjXh0bAenftLfk6KqMXJoA9SOhcd8lKQf1ZWev7gL2gOaaZf7wsw)

To achieve these goals, we need to find AI solution approaches using certain methods, including:

### Content Based Filtering
This method is a recommendation approach where the system will use the characteristics or properties of items/products that will serve as the basis for recommendations to users. Generally, Content-Based Filtering uses 2 common techniques in making recommendations: *heuristic-based* and *model-based*. The details are as follows:

#### *Heuristic-based*
- Cosine Similarity
- Boolean Query
- TF-IDF
- Clustering

#### *Model-based*
- Bayesian Classifier & Clustering
- Decision Tree
- Artificial Neural Network

### Collaborative Filtering
This method is currently the most popular. Many studies discuss this technique due to its advantages, such as generating serendipitous (unexpected) items, aligning with market trends, being easy to implement, and allowing application across several domains (books, movies, music, etc.). The method works by finding similarities in data among users by utilizing community data where users with similar past preferences tend to have similar future preferences.

## Data Understanding

- **Data Source**: [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data)

The dataset taken from Kaggle aims to create a user-based recommendation system, including book data such as ISBN, title, author, and publisher, as well as rating data containing the number of user ratings for book items.

- **Number of Rows and Columns**
The dataset consists of 3 files named `Books.csv`, `Ratings.csv`, and `Users.csv`. 
  - `Books.csv` has 271,360 rows and 8 columns
  - `Ratings.csv` has 1,149,780 rows and 3 columns
  - `Users.csv` has 278,858 rows and 3 columns

- **Data Conditions**
  - First, in `Books.csv`, there are 3 columns/features that do not affect the recommendation system, with 4 data entries experiencing **missing values** in the *Book-Author* and *Publisher* features. The feature titles are also not tidy, so the features Book-Author, Year-Of-Publication, and Book-Title are renamed to book_author, YoP, and book_title.
  - Second, `Ratings.csv` has no **missing values**, no **duplicated data**, and all features are important for the recommendation system, making the data quite clean.
  - Third, `Users.csv` has 110,762 data entries with `missing values` in the **Age** column and untidy location listings. The rest of the data is clean and actionable.

  - The total data obtained from the dataset above is:
    - 271,360 rows with 8 columns in `Books.csv`
    - 1,149,780 rows with 3 columns in `Ratings.csv`
    - and 278,858 rows with 3 columns in `Users.csv`

- **Description of All Features in the Data**

  Variables in `Books.csv`:
  | **Variable**         | **Description**                                                                                              |
  |----------------------|------------------------------------------------------------------------------------------------------------|
  | **Book_Title**        | The title of the book that has been read.                                                                                |
  | **Book_Author**       | The author of the book.                                                                                  |
  | **ISBN**              | The identification number of the book. Each book with the same title but different publishers or release years has a different ISBN. |
  | **Year of Publication** | The year the book was published.                                                                            |
  | **Publisher**         | The publisher of the book.                                                                                 |
  | **Image-URL-S**       | The cover image of the book in Small size.                                                              |
  | **Image-URL-M**       | The cover image of the book in Medium size.                                                             |
  | **Image-URL-L**       | The cover image of the book in Large size.                                                              |

  Description in `Ratings.csv`

  | **Variable**    | **Description**                                                                                                                    |
  | --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
  | **User -ID**     | Unique ID of each user who provides a rating.                                                                             |
  | **ISBN**        | The identification number of the book. Each book with the same title but different publishers or release years will have a different ISBN. |
  | **Book-Rating** | The rating value given by the user for a particular book, usually in the range of 1 to 5.                                    |

  Description in `Users.csv`

  | **Variable** | **Description**                                                                                   |
  | ------------ | ----------------------------------------------------------------------------------------------- |
  | **User -ID**  | Unique ID for each user that has been anonymized into integer data.                      |
  | **Location** | The user's location consisting of country, state, and city/village, separated by commas.   |
  | **Age**      | The age of the user. |

- If visualized against the book authors' data, there are 10 authors with the most books or, in other words, the most productive.
![Top 10 Authors](Assets/Prolific%20Authors.png)

  The data shows that Agatha Christie is the most productive author among all authors in the dataset, followed by William Shakespeare and Stephen King.
- Then, the distribution of book ratings can be seen in the following visualization.
![Book Ratings](/Assets/book_rating.png)

  It can be seen that more user data did not provide ratings, indicated by a zero star (out of 10).
- Finally, the distribution of publication years from the dataset is displayed as follows.
![Year Publication Distribution](/Assets/distribution_year.png)

It appears that there are data entries for which the publication year of the book is unknown.

**Additional Notes**:
To understand the data, **`Exploratory Data Analysis (EDA)`** needs to be conducted. This stage is crucial for understanding the context of the existing data, such as the data shape, the number of data entries, and the content of the data itself. The details of the EDA conducted in this project will be explained in the [Data Preparation](#data-preparation) section.

## Data Preparation

![Data Clean Illustration](https://sp-ao.shortpixel.ai/client/to_auto,q_lossy,ret_img,w_1595/https://mammoth.io/wp-content/uploads/2024/02/data-preparation-with-mammoth.jpg)

At this stage, we perform EDA with the following details:
In all three datasets, we start by performing `drop_duplicates()` to eliminate duplicate data.

### Data Preparation for `df_books.csv`
- **Removing Duplicated Data**
There are duplicated data in the dataset, which is addressed at the beginning of the EDA process.
- **Feature Removal**
In the `books.csv` dataset, there are features that are not necessary for the recommendation system training process, so they can be removed, such as the novel cover images in sizes M, S, and L. If needed for visualization, that is acceptable, but in this project, they are not required for the model training process, so we can `drop` those columns.
- **Handling Missing Values**
There are 2 missing values in the publisher and Book-Author columns. Given the small number, we can apply dropna.
- **Renaming Features**
In `books.csv`, feature renaming is performed because the writing format is difficult to process in the next stages, necessitating renaming using the `.rename()` function.
- **Feature Selection**
The most important features selected for the subsequent training process are ISBN, book title, author name, and year of publication.

### Data Preparation for `df_ratings.csv`
- **Renaming Features**
In the `df_ratings.csv` dataset, there are characters in the feature names that need to be replaced to facilitate faster data processing, so a 'rename' operation is necessary.
After checking, it turns out that the `df_ratings.csv` dataset is quite clean, with no missing values, duplicated data, and features that are significant for building the recommendation system.

### Data Preparation for `df_users.csv`
This dataset has 3 columns: **User -ID**, **Location**, and **Age**.
- **Removing Missing Values**
In the **Age** column, there are 110,762 user data entries that lack data. With such a large number, it would be unfortunate to delete them all using the dropna method. Therefore, we can fill them using the Group-by Location method, where the tendency in region *A* has an average age of *X* years, so the empty data in region *A* will be filled with age *X* years.
- **Correcting Location Data**
Upon closer inspection, it turns out that the user location data has inconsistent and redundant inputs, such as USA, US, America, United States, etc. Therefore, the user performs data manipulation with Regex to only extract the country name.
- **Feature Selection**

### TF-IDF
Finally, we apply TF-IDF, a statistical method to measure the importance of a word in a document relative to other documents. In Content-based filtering, we use this to measure how important a title or author is from a dataset relative to other data collections in that dataset. The calculation involves counting the frequency of a word's occurrence in that document. Secondly, we calculate the Inverse Document Frequency, which is the ratio of the number of documents to the number of documents containing that word.

This stage is also performed to facilitate the process of creating the recommendation system model. In the first stage, sampling is done by taking a portion of the data from the entire dataset, specifically the first 10,000 data entries. This is because the dataset is too large and could lead to memory overflow, halting the modeling process. Secondly, the `Books.csv` and `Ratings.csv` data are merged using the ISBN data and the `left` method. Then, the dataframe is converted to a list using `.to_list()`.

**Additional Notes**: 
- `Sampling`: Taking a portion (the first 10,000 rows) from the entire dataset.
- `Merge`: Using the left join method, merging dataframes based on key columns and retaining the left side even if there are no matching pairs in the right dataframe. This is important so that each user interaction (e.g., rating) has complete context (e.g., book title, genre). It can generate combined features (e.g., book ratings based on genre, user age, etc.). The model has a complete representation of the user-item relationship.
- `Series to List`: The process of converting a series object to a list using the `.to_list()` method provided by the pandas library. The goal is to prepare the data before entering the modeling process that trains list-based data such as sklearn and matrix operations that we will perform in building the recommendation system.
- **Data Splitting**: The process of dividing the entire dataset into training and validation data. This process is performed during the modeling stage so that the model can train itself and also validate with new data outside the training data to test its generalization against new data. The splitting process is divided into 70% training data and 30% validation data.

## Model & Results

At this stage, the process of building and evaluating the book recommendation system is conducted to encourage increased reading interest among Indonesia's youth. This recommendation system is built using two main approaches: **Content-Based Filtering** and **Collaborative Filtering**, then presented in the form of Top-10 Recommendations as personalized output for each user.

### **Content-Based Filtering**
Content-Based Filtering recommends books based on content similarity with books previously liked or read by users. The content features used include:
- Authors

This model utilizes techniques such as:
- TF-IDF Vectorization on author names
- Cosine Similarity to measure similarity between authors

1. Using the `cosine similarity` method, which is a technique to measure the similarity between two vectors based on the angle between them. In this project, the **sklearn.metrics.pairwise** library is used to calculate `cosine similarity`.
2. The `author_recommendations()` function is used to provide recommendations based on author similarity **(Book-Author)**. This function likely takes the author's name as input and returns other books by the same author or authors with similar profiles.

The results of the model creation for Content-Based Filtering are shown with the following top N recommendations:

**Recommendations with the book previously read "The Diaries of Adam and Eve"**
| No | Book Title                                         | Book Author |
|-------|----------------------------------------------------|-------------|
| 1     | The Adventures of Tom Sawyer                       | Mark Twain  |
| 2     | The Adventures of Tom Sawyer                       | Mark Twain  |
| 3     | A Connecticut Yankee in King Arthur's Court (D...  | Mark Twain  |
| 4     | A Connecticut Yankee in King Arthur's Court        | Mark Twain  |
| 5     | A Connecticut Yankee in King Arthur's Court        | Mark Twain  |
| 6     | A Connecticut Yankee in King Arthur's Court        | Mark Twain  |
| 7     | A Connecticut Yankee in King Arthur's Court        | Mark Twain  |
| 8     | Treasury of Illustrated Classics: Adventures o...  | Mark Twain  |
| 9     | The Adventures of Tom Sawyer                       | Mark Twain  |
| 10    | The Adventures of Tom Sawyer                       | Mark
