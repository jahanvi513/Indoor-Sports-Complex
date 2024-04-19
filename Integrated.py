import mysql.connector
import streamlit as st

try:
    # Establishing connection with the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#College2024",
        database="ISC"  # Changed database name to match backend
    )
    mycursor = mydb.cursor()
except mysql.connector.Error as e:
    st.error(f"Error connecting to MySQL database: {e}")
    st.stop()

# Function to create a new student
def create_student():
    try:
        st.subheader("Student Registration")
        roll_number = st.text_input("Enter Roll Number")
        name = st.text_input("Enter Name")
        email = st.text_input("Enter Email")
        password = st.text_input("Enter Password", type="password")
        phone_number = st.text_input("Enter Phone Number")
        department = st.text_input("Enter Department")
        year = st.number_input("Enter Year", min_value=1)
        if st.button("Register"):
            # Using the provided stored procedure to insert a new student
            mycursor.callproc("insert_new_student", (roll_number, name, email, password, phone_number, department, year))
            mydb.commit()
            st.success("Registration Successful!")
            student_portal()  # After successful registration, go to student portal
    except mysql.connector.Error as e:
        st.error(f"Error creating student: {e}")

# Function to create a booking
def create_booking():
    try:
        st.subheader("Create Booking")
        student_id = st.text_input("Enter Student ID")
        room_type = st.selectbox("Select Room Type", ["Badminton", "Tennis", "Squash", "Swimming"])
        booking_date = st.date_input("Select Booking Date")
        booking_time = st.time_input("Select Booking Time")
        if st.button("Book"):
            # Using the provided stored procedure to search for available rooms
            mycursor.callproc("search_room", (room_type, booking_date, booking_time))
            result = mycursor.fetchall()
            if result:
                room_id = result[0][0]  # Assuming room ID is the first column in the result
                # Inserting the booking details into the 'booking' table
                sql = "INSERT INTO booking (room_id, booked_date, booked_time, student_id) VALUES (%s, %s, %s, %s)"
                val = (room_id, booking_date, booking_time, student_id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Booking Successful!")
            else:
                st.error("No available rooms matching the criteria.")
    except mysql.connector.Error as e:
        st.error(f"Error creating booking: {e}")

# Function to cancel a booking
def cancel_booking():
    try:
        st.subheader("Cancel Booking")
        booking_id = st.number_input("Enter Booking ID")
        if st.button("Cancel"):
            # Using the provided stored procedure to manage booking request
            mycursor.callproc("manage_booking_request", (booking_id, 'Denied'))
            mydb.commit()
            st.success("Booking Cancelled!")
    except mysql.connector.Error as e:
        st.error(f"Error canceling booking: {e}")

# Function to view bookings for a student
def view_bookings():
    try:
        st.subheader("View Bookings")
        student_id = st.text_input("Enter Student ID")
        # Using the provided stored procedure to view bookings
        mycursor.callproc("view_booking", (student_id,))
        result = mycursor.fetchall()
        for row in result:
            st.write(row)
    except mysql.connector.Error as e:
        st.error(f"Error viewing bookings: {e}")

# Function to navigate to student portal
def student_portal():
    st.title("Student Portal")
    option = st.sidebar.selectbox("Select an operation", ("Create Booking", "Cancel Booking", "View Bookings"))
    if option == "Create Booking":
        create_booking()
    elif option == "Cancel Booking":
        cancel_booking()
    elif option == "View Bookings":
        view_bookings()

# Function to navigate to supervisor portal
def supervisor_portal():
    st.title("Supervisor Portal")
    # Add Supervisor Portal functionality here

# Main function
def main():
    st.title("ISC Slot booking System")

    user_type = st.sidebar.selectbox("Select User Type", ("Student", "Supervisor"))
    if user_type == "Student":
        create_student()
    elif user_type == "Supervisor":
        supervisor_portal()

if __name__ == "__main__":
    main()
