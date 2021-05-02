from input import *

def test(request):
    name = request.get_json().get(a,b)
    return "Inputs received"

def sort_comb(a,b):
    #Combine the arrays
    list = a + b
    #Sort the combined array
    list.sort()
    return list
	
