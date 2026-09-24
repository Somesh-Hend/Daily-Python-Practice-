# Addition of material in inventary by using if in
bag={"Water bottel":1,"bread":5,"pikax":1}
item="Water bottel"
no=2
if item in bag:
    bag[item]=bag[item]+no
    print(bag)
else:
    print(bag)