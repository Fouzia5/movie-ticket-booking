import streamlit as st

movies = [
    "The King's Speech",
    "Forrest Gump",
    "The Pursuit of Happyness",
    "The Intern",
    "Harry Potter and the Philosopher's Stone"
]

tict_rate = {
    "Adult": 800,
    "Student": 600,
    "Child": 500
}

st.set_page_config(
    page_title="Cinema Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f0f0f, #1b1b1b);
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 23px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 12px;
}

.booking-box {
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #444;
    margin-top: 20px;
}

.total {
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    margin-top: 15px;
}

.cinema-footer {
    text-align: center;
    margin-top: 30px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🎬 Movie Ticket Booking</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your movie night starts here 🍿</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🎥 Select Your Movie</div>',
    unsafe_allow_html=True
)

option = st.selectbox(
    "Choose a movie",
    movies,
    label_visibility="collapsed"
)

st.markdown(
    '<div class="section-title">🎟️ Ticket Rates</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👤 Adult", "Rs. 800")

with col2:
    st.metric("🎓 Student", "Rs. 600")

with col3:
    st.metric("🧒 Child", "Rs. 500")

st.markdown(
    '<div class="section-title">🎟️ Choose Your Tickets</div>',
    unsafe_allow_html=True
)

adult_ticts = st.number_input(
    "Adult Tickets",
    min_value=0,
    step=1
)

student_ticts = st.number_input(
    "Student Tickets",
    min_value=0,
    step=1
)

child_ticts = st.number_input(
    "Child Tickets",
    min_value=0,
    step=1
)

if st.button("🎟️ Book Tickets", use_container_width=True):

    t_ticts = adult_ticts + student_ticts + child_ticts

    if t_ticts == 0:
        st.error("You must buy at least one ticket!")

    else:
        adult_value = adult_ticts * tict_rate["Adult"]
        student_value = student_ticts * tict_rate["Student"]
        child_value = child_ticts * tict_rate["Child"]

        s_total = adult_value + student_value + child_value

        if student_ticts >= 2:
            student_off = student_value * 0.10
        else:
            student_off = 0

        t_dis = s_total - student_off

        if t_ticts >= 5:
            booking_off = t_dis * 0.05
        else:
            booking_off = 0

        t_pay = t_dis - booking_off

        st.success("🎉 Booking Confirmed!")

        st.markdown(
            '<div class="section-title">🧾 Your Booking</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="booking-box">

            <h3>🎬 {option}</h3>

            <p>👤 Adult Tickets: {adult_ticts} = Rs. {adult_value}</p>

            <p>🎓 Student Tickets: {student_ticts} = Rs. {student_value}</p>

            <p>🧒 Child Tickets: {child_ticts} = Rs. {child_value}</p>

            <hr>

            <p>🎟️ Total Tickets: {t_ticts}</p>

            <p>💰 Subtotal: Rs. {s_total}</p>

            <p>🎓 Student Discount: Rs. {student_off:.0f}</p>

            <p>🎟️ Booking Discount: Rs. {booking_off:.0f}</p>

            <div class="total">
                💳 You Pay: Rs. {t_pay:.0f}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="cinema-footer">🍿 Have fun and enjoy the show! 🎬</div>',
            unsafe_allow_html=True
        )
