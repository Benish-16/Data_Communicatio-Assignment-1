import numpy as np
import matplotlib.pyplot as plt

# AMI Encoding (Alternate Mark Inversion)
def ami(bits):
    ami_signal = []
    current_level = 1
    for bit in bits:
        if bit == '1':
            ami_signal.append(current_level)
            current_level = -current_level
        else:
            ami_signal.append(0)
    return np.array(ami_signal)

# HDB3 (High-Density Bipolar 3 Zeros) Encoding
def hdb3(bits):
    ami_signal = ami(bits)  # Initial AMI signal
    zero_count = 0
    pulse_count = 0
    scrambled_segments = []  # Store the scrambled segments
    
    for i in range(len(bits)):
        if bits[i] == '1':
            pulse_count += 1
            zero_count = 0
        else:
            zero_count += 1
            if zero_count == 4:
                # Handling scrambling for 4 consecutive zeros
                if pulse_count % 2 == 0:
                    ami_signal[i - 3] = 1   # Replace the 4th zero with a positive pulse
                    ami_signal[i] = -1      # Replace the last zero with a negative pulse
                    scrambled_segment = np.array([1, 0, 0, -1])
                else:
                    ami_signal[i] = 1       # Replace the last zero with a positive pulse
                    scrambled_segment = np.array([0, 0, 0, 1])
                zero_count = 0
                pulse_count += 1
                scrambled_segments.append(scrambled_segment)
    return ami_signal, scrambled_segments

# HDB3 Decoding
def hdb3_decoding(encoded_bits):
    decoded_bits = []
    i = 0
    while i < len(encoded_bits):
        if i + 3 < len(encoded_bits) and np.array_equal(encoded_bits[i:i+3], np.array([0, 0, 0])):
            if encoded_bits[i + 3] == 1 or encoded_bits[i + 3] == -1:
                decoded_bits.append('0')
                i += 4
            else:
                decoded_bits.append('0')
                i += 1
        else:
            if encoded_bits[i] == 1 or encoded_bits[i] == -1:
                decoded_bits.append('1')
                i += 1
            else:
                decoded_bits.append('0')
                i += 1

    return ''.join(decoded_bits)

# Plotting the HDB3 Encoded Data (without scrambled segments)
def plot_hdb3(encoded_data):
    plt.figure(figsize=(10, 6))
    
    # Plot HDB3 encoded data
    plt.step(np.arange(len(encoded_data)), encoded_data, where='post', color='grey', linewidth=4, label="HDB3 Encoded Data")
    
    plt.title('HDB3 Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red', linestyle='--')
    plt.ylim(-1.5, 1.5)  # Setting the y-axis range for clarity
    for i in range(0, len(encoded_data)):
        plt.axvline(i, color='black', linestyle='--', alpha=0.3)

    # Adding labels to the graph
    plt.legend(loc="upper right")
    plt.show()

# Main program logic
if __name__ == '__main__':
    try:
        size = int(input("Enter the number of bits you want to input: "))
        if size <= 0:
            print("The size must be a positive integer.")
            exit()
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        exit()

    binary_data = []
    print(f"Enter the binary data (0 or 1) for {size} bits:")
    for i in range(size):
        while True:
            bit = input(f"Bit {i + 1}: ")
            if bit in ['0', '1']:
                binary_data.append(bit)
                break
            else:
                print("Invalid input. Only binary values (0 or 1) are allowed.")

    # Encoding the data using HDB3
    hdb3_data, scrambled_segments = hdb3(binary_data)
    print("Binary Data:", binary_data)
    print("HDB3 Encoded Data:", hdb3_data)
    
    # Check if scrambling occurred
    if scrambled_segments:
        print("Scrambled Signal Produced:")
        for segment in scrambled_segments:
            print(segment)
    else:
        print("No scrambling was necessary in the encoded data.")

    # Plotting the HDB3 encoded data without scrambled segments
    plot_hdb3(hdb3_data)

    # Decoding the data if desired
    decode_choice = input("Do you want to decode the HDB3 encoded data? (yes/no): ").strip().lower()
    if decode_choice == 'yes':
        decoded_data = hdb3_decoding(hdb3_data)
        print("Decoded Data:", decoded_data)
    else:
        print("Decoding skipped.")
