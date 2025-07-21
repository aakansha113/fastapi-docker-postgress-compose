from fastapi import FastAPI  # ✅ Correct class name and import

app = FastAPI()  # ✅ Now instantiate it here

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI inside Docker!"}

@app.get("/hello/")
def hello():
    return{"message":"hii iam am hello"}

@app.get("/welcome/")
def welcome():
    return{"message":"hello welcome"}

@app.get("/home/")
def home():
    return{"message":"its home tab"}