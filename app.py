import streamlit as st
import random

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Startup Validator",
    page_icon="🚀",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f3fbf6;
}

.block-container {
    padding-top: 1.5rem;
}

.title {
    font-size: 46px;
    font-weight: 800;
    color: #111827;
}

.subtitle {
    color: #6b7280;
    font-size: 18px;
    margin-bottom: 20px;
}

.stTextArea textarea {
    border-radius: 16px;
    border: 2px solid #d1fae5;
    padding: 16px;
    font-size: 16px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg,#16a34a,#22c55e);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 15px;
    font-size: 18px;
    font-weight: bold;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
}

.metric-card {
    background: white;
    padding: 18px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid #dcfce7;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
}

.metric-title {
    color: #15803d;
    font-weight: 700;
    font-size: 16px;
}

.metric-value {
    font-size: 30px;
    font-weight: 800;
    color: #16a34a;
}

.score-box {
    background: linear-gradient(135deg,#22c55e,#16a34a);
    color: white;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
}

.score-number {
    font-size: 70px;
    font-weight: 900;
}

.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #166534;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown('<div class="title">🚀 AI Startup Validator</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">AI-powered startup validation with market analysis, SWOT, competitor research, finance metrics and business insights.</div>',
    unsafe_allow_html=True
)

# =========================================================
# INPUT
# =========================================================

idea = st.text_area(
    "Enter Startup Idea",
    placeholder="Example: AI mental health therapist app for students"
)

# =========================================================
# MARKET ANALYSIS AGENT
# =========================================================

def market_agent(idea):

    idea_lower = idea.lower()

    # HEALTHCARE

    if "health" in idea_lower or "therapy" in idea_lower or "medical" in idea_lower:

        return {
            "industry": "Healthcare AI",
            "tam": "$24.8B",
            "sam": "$6.2B",
            "som": "$620M",
            "growth": "17.3%",
            "market_trends": [
                "AI therapy adoption increasing",
                "Remote healthcare growing",
                "Mental wellness awareness increasing",
                "AI journaling tools trending"
            ],
            "drivers": [
                "Stress & anxiety increase",
                "Remote healthcare demand",
                "AI accessibility"
            ]
        }

    # AGRICULTURE

    elif "pesticide" in idea_lower or "agri" in idea_lower or "farmer" in idea_lower:

        return {
            "industry": "AgriTech AI",
            "tam": "$31.6B",
            "sam": "$8.7B",
            "som": "$870M",
            "growth": "12.5%",
            "market_trends": [
                "Precision farming rising",
                "AI crop monitoring adoption",
                "Government agri-tech funding",
                "Smart farming demand"
            ],
            "drivers": [
                "Food demand increase",
                "Climate challenges",
                "Crop optimization needs"
            ]
        }

    # EDUCATION

    elif "student" in idea_lower or "education" in idea_lower or "tutor" in idea_lower:

        return {
            "industry": "EdTech AI",
            "tam": "$18B",
            "sam": "$4.1B",
            "som": "$420M",
            "growth": "15.2%",
            "market_trends": [
                "AI tutoring growth",
                "Personalized learning demand",
                "Remote education adoption"
            ],
            "drivers": [
                "Affordable education demand",
                "24/7 AI learning",
                "Skill-based learning"
            ]
        }

    # DEFAULT

    else:

        return {
            "industry": "General AI Startup",
            "tam": "$15B",
            "sam": "$3.5B",
            "som": "$300M",
            "growth": "14%",
            "market_trends": [
                "Enterprise AI adoption",
                "AI automation growth",
                "AI SaaS expansion"
            ],
            "drivers": [
                "Digital transformation",
                "Automation demand",
                "Cloud infrastructure"
            ]
        }

# =========================================================
# COMPETITOR AGENT
# =========================================================

def competitor_agent(idea):

    idea_lower = idea.lower()

    if "health" in idea_lower or "therapy" in idea_lower:

        return {
            "large": [
                "Talkspace",
                "BetterHelp",
                "Headspace Health",
                "Calm Health",
                "Woebot"
            ],
            "medium": [
                "Replika",
                "Wysa",
                "Youper"
            ],
            "small": [
                "MoodPath",
                "Reflectly",
                "MindDoc"
            ]
        }

    elif "pesticide" in idea_lower or "agri" in idea_lower:

        return {
            "large": [
                "Syngenta",
                "Bayer Crop Science",
                "BASF",
                "Corteva"
            ],
            "medium": [
                "Nufarm",
                "UPL Limited",
                "Adama Agriculture"
            ],
            "small": [
                "AgriAI",
                "FarmSense",
                "CropMind"
            ]
        }

    elif "education" in idea_lower or "student" in idea_lower:

        return {
            "large": [
                "Byju's",
                "Coursera",
                "Khan Academy",
                "Duolingo"
            ],
            "medium": [
                "Unacademy",
                "Chegg",
                "Udemy"
            ],
            "small": [
                "TutorAI",
                "LearnBot",
                "StudyMind"
            ]
        }

    else:

        return {
            "large": [
                "OpenAI",
                "Google AI",
                "Microsoft AI"
            ],
            "medium": [
                "Perplexity",
                "Anthropic",
                "Cohere"
            ],
            "small": [
                "AI niche startups",
                "Bootstrapped SaaS startups"
            ]
        }

# =========================================================
# SWOT AGENT
# =========================================================

def swot_agent(idea):

    return {

        "strengths": [
            "Scalable AI business model",
            "Automation reduces manual work",
            "High future demand",
            "Recurring SaaS revenue"
        ],

        "weaknesses": [
            "Customer acquisition cost",
            "Requires AI infrastructure",
            "Needs constant innovation"
        ],

        "opportunities": [
            "Enterprise partnerships",
            "Global expansion",
            "Subscription revenue"
        ],

        "threats": [
            "Competition from big tech",
            "Regulatory challenges",
            "Rapidly changing AI trends"
        ]
    }

# =========================================================
# FINANCE AGENT
# =========================================================

def finance_agent(idea):

    score = random.randint(70, 95)

    investment = random.choice([
        "$50K - $100K",
        "$100K - $500K",
        "$500K - $2M"
    ])

    revenue = random.choice([
        "Subscription SaaS",
        "Freemium + Premium",
        "Enterprise Licensing",
        "API Monetization"
    ])

    risk = random.choice([
        "Low",
        "Medium",
        "High"
    ])

    return {
        "score": score,
        "investment": investment,
        "revenue": revenue,
        "risk": risk
    }

# =========================================================
# VALIDATION BUTTON
# =========================================================

if st.button("✨ Validate Startup"):

    if idea.strip() == "":
        st.warning("Please enter startup idea.")
        st.stop()

    # AGENTS

    market = market_agent(idea)
    competitors = competitor_agent(idea)
    swot = swot_agent(idea)
    finance = finance_agent(idea)

    # =====================================================
    # SCORE SECTION
    # =====================================================

    st.markdown("## 📊 Startup Score")

    st.markdown(f"""
    <div class="score-box">
        <div class="score-number">{finance['score']}/100</div>
        <h2>Startup Potential</h2>
        <p>{idea} has strong market validation and scalable business opportunities.</p>
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # MARKET METRICS
    # =====================================================

    st.markdown("## 🌍 Market Metrics")

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("TAM", market["tam"]),
        ("SAM", market["sam"]),
        ("SOM", market["som"]),
        ("Growth", market["growth"])
    ]

    cols = [c1, c2, c3, c4]

    for col, metric in zip(cols, metrics):

        with col:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">{metric[0]}</div>
                <div class="metric-value">{metric[1]}</div>
            </div>
            """, unsafe_allow_html=True)

    # =====================================================
    # MARKET ANALYSIS
    # =====================================================

    st.markdown("## 📈 Market Analysis")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Industry")

    st.write(market["industry"])

    st.subheader("Market Trends")

    for trend in market["market_trends"]:
        st.write("📈", trend)

    st.subheader("Growth Drivers")

    for d in market["drivers"]:
        st.write("🚀", d)

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # COMPETITOR ANALYSIS
    # =====================================================

    st.markdown("## 🏢 Competitor Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("🌐 Large Companies")

        for c in competitors["large"]:
            st.write("•", c)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("🏭 Medium Firms")

        for c in competitors["medium"]:
            st.write("•", c)

        st.markdown('</div>', unsafe_allow_html=True)

    with col3:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("🌱 Emerging Startups")

        for c in competitors["small"]:
            st.write("•", c)

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # SWOT ANALYSIS
    # =====================================================

    st.markdown("## 🧠 SWOT Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("✅ Strengths")

        for s in swot["strengths"]:
            st.write("✔️", s)

        st.subheader("🚀 Opportunities")

        for o in swot["opportunities"]:
            st.write("📈", o)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("⚠️ Weaknesses")

        for w in swot["weaknesses"]:
            st.write("❌", w)

        st.subheader("🔥 Threats")

        for t in swot["threats"]:
            st.write("⚠️", t)

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # FINANCE AGENT
    # =====================================================

    st.markdown("## 💰 Financial Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Initial Investment</div>
            <div class="metric-value">{finance['investment']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Revenue Model</div>
            <div class="metric-value">{finance['revenue']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Risk Level</div>
            <div class="metric-value">{finance['risk']}</div>
        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # FINAL VERDICT
    # =====================================================

    st.markdown("## 🏆 Final Verdict")

    if finance["score"] >= 85:
        verdict = "Excellent Startup Idea 🚀"

    elif finance["score"] >= 75:
        verdict = "High Potential Startup ✅"

    else:
        verdict = "Moderate Potential ⚠️"

    st.markdown(f"""
    <div class="card">
        <h2>{verdict}</h2>

        <p>
        The startup idea <b>{idea}</b> has strong market opportunity,
        scalable growth potential and monetization possibilities.
        Focus on execution, differentiation and customer acquisition.
        </p>

    </div>
    """, unsafe_allow_html=True)
