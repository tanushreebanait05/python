import matplotlib.pyplot as plt

# Data (sample cosmetic company data)
months = [1,2,3,4,5,6,7,8,9,10,11,12]

facecream = [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash = [1500,1200,1340,1130,1740,1555,1120,1500,1780,1890,2100,1760]
toothpaste = [5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
bathingsoap = [9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400]
shampoo = [1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800]
moisturizer = [1500,1200,1340,1130,1740,1555,1120,1500,1780,1890,2100,1760]

# Total profit
profit = [211000,183300,224700,222700,209600,201400,
          295500,361400,234000,266700,412800,300200]

# a) Line Plot (Profit)
plt.plot(months, profit, marker='o')
plt.title("Company Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline Plot (All products)
plt.plot(months, facecream, label="Face Cream")
plt.plot(months, facewash, label="Face Wash")
plt.plot(months, toothpaste, label="Toothpaste")
plt.plot(months, bathingsoap, label="Bathing Soap")
plt.plot(months, shampoo, label="Shampoo")
plt.plot(months, moisturizer, label="Moisturizer")

plt.legend()
plt.title("Sales Data of Products")
plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.show()

# c) Bar Chart (Face cream & Face wash)
import numpy as np
x = np.arange(len(months))

plt.bar(x-0.2, facecream, width=0.4, label="Face Cream")
plt.bar(x+0.2, facewash, width=0.4, label="Face Wash")

plt.legend()
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Face Cream vs Face Wash Sales")
plt.show()

# d) Pie Chart (Total yearly sales per product)
total_sales = [
    sum(facecream),
    sum(facewash),
    sum(toothpaste),
    sum(bathingsoap),
    sum(shampoo),
    sum(moisturizer)
]

labels = ["Face Cream", "Face Wash", "Toothpaste",
          "Bath Soap", "Shampoo", "Moisturizer"]

plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()