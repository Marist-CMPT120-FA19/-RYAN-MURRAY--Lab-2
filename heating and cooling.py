Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
        temp= input("Enter the average tempurature per day separated by spaces: ")
        temp=temp.split(" ")
        cooling=0
        heating=0

        for i in temp:
            if float(i)> 80 or float(i)<60:
                if float(i)> 80:
                    cooling += float(i)-80
                else:
                    heating += 60-float(i)

        print("There are", cooling, "cooling degrees days and there are ", heating, "heating degrees days")
        main()

        
>>> 
