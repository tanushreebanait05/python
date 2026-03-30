import matplotlib.pyplot as plt

# Company recruitment data
companies = ["Microsoft", "Google", "Amazon", "IBM",
             "Deloitte", "Capgemini", "ATOS", "Amdocs"]

recruitments = [120, 150, 180, 90, 110, 130, 80, 100]

# a) Bar Chart
plt.bar(companies, recruitments)
plt.title("New Recruitments in Companies")
plt.xlabel("Companies")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.show()

# b) Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
explode = [0,0.1,0,0,0,0,0,0]  # highlight Google

plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        explode=explode, shadow=True)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Doughnut Chart")
plt.show()

# e) Compare IBM & Amdocs
names = ["IBM", "Amdocs"]
values = [90, 100]

plt.bar(names, values)
plt.title("IBM vs Amdocs Recruitment")
plt.ylabel("Employees")
plt.show()