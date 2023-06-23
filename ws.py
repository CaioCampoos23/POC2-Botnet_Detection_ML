import numpy as np

# Assuming you have the reconstruction errors stored in a 
# list or numpy array called 'reconstruction_errors' and 'threshold'
# represents the threshold value for determining anomalies.

window_size = 10  # Size of the sliding window

def detect_anomalies_with_sliding_window(reconstruction_errors, threshold):
    num_samples = len(reconstruction_errors)
    anomaly_labels = np.zeros(num_samples)  # Initialize the anomaly labels
    
    for i in range(0, num_samples, window_size):
        print(i)
        window_errors = reconstruction_errors[i:i+window_size]
        print(window_errors)
        
        # If the majority of errors in the window exceed the threshold, label the window as anomalous
        if sum(i > threshold for i in window_errors) > (len(window_errors) / 2):
            anomaly_labels[i:i+window_size] = 1
    
    return anomaly_labels

reconstruction_errors = [0.1, 0.2, 0.61, 0.8, 0.9, 0.71, 0.2, 0.1, 0.9, 0.7, 0.8, 0.3, 0.1, 0.2, 0.9]
threshold = 0.6

print(reconstruction_errors)
anomaly_labels = detect_anomalies_with_sliding_window(reconstruction_errors, threshold)
print(f'\n\nAnomaly: {anomaly_labels}')

