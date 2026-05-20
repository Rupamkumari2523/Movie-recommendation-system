# 🎬 Movie Recommendation System

An AI-powered **Content-Based Movie Recommendation System** built using **Machine Learning** and **Streamlit**.  
The system recommends movies similar to a selected movie by analyzing movie metadata such as genres, keywords, cast, crew, and overview.



## 📸 Application Preview
<img width="1919" height="922" alt="home" src="https://github.com/user-attachments/assets/b1931bf1-2b5d-4d26-90ff-5d1e82fdbfec" />


---

## 🚀 Features

✅ Content-Based Movie Recommendation  
✅ Interactive Streamlit User Interface  
✅ Movie Poster Fetching using TMDB API  
✅ Cosine Similarity Recommendation Engine  
✅ Fast & Dynamic Recommendations  
✅ Jupyter Notebook for Model Training  
✅ Clean and Responsive UI  

---

## 🧠 Machine Learning Workflow

The recommendation system follows these steps:

1. Data Collection using Kaggle TMDB datasets  
2. Data Cleaning & Preprocessing  
3. Feature Extraction  
4. Combining Important Tags  
5. Text Vectorization using CountVectorizer  
6. Similarity Calculation using Cosine Similarity  
7. Recommendation Generation  

---

## 🛠️ Technologies Used

### 👨‍💻 Programming Language
- Python

### 📚 Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- NLTK

### 🎯 Machine Learning Techniques
- NLP
- Vectorization
- Cosine Similarity
- Content-Based Filtering

---

## 📂 Project Structure

```bash
Movie-recommendation-system/
│ 
│
├── app.py
├── movie-recommender-system.ipynb
├── movies.pkl
├── similarity.pkl
├── README.md
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset** collected from **Kaggle**.

🔗 Dataset Source:  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

### Dataset Includes:
- Movie Titles
- Genres
- Keywords
- Cast
- Crew
- Overview
- Popularity
- Production Companies

---

## 🧠 Model Training Notebook

📌 [Open Jupyter Notebook](./movie-recommender-system.ipynb)

The notebook contains:
- Data preprocessing
- Feature engineering
- Vectorization
- Similarity matrix generation
- Model creation

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rupamkumari2523/Movie-recommendation-system.git
```

---

### 2️⃣ Navigate to Project Folder

```bash
cd Movie-recommendation-system
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

- Add Collaborative Filtering
- Deploy Online using Streamlit Cloud
- Improve Recommendation Accuracy
- Add User Authentication
- Add Search Suggestions
- Add Movie Ratings & Reviews

---

## 🌐 API Used

This project uses the **TMDB API** to fetch movie posters and movie details dynamically.



