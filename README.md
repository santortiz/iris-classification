# Iris Species Prediction API

## 📘 Overview
This application is a machine learning-powered API designed to predict the species of Iris flowers based on their morphological features (sepal length, sepal width, petal length, and petal width). It is built using **FastAPI** and exposes a REST endpoint for making predictions.

### 🌟 Features
- Predict the species of an Iris flower: *Setosa*, *Versicolor*, or *Virginica*.
- Optionally return predictions as numeric labels (0, 1, 2).
- Scalable and easy-to-integrate API.

---

## 🧠 Model Training and Selection
The machine learning model used in this API is trained on the famous Iris dataset. Here are the steps involved in training and selecting the best model:

1. **Preprocessing:**
   - Data was standardized using a scaler to ensure features are on the same scale.
2. **Model Selection:**
   - Various models were evaluated, including Logistic Regression, SVM, and Random Forest.
   - Performance was compared using cross-validation metrics.
3. **Best Model:**
   - The model with the highest accuracy and generalization capability was selected.
   - The chosen model and the scaler were serialized using **pickle**.

Both the trained model and the scaler are loaded during runtime to make predictions.

---

## 🚀 How to Use the API

### 1️⃣ Endpoint: `/predict`
- **Method:** `POST`
- **Description:** Predicts the species of an Iris flower based on input features.

### 2️⃣ Request Format:
Send a JSON payload with the following structure:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Optional query parameter:
- `return_label`: Set to `true` to receive the species as a numeric label (default: `false`).

### 3️⃣ Response Format:
The API responds with the predicted species in JSON format:

- **If `return_label=false` (default):**
  ```json
  {
    "species": "setosa"
  }
  ```

- **If `return_label=true`:**
  ```json
  {
    "species": 0
  }
  ```

---

## 📋 Examples

### Example 1: Predict Species by Features
**Request:**
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

**Response:**
```json
{
  "species": "setosa"
}
```

### Example 2: Return Numeric Label
**Request:**
```bash
curl -X POST "http://127.0.0.1:8000/predict?return_label=true" \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

**Response:**
```json
{
  "species": 0
}
```

---

## 🛠️ Development

### Prerequisites
- Python 3.8+
- Install dependencies using `pip install -r requirements.txt`.

### Running the App
Start the FastAPI server locally:
```bash
uvicorn main:app --reload
```

The API will be accessible at `http://127.0.0.1:8000`.

### Testing
You can test the API using tools like **curl**, **Postman**, or **FastAPI's interactive Swagger UI** at `http://127.0.0.1:8000/docs`.

---

## 🤖 Environment Variables
- `BEST_MODEL_PATH`: Path to the serialized best model file.
- `SCALER_PATH`: Path to the serialized scaler file.

Ensure these files are available and correctly referenced in the environment before running the app.

---

## 👥 Contributors

Santiago Ortiz \
+57 3234921342 \
sant3765@gmail.com

