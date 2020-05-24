class Ereader():
    def __init__(self, make, model, backlight, battery, screen_type):
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
        self.library_count = 0
    def get_ereader_name(self):
        long_name = self.make + "-" + self.model + "-" + self.backlight + "-" + self.battery + "-" + self.screen_type
        return long_name.title()
    def read_library_count(self):
        print("You have " + str(self.library_count) + " in your kindle library")
my_new_ereader = Ereader("Amazon Kindle","Fire 8","Paperwhite","5000Mah", "touch")
print(my_new_ereader.get_ereader_name())
my_new_ereader.read_library_count()