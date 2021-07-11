from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == 'POST':
		#do stuff
		name = request.POST['name']
		message_email = request.POST['message-email']
		mobile_number = request.POST['mobile-number']
		message = request.POST['message']

		send_mail(
			name, #subject
			message, #message
			message_email, # from email
			# mobile_number, # mobile number
			['sahmed2190@gmail.com'], #To email
			fail_silently=False,
			)

		return render(request, 'contact_us.html', {'name':name})
	else:
		return render(request, 'contact_us.html', {})