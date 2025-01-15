import streamlit as st
from database import engine, get_session
from models import Base, User

# Create DB and tables if not existing
Base.metadata.create_all(bind=engine)

st.title("Streamlit app - SQLite Database Editor with SQLAlchemy")

# Display and edit users
def manage_users():
    st.subheader("User Management")

    session = get_session()  # Open session
    try:
        users = session.query(User).all()

        if users:
            st.write("Current Users:")
            for user in users:
                st.write(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
        else:
            st.write("No users found.")

        st.write("---")
        st.subheader("Add or Update a User")

        user_id = st.number_input("User ID (leave 0 for new user)", min_value=0, step=1)
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, step=1)

        if st.button("Save"):
            if user_id == 0:
                # Add new user
                new_user = User(name=name, age=age)
                session.add(new_user)
                st.success("User added successfully!")
            else:
                # Update existing user
                user = session.query(User).get(user_id)
                if user:
                    user.name = name
                    user.age = age
                    st.success("User updated successfully!")
                else:
                    st.error("User not found!")

            session.commit()
    finally:
        session.close()

manage_users()
