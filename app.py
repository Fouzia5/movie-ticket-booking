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

st.title("Movie Ticket Booking")

option = st.selectbox("Choose a movie", movies)

st.write("Ticket Rates")
st.write("Adult: Rs.", tict_rate["Adult"])
st.write("Student: Rs.", tict_rate["Student"])
st.write("Child: Rs.", tict_rate["Child"])

adult_ticts = st.number_input(
    "How many Adult tickets do you want?",
    min_value=0,
    step=1
)

student_ticts = st.number_input(
    "How many Student tickets do you want?",
    min_value=0,
    step=1
)

child_ticts = st.number_input(
    "How many Child tickets do you want?",
    min_value=0,
    step=1
)

if st.button("Book Tickets"):

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

        st.success("Booking Done!")

        st.write("## Your Booking")
        st.write("Movie:", option)

        st.write("Adult Tickets:", adult_ticts, "=", adult_value)
        st.write("Student Tickets:", student_ticts, "=", student_value)
        st.write("Child Tickets:", child_ticts, "=", child_value)

        st.write("Tickets:", t_ticts)
        st.write("Subtotal:", s_total)
        st.write("Student Off:", student_off)
        st.write("Booking Off:", booking_off)
        st.write("You Pay:", t_pay)

        st.write("Have fun!")
