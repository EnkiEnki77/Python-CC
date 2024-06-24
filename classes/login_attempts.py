from userss import User

login_attempts = User('Enki', 'layman', 'elayman', 25)

login_attempts.increment_login_attempts()
login_attempts.increment_login_attempts()
login_attempts.increment_login_attempts()
login_attempts.reset_login_attempts()