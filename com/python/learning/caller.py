from com.python.learning import pi
from com.python.learning.domain import User

print(__name__)
pi.print_name_test()
pi_value = pi.calculate_pi(10000)
print('Approx value of PI {}'.format(pi_value))

user = User
print(user)
