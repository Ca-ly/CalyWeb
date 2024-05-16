# CalyWeb
Caly is a web application designed to streamline and simplify event planning and scheduling. This README provides a high-level overview of the project and instructions for setting up the application locally.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Local Deployment](#local-deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
Caly allows users to create, manage, and share events effortlessly. It integrates with Google Calendar to ensure users can keep track of their schedules and avoid double bookings.

## Features
- Event creation and management
- Google Calendar integration
- User authentication and authorization
- Admin panel for user and event management

## Tech Stack
- **Backend:** Django, Django REST Framework, PostgreSQL
- **Frontend:** Next.js, React, Yarn, Node.js

## Local Deployment
To deploy Caly locally, you need to set up both the backend and frontend. Detailed instructions for each part are provided in their respective README files.

### Backend Setup
Follow the instructions in the [Backend README](api/README.md) to set up the backend services, including PostgreSQL and the Django application.

### Frontend Setup
Follow the instructions in the [Frontend README](frontend/README.md) to set up the frontend application using Next.js.

## Project Structure
The project is divided into two main directories:

- `api/`: Contains the Django backend application.
- `frontend/`: Contains the Next.js frontend application.

Each directory has its own README with detailed setup instructions.

## Contributing
We welcome contributions from the community. To contribute, please fork the repository, create a new branch, and submit a pull request with your changes. Ensure your code adheres to the project's coding standards and includes appropriate tests.

## License
Caly is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
