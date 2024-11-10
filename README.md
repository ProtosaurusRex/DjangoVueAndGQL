# DjangoVueAndGQL
This is a simple blog application built using Django, Vue, and GraphQL. The project is based on the tutorial from Real Python, which you can follow here: https://realpython.com/python-django-blog/

I’ve enhanced the original tutorial by adding the functionality for users to create their own blog posts through the user interface. These posts are submitted to the backend and stored in the database using a combination of Vue tools and GraphQL mutations.

# Features
Users can write and submit blog posts through a frontend UI.
The frontend is built using Vue.js.
The backend is powered by Django with a GraphQL API.
The frontend communicates with the backend via GraphQL mutations.

# Installation

~Set up Virtual Environment
Create a virtual environment for the backend: python -m venv venv

~Download Project Files
Clone or download the project files to your desired parent directory.

~ Install Backend Dependencies
Navigate to the backend directory and install the required Python dependencies: pip install -r requirements.txt

~Run Django Development Server
Ensure the Django backend is working correctly by running the server: python manage.py runserver
    Note: The default URL will show an error page since there’s no view associated with it. However, you can verify that the server is running by navigating to:
      /admin (for the Django admin panel)
      /graphql (for GraphQL interface)

~Set Up Frontend Dependencies
Move the following frontend files to a new directory (e.g., frontend):
    package.json
    index.html
    vite.config.js
    package-lock.json

Once the files are moved, navigate to the frontend folder and install the required Node.js dependencies: npm install
Install the Vue plugin for Vite: npm install @vitejs/plugin-vue

~Verify Frontend
Ensure that the frontend is working by running the development server: npm run dev
This should start the frontend and you can navigate to the local server to see the Vue application in action.

# Notes
~The project uses GraphQL to handle interactions between the frontend and the Django backend. The frontend sends GraphQL mutations to create blog posts, which are then added to the database.
~Make sure the backend is running before starting the frontend, as the frontend depends on the API provided by the Django server.

# Want to contribute?
~Add user authentication to allow users to log in and manage their blog posts.
~Enhance the styling of the blog using frameworks like TailwindCSS or Bootstrap.
~Implement more advanced features like image uploads, post editing, and comment sections.
~Feel free to fork and contribute to the project!
