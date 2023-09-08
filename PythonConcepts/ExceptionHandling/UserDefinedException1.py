class PercentageError(Exception):
    pass
        
# Exception class for percentage > 100
class InvalidPercentageError(PercentageError):
    def __init__(self):
        super().__init__("Percentage is invalid")
        
# Exception class for percentage < 80
class LessPercentageError(PercentageError):
    def __init__(self):
        super().__init__("The Percentage is lesser than the Cut-off, Please try again!")

# class to check percentage range
class checkPercentage(PercentageError):
    def __init__(self, per):
        if per<80:
            raise LessPercentageError
        if per>100:
            raise InvalidPercentageError
        print("Congrats you're Enrolled")
        
# different cases and output
try:
    print("For Percenatge: 93")
    checkPercentage(93)
except Exception as e:
    print(e)
    
try:
    print("\nFor Percenatge: 102")
    checkPercentage(102)
except Exception as e:
    print(e)
    
try:
    print("\nFor Percenatge: 58")
    checkPercentage(58)
except Exception as e:
    print(e)