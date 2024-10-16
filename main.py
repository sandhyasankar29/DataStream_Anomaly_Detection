import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Model import StreamingIsolationForest
from DataStream import generate_synthetic_data_stream

if __name__ == '__main__':
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    anomalies = []
    ln, = plt.plot([], [], 'b-', label='Data Stream')
    anomaly_ln, = plt.plot([], [], 'ro', label='Anomalies')
    streaming_iforest = StreamingIsolationForest(window_size=100)
    
    def init():
        ax.set_xlim(0, 200)
        ax.set_ylim(-15, 60)
        ax.set_xlabel("Time Steps")
        ax.set_ylabel("Value")
        ax.legend()
        return ln, anomaly_ln

    def update(frame):
        new_value = next(stream)
        xdata.append(len(xdata))
        ydata.append(new_value)

        # Anomaly detection using Isolation Forest
        prediction = streaming_iforest.fit_predict(new_value)
        if prediction == -1:  # Detected as anomaly
            anomalies.append((xdata[-1], ydata[-1]))

        # Update the data stream plot
        ln.set_data(xdata, ydata)

        # Update the anomalies plot
        anomaly_x, anomaly_y = zip(*anomalies) if anomalies else ([], [])
        anomaly_ln.set_data(anomaly_x, anomaly_y)

        ax.set_xlim(max(0, len(xdata) - 200), len(xdata))

        return ln, anomaly_ln
    
    stream = generate_synthetic_data_stream()
    ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=100, cache_frame_data=False)
    plt.show()