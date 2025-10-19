
import streamlit as st
import requests
import time

# Page configuration
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .churn-yes {
        background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
        border-left: 5px solid #e17055;
    }
    .churn-no {
        background: linear-gradient(135deg, #a8e6cf 0%, #56c596 100%);
        border-left: 5px solid #00b894;
    }
    h1 {
        color: #2d3436;
        font-weight: 700;
        text-align: center;
        padding: 1rem 0;
    }
    .section-header {
        color: #667eea;
        font-weight: 600;
        font-size: 1.3rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #667eea;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("# E-Commerce Customer Churn Predictor")
st.markdown("### Predict customer retention with AI-powered analytics")
st.markdown("---")

# Sidebar for additional info
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/customer-insight.png", width=80)
    st.markdown("## 📋 About")
    st.info(
        """
        This tool helps predict whether a customer is likely to churn 
        based on their behavior and demographics.
        
        **How to use:**
        1. Fill in customer details
        2. Click 'Predict Churn'
        3. View results and probability
        """
    )
    
    st.markdown("---")
    st.markdown("### 🎯 Prediction Factors")
    st.markdown("""
    - Customer tenure
    - Shopping behavior
    - Satisfaction scores
    - Order patterns
    - Payment preferences
    """)

# Create tabs for better organization
tab1, tab2, tab3 = st.tabs(["👤 Demographics", "🛍️ Shopping Behavior", "📦 Order Details"])

with tab1:
    st.markdown('<div class="section-header">Customer Demographics</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        Tenure = st.number_input("📅 Tenure (months)", min_value=0, step=1, help="How long the customer has been with us")
        Gender = st.selectbox("👥 Gender", ["Male", "Female"])
        MaritalStatus = st.selectbox("💑 Marital Status", ["Single", "Married"])
    
    with col2:
        CityTier = st.selectbox("🏙️ City Tier", [1, 2, 3], help="1 = Metro, 2 = Tier-2, 3 = Tier-3")
        NumberOfAddress = st.number_input("🏠 Number of Addresses", min_value=1)
        WarehouseToHome = st.number_input("📍 Warehouse to Home Distance (km)", min_value=0.0)

with tab2:
    st.markdown('<div class="section-header">Shopping Preferences & Behavior</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        PreferredLoginDevice = st.selectbox("📱 Preferred Login Device", ["Mobile Phone", "Computer"])
        PreferredPaymentMode = st.selectbox("💳 Preferred Payment Mode", 
                                            ["Debit Card", "Credit Card", "UPI", "Cash on Delivery"])
        PreferredOrderCat = st.selectbox("🛒 Preferred Order Category", 
                                         ["Laptop & Accessory", "Mobile", "Fashion", "Grocery"])
    
    with col2:
        HourSpendOnApp = st.number_input("⏱️ Hours Spent on App (per day)", min_value=0.0, step=0.5)
        NumberOfDeviceRegistered = st.number_input("📲 Number of Devices Registered", min_value=1)
        CouponUsed = st.number_input("🎟️ Coupons Used", min_value=0)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        SatisfactionScore = st.slider("⭐ Satisfaction Score", 1, 5, 3)
        st.markdown(f"**Current Rating:** {'⭐' * SatisfactionScore}")
    with col2:
        Complain = st.selectbox("⚠️ Any Complaint Filed?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

with tab3:
    st.markdown('<div class="section-header">Order History & Patterns</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        OrderCount = st.number_input("📦 Total Order Count", min_value=1)
        DaySinceLastOrder = st.number_input("📅 Days Since Last Order", min_value=0)
        OrderAmountHikeFromlastYear = st.number_input("📈 Order Amount Hike from Last Year (%)", min_value=0.0)
    
    with col2:
        CashbackAmount = st.number_input("💰 Total Cashback Amount", min_value=0.0)
        
        # Display some calculated metrics
        if OrderCount > 0:
            avg_days_between_orders = DaySinceLastOrder / OrderCount if OrderCount > 0 else 0
            st.metric("📊 Avg Days Between Orders", f"{avg_days_between_orders:.1f}")

# Prediction section
st.markdown("---")
st.markdown('<div class="section-header">🔮 Generate Prediction</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🚀 Predict Churn", use_container_width=True)

if predict_button:
    with st.spinner('🔄 Analyzing customer data...'):
        input_data = {
            "Tenure(months)": Tenure,
            "PreferredLoginDevice": PreferredLoginDevice,
            "CityTier": CityTier,
            "WarehouseToHome": WarehouseToHome,
            "PreferredPaymentMode": PreferredPaymentMode,
            "Gender": Gender,
            "HourSpendOnApp": HourSpendOnApp,
            "NumberOfDeviceRegistered": NumberOfDeviceRegistered,
            "PreferredOrderCat": PreferredOrderCat,
            "SatisfactionScore": SatisfactionScore,
            "MaritalStatus": MaritalStatus,
            "NumberOfAddress": NumberOfAddress,
            "Complain": Complain,
            "OrderAmountHikeFromlastYear(%)": OrderAmountHikeFromlastYear,
            "CouponUsed": CouponUsed,
            "OrderCount": OrderCount,
            "DaySinceLastOrder": DaySinceLastOrder,
            "CashbackAmount": CashbackAmount
        }

        api_url = "https://ecommerce-churn-api-p8im.onrender.com/predict"
        
        try:
            response = requests.post(api_url, json=input_data, timeout=60)

            if response.status_code == 200:
                result = response.json()
                churn = result["churn_prediction"]
                proba = result["churn_probability"]
                
                # Display results with custom styling
                st.markdown("---")
                
                if churn == 1:
                    st.markdown("""
                        <div class="prediction-box churn-yes">
                            <h2 style="color: #d63031;">⚠️ Customer Likely to Churn</h2>
                            <p style="font-size: 1.2rem; color: #2d3436;">Immediate action recommended</p>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                        <div class="prediction-box churn-no">
                            <h2 style="color: #00b894;">✅ Customer Likely to Stay</h2>
                            <p style="font-size: 1.2rem; color: #2d3436;">Customer retention is strong</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                # Metrics display
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Prediction", "Will Churn" if churn == 1 else "Won't Churn")
                # with col2:
                #     st.metric("Churn Probability", f"{proba * 100:.1f}%")
                # with col3:
                #     st.metric("Confidence", f"{(1 - abs(0.5 - proba) * 2) * 100:.1f}%")
                
                # Progress bar for probability
                st.markdown("### Churn Risk Level")
                st.progress(proba)
                
                # Recommendations
                st.markdown("---")
                st.markdown("### 💡 Recommendations")
                
                if churn == 1:
                    st.warning("""
                        **High Risk Customer - Suggested Actions:**
                        - 🎁 Offer personalized discounts or loyalty rewards
                        - 📞 Reach out with a customer satisfaction survey
                        - ⚡ Provide exclusive early access to new products
                        - 💬 Schedule a follow-up call from customer success team
                    """)
                else:
                    st.success("""
                        **Healthy Customer - Suggested Actions:**
                        - 🌟 Continue providing excellent service
                        - 📧 Send regular updates about new features
                        - 🎯 Consider upselling premium features
                        - 💎 Invite to loyalty/VIP program
                    """)
                    
            else:
                st.error(f"❌ Error: API returned status code {response.status_code}")
                
        except requests.exceptions.Timeout:
            st.error("⏱️ Request timeout. The API might be waking up (Render free tier). Please try again in a minute.")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error connecting to API: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #636e72; padding: 2rem;'>
        <p>Built with Streamlit | Powered by Machine Learning</p>
    </div>
""", unsafe_allow_html=True)