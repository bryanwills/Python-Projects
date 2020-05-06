

class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Bryan', 'Wills', 100000)
emp_2 = Employee('Jessica', 'Barrett', 90000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())
