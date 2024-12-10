# بيانات المدخلات
# sub_id = رمز المقرر
# Conflict_sub_id =رمز المقرر المتداخل 
# NumOfInteraction =عدد المتداخلات 

conflict_table = [
    {"NumOfInteraction": 30, "Conflict_sub_id": 200, "sub_id": 100},
    {"NumOfInteraction": 15, "Conflict_sub_id": 300, "sub_id": 200},
]

levels = [
    {"sub_id": 100, "level": 1},
    {"sub_id": 200, "level": 2},
    {"sub_id": 300, "level": 3},
]

# حساب التكلفة النهائية بناءً على الترتيب
def calculate_final_cost(order, conflict_table):
    total_cost = 0
    for conflict in conflict_table:
        sub1_index = order.index(conflict["sub_id"])
        sub2_index = order.index(conflict["Conflict_sub_id"])
        # تحقق من وضع التداخلات في أيام متتالية
        if abs(sub1_index - sub2_index) == 1:
            total_cost += conflict["NumOfInteraction"]
    return total_cost

# ترتيب المستويات
from itertools import permutations

# جميع احتمالات ترتيب المستويات
all_orders = permutations([100, 200, 300])

# البحث عن الترتيب الأمثل
min_cost = float("inf")
best_order = None

for order in all_orders:
    cost = calculate_final_cost(order, conflict_table)
    if cost < min_cost:
        min_cost = cost
        best_order = order

print("bast tidy up:", best_order)
print("less expensive:", min_cost)