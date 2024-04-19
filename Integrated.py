import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@123",
    database="crud_new1"
)
mycursor = mydb.cursor()

def create_student():
    st.subheader("Student Registration")
    roll_number = st.text_input("Enter Roll Number")
    name = st.text_input("Enter Name")
    email = st.text_input("Enter Email")
    if st.button("Register"):
        sql = "INSERT INTO students (roll_number, name, email) VALUES (%s, %s, %s)"
        val = (roll_number, name, email)
        mycursor.execute(sql, val)
        mydb.commit()
        st.success("Registration Successful!")
        student_portal()  # After successful registration, go to student portal

def student_portal():
    st.title("Student Portal")
    option = st.sidebar.selectbox("Select an operation", ("Create Booking", "Cancel Booking", "View Bookings"))
    if option == "Create Booking":
        create_booking()
    elif option == "Cancel Booking":
        cancel_booking()
    elif option == "View Bookings":
        view_bookings()

def create_booking():
    st.subheader("Create Booking")
    student_id = st.text_input("Enter Student ID")
    room_id = st.selectbox("Select Room ID", ["101", "102", "103", "104", "105", "106"])
    booking_date = st.date_input("Select Booking Date")
    booking_time = st.time_input("Select Booking Time")
    if st.button("Book"):
        sql = "INSERT INTO bookings (student_id, room_id, booking_date, booking_time) VALUES (%s, %s, %s, %s)"
        val = (student_id, room_id, booking_date, booking_time)
        mycursor.execute(sql, val)
        mydb.commit()
        st.success("Booking Successful!")

def cancel_booking():
    st.subheader("Cancel Booking")
    booking_id = st.number_input("Enter Booking ID")
    if st.button("Cancel"):
        sql = "DELETE FROM bookings WHERE id = %s"
        val = (booking_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        st.success("Booking Cancelled!")

def view_bookings():
    st.subheader("View Bookings")
    student_id = st.text_input("Enter Student ID")
    sql = "SELECT * FROM bookings WHERE student_id = %s"
    val = (student_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    for row in result:
        st.write(row)

def supervisor_portal():
    st.title("Supervisor Portal")
    # Add Supervisor Portal functionality here

def main():
    st.title("CRUD Operations with MySQL")

    user_type = st.sidebar.selectbox("Select User Type", ("Student", "Supervisor"))
    if user_type == "Student":
        create_student()
    elif user_type == "Supervisor":
        supervisor_portal()

if __name__ == "__main__":
    main()
