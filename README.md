### 1. Prepare the backend

Put the trained model in `backend/models`
the link to the trained model is [here](https://drive.google.com/file/d/1n_hKnoGmPQ63CV6WjMw_4zLlc7Tzh_ZT/view?usp=sharing)

Put all the photos in `backend/photos`
with this structure:

```
photos
├── 331707239_781362983711955_8696776923217120552_n.jpg
├── 331697911_479660887546410_5536338796589273170_n.jpg
```

### 2. Install the dependencies for the backend

```bash
cd backend
pip install -r requirements.txt
```

### 3. Run the backend

```bash
fastapi run
```

### 4. Install the dependencies for the frontend

```bash
cd frontend
npm install
```

### 5. Run the frontend

```bash
npm start
```

### 6. Open the browser

Open the browser and go to `http://localhost:3000`
