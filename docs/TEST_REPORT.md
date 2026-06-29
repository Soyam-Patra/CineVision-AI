# Functional Test Report

## Environment

* **OS:** Windows 11
* **Python:** 3.x
* **Frontend:** React (Vite)
* **Backend:** FastAPI
* **Face Recognition:** InsightFace (ArcFace)
* **Vector Search:** FAISS
* **Database:** SQLite

---

## Image Upload

| Test                | Status                                         |
| ------------------- | ---------------------------------------------- |
| JPG Upload          | ✅ Passed                                       |
| PNG Upload          | ✅ Passed                                       |
| JPEG Upload         | ✅ Passed                                       |
| Invalid File Upload | ✅ Passed (Unsupported file types are rejected) |

---

## Face Detection

| Test           | Status                                 |
| -------------- | -------------------------------------- |
| Single Face    | ✅ Passed                               |
| Multiple Faces | ✅ Passed                               |
| No Face        | ✅ Passed ("No face detected" returned) |

---

## Face Recognition

| Test                      | Status   |
| ------------------------- | -------- |
| Correct Actor Recognition | ✅ Passed |
| Confidence Score Display  | ✅ Passed |
| Actor Selection           | ✅ Passed |

---

## Recommendation Engine

| Test                   | Status   |
| ---------------------- | -------- |
| Top 10 Movies Returned | ✅ Passed |
| IMDb Ratings           | ✅ Passed |
| Genres                 | ✅ Passed |
| Runtime                | ✅ Passed |
| Posters                | ✅ Passed |
| Movie Overview         | ✅ Passed |
| Trailer Links          | ✅ Passed |

---

## Additional Tests

| Test                     | Result   |
| ------------------------ | -------- |
| 6 Face Detection         | ✅ Passed |
| Unknown Object (No Face) | ✅ Passed |
| Invalid File Upload      | ✅ Passed |
| Multiple Actor Selection | ✅ Passed |
| Re-upload New Image      | ✅ Passed |

---

## REST API Testing

| Endpoint            | Status   |
| ------------------- | -------- |
| GET /health         | ✅ Passed |
| POST /predict       | ✅ Passed |
| GET /movies/{actor} | ✅ Passed |

---

## Error Handling

| Test                | Status       |
| ------------------- | ------------ |
| Invalid File Upload | ✅ Passed    |
| No Face Found       | ✅ Passed    |
| Backend Offline     | ✅ Passed    |

---

## Overall Result

**PASS ✅**

All functional requirements specified in the assignment were successfully verified. The application correctly performs actor recognition, multi-face detection, movie recommendation, REST API communication, and frontend interaction under normal operating conditions.
