# MovieRecommender

# Movie Recommendation System

## Project Description
The Movie Recommendation System is a content-based recommendation engine that suggests movies based on user-selected movie attributes such as genres, cast, director, and tags. This system leverages machine learning techniques to compute similarity between movies and recommend the most relevant ones. It uses a **Bag-of-Words (BoW)** model for text vectorization and **cosine similarity** to determine similarity scores. 

The recommendation system is built with **Python** and utilizes libraries such as **pandas**, **scikit-learn**, and **Streamlit** for the implementation and deployment of the interactive user interface.

## What I've Done
- Developed the recommendation system using **content-based filtering**, where movie metadata such as genres, cast, director, and tags are used to make movie suggestions.
- Engineered features by combining movie metadata to create a meaningful representation for similarity calculation.
- Implemented a **Bag-of-Words (BoW)** model for vectorizing the text data (e.g., movie descriptions) and used **cosine similarity** to compute pairwise similarities between movies.
- Designed an intuitive and interactive user interface using **Streamlit**, allowing users to search for movies and receive personalized recommendations.
- Optimized the system to recommend the **top 5 most similar movies** to the user-selected title based on high accuracy and relevance.

## Key Technologies
- **Python**: Programming language used for the system.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For implementing machine learning algorithms, specifically cosine similarity and feature engineering.
- **Streamlit**: To create an interactive web-based user interface.

## How It Works
1. **User Input**: The user selects a movie from the dataset.
2. **Feature Extraction**: The system extracts key attributes (e.g., genres, cast, director) of the selected movie.
3. **Similarity Calculation**: The system computes the similarity between the selected movie and all others using cosine similarity based on their metadata.
4. **Recommendation**: The top 5 most similar movies are displayed for the user, providing personalized suggestions.

## Conclusion
This project demonstrates the power of content-based filtering for personalized movie recommendations, offering an engaging and interactive experience for users to discover new movies based on their preferences.
