from django.shortcuts import render
from .forms import EmailForm
from .models import Subscription, Post
from django.template import Context,Template
def home(request):

	form = EmailForm(request.POST or None)
	posts = Post.objects.all()[:5]
	side = 0
	string = ""
	for e in reversed(posts):
		side+=1
		title = e.title
		subtitle = e.author
		image = e.image
		content = e.short_content
		string+=construct_post(image,title,subtitle,content,side)
	context = Context({"hello": string}, autoescape=False)

	if form.is_valid():
		print request
		ip = request.META.get("REMOTE_ADDR")
		new_join, created = Subscription.objects.get_or_create(ip="hello", email=form.cleaned_data['email'])

	template = "home.html"
	return render(request,template,context);

def construct_post(img, title, subtitle, content, side):
	if(side%2==0):
		ret = '<div class="row featurette">       <div class="col-md-7">        <h2 class="featurette-heading">'
		ret += title
		ret += '<span class="text-muted"><br>'
		ret += subtitle
		ret += '</span></h2>        <p class="lead">'
		ret += content
		ret += '</div>'
		ret += '<div class="col-md-5">       <img class="featurette-image img-responsive center-block" data-src="'
		ret += img
		ret += '" alt="Generic placeholder image">     </div>    </div>'
	else:
		ret = '<div class="row featurette">  <div class="col-md-7 col-md-push-5">           <h2 class="featurette-heading">'
		ret += title
		ret += '<span class="text-muted"><br>'
		ret += subtitle 
		ret += '</span></h2>'
		ret += content
		ret += '</div>'
		ret += '<div class="col-md-5 col-md-pull-7">       <img class="featurette-image img-responsive center-block" data-src="'
		ret += img
		ret += '" alt="Generic placeholder image">     </div>    </div>'
	return ret+'<hr class="featurette-divider">'
#
#<div class="row featurette">
#        <div class="col-md-7">
#          <h2 class="featurette-heading">And lastly, this one. <span class="text-muted">Checkmate.</span></h2>
#          <p class="lead">Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.</p>
#        </div>
#        <div class="col-md-5">
#          <img class="featurette-image img-responsive center-block" data-src="holder.js/500x500/auto" alt="Generic placeholder image">
#        </div>
#      </div>*/