import matplotlib.pyplot as plt
import numpy as np  


# NRZ-L Encoding
def nrz_l_encoding(data):
    encoded_data = np.where(np.array(list(data)) == "1", 1, -1)
    return encoded_data


# NRZ-L Decoding
def nrz_l_decoding(encoded_data):
    decoded_data = np.where(encoded_data == 1, "1", "0")
    return "".join(decoded_data)


# Finding Longest Palindrome
def longestPalindrome(s):
    longest_palindrom = ""
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    if len(longest_palindrom) < len(s[i : j + 1]):
                        longest_palindrom = s[i : j + 1]
    return longest_palindrom


# Plotting NRZ-L Encoded Data
def plot(nrz_l_data):
    plt.step(
        range(len(nrz_l_data)), nrz_l_data, where="post", color="grey", linewidth=4
    )
    plt.title("NRZ-L Encoded Data")
    plt.xlabel("Bit Index")
    plt.ylabel("Voltage Level")
    plt.axhline(0, color="red")
    plt.ylim(-1.5, 1.5)
    for i in range(0, len(nrz_l_data)):
        plt.axvline(i, color="black", linestyle="--")
    plt.show()


if __name__ == "__main__":
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
            bit = input(f"Bit {i+1}: ")
            if bit in ["0", "1"]:
                binary_data.append(bit)
                break
            else:
                print("Invalid input. Only binary values (0 or 1) are allowed.")

    binary_string = "".join(binary_data)
    nrz_l_data = nrz_l_encoding(binary_string)
    print("Binary Data:", binary_data)
    print("NRZ-L Encoded Data:", nrz_l_data)

    # Finding the longest palindrome
    palindrome = longestPalindrome(binary_string)
    print("Longest palindrome in dataStream: ", palindrome)

 
    plot(nrz_l_data)

    decode_choice = (
        input("Do you want to decode the NRZ-L encoded signal? (yes/no): ")
        .strip()
        .lower()
    )
    if decode_choice == "yes":
        decoded_data = nrz_l_decoding(nrz_l_data)
        print("Decoded Data:", decoded_data)
    else:
        print("Decoding skipped.")
