tempincelsius = input("Please enter a temperature in celsius...")
#print(tempincelsius)
#print(type(tempincelsius))

tempinfarenheit = float(tempincelsius) * 1.8 + 32

roundedf = round(tempinfarenheit, 2)
# print(tempinfarenheit)
# print(type(tempinfarenheit))
print(str(tempincelsius) + " degrees celsius is " + str(roundedf) + " degrees farenheit")
