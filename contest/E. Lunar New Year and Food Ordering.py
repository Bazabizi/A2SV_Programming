foods, customer = map(int, input().split())

food = list(map(int, input().split()))
cost = list(map(int, input().split()))

sorted_cost = [(cost, idx) for idx, cost in enumerate(cost)]
sorted_cost.sort()

minptr = 0
for i in range(customer):
    kind, dish = map(int, input().split())

    price = 0
    if food[kind - 1] >= dish:
        price += (dish * cost[kind - 1])
        food[kind - 1] -= dish
        dish = 0
    else:
         price += (food[kind - 1] * cost[kind - 1])
         dish -= food[kind - 1]
         food[kind - 1] = 0

    while dish > 0:
        minFood = None
        while minptr < foods and minFood == None:
            minCost, minFood = sorted_cost[minptr]

            if food[minFood] == 0:
                minFood = None
                minptr += 1
            else:
                break

        if minFood == None:
            price = 0
            break

        if food[minFood] >= dish:
            price += (dish * minCost)
            food[minFood] -= dish
            dish = 0
        else:
            price += (food[minFood] * minCost)
            dish -= food[minFood]
            food[minFood] = 0
        
    if dish > 0:
         price = 0
    
    print(price)
