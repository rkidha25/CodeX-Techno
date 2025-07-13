def calculate_bmi(weight,height):
    bmi = weight/(height*height)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal weight"
    elif 25 < bmi:
        return "overweight"
    else:
        return "obese"

def main():
    print("BMI CALCULATOR")
    try:
        weight = float(input("enter the weight in kg: "))
        height = float(input("enter your height in m: "))

        if weight<=0 or height <=0:
           print("enter positive values")
           return
    
        bmi = calculate_bmi(weight,height)
        category = classify_bmi(bmi)

        print(f"your BMI is: {bmi:.2f}")
        print(f"category is:{category}")

    except ValueError:
        print("please enter valid numeric values for height and weight")

if __name__ == "__main__":
    main()
