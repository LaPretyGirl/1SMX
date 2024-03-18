def lparaulaf(l):
	ll=[]
	a = l.split("Hey que tal")
	for e in a:
	    ll.append(len(e))
	return ll
print(lparaulaf("hola, avui fa bon temps i ho aprofitarem"))
