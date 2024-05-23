from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add, sub
from celery.result import AsyncResult




# Create your views here.

def index(request):
    # Start the tasks asynchronously
    result1 = add.delay(10, 20)
    result2 = sub.delay(50, 10)

    # Wait for the tasks to complete
    # result1.wait()
    # result2.wait()

    # Retrieve the results
    # result1_value = result1.get()
    # result2_value = result2.get()

    # Print the results (for debugging)
    print("Result 1:", result1.result)
    print("Result 2:", result2.result)

    # Return an HTTP response
    return HttpResponse("Tasks completed. Check console for results.")
