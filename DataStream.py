import numpy as np
import random
import time

def generate_synthetic_data_stream():
    t = 0
    while True:
        # Simulating seasonal pattern using a sine wave with random noise
        seasonal_pattern = 10 * np.sin(t / 20) 
        noise = random.uniform(-2, 2)  # Random noise
        value = seasonal_pattern + noise
        #Inject a large anomalous value
        if random.random() > 0.99:
            value += random.uniform(20, 50)
        yield value
        t += 1
        time.sleep(0.1) 