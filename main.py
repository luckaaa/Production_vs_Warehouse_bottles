import pandas as pd

ostanek=["Cambridge Distillery Japanese Gin Tbox", "Cambridge Distillery Three Seasons Gin Tbox", "Cambridge Distillery Truffle Gin Tbox",
         "Dingle Original Gin Tbox", "Extension, black box", "Glass insert", "Labels, extension", "Lid", "Rack #3", "Rack #5",
         "Ribbon", "Ron Colón Salvadoreño Coffee Infused Rum Green Label Tbox", "Ron Colón Salvadoreño Dark Aged Rum Tbox",
         "Ron Colón Salvadoreño RumRye Tbox", "Sample Box", "Shipping Carton", "Shipping Carton", "Shipping Carton", "Stauning Kaos Danish Whisky Tbox",
         "Stauning Rye Danish Whisky Tbox", "Stork Club Straight Rye Whiskey Tbox"]

production_bottles = []

production = pd.read_csv("production_bottles.csv", encoding= "utf-8", delimiter =";")
for row in production["Title"]:
    production_bottles.append(row)


warehouse_bottles = []
warehouse = pd.read_csv("warehouse_bottles.csv", encoding= "utf-8", delimiter =";")
for row in warehouse["Title"]:
    warehouse_bottles.append(row)

not_in_stock = []
for bottle in production_bottles:
    if bottle not in warehouse_bottles:
        not_in_stock.append(bottle)

for item in ostanek:
    if item in not_in_stock:
        not_in_stock.remove(item)

for b in not_in_stock:
    print(b)

print(f"\n{len(not_in_stock)} bottles that need to be sourced / transfered to warehouse")

