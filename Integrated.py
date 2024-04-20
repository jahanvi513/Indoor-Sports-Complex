import mysql.connector
import streamlit as st

# Establishing connection with the MySQL database
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#College2024",
        database="ISC"  
    )
    mycursor = mydb.cursor()
except mysql.connector.Error as e:
    st.error(f"Error connecting to MySQL database: {e}")
    st.stop()

# Session state management
class SessionState:
    def __init__(self, **kwargs):
        self.logged_in = False
        self.__dict__.update(kwargs)

def get():
    if not hasattr(st, 'st.session_state'):
        st.st.session_state = SessionState()
    return st.st.session_state

# Function for student login
def student_login():
    if not st.session_state.logged_in:
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
                    st.session_state.logged_in = True
                    st.session_state.student_id = result[0]
                    student_portal()
                else:
                    st.error("Invalid Credentials. Please try again.")

            except mysql.connector.Error as e:
                st.error(f"Error during login: {e}")
    else:
        student_portal()

# Function to create a booking
def create_booking():
    if not st.session_state.logged_in:
        st.error("Please login first.")
        return
    st.subheader("Create Booking")
    room_type = st.selectbox("Select Room Type", ["Badminton", "Yoga", "Basketball", "Gym"])
    booking_date = st.date_input("Select Booking Date")
    booking_time = st.time_input("Select Booking Time")
    
    # st.write("Session State (Before Button Click):", st.session_state.__dict__)
    
    if st.button("Book"):
        if not st.session_state.logged_in:
            st.error("Please login first.")
            return  # Exit the function if not logged in
        
        student_id = st.session_state.student_id
        try:
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
        
# Function to navigate to student portal
def student_portal():
    st.title("Student Portal")
    option = st.sidebar.selectbox("Select an operation", ("Create Booking", "View Bookings", "Delete Booking"))
    if option == "Create Booking":
        create_booking()
    elif option == "View Bookings":
        view_bookings()  # Implement view_bookings function
    elif option == "Delete Booking":
        delete_booking()  # Implement delete_booking function

# Main function
def main():
    st.title("Indoor Sports Complex")
    
    if 'logged_in' not in st.session_state:
       st.session_state.logged_in = False

    if 'student_id' not in st.session_state:
      st.session_state.student_id = None
   
    # st.session_state = get()

    user_type = st.sidebar.selectbox("Select User Type", ("Student", "Supervisor"))
    if user_type == "Student":
        student_login()
    elif user_type == "Supervisor":
        supervisor_login()

if __name__ == "__main__":
    main()
