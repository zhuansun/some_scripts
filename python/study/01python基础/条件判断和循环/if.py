'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''

#heightstr = input("请输入您的身高(单位米，保留两位小数)")
#height = float(heightstr)
#print("{0:.2f}".format(height))
#weight = float(input("请输入您的体重(单位千克，保留一位小数)"))
#print("身高: {0:.2f}, 体重: {1:.1f}".format(height,weight)
#print("您的BMI指数是: %.1f" % float(height)/(float(weight)*float(weight)))

height = float(input("请输入您的身高(单位米，保留两位小数)"))
weight = float(input("请输入您的体重(单位千克，保留一位小数)"))
print("身高: {0:.2f} 米, 体重: {1:.1f} 千克".format(height,weight))
bmi = weight/(height*height)
print("您的BMI指数是: {0:.1f}".format(bmi))
if bmi<18.5:
	print("过轻");
elif 12.8<=bmi<25:
	print("正常");
elif 25<=bmi<28:
	print("过重");
elif 28<=bmi<32:
	print("肥胖");
elif bmi>=32:
	print("严重肥胖");
else:
	print("你是个什么鬼")