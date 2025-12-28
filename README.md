# 🛒 AI-Driven Customer Segmentation Engine

### 🚀 **Live Demo:** [INSERT YOUR STREAMLIT APP LINK HERE]

## 📌 Project Overview
In the highly competitive retail landscape, treating every customer the same is a recipe for inefficiency. This project solves that problem by building an **Unsupervised Machine Learning pipeline** to segment customers based on their purchasing behavior. 

Using the **RFM (Recency, Frequency, Monetary)** framework, I analyzed over 500,000 transactions to identify distinct customer personas. The final model feeds into an interactive **Streamlit Dashboard** that allows marketing teams to visualize segments and generate instant, AI-driven strategies for individual customers.

## 🛠️ Tech Stack
* **Language:** Python 3.9
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (K-Means Clustering)
* **Visualization:** Matplotlib, Seaborn
* **Deployment:** Streamlit Cloud

## 📊 Methodology

### 1. Data Engineering
* **Cleaning:** Processed raw transaction logs (Online Retail Dataset), handling missing values and filtering out cancelled orders (negative quantities).
* **Feature Extraction:** Transformed transaction-level data into customer-level metadata using **RFM Analysis**:
    * **Recency:** Days since last purchase.
    * **Frequency:** Total number of transactions.
    * **Monetary:** Total revenue generated.

### 2. Preprocessing & Scaling
* **Log Transformation:** Applied to handle the extreme right-skewness of the data (since spending follows a Power Law distribution).
* **Standardization:** Used `StandardScaler` to normalize metrics, ensuring the K-Means algorithm treats Recency (days) and Monetary ($) equally.

### 3. Machine Learning (K-Means)
* **Elbow Method:** Used to determine the optimal number of clusters ($K=3$).
* **Clustering:** The algorithm grouped customers into three distinct segments based on multi-dimensional distance.

## 💡 Results: Customer Segments identified
The model identified 3 clear actionable personas:

| Segment | Characteristics | Strategy |
| :--- | :--- | :--- |
| **🥇 VIP** | High spenders, frequent buyers, recent activity. | **Retain:** VIP access, exclusive offers, no discounts needed. |
| **📈 Potential Loyalist** | Moderate spenders, active recently. | **Upsell:** Loyalty programs, cross-selling to boost basket size. |
| **💤 Lost / At-Risk** | Low spenders, haven't purchased in months. | **Reactivate:** Aggressive discounts or "We Miss You" campaigns. |

## 🖥️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/customer-segmentation-app.git](https://github.com/your-username/customer-segmentation-app.git)
   cd customer-segmentation-app

   Install dependencies

Bash

pip install -r requirements.txt
Run the app

Bash

streamlit run app.py
Created by **Ritesh Bastola**
