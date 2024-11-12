import numpy as np
import matplotlib.pyplot as plt

# PCM Encoding
def pcm_encoding(analog_signal, quantization_levels):
    # Normalize the analog signal to the range [0, 1]
    normalized_signal = (analog_signal - min(analog_signal)) / (max(analog_signal) - min(analog_signal))

    # Quantize the normalized signal
    quantized_signal = np.round(normalized_signal * (quantization_levels - 1))

    return quantized_signal

# PCM Decoding
def pcm_decoding(quantized_signal, original_signal, quantization_levels):
    min_val = min(original_signal)
    max_val = max(original_signal)
    normalized_signal = quantized_signal / (quantization_levels - 1)
    decoded_signal = normalized_signal * (max_val - min_val) + min_val

    return decoded_signal

# Main Function
if __name__ == "__main__":
    time = np.arange(0, 1, 0.001)
    amp = float(input("Enter Amplitude of signal:\n"))
    freq = float(input("Enter frequency of signal:\n"))
    analog_signal = amp * np.sin(2 * np.pi * freq * time) + amp * np.sin(2 * np.pi * (2 * freq) * time)

    # Set the number of quantization levels (bits per sample)
    quantization_levels = 8

    # PCM encoding
    pcm_encoded_signal = pcm_encoding(analog_signal, quantization_levels)

    # Plot the original analog signal and the PCM encoded signal
    plt.subplot(2, 1, 1)
    plt.plot(time, analog_signal)
    plt.title('Original Analog Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.subplot(2, 1, 2)
    plt.step(time, pcm_encoded_signal, linewidth=1)
    plt.title('PCM Encoded Signal')
    plt.xlabel('Time')
    plt.ylabel('Quantized Level')

    plt.tight_layout()
    plt.show()
    decode_choice = input("Do you want to decode the PCM encoded signal? (yes/no): ").strip().lower()

    if decode_choice == 'yes':
        # PCM Decoding
        pcm_decoded_signal = pcm_decoding(pcm_encoded_signal, analog_signal, quantization_levels)

        # Plot the original analog signal, the PCM encoded signal, and the decoded signal
        plt.figure(figsize=(10, 6))

        plt.subplot(3, 1, 1)
        plt.plot(time, analog_signal)
        plt.title('Original Analog Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')

        plt.subplot(3, 1, 2)
        plt.step(time, pcm_encoded_signal, linewidth=1)
        plt.title('PCM Encoded Signal')
        plt.xlabel('Time')
        plt.ylabel('Quantized Level')

        plt.subplot(3, 1, 3)
        plt.plot(time, pcm_decoded_signal)
        plt.title('PCM Decoded Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')

        plt.tight_layout()
        plt.show()

        # Print the PCM encoded and decoded signal
        
        print("PCM Encoded Signal:", pcm_encoded_signal)
        print("PCM Decoded Signal:", pcm_decoded_signal)
    else:
        print("Decoding skipped.")
        print("PCM Encoded Signal:", pcm_encoded_signal)
