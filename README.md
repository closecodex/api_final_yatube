# API_FINAL🌐
### Project "API for Yatube"

This project provides an API for a social network that allows users to follow each other.

### Project Description:

The application allows users to:

1. Create, delete, and edit posts, as well as retrieve information about posts.
2. Add comments, retrieve one or multiple comments for a post.
3. Retrieve information about communities (groups).
4. Follow other users and view their followers.

### How to Run the Project:

1. **Clone the repository:**
    
    ```bash
    git clone git@github.com:closecodex/api_final_yatube.git
    cd api_final_yatube
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv\Scripts\activate
    ```

3. **Upgrade pip and install dependencies:**
   
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the application:**

   ```bash
   python manage.py runserver
   ```

### Example Requests:

Create a subscription:
- URL: /api/v1/follow/
- Method: POST

Retrieve the list of subscriptions:
- URL: /api/v1/follow/
- Method: GET
