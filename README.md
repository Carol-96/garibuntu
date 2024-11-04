
# Garibuntu Platform

The **Garibuntu Platform** is designed to bring car enthusiasts together, allowing them to join events, participate in discussions, and access sponsorships. This README provides setup instructions, key features, and usage guidelines.

## Features

- **Event Management**: Users can create, view, and register for events (e.g., meetups, charity events).
- **Sponsorship System**: Sponsors can register and support car groups and events.
- **Forums**: Engage in discussions, post replies, and share knowledge within the car community.
- **Admin Dashboard**: Manage events, sponsors, user registrations, and payments.

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
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Database Setup

1. Open the `garibuntu/settings.py` file and configure your database settings:

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
   ```

2. Ensure PostgreSQL is installed and running. If you need to create the database, you can do so by running:

   ```bash
   createdb garibuntu_db
   ```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Collect Static Files

```bash
python manage.py collectstatic
```

### 7. Run the Server

```bash
python manage.py runserver
```

## Project Structure

```plaintext
garibuntu/
├── events/                # App for event management
├── sponsors/              # App for sponsor registration and management
├── cargroups/             # App for managing car groups and their members
├── forum/                 # App for forum posts and replies
```

## Usage

### Event Management

- **View Events**: Users can browse through available events and filter by type (e.g., meetups, charity events).
- **Register for Events**: Logged-in users can register for events by providing a payment confirmation code after making a payment through mobile money.

### Sponsorship Registration

- Sponsors can register on the platform by providing their company details, enabling them to support events hosted on the platform.

### Forum and Discussions

- Users can create threads, post replies, and participate in discussions within car groups, fostering community engagement.

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

## Future Improvements

- *****Social Media Login Integration**: Allow users to register/login via social media platforms like Google and Facebook.
- **Enhanced User Analytics**: Provide analytics for user engagement in events, sponsorships, and forums.
- **Automated Payment Integration**: Integrate a payment gateway for direct payments and automatic verification.

### Project Completed by
- Caroline Kalumu
- Ndigirigi Benedict Gichuhi
- Erick Otieno Awino
