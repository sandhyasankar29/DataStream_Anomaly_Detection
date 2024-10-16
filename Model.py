from sklearn.ensemble import IsolationForest
import numpy as np

class StreamingIsolationForest:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.model = IsolationForest(contamination=0.01, warm_start=False, n_estimators=100)
        self.data_window = []

    def fit_predict(self, new_value):
        self.data_window.append(new_value)
        
        if len(self.data_window) > self.window_size:
            self.data_window.pop(0)

        if len(self.data_window) < self.window_size:
            return 0 
        
        self.model.fit(np.array(self.data_window).reshape(-1, 1))
        prediction = self.model.predict([[new_value]])
        
        return prediction[0]