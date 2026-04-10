s1="   Los Angeles   "

# lstrip() --> removes left spaces
# rstrip() --> removes right spaces
# strip() --> does bot but doesnt remove spaces in between

stp_string=s1.strip()
print(stp_string)

class TestCity:

    def verifyCity(self):

        s1=input("Enter the city you want to check")
        strip_s1=s1.strip()

        if strip_s1=="Los Angeles":
            print("The city you entered is Los Angeles")

        elif strip_s1=="New York":
            print("The city you entered is New York")

        else:
            print("The city you entered is not in the list")

tc=TestCity()
tc.verifyCity()