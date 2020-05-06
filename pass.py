from webbot import Browser 
import http
import http.client
http.__file__

web = Browser()
web.go_to('google.com') 
web.click('Sign in')
web.type('bryanwi09@gmail.com' , into='Email')
web.click('NEXT' , tag='span')
web.type('Wendell!017' , into='Password' , id='passwordFieldId') # specific selection
web.click('NEXT' , tag='span') # you are logged in ^_^