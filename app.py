import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Customer Segmentation Engine", layout="wide")
st.title("🤖 AI Customer Segmentation Tool")
st.markdown("Use this dashboard to analyze customer behavior and get AI-driven marketing strategies.")

@st.cache_data
def load_data():
    # We use the file you generated earlier
    data = pd.read_csv('rfm_final_labeled.csv', index_col=0)
    return data

df = load_data()

# --- SIDEBAR ---
st.sidebar.header("Filter Options")
selected_segment = st.sidebar.multiselect(
    "Select Segments to View",
    options=df['Segment'].unique(),
    default=df['Segment'].unique()
)
df_filtered = df[df['Segment'].isin(selected_segment)]

# --- MAIN METRICS ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", df_filtered.shape[0])
col2.metric("Avg Spend", f"£{df_filtered['Monetary'].mean():.2f}")
col3.metric("Avg Recency", f"{df_filtered['Recency'].mean():.0f} Days")

# --- CHART ---
st.subheader("Customer Clusters Visualized")
fig = plt.figure(figsize=(10, 5))
sns.scatterplot(
    data=df_filtered, x='Recency', y='Monetary', hue='Segment', palette='viridis', s=60, alpha=0.6
)
plt.title("Recency vs. Monetary (Filtered)")
st.pyplot(fig)

# --- LOOKUP TOOL ---

st.markdown("---")
st.subheader("🔍 Individual Customer Lookup")


customer_ids = df.index.tolist()

# The Magic Dropdown (Searchable)
selected_customer_id = st.selectbox(
    "Select a Customer ID to view their profile:",
    options=customer_ids
)

if st.button("Generate Strategy"):

    customer = df.loc[selected_customer_id]
    segment = customer['Segment']
    
    st.success(f"Customer Found! Segment: **{segment}**")
    
    c1, c2, c3 = st.columns(3)
    c1.write(f"**Last Seen:** {customer['Recency']:.0f} days ago")
    c2.write(f"**Frequency:** {customer['Frequency']:.0f} orders")
    c3.write(f"**Total Spent:** £{customer['Monetary']:.2f}")
    
    if segment == 'VIP':
        st.info("🌟 **Action:** Send personal Thank You note. Offer early access.")
    elif segment == 'Potential Loyalist':
        st.warning("📈 **Action:** Upsell. Offer a 'Spend £50 get Free Shipping' coupon.")
    elif segment == 'Lost':
        st.error("💤 **Action:** Re-activate. Send 'We Miss You' email with 10% discount.")
