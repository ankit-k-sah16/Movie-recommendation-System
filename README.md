# 🎬 Movie Recommendation System using TMDB 5000 Dataset

## 🚀 Overview

This project is a content-based movie recommendation system built using the TMDB 5000 dataset. The system suggests movies similar to a given input by analyzing features such as genres, keywords, cast, and crew.

The goal of this project is to demonstrate how machine learning techniques can be used to build personalized recommendation systems, similar to platforms like Netflix or Amazon Prime.

## 🎯 Key Features

🎥 Recommends movies based on user input

🔍 Uses content-based filtering approach

🧠 Considers multiple features: genres, keywords, cast, crew

⚡ Fast similarity-based recommendations

📊 Clean and structured data preprocessing pipeline

## 🛠️ Tech Stack

Language: Python

Libraries: Pandas, NumPy, Scikit-learn

NLP Techniques: Text vectorization (CountVectorizer / TF-IDF)

Similarity Measure: Cosine Similarity

Environment: Jupyter Notebook

## 🧠 Methodology

1. Data Preprocessing

     Merged datasets (movies + credits)

     Handled missing values

     Extracted important features:
                    Genres
                    Keywords
                    Cast (top actors)
                    Director

2. Feature Engineering

    Converted textual data into a single “tags” column

    Applied text cleaning:
                   Lowercasing
                   Removing spaces
    Used vectorization to convert text into numerical format

3. Model Building

   Applied CountVectorizer / TF-IDF to generate feature vectors

   Calculated similarity using cosine similarity

   Built a recommendation function that returns top similar movies

## 📂 Dataset

 Dataset Used: TMDB 5000 Movie Dataset

 Contains:

   Movie metadata
    
   Cast and crew details
    
   Keywords and genres

   
## ⚙️ How It Works

   User inputs a movie name
    
   System finds the movie in dataset
    
   Computes similarity scores
    
   Recommends top 5–10 similar movies

## 📸 Output

  Displays list of recommended movies
  
  Based on similarity scores

 


##💡 What I Learned

   Building recommendation systems from scratch
   
   Applying NLP techniques for feature extraction
   
   Understanding cosine similarity and vector space models
   
   Data preprocessing and feature engineering
   
   Designing efficient lookup systems

## 🚧 Future Improvements

   Add collaborative filtering
   
   Build a hybrid recommendation system
   
   Deploy using Streamlit / Web App
   
   Add movie posters using TMDB API
   
   Improve recommendations using embeddings (Word2Vec / BERT)


## 📌 Applications

  OTT platforms (Netflix, Prime Video)
  
  E-commerce recommendations
  
  Personalized content systems

-------

## 🧑‍💻 Author

Ankit Kumar Sah

Data Science & AI Enthusiast
 
