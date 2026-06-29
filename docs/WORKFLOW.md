# Workflow Report

# AI/ML Engineer Hiring Assignment

## Project Title

**CineVision AI – AI Powered Movie Recommendation System Using Actor Face Recognition**

---

# 1. Objective

The objective of this project is to build an end-to-end AI application capable of recognizing actors from uploaded images and recommending their highest-rated movies through an interactive web interface.

The application combines computer vision, vector similarity search, database querying and REST APIs to deliver real-time movie recommendations.

---

# 2. Technology Stack

## Backend

- Python
- FastAPI
- InsightFace (ArcFace)
- FAISS
- SQLite
- OpenCV
- NumPy
- Uvicorn

## Frontend

- React
- Vite
- Axios
- CSS

## Data

- IMDb Movie Metadata
- TMDB Enriched Metadata
- Actor Face Dataset

---

# 3. Dataset Preparation

The project consists of two primary datasets:

### Actor Dataset

A collection of actor images was used to build the facial recognition database.

Each actor contains multiple images representing different poses, expressions and lighting conditions.

### Movie Dataset

The movie metadata includes:

- Movie title
- Actor names
- IMDb rating
- Genres
- Release year
- Runtime
- Poster path
- Overview
- Trailer key
- Popularity
- TMDB rating

The movie data was stored in a SQLite database for fast querying.

---

# 4. Face Embedding Generation

Instead of storing raw images for recognition, facial embeddings were generated.

The process involved:

1. Reading every actor image.
2. Detecting the face using InsightFace.
3. Extracting ArcFace embeddings.
4. Normalizing embeddings.
5. Saving embeddings for future inference.

Generated files:

- embeddings.npy
- metadata.pkl

This preprocessing step allows inference without requiring the original training images.

---

# 5. FAISS Index Creation

The generated embeddings were indexed using Facebook AI Similarity Search (FAISS).

The FAISS index enables extremely fast nearest-neighbor search among thousands of actor embeddings.

During inference:

- The uploaded image embedding is generated.
- FAISS searches for the closest embeddings.
- Multiple nearest neighbors are considered.
- A weighted voting mechanism determines the final actor prediction.

---

# 6. Database Creation

Movie metadata was imported into SQLite.

Each record stores:

- Actor names
- IMDb rating
- Genres
- Runtime
- Poster path
- Overview
- Trailer information

Recommendations are retrieved using SQL queries and sorted by IMDb rating.

---

# 7. Backend Development

The backend was implemented using FastAPI.

Main responsibilities include:

- Accepting uploaded images
- Detecting faces
- Generating embeddings
- Querying the FAISS index
- Recognizing actors
- Fetching recommended movies
- Returning structured JSON responses

The backend exposes REST APIs that communicate with the frontend.

---

# 8. Frontend Development

The frontend was developed using React.

Major components include:

- Image Upload
- Actor Selector
- Actor Information Card
- Movie Cards
- Movie Grid
- Face Overlay

The interface supports:

- Image preview
- Multiple actor selection
- Responsive movie recommendations
- Trailer links
- Error handling

---

# 9. Recognition Pipeline

The complete inference pipeline is:

1. User uploads an image.
2. Backend receives the image.
3. InsightFace detects all faces.
4. ArcFace embeddings are generated.
5. FAISS searches the nearest embeddings.
6. Weighted similarity determines the actor.
7. SQLite retrieves matching movies.
8. Top 10 movies are returned.
9. React renders recommendations.

---

# 10. REST APIs

The following APIs were implemented.

## POST /predict

Accepts an image and returns:

- Number of faces
- Actor names
- Confidence score
- Bounding boxes
- Recommended movies

---

## GET /movies/{actor}

Returns the top movies for a specified actor.

---

## GET /health

Health endpoint for checking backend availability.

---

# 11. Testing

The application was tested for the following scenarios:

- JPG Upload
- PNG Upload
- JPEG Upload
- Invalid File Upload
- Single Face Detection
- Multiple Face Detection
- No Face Detection
- Actor Recognition
- Recommendation Retrieval
- API Testing
- Backend Failure Handling

Detailed results are documented in:

**TEST_REPORT.md**

---

# 12. Challenges Faced

During development several challenges were encountered.

### Large-scale embedding generation

Generating embeddings for over six thousand actors required preprocessing and efficient storage.

### Multi-face recognition

The system needed to correctly identify multiple actors from a single uploaded image while allowing the user to switch between recommendations.

### Recommendation quality

Recommendations were sorted using IMDb ratings while enriching each result with posters, trailers and movie metadata.

### Frontend integration

React components were connected with FastAPI through Axios while maintaining responsive user interaction.

---

# 13. Future Improvements

Potential improvements include:

- User authentication
- Cloud deployment
- Vector database integration
- Personalized movie recommendations
- Semantic movie search
- Actor biography generation using LLMs
- Recommendation explanations
- Better confidence calibration
- Recommendation caching
- CI/CD pipeline

---

# 14. Conclusion

The project successfully combines modern AI techniques with full-stack web development to build a complete movie recommendation system.

The application demonstrates:

- Face Detection
- Face Recognition
- Vector Similarity Search
- Database Querying
- REST API Development
- React Frontend Integration

# 15. Project Statistics

- Actors Processed: **6,255**
- Face Embeddings Generated: **11,223**
- Images Without Detectable Faces: **51**
- Multi-face Reference Images: **53**
- Recommendation Database: **IMDb + TMDB Enriched SQLite**
- Similarity Search Engine: **FAISS**
- Recognition Model: **InsightFace (ArcFace)**
- Frontend: **React + Vite**
- Backend: **FastAPI**

The final system provides an intuitive workflow for recognizing actors and recommending their highest-rated movies through an end-to-end AI application.