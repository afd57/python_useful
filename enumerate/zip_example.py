colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
aa= [1,2,3,4]
for color, ratio, a in zip(colors, ratios, aa):
    print("{} {}% {}".format(a, ratio * 100, color))

# Source: https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
# Loop over multiple lists at the same time with zip:

