
 <p align="Left">
  <img src="https://github.com/user-attachments/assets/a71b96af-89d0-451c-8ec2-f0a8b8022d9d" width="800" height="500" alt="Alt text">
   </p>

## Table of Contents

1. [Overview](#OVERVIEW)  
2. [Background & Problem Statement](#background--problem-statement) 
3. [Aim](#AIM)
4. [Tech Stack](#TECH-STACK)
5. [Data](#Dataset-Description)
6. [Model Building](#MODEL-BUILDING)
7. [Project Insights & Outcomes](#project-Insights--outcomes)   
8. [Challenges](#challenges)
9. [Future Enhancement](#Future-Enhancements)
10. [References](#references)  

## Overview
A content-based movie recommendation system built using Python, NLP techniques, and machine learning. The system leverages movie metadata from TMDB to recommend similar movies based on user-selected titles. A Streamlit web application provides an interactive interface for users to select a movie and view recommendations.


## Background & Problem Statement
Movie enthusiasts often seek recommendations based on their interests. Traditional recommendation systems may rely on collaborative filtering, but these can struggle with new or less popular movies.

**Problem Statement:**

The challenge is to build a recommendation system that can accurately suggest similar movies based on content (metadata) alone. This involves processing multiple attributes of movies—such as genres, overviews, keywords, cast, and crew—to build a model that can capture the context of each film and return relevant recommendations.

## Aim
- **Develop a content-based recommendation engine** that utilizes movie metadata to generate movie suggestions based on the similarity score.
- **Create an interactive web application** using Streamlit, where users can easily select a movie and view recommendations.

## Tech Stack

- **Programming Language:**
   - Python
- **Libraries & Frameworks:**
  - **pandas & numpy:** For data manipulation and numerical operations.
  - **nltk:** For natural language processing (tokenization, stemming).
  - **scikit-learn:** For feature extraction (CountVectorizer) and computing cosine similarity.
  - **pickle:** For serializing processed data and similarity matrices.
  - **Streamlit:** For building the interactive web application.
- **Development Environment:**
  - Jupyter Notebook for experimentation and development
- **Web Framework:**
  - **Streamlit:** For building an interactive web application that allows users to select a movie from a dropdown menu and get recommendations in real time.

## Dataset Description

The project uses two datasets from TMDB:

**tmdb_5000_movies.csv:**  Contains movie details such as id, title, genres, overview, and keywords.<br>
**tmdb_5000_credits.csv:**  Contains additional information on cast and crew for each movie.

These datasets are merged on the common column title and further processed to create a consolidated view for recommendation.

**Link to the dataset**<br>
Dataset TMDB 5000 Movies:https://tinyurl.com/5000-movies<br>
Dataset TMDB 5000 credits:https://tinyurl.com/5000-credits

## Data Preparation & Pre-processing

1) **Data Cleaning & Merging:**
    - Retain only useful features: id, genres, overview, keywords, title (from movies) and title, cast, crew (from credits).
    - Merge datasets on the title column and drop rows with missing values.

2) **Processing Textual Data:**

    - Convert string representations of lists (for genres, keywords, cast, and crew) into actual lists using ast.literal_eval.
    - Extract relevant attributes:
      - From genres and keywords: extract the name field.
      - From cast: extract up to the first 5 names.
      - From crew: extract up to the first 2 names and remove duplicates.
      - Tokenize the overview text using nltk.word_tokenize.
    - Tokenize the overview text using nltk.word_tokenize.

3) **Creating a Unified Tags Column:**
    - Combine the processed genres, overview tokens, keywords, cast, and crew into a single tags column.
    - Process the tags by:
      - Removing spaces within words.
      - Filtering non-alphanumeric characters using regex.
      - Converting the text to lowercase.
      - applying stemming (using PorterStemmer) to reduce words to their root forms.
    
4) **Feature Extraction:**
    - Use CountVectorizer to convert the tags into numerical feature vectors (with a maximum of 5000 features and English stop words removal).
    - Compute the cosine similarity between movie vectors to quantify the similarity between films.

5) **Saving Processed Data:**
    - The processed movies data and similarity matrix are saved using pickle for later use in the web app.

## Model Building
The recommendation engine is built on the following steps:

- **Feature Extraction:**
  The tags for each movie are vectorized using CountVectorizer with a maximum of 5000 features and English stopwords removal.

- **Similarity Computation:**
  Cosine similarity is calculated on the vectorized data, providing a measure of how similar each movie is to every other movie.

- **Recommendation Function:**
  A function **recommend(title)** is defined that:

  - Finds the index of the movie in the dataset.
  - Sorts movies based on similarity scores.
  - Returns the top 5 recommendations (movie IDs and titles).

## Usage
1) **Data Processing & Model Building:**
    - Run the data pre-processing and model-building scripts to generate the processed movie dataset and similarity matrix.

2) **Recommendation Function:**
    - Call the recommend(title) function by passing a movie title (e.g., 'Batman Begins') to receive a list of similar movies.

3) **Web Application:**
    - Launch the Streamlit web app which provides an interactive interface to select a movie from a dropdown menu and display recommendations in real time.
  
## Project Insights & Outcomes

- **Content-Based Recommendations:**
    The system successfully generates movie recommendations based on the content features extracted from movie metadata.

- **Improved User Experience:**
    The interactive Streamlit web app makes it easy for users to explore movie suggestions.

- **Performance Evaluation:**
    Cosine similarity has proven effective in capturing the context and similarity between movies, leading to relevant recommendations.

- **Scalability:**
    The modular design of the data pre-processing and recommendation function allows for easy scaling and future improvements.

## Challenges

- Data Quality:

   - Ensuring the consistency and correctness of movie metadata.
   - Handling missing or malformed data entries.
  
- Text Processing Complexity:

   - Processing and combining multiple text sources (genres, overview, keywords, cast, crew) requires careful cleaning and transformation.

- Feature Engineering:

   - Creating a unified and meaningful tags column that accurately represents each movie.

- Balancing Performance:

   - Optimizing the system to provide fast recommendations while handling a large dataset.

## Future Enhancements

- User Feedback Integration:

   - Incorporate user ratings to refine recommendations.
     
- Hybrid Recommendation System:

   - Combine content-based filtering with collaborative filtering to further improve accuracy.

- Advanced NLP Techniques:

   - Experiment with more sophisticated NLP models (e.g., Word2Vec, BERT) for improved feature extraction.

- Deployment:

   - Deploy the web app on cloud platforms for broader accessibility and real-time performance improvements.

## References

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
