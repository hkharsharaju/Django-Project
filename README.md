# Hotel-Management-Project-Django

**Hotel Reservation Management** is a Django-based web application designed to streamline the process of booking hotel rooms. The application includes user authentication, admin verification, and a secure booking system to ensure a seamless experience for both users and administrators.
# For Demonstration video link :  
https://drive.google.com/file/d/128Mc39kcFoEe7-WL9MmXv6lj1ypaWkp8/view?usp=drive_link

## Features

- **User Authentication**: Users must log in to access the application.
- **Admin Verification**: New users are initially restricted from booking rooms until an admin verifies their identity to prevent bot activity.
- **Room Booking**: Once verified by an admin, users can book rooms through the application.

## How It Works

1. **User Registration and Login**:
    - Users must create an account and log in to access the application features.
    - After logging in, users can view available rooms but cannot book them until verified by an admin.

2. **Admin Verification**:
    - An admin reviews new user accounts to ensure they are legitimate.
    - The admin updates the user's status to "verified," allowing them to book rooms.

3. **Room Booking**:
    - Verified users can book rooms through the application.
    - The booking process ensures secure and efficient reservations.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **Python**: The programming language used to develop the application.
- **SQLite**: The default database used for development and testing.
- **HTML, CSS, JavaScript**: Front-end technologies for building the user interface.
- **Bootstrap**: A front-end framework for developing responsive and mobile-first web pages.
- **Git**: Version control for tracking changes and collaboration.
- **GitHub**: Hosting for version control and project collaboration.
