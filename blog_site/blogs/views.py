from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index", status=200)


# class FourDigitYearConverter:
#     regex = "[0-9]{4}"
#
#     def to_python(self, value):
#         return int(value) + 1
#
#     def to_url(self, value):
#         return "%04d" % value

