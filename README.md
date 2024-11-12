# Digital Signal Generator

## Project Overview

This project implements various *line coding* and *scrambling* schemes for digital signal generation, along with *Pulse Code Modulation (PCM)* and *Delta Modulation (DM)* for encoding analog signals. It allows users to generate digital signals based on user input, apply encoding techniques, and detect palindromes in the data stream. Additionally, it includes optional features for scrambling (B8ZS, HDB3) and decoding of the signals for extra credit.

## Key Features

### Line Coding Techniques:
- *NRZ-L (Non-Return-to-Zero-Level)*
- *NRZ-I (Non-Return-to-Zero-Inverted)*
- *Manchester Encoding*
- *Differential Manchester Encoding*
- *AMI (Alternate Mark Inversion)*

### Scrambling Techniques:
- *B8ZS (Bipolar 8-Zero Substitution)*
- *HDB3 (High-Density Bipolar 3-Zero Substitution)*

### Modulation Techniques:
- *Pulse Code Modulation (PCM)*
- *Delta Modulation (DM)*

### Additional Features:
- *Longest Palindrome Detection*: Identifies the longest palindromic substring in the digital data stream.
- *Graphical Output*: Visualizes the digital and scrambled signals using matplotlib.
- *Signal Decoding (Extra Credit)*: Decodes the chosen encoding scheme to retrieve the original digital stream.

## Requirements

- *Python 3.x*
- *Libraries*: numpy, matplotlib

You can install the necessary libraries using pip:

```bash
pip install numpy matplotlib
