import matplotlib.pyplot as plt

# WIRELESS stesse condizioni del dataset
# Sample data
categories = ['Wireless', 'Wired']
values = [96, 4]
bar_colors = ['red', 'green']

# Create a bar plot
bars = plt.bar(categories, values, color=bar_colors)

# Add labels and title
plt.xlabel('Traffico')
plt.ylabel('%')
plt.title('Percentuale classificazione traffico\n catturato da interfaccia wireless')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), ha='center', va='bottom')

# Show the plot
plt.show()

# WIRED
# Sample data
categories = ['Wireless', 'Wired']
values = [2, 98]
bar_colors = ['red', 'green']

# Create a bar plot
bars = plt.bar(categories, values, color=bar_colors)

# Add labels and title
plt.xlabel('Traffico')
plt.ylabel('%')
plt.title('Percentuale classificazione traffico\n catturato da interfaccia wired')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), ha='center', va='bottom')

# Show the plot
plt.show()

# WIRELESS condizioni diverse rispetto al dataset
# Sample data
categories = ['Wireless', 'Wired']
values = [84, 16]
bar_colors = ['red', 'green']

# Create a bar plot
bars = plt.bar(categories, values, color=bar_colors)

# Add labels and title
plt.xlabel('Traffico')
plt.ylabel('%')
plt.title('Percentuale classificazione traffico\n catturato da interfaccia wireless\n (in condizioni diverse rispetto a quelle del dataset)')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), ha='center', va='bottom')

# Show the plot
plt.show()