import os
import json  


def save_results(results):
    with open('results.txt', 'w') as file:
        json.dump(results, file)


# Main options menu integration
if __name__ == '__main__':
    # Assuming `tracking_results` is a variable that contains results
    tracking_results = []  # Placeholder for tracking results
    # Call this function when saving results is needed
    save_results(tracking_results)  
