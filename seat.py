# Car seat adjustment
def calculate_adjustments(height, leg_length, arm_length, preference):
    # Basic ergonomic rules for adjustments
    seat_distance = 0.4 * leg_length  # Distance from seat to pedals
    backrest_angle = 90 
    if preference.lower() == "sporty" else 110  # Sporty vs. relaxed angle
    steering_wheel_position = 0.6 * arm_length  # Distance to steering wheel
    headrest_height = 0.8 * height  # Headrest position
    
    return {
        "seat_distance": seat_distance,
        "backrest_angle": backrest_angle,
        "steering_wheel_position": steering_wheel_position,
        "headrest_height": headrest_height,
    }

def main():
    print("Welcome to the Car Seat Adjustment Simulator!")
    
    # Collect user inputs
    height = int(input("Enter your height (cm): "))
    leg_length = int(input("Enter your leg length (cm): "))
    arm_length = int(input("Enter your arm length (cm): "))
    preference = input("Enter your driving preference (sporty/relaxed): ")
    
    # Calculate adjustments
    adjustments = calculate_adjustments(height, leg_length, arm_length, preference)
    
    # Display the results
    print("\nRecommended Adjustments:")
    print(f"Seat Distance: {adjustments['seat_distance']:.2f} cm")
    print(f"Backrest Angle: {adjustments['backrest_angle']}°")
    print(f"Steering Wheel Position: {adjustments['steering_wheel_position']:.2f} cm")
    print(f"Headrest Height: {adjustments['headrest_height']:.2f} cm")

if __name__ == "__main__":
    main()
