class laptops:
    price="10000"
    processor="i?"
    ram="gb"
    def hp(self):
        print("hp laptop")
    def lenovo(self):
        print("lenovo laptop")
    def dell(self):
        print("dell laptop")


hp=laptops()
hp.price="40000"
hp.processor="i5"
hp.ram="500gb"
print(hp.price)
print(hp.processor)
print(hp.ram)

lenovo=laptops()
##same process to lenovo
dell=laptops()
##same process to dell

