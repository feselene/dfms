---

# Dynamic Fleet Management System (DFMS)

A comprehensive solution for managing a fleet of vehicles with real-time tracking, driver dispatching, route optimization, and more.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Testing](#testing)

---

## Overview

The **Dynamic Fleet Management System (DFMS)** provides tools for fleet operators to track vehicles, manage drivers, and optimize routes dynamically. Designed for scalability and efficiency, this system includes a Django backend with real-time communication, an Android app for drivers, and real-time notifications for streamlined operations.

---

## Features

- **Real-Time Vehicle Tracking**: Track each vehicle’s location on a live map with updates pushed in real-time.
- **Driver Dispatching**: Assign drivers based on availability and proximity.
- **Route Optimization**: Calculate optimal routes using Google Maps API for reduced travel time and cost.
- **Maintenance Scheduling**: Track and manage vehicle maintenance schedules.
- **Notifications**: Send real-time updates to drivers using Firebase Cloud Messaging.
- **User and Role Management**: Secure access control for different user roles (e.g., drivers, dispatchers, and admins).

---

## Technologies Used

### Backend
- **[Django](https://www.djangoproject.com/)**: Python-based web framework for rapid development.
- **[Django REST Framework](https://www.django-rest-framework.org/)**: Provides a robust toolkit for building Web APIs.
- **[PostgreSQL with PostGIS](https://postgis.net/)**: Relational database with geospatial capabilities.
- **[Django Channels](https://channels.readthedocs.io/en/stable/)**: Enables WebSocket support in Django for real-time updates.
- **[Celery](https://docs.celeryproject.org/en/stable/)**: Task queue for handling background jobs asynchronously.

### Frontend
- **[Kotlin](https://developer.android.com/kotlin)** and **[Jetpack Compose](https://developer.android.com/jetpack/compose)**: Used for building the Android app with modern UI components.
- **[Google Maps API](https://developers.google.com/maps)**: Provides map visualization and route optimization.

### Notifications
- **[Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging)**: Real-time push notifications for Android app.

### DevOps and Deployment
- **[Docker](https://www.docker.com/)**: Containerization for consistent deployment.
- **[Kubernetes](https://kubernetes.io/)**: Orchestration for managing containerized applications across clusters.

### Version Control
- **[GitHub](https://github.com/)**: Version control and code collaboration platform.

### Testing
- **[Jest](https://jestjs.io/)**: JavaScript testing framework for frontend code.
- **[Pytest](https://docs.pytest.org/en/stable/)**: Python testing framework for backend code.

---

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/dfms.git
   cd dfms
   ```

2. **Backend Setup (Django)**

   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Set up **PostgreSQL** and enable the **PostGIS** extension.
   - Create and configure `.env` file with your database credentials and other sensitive information.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```
   - Start Django server:
     ```bash
     python manage.py runserver
     ```

3. **Real-Time Communication Setup**
   - Ensure **Django Channels** is configured for WebSocket support.
   - Start the Channels layer (Redis or similar for real-time processing).

4. **Celery Setup for Background Jobs**
   - Start the Celery worker:
     ```bash
     celery -A dfms worker -l info
     ```

5. **Android App Setup**

   - Open the Android app in **Android Studio**.
   - Ensure dependencies are installed and project is synced.
   - Configure Firebase Cloud Messaging (FCM) in the app for notifications.
   - Build and run the app on an emulator or physical device.

6. **Docker and Kubernetes Deployment**

   - Build and run the Docker containers:
     ```bash
     docker-compose up --build
     ```
   - For Kubernetes, ensure configuration files are set up, then deploy:
     ```bash
     kubectl apply -f k8s/
     ```

---

## Testing

- **Backend Testing (Pytest)**
  ```bash
  pytest
  ```

- **Frontend Testing (Jest)**
  ```bash
  npm run test
  ```

### End-to-End Testing

For end-to-end testing, tools like **Postman** for API testing or **Selenium** for UI testing can be integrated based on the project requirements.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for enhancements, bug fixes, or new features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- 

This README provides a structured overview of your DFMS project, including the key technologies, installation steps, and basic usage instructions. Update the links and commands as necessary to suit your project structure.
