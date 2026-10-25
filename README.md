# Digital Communication Signal Analyzer

## Overview

The Digital Communication Signal Analyzer is a Python-based project that simulates and analyzes BPSK and QPSK digital modulation techniques in the presence of Additive White Gaussian Noise (AWGN).

It compares the Bit Error Rate (BER) at different Signal-to-Noise Ratio (SNR) levels and visualizes the effect of noise on transmitted signals using constellation diagrams.

## Objectives

* Implement BPSK and QPSK modulation.
* Simulate AWGN noise in digital communication signals.
* Calculate BER at different SNR levels.
* Compare BPSK and QPSK BER performance.
* Visualize constellation diagrams at different noise levels.
* Compare transmitted and received signals.

## Technologies Used

* Python
* NumPy
* Matplotlib

## Features

* BPSK modulation and demodulation
* QPSK modulation and demodulation
* AWGN noise simulation
* BER analysis at multiple SNR levels
* BPSK vs QPSK performance comparison
* Constellation diagrams
* Transmitted vs received signal visualization
* Automatic graph saving

## Generated Graphs

The project generates and saves the following visualizations:

1. `bpsk_vs_qpsk_ber.png`
2. `qpsk_constellation.png`
3. `bpsk_constellation.png`
4. `qpsk_different_snr.png`
5. `bpsk_different_snr.png`
6. `bpsk_transmitted_received.png`
7. `qpsk_transmitted_received.png`

## Installation

Install the required Python libraries:

```bash
pip install numpy matplotlib
```

## How to Run

Run the following command in the terminal:

```bash
python main.py
```

The program calculates BER values, displays the graphs, and saves the visualizations as PNG files.

## Learning Outcomes

This project provides practical experience in digital modulation, AWGN noise simulation, BER analysis, constellation diagrams, and signal visualization using Python.

## Project Status

Completed initial simulation and visualization.
