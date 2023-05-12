Following are the steps to run this application:
1. Clone the repository
    - <code>git clone https://github.com/surojitdey/django-quiz.git</code>
2. Create python virtual environment and activate it(optional)
    - <code>python -m venv venv</code>
    - <code>source venv/bin/activate</code>(Unix)
    - <code>.\venv\Script\activate</code>(Windows)

3. Install the required dependencies
    - <code>pip install -r requirements.txt</code>

4. Migrate the database 
    - <code>python manage.py migrate</code> 

5. Run this application
    - <code>python manage.py runserver</code> 

6. Open <url>http://127.0.0.1:8000</url> in browser