# README for the Garibuntu Platform

Garibuntu is a community-focused platform designed to connect car enthusiasts. It provides a centralized space for various car groups, allows event registration, sponsorship opportunities, and enables interactions through discussions, forums, and announcements. This platform is built using Django and JavaScript and aims to streamline event organization, sponsorship management, and social interactions within the car community.

## Features

- **Event Management**: Create, view, and register for events.
- **Sponsorship System**: Sponsors can register and offer sponsorships to car groups and events.
- **Forums**: Engage in discussions, post replies, and share knowledge within the car community.
- **Admin Dashboard**: Admins can manage events, sponsors, user registrations, and payments.
- **Payment Confirmation**: Users can enter a payment code after paying through mobile money for manual verification by admins.

## Prerequisites

- Python 3.9+
- SQLite3
- Django 4.x
- Git

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Carol-96/garibuntu.git
cd garibuntu

2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required Python packages:
```bash
pip install -r requirements.txt

4. Set up the database by following the steps below:
# Open the `garibuntu/settings.py` file.
# Locate the `DATABASES` section and update it with your database details. Below is a sample configuration for a PostgreSQL database:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'garibuntu_db',  # Replace with your database name
           'USER': 'yourusername',    # Replace with your database username
           'PASSWORD': 'yourpassword', # Replace with your database password
           'HOST': 'localhost',       # Database host (usually 'localhost' for local setups)
           'PORT': '5432',            # Default PostgreSQL port
       }
   }

5. Make sure PostgreSQL is installed and running. If you need to create the database, you can do so by running:
```bash
createdb garibuntu_db

6. Save the changes in settings.py and proceed to the migration steps.

7. Apply the database migrations to set up the required tables:
```bash
python manage.py migrate

8. To access the Django admin, create a superuser account:
```bash
python manage.py createsuperuser

9. Collect all static files for production use:
```bash
python manage.py collectstatic

10. Start the Django development server:
```bash
python manage.py runserver

Here is the Directory of the Project Structure
garibuntu/
├── events/                # App for event management
├── sponsors/              # App for sponsor registration and management
├── cargroups/             # App for managing car groups and their members
├── forum/                 # App for forum posts and replies
├── templates/             # Shared templates
├── static/                # Static files (CSS, JS)
├── garibuntu/             # Main project configuration
├── manage.py              # Django management script
└── README.md              # Project documentation

## Usage

### Event Management
- **View Events**: Users can browse through available events and filter them by type (e.g., meetups, charity events).
- **Register for Events**: Logged-in users can register for events by providing a payment confirmation code after making a payment through mobile money.

### Sponsorship Registration
- Sponsors can register on the platform by providing their company details. This registration allows them to support various events hosted on the platform.

### Forum and Discussions
- Users can create threads, post replies, and participate in discussions within the car groups. This feature facilitates community engagement and knowledge sharing.

### Manual Payment Verification
- Users make payments externally (e.g., via mobile money) and input their payment code upon registration. Admins verify these codes manually and confirm the user’s registration for events.

### Admin Dashboard
Admins have access to a dashboard where they can:
- Approve user registrations and payments
- Manage events, sponsorships, and car group information
- Send email notifications for updates, new events, announcements, and forum activities

### Email Notifications
The system sends email notifications to users for the following activities:
- Event registration and confirmations
- New events or announcements
- Forum updates (new posts or responses)
- Sponsorship confirmations

### Future Improvements
- **Social Media Login Integration**: Allow users to register/login via social media platforms like Google and Facebook.
- **Enhanced User Analytics**: Provide analytics for user engagement in events, sponsorships, and forums.
- **Automated Payment Integration**: Integrate a payment gateway for direct payments and automatic verification.



