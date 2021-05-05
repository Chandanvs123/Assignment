#When inputs are in the storage bucket


def test(request):
    name = request.get_json().get('a','b')
    return "Inputs received"


#Sample inputs
a = [10,12,23,34,45,56,67,78]
b = [20,21,24,35,79,46,89,98]


def sort_comb(a,b):
    #Combine the arrays
    list = a + b
    #Sort the combined array
    list.sort()
    return list
	
