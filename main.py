# Digital-Communication-Signal-Analyzer

import numpy as np
import matplotlib.pyplot as plt

# Generate random bits
bits = np.random.randint(0, 2, 10000)

print("Generate bits:", bits)

# BPSK modulation
bpsk_Signal = 2 * bits - 1

print("BPSK Signal:", bpsk_Signal)

# SNR values
snr_values = [0, 2, 4, 6, 8, 10]

# BPSK BER calculation
ber_values = []

for snr_db in snr_values:

    noise_power = 1 / (10 ** (snr_db / 10))

    noise = np.sqrt(noise_power) * np.random.randn(len(bpsk_Signal))

    received_signal = bpsk_Signal + noise

    detected_bits = (received_signal > 0).astype(int)

    bit_errors = np.sum(bits != detected_bits)

    ber = bit_errors / len(bits)

    ber_values.append(ber)

    print("SNR:", snr_db, "dB | BER:", ber)


# QPSK modulation

qpsk_bits = bits[:len(bits) // 2 * 2]

bit_pairs = qpsk_bits.reshape(-1, 2)

print("First 5 bit pairs:")
print(bit_pairs[:5])

qpsk_signal = np.zeros(len(bit_pairs), dtype=complex)

for i, pair in enumerate(bit_pairs):

    if np.array_equal(pair, [0, 0]):
        qpsk_signal[i] = 1 + 1j

    elif np.array_equal(pair, [0, 1]):
        qpsk_signal[i] = -1 + 1j

    elif np.array_equal(pair, [1, 0]):
        qpsk_signal[i] = 1 - 1j

    else:
        qpsk_signal[i] = -1 - 1j

print("First 5 QPSK symbols:")
print(qpsk_signal[:5])

qpsk_signal = qpsk_signal / np.sqrt(2)


# Add AWGN noise to QPSK signal

snr_db = 5

noise_power = 1 / (10 ** (snr_db / 10))

noise = np.sqrt(noise_power / 2) * (
    np.random.randn(len(qpsk_signal))
    + 1j * np.random.randn(len(qpsk_signal))
)

received_qpsk = qpsk_signal + noise

print("First 5 received QPSK symbols:")
print(received_qpsk[:5])


# QPSK demodulation

detected_qpsk_bits = []

for symbol in received_qpsk:

    if symbol.real >= 0 and symbol.imag >= 0:
        detected_qpsk_bits.extend([0, 0])

    elif symbol.real < 0 and symbol.imag >= 0:
        detected_qpsk_bits.extend([0, 1])

    elif symbol.real >= 0 and symbol.imag < 0:
        detected_qpsk_bits.extend([1, 0])

    else:
        detected_qpsk_bits.extend([1, 1])

detected_qpsk_bits = np.array(detected_qpsk_bits)

print("First 10 detected QPSK bits:")
print(detected_qpsk_bits[:10])


# Calculate QPSK BER

qpsk_bit_errors = np.sum(qpsk_bits != detected_qpsk_bits)

qpsk_ber = qpsk_bit_errors / len(qpsk_bits)

print("QPSK bit errors:", qpsk_bit_errors)
print("QPSK BER:", qpsk_ber)


# Test QPSK at different SNR values

qpsk_ber_values = []

for snr_db in snr_values:

    noise_power = 1 / (10 ** (snr_db / 10))

    noise = np.sqrt(noise_power / 2) * (
        np.random.randn(len(qpsk_signal))
        + 1j * np.random.randn(len(qpsk_signal))
    )

    received_qpsk = qpsk_signal + noise

    detected_qpsk_bits = []

    for symbol in received_qpsk:

        if symbol.real >= 0 and symbol.imag >= 0:
            detected_qpsk_bits.extend([0, 0])

        elif symbol.real < 0 and symbol.imag >= 0:
            detected_qpsk_bits.extend([0, 1])

        elif symbol.real >= 0 and symbol.imag < 0:
            detected_qpsk_bits.extend([1, 0])

        else:
            detected_qpsk_bits.extend([1, 1])

    detected_qpsk_bits = np.array(detected_qpsk_bits)

    bit_errors = np.sum(qpsk_bits != detected_qpsk_bits)

    ber = bit_errors / len(qpsk_bits)

    qpsk_ber_values.append(ber)

    print("QPSK SNR:", snr_db, "dB | BER:", ber)


# Compare BPSK and QPSK

plt.figure()

plt.semilogy(snr_values, ber_values, marker='o', label='BPSK')
plt.semilogy(snr_values, qpsk_ber_values, marker='s', label='QPSK')

plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BPSK vs QPSK Performance")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("bpsk_vs_qpsk_ber.png", dpi=300, bbox_inches="tight")

plt.show()


# QPSK constellation diagram

plt.figure()

plt.scatter(received_qpsk.real, received_qpsk.imag, s=5)

plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.title("QPSK Constellation with AWGN")

plt.grid(True)
plt.axis("equal")
plt.tight_layout()

plt.savefig("qpsk_constellation.png", dpi=300, bbox_inches="tight")

plt.show()


# BPSK constellation diagram

plt.figure()

plt.scatter(received_signal, np.zeros(len(received_signal)), s=5)

plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.title("BPSK Constellation with AWGN")

plt.grid(True)
plt.axis("equal")
plt.tight_layout()

plt.savefig("bpsk_constellation.png", dpi=300, bbox_inches="tight")

plt.show()


# QPSK constellation at different SNR values

plt.figure(figsize=(12, 4))

for i, snr_db in enumerate([0, 5, 10]):

    noise_power = 1 / (10 ** (snr_db / 10))

    noise = np.sqrt(noise_power / 2) * (
        np.random.randn(len(qpsk_signal))
        + 1j * np.random.randn(len(qpsk_signal))
    )

    received = qpsk_signal + noise

    plt.subplot(1, 3, i + 1)

    plt.scatter(received.real, received.imag, s=5)

    plt.xlabel("I")
    plt.ylabel("Q")
    plt.title(f"{snr_db} dB SNR")

    plt.grid(True)
    plt.axis("equal")

plt.suptitle("QPSK Constellation at Different SNR Levels")
plt.tight_layout()

plt.savefig("qpsk_different_snr.png", dpi=300, bbox_inches="tight")

plt.show()


# BPSK constellation at different SNR values

plt.figure(figsize=(12, 4))

for i, snr_db in enumerate([0, 5, 10]):

    noise_power = 1 / (10 ** (snr_db / 10))

    noise = np.sqrt(noise_power) * np.random.randn(len(bpsk_Signal))

    received = bpsk_Signal + noise

    plt.subplot(1, 3, i + 1)

    plt.scatter(received, np.zeros(len(received)), s=5)

    plt.xlabel("I")
    plt.ylabel("Q")
    plt.title(f"{snr_db} dB SNR")

    plt.grid(True)
    plt.axis("equal")

plt.suptitle("BPSK Constellation at Different SNR Levels")
plt.tight_layout()

plt.savefig("bpsk_different_snr.png", dpi=300, bbox_inches="tight")

plt.show()


# Transmitted vs Received BPSK signal

plt.figure()

plt.plot(bpsk_Signal[:100], label="Transmitted Signal")
plt.plot(received_signal[:100], label="Received Signal")

plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.title("Transmitted vs Received BPSK Signal")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("bpsk_transmitted_received.png", dpi=300, bbox_inches="tight")

plt.show()


# Transmitted vs Received QPSK signal

plt.figure()

plt.plot(qpsk_signal.real[:100], label="Transmitted QPSK")
plt.plot(received_qpsk.real[:100], label="Received QPSK")

plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.title("Transmitted vs Received QPSK Signal")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("qpsk_transmitted_received.png", dpi=300, bbox_inches="tight")

plt.show()


# Completion message

print("\nSimulation completed successfully!")
print("All graph files have been saved.")