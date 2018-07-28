import django.dispatch

csv_uploaded = django.dispatch.Signal(providing_args=["user", "csv_file_list"])