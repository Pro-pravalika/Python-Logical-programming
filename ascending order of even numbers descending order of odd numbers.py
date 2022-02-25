def asce_desc(list):
	ascen,desc = [],[]
	for each in list:
		if each%2 == 0:
			ascen.append(each)
		else:
			desc.append(each)
	ascen.sort(reverse = False)
	desc.sort(reverse = True)
	ascen.extend(desc)
	return ascen
print(asce_desc([1,32,15,42,377,89,76,40,52,29,50]))
