from flask import Flask, render_template, request, redirect, session, jsonify
import pandas as pd
import cv2
import pickle
import numpy as np
import os

app = Flask(__name__)
app.secret_key = "premium_data_engineering_portfolio"

# ---------------- LOAD & SYNC DATA ----------------
def load_data():
    try:
        df_cart_items = pd.read_csv("csv/cart_items.csv")
        df_products = pd.read_csv("csv/products.csv")
        df_carts = pd.read_csv("csv/carts.csv")

        df_cart_items['revenue'] = pd.to_numeric(df_cart_items['revenue'], errors='coerce').fillna(0)
        df_cart_items['quantity'] = pd.to_numeric(df_cart_items['quantity'], errors='coerce').fillna(0)

        return df_cart_items, df_products, df_carts
    except Exception as e:
        print(f"Error loading CSVs: {e}")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

# ---------------- LOAD FACE MODEL ----------------
try:
    with open('data/names.pkl', 'rb') as f:
        LABELS = pickle.load(f)
    with open('data/faces_data.pkl', 'rb') as f:
        FACES = pickle.load(f)

    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(FACES, LABELS)
    facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
    face_model_loaded = True
except:
    face_model_loaded = False

# ---------------- ROUTES ----------------

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] == "Rohit" and request.form["password"] == "Rohit@10":
            session["user"] = "Rohit"
            return redirect("/home")
        error = "Invalid credentials"
    return render_template("login.html", error=error)

@app.route("/face_login")
def face_login():
    if not face_model_loaded: return redirect("/")
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        if not ret: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            crop_img = cv2.resize(gray[y:y+h, x:x+w], (50, 50)).flatten().reshape(1, -1)
            name = str(knn.predict(crop_img)[0])
            if name == "Rohit":
                video.release()
                cv2.destroyAllWindows()
                session["user"] = name
                return redirect("/home")
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    video.release()
    cv2.destroyAllWindows()
    return redirect("/")

@app.route("/home")
def home():
    if "user" not in session: return redirect("/")
    
    df_items, df_prod, df_carts = load_data()

    total_revenue = float(df_items["revenue"].sum())
    total_orders = int(df_carts["cart_id"].nunique() if not df_carts.empty else df_items["cart_id"].nunique())
    total_qty = int(df_items["quantity"].sum())
    avg_cart_val = float(total_revenue / total_orders if total_orders > 0 else 0)
    
    null_count = df_items.isnull().sum().sum() + df_prod.isnull().sum().sum()
    total_cells = df_items.size + df_prod.size
    data_health = round(((total_cells - null_count) / total_cells) * 100, 1) if total_cells > 0 else 100

    top_products = df_items.groupby("product_name")["revenue"].sum().sort_values(ascending=False).head(5).to_dict()

    try:
        merged_df = pd.merge(df_items, df_prod[['product_name', 'category']], on='product_name', how='left')
        cat_revenue = merged_df.groupby("category")["revenue"].sum().to_dict()
    except:
        cat_revenue = {"Uncategorized": total_revenue}

    order_status = df_carts["status"].value_counts().to_dict() if "status" in df_carts.columns else {"Completed": 10}

    return render_template("index.html",
                           total_revenue=total_revenue,
                           total_orders=total_orders,
                           total_products=total_qty,
                           avg_cart_value=avg_cart_val,
                           data_health=data_health,
                           top_products=top_products,
                           cat_dist=cat_revenue,
                           order_status=order_status)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)