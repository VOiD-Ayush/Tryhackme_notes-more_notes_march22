year = "1994"
month = "08"

for i in range(2,9):
    day = "0"+str(i)
    print("{}{}{}".format(year,month,day))
    print("{}{}{}".format(day,month,year))
    print("{}{}{}".format(month,day,year))
    print("{}-{}-{}".format(year,month,day))
    print("{}-{}-{}".format(day,month,year))
    print("{}-{}-{}".format(month,day,year))
    print("{}/{}/{}".format(year,month,day))
    print("{}/{}/{}".format(day,month,year))
    print("{}/{}/{}".format(month,day,year))