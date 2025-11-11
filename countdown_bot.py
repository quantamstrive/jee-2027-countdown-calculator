from datetime import datetime

def calculate_days_remaining(start_date, exam_date):
    delta = exam_date - start_date
    return delta.days

def main():
    exam_date = datetime(2027, 1, 1)
    
    print("=" * 40)
    print("JEE 2027 COUNTDOWN CALCULATOR")
    print("=" * 40)
    print(f"Exam Date: {exam_date.strftime('%B %d, %Y')}")
    print("=" * 40)
    
    while True:
        print("\nEnter start date to calculate days remaining:")
        print("(or type 'quit' to exit)")
        
        year_input = input("Year (YYYY): ")
        if year_input.lower() == 'quit':
            break
        
        month_input = input("Month (1-12): ")
        if month_input.lower() == 'quit':
            break
        
        day_input = input("Day (1-31): ")
        if day_input.lower() == 'quit':
            break
        
        try:
            year = int(year_input)
            month = int(month_input)
            day = int(day_input)
            
            start_date = datetime(year, month, day)
            days_left = calculate_days_remaining(start_date, exam_date)
            
            print("\n" + "-" * 40)
            if days_left > 0:
                print(f"DAYS REMAINING: {days_left}")
                
                years = days_left // 365
                remaining = days_left % 365
                months = remaining // 30
                days = remaining % 30
                
                print(f"That's approximately {years} years, {months} months, and {days} days")
            elif days_left == 0:
                print("EXAM IS TODAY!")
            else:
                print("The exam date has already passed!")
            print("-" * 40)
            
        except ValueError:
            print("\nInvalid date! Please try again.")
    
    print("\nGood luck with your preparation!")

if __name__ == "__main__":
    main()
