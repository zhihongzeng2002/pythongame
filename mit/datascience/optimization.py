
def optimal_score(toConsider, avail, score):
    print(toConsider, avail, score)
    if avail <= 20 or not toConsider:
        return (score, toConsider)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = optimal_score(toConsider[1:], avail, score)
        withoutVal, withoutToTake = optimal_score(toConsider[1:], avail-10, score-nextItem)

        if withVal >= withoutVal:
            return (withVal, withToTake + [nextItem])
        else:
            return (withoutVal, withoutToTake)

# Score	=	((60	–	(a+b+c+d+e))*F	+	a*ps1	+	b*ps2	+	c*ps3	+	d*ps4	+	e*ps5
#       = 60*F + (-F + ps1)*a + (-F + ps2)*b + (-F + ps3)*c + (-F + ps4)*d + (-F + ps5)*e

def formulize_items(params):
    weight = 10
    items = []
    for i, p in enumerate(params):
        if not i:
            F = p
        else:
            items.append((-F+p)*weight)
    return items

params = [100, 10, 20, 30, 40, 50]
items = formulize_items(params)

score = params[0] * 60 
for x in items:
    score += x

print('base score: {}'.format(score))
max_score = optimal_score(items, len(items) * 10, score)
print(max_score)

