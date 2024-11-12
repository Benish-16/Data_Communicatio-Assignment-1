import matplotlib.pyplot as plt
import numpy as np

# HDB3 (Scrambled AMI Encoding)
def hdb3_encoding(bits):
    encoded_bits = np.array([]) 
    consecutive_zeros_count = 0
    last_substitution = 0
    current_level = 1
    scrambled_segments = [] 

    for bit in bits:
        if bit == '1':
            encoded_bits = np.append(encoded_bits, current_level)
            consecutive_zeros_count = 0
            last_substitution = 0
            current_level = -current_level
        elif bit == '0':
            consecutive_zeros_count += 1
            if consecutive_zeros_count == 4:
                encoded_bits = encoded_bits[:-3]  

                if last_substitution % 2 == 0:
                    current_level = -current_level
                    scrambled_segment = np.array([-current_level, 0, 0, -current_level])
                else:
                    scrambled_segment = np.array([0, 0, 0, -current_level])
                encoded_bits = np.append(encoded_bits, scrambled_segment)
                scrambled_segments.append(scrambled_segment) 
                last_substitution += 1
                consecutive_zeros_count = 0
            else:
                encoded_bits = np.append(encoded_bits, 0)

    return encoded_bits, scrambled_segments


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


# Finding Longest Palindrome 
def longestPalindrome(s):
    longest_palindrom = ''
    dp = np.zeros((len(s), len(s)), dtype=bool)
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):  
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    if len(longest_palindrom) < len(s[i:j + 1]):
                        longest_palindrom = s[i:j + 1]                
    return longest_palindrom

# Plot the HDB3 Encoded Data and Scrambled Signal
def plot(hdb3_data, scrambled_segments):
    plt.figure(figsize=(10, 6))
    
    # Plot HDB3 encoded data
    plt.step(np.arange(len(hdb3_data)), hdb3_data, where='post', color='grey', linewidth=4, label="HDB3 Encoded Data")

    # Plot scrambled signal segments
    for segment in scrambled_segments:
        segment_start = len(hdb3_data) - len(np.concatenate(scrambled_segments)) 
        plt.plot(np.arange(segment_start, segment_start + len(segment)), segment, color='blue', label="Scrambled Segment")
    
    plt.title('HDB3 Encoded Data with Scrambled Signal')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red', linestyle='--')
    plt.ylim(-1.5, 1.5)  
    for i in range(0, len(hdb3_data)):
        plt.axvline(i, color='black', linestyle='--', alpha=0.3)

    # Adding labels to the graph
    plt.legend(loc="upper right")
    plt.show()


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
    hdb3_data, scrambled_segments = hdb3_encoding(binary_data)
    print("Binary Data:", binary_data)
    print("HDB3 Encoded Data:", hdb3_data)
    
    # Check if scrambling occurred
    if scrambled_segments:
        print("Scrambled Signal Produced:")
        for segment in scrambled_segments:
            print(segment)
    else:
        print("No scrambling was necessary in the encoded data.")

    # Finding the longest palindrome in the data stream
    palindrome = longestPalindrome(''.join(binary_data))
    print("Longest palindrome in dataStream:", palindrome)

    # Plotting the HDB3 encoded data along with scrambled segments
    plot(hdb3_data, scrambled_segments)

    # Decoding the data if desired
    decode_choice = input("Do you want to decode the HDB3 encoded data? (yes/no): ").strip().lower()
    if decode_choice == 'yes':
        decoded_data = hdb3_decoding(hdb3_data)
        print("Decoded Data:", decoded_data)
    else:
        print("Decoding skipped.")
