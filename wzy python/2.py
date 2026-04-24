#用input算（BMI = 体重/（身高 ** 2）
user_weight = float(input("请输入您的体重(单位是:kg):"))
user_hight = float(input("请输入您的身高(单位是:m):"))
user_BMI = user_weight / (user_hight) ** 2
print("您的BMI值为:" + str(user_BMI))
if user_BMI <= 18.5:
    print("偏瘦")
elif 18.5 < user_BMI <=25:
    print("正常")
elif 25< user_BMI <=30:
    print("偏胖")
else:
    print("肥胖")

#条件语句，else不可单独存在
mood_index = int(input("心情指数是："))
if mood_index >= 60:
    print("恭喜")
else:
    print("不好")