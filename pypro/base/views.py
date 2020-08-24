from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<html><body>Hello Django</body></html>', content_type='text/html')


def trigger_error(request):
    division_by_zero = 1 / 0
