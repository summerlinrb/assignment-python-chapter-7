# Follow the instructions for coding a weather app

daily_high_temps = [62, 64, 79, 52, 46, 50, 58, 66, 71, 77, 78, 78, 76, 79, 77]
daily_low_temps = [42, 48, 47, 24, 28, 28, 32, 37, 43, 46, 48, 47, 48, 49, 50]
daily_humidity = [0.48, 0.53, 0.46, 0.44, 0.4, 0.6,
                  0.58, 0.5, 0.48, 0.43, 0.41, 0.39, 0.39, 0.38, 0.4]

max_high_temp = (max(daily_high_temps))
average_high_temp = sum(daily_high_temps)/len(daily_high_temps)
min_low_temp = (min(daily_low_temps))
average_low_temp = sum(daily_low_temps)/len(daily_low_temps)
average_humidity = sum(daily_humidity)/len(daily_humidity)

print(
    f"Weather forecast for the next 15 days: The average high will be {average_high_temp:.0f} and the average low will be {average_low_temp:.0f}. The highest temperature will be {max_high_temp}. The lowest temperature will be {min_low_temp}. The average humidity will be {average_humidity:.2f}.")
