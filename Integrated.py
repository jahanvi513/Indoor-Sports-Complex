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

# Function for student login
def student_login():
    st.subheader("Student Login")
    name = st.text_input("Enter Name")
    roll_number = st.text_input("Enter Roll Number", max_chars=10)
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        try:
            # Check if the entered credentials match with records in the 'student' table
            sql = "SELECT * FROM student WHERE Name = %s AND roll_no = %s AND Email = %s AND password = %s"
            val = (name, roll_number, email, password)
            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if result:
                st.success("Login Successful!")
                student_portal()  # Proceed to student portal
            else:
                st.error("Invalid Credentials. Please try again.")

        except mysql.connector.Error as e:
            st.error(f"Error during login: {e}")

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
    option = st.sidebar.selectbox("Select an operation", ("Manage Booking Requests", "View Pending Bookings"))
    if option == "Manage Booking Requests":
        # Implement manage booking requests functionality here
        pass
    elif option == "View Pending Bookings":
        # Implement view pending bookings functionality here
        pass

# Main function
def main():
    st.title("CRUD Operations with MySQL")

    user_type = st.sidebar.selectbox("Select User Type", ("Student", "Supervisor"))
    if user_type == "Student":
        student_login()  # Changed to student login instead of student registration
    elif user_type == "Supervisor":
        supervisor_portal()

if __name__ == "__main__":
    main()
