import concurrent.futures
from login import app as login_app
from signup import app as signup_app

def run_signup_app():
    signup_app.run(debug=False)
def run_login_app():
    login_app.run(debug=False)


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(run_signup_app)
        executor.submit(run_login_app)
      
       