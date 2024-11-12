import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
sampling_frequency = float(input("Enter Sampling Frequency:\n"))
signal_duration = float(input("Enter Signal Duration:\n"))
time = np.arange(signal_duration * sampling_frequency) / sampling_frequency

# Message signal parameters
message_frequency_cosine = float(input("Enter message_frequency_cosine:"))
message_frequency_sine = float(input("Enter message_frequency_sine:"))
message_amplitude_cosine = float(input("Enter message_amplitude_cosine:"))
message_amplitude_sine = float(input("Enter message_amplitude_sine:"))

# Message signal creation
message_cosine = message_amplitude_cosine * np.cos(2 * np.pi * message_frequency_cosine * time)
message_sine = message_amplitude_sine * np.sin(2 * np.pi * message_frequency_sine * time)
message = message_cosine + message_sine

# Bandwidth and Nyquist rate
bandwidth = max(message_frequency_cosine, message_frequency_sine)
nyquist_rate = float(input("Enter the nyquist_rate:"))
delta_sampling_frequency = nyquist_rate * 2 * bandwidth

# Delta signal parameters
delta_epsilon = float(input("Enter the value of delta epsilon:"))

# Time for delta sampling
delta_time = np.arange(signal_duration * delta_sampling_frequency) / delta_sampling_frequency

# Sampled message creation
sampled_message_cosine = message_amplitude_cosine * np.cos(2 * np.pi * message_frequency_cosine * delta_time)
sampled_message_sine = message_amplitude_sine * np.sin(2 * np.pi * message_frequency_sine * delta_time)
sampled_message = sampled_message_cosine + sampled_message_sine

# Modulation process
prediction = np.zeros((len(sampled_message),))
modulated = np.zeros_like(prediction)

for i, s_amplitude in enumerate(sampled_message[1:]):
    amplitude_diff = s_amplitude - prediction[i]
    modulated[i + 1] = (2 * float(amplitude_diff > 0) - 1) * delta_epsilon
    prediction[i + 1] = prediction[i] + modulated[i + 1]

# Output signal after modulation
output = [1] + [float(modulated[i] > 0) for i in range(1, len(modulated))]

# Plotting the message signal and modulated signal
plt.figure(figsize=(20, 12))
plot_time = 0.1

# Plot message and predicted signals
plt.subplot(2, 1, 1)
plt.plot(time, message, 'b')
plt.step(delta_time, prediction, 'r', where='post')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Message and Predicted Signals')
plt.legend(['Message signal', 'Predicted signal'])
plt.axis([0, plot_time, -2, 2])
plt.xticks(np.arange(0, plot_time, plot_time/10))
plt.grid()

# Plot modulated signal
plt.subplot(2, 1, 2)
plt.stem(delta_time, modulated, 'b')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Transmitted DM Signal')
plt.axis([0, plot_time, -2 * delta_epsilon, 2 * delta_epsilon])
plt.xticks(np.arange(0, plot_time, plot_time/10))
plt.grid()

plt.show()

# Decoding the modulated signal (after encoding)
def dm_decoding(modulated_signal, delta_epsilon):
    decoded_signal = np.zeros_like(modulated_signal)
    for i in range(1, len(modulated_signal)):
        decoded_signal[i] = decoded_signal[i - 1] + (modulated_signal[i] / delta_epsilon)
    return decoded_signal


decode_choice = input("Do you want to decode the DM modulated signal? (yes/no): ").strip().lower()

if decode_choice == 'yes':
    # Decode the signal
    decoded_signal = dm_decoding(modulated, delta_epsilon)

    # Plot the original message, modulated, and decoded signal
    plt.figure(figsize=(20, 12))

    # Plot message signal
    plt.subplot(3, 1, 1)
    plt.plot(time, message, 'b')
    plt.title('Original Message Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()

    # Plot modulated signal
    plt.subplot(3, 1, 2)
    plt.stem(delta_time, modulated, 'b')
    plt.title('Modulated DM Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()

    # Plot decoded signal
    plt.subplot(3, 1, 3)
    plt.plot(delta_time, decoded_signal, 'r')
    plt.title('Decoded DM Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()

    plt.tight_layout()
    plt.show()

    # Print decoded signal
    print("Decoded Signal:", decoded_signal)
else:
    print("Decoding skipped.")
    print("Modulated Signal:", modulated)
