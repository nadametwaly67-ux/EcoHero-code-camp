# EcoHero-code-camp
<div align="center">
  <img src="https://img.icons8.com/fluency/96/bot.png" alt="EcoBot Logo" width="100" />
  <h1>🎮 EcoHero Adventure & AI Guide 🌿</h1>
  <p><b>تطبيق تعليمي تفاعلي مدعوم بالذكاء الاصطناعي لتعليم الأطفال حماية البيئة</b></p>
  
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />
</div>

<hr />

## 📖 فكرة المشروع
مشروع **EcoHero** هو تطبيق مبني بمكتبة **Streamlit**، يهدف إلى تحويل تعلم البيئة إلى تجربة ممتعة. يعتمد التطبيق على مسارين أساسيين:
1.  **السيناريو القصصي:** رحلة مبنية على اختيارات الطفل، كل اختيار يؤثر على مجموع نقاطه (Points) ولقبه (Titles).
2.  **Eco-Bot (Chatbot):** صديق ذكي للإجابة على تساؤلات الأطفال حول إعادة التدوير وكيفية الحفاظ على الكوكب بلغة مبسطة.

<hr />

## 🏆 نظام النقاط والألقاب
يتم تتبع تقدم الطفل من خلال شريط جانبي (Sidebar) يظهر نقاطه الحالية واللقب الذي استحقه:
* 🌱 **مدافع ناشئ:** (0-50 نقطة)
* 🌳 **حارس الغابة:** (51-150 نقطة)
* 👑 **بطل الكوكب الذهبي:** (+150 نقطة)

<hr />

## 💻 الكود التوضيحي للهيكل (App Structure)
يمكنك وضع هذا الكود في ملف `app.py` لتوضيح كيفية عمل النظامين معاً:

```python
import streamlit as st

# 1. إعداد نظام النقاط
if 'points' not in st.session_state:
    st.session_state.points = 0

# 2. الشات بوت (Eco-Bot)
st.sidebar.title("🤖 Eco-Bot")
user_question = st.sidebar.text_input("اسأل صديقك الآلي عن البيئة:")
if user_question:
    st.sidebar.info(f"أنا ذكاء اصطناعي، وسأخبرك أن {user_question} مهم جداً لكوكبنا!")

# 3. واجهة اللعبة والسيناريو
st.title("🌍 مغامرة البطل الأخضر")
st.metric(label="نقاطك الحالية", value=st.session_state.points)

# مشهد تفاعلي
st.subheader("الموقف: وجدت صنبور مياه مفتوح في المدرسة! 💧")
col1, col2 = st.columns(2)

with col1:
    if st.button("أغلقه فوراً ✅"):
        st.session_state.points += 20
        st.success("أحسنت! لقد وفرت الكثير من المياه.")
        
with col2:
    if st.button("أتجاهله ❌"):
        st.warning("تذكر أن كل قطرة ماء غالية!")
