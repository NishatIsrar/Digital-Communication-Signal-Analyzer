# Digital Communication Signal Analyzer
# BPSK and QPSK Performance Analysis under AWGN

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Generate Random Binary Data
# --------------------------------------------------

np.random.seed(42)

bits = np.random.randint(0, 2, 10000)

print("DIGITAL COMMUNICATION SIGNAL ANALYZER")
print("=" * 45)
print("Total bits generated:", len(bits))


# --------------------------------------------------
# 2. BPSK Modulation
# --------------------------------------------------

bpsk_signal = 2 * bits - 1

print("\nFirst 10 BPSK symbols:")
print(bpsk_signal[:10])


# --------------------------------------------------
# 3. BPSK BER Calculation
# --------------------------------------------------

snr_values = [0, 2, 4, 6, 8, 10]

bpsk_ber_values = []

for snr_db in snr_values:

    noise_power = 1 / (10 ** (snr_db / 10))

    noise = np.sqrt(noise_power) * np.random.randn(len(bpsk_signal))

    received_bpsk = bpsk_signal + noise

    detected_bits = (received_bpsk > 0).astype(int)

    bit_errors = np.sum(bits != detected_bits)

    ber = bit_errors / len(bits)

    bpsk_ber_values.append(ber)

    print(f"BPSK | SNR: {snr_db} dB | BER: {ber:.6f}")


# --------------------------------------------------
# 4. QPSK Modulation
# --------------------------------------------------

qpsk_bits = bits[:len(bits) // 2 * 2]

bit_pairs = qpsk_bits.reshape(-1, 2)

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

# Normalize QPSK symbols
qpsk_signal = qpsk_signal / np.sqrt(2)

print("\nFirst 5 QPSK symbols:")
print(qpsk_signal[:5])


# --------------------------------------------------
# 5. QPSK BER Calculation
# --------------------------------------------------

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

    print(f"QPSK | SNR: {snr_db} dB | BER: {ber:.6f}")


# --------------------------------------------------
# 6. BPSK vs QPSK BER Comparison
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.semilogy(
    snr_values,
    bpsk_ber_values,
    marker="o",
    label="BPSK"
)

plt.semilogy(
    snr_values,
    qpsk_ber_values,
    marker="s",
    label="QPSK"
)

plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BPSK vs QPSK Performance")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("bpsk_vs_qpsk_ber.png", dpi=300, bbox_inches="tight")
plt.show()


# --------------------------------------------------
# 7. QPSK Constellation Diagram
# --------------------------------------------------

snr_db = 5

noise_power = 1 / (10 ** (snr_db / 10))

noise = np.sqrt(noise_power / 2) * (
    np.random.randn(len(qpsk_signal))
    + 1j * np.random.randn(len(qpsk_signal))
)

received_qpsk = qpsk_signal + noise

plt.figure(figsize=(7, 5))

plt.scatter(
    received_qpsk.real,
    received_qpsk.imag,
    s=5
)

plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.title("QPSK Constellation with AWGN")
plt.grid(True)
plt.axis("equal")
plt.tight_layout()

plt.savefig("qpsk_constellation.png", dpi=300, bbox_inches="tight")
plt.show()


# --------------------------------------------------
# 8. BPSK Constellation Diagram
# --------------------------------------------------

noise_power = 1 / (10 ** (snr_db / 10))

noise = np.sqrt(noise_power) * np.random.randn(len(bpsk_signal))

received_bpsk = bpsk_signal + noise

plt.figure(figsize=(7, 5))

plt.scatter(
    received_bpsk,
    np.zeros(len(received_bpsk)),
    s=5
)

plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.title("BPSK Constellation with AWGN")
plt.grid(True)
plt.axis("equal")
plt.tight_layout()

plt.savefig("bpsk_constellation.png", dpi=300, bbox_inches="tight")
plt.show()


# --------------------------------------------------
# 9. QPSK Constellation at Different SNR Levels
# --------------------------------------------------

plt.figure(figsize=(12, 4))

for i, snr_db in enumerate([0, 5, 10]):

    noise_power = 1 / (10 ** (snr_db / 10))

    noise = np.sqrt(noise_power / 2) * (
        np.random.randn(len(qpsk_signal))
        + 1j * np.random.randn(len(qpsk_signal))
    )

    received = qpsk_signal + noise

    plt.subplot(1, 3, i + 1)

    plt.scatter(
        received.real,
        received.imag,
        s=5
    )

    plt.xlabel("In-phase (I)")
    plt.ylabel("Quadrature (Q)")
    plt.title(f"SNR = {snr_db} dB")
    plt.grid(True)
    plt.axis("equal")

plt.suptitle("QPSK Constellation at Different SNR Levels")
plt.tight_layout()

plt.savefig("qpsk_different_snr.png", dpi=300, bbox_inches="tight")
plt.show()


# --------------------------------------------------
# 10. BPSK Constellation at Different SNR Levels
# --------------------------------------------------

plt.figure(figsize=(12, 4))

for i, snr_db in enumerate([0, 5, 10]):

    noise_power = 1 / (10 ** (snr_db / 10))

    noise = np.sqrt(noise_power) * np.random.randn(len(bpsk_signal))

    received = bpsk_signal + noise

    plt.subplot(1, 3, i + 1)

    plt.scatter(
        received,
        np.zeros(len(received)),
        s=5
    )

    plt.xlabel("In-phase (I)")
    plt.ylabel("Quadrature (Q)")
    plt.title(f"SNR = {snr_db} dB")
    plt.grid(True)
    plt.axis("equal")

plt.suptitle("BPSK Constellation at Different SNR Levels")
plt.tight_layout()

plt.savefig("bpsk_different_snr.png", dpi=300, bbox_inches="tight")
plt.show()


# --------------------------------------------------
# 11. Transmitted vs Received BPSK Signal
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    bpsk_signal[:100],
    label="Transmitted BPSK Signal"
)

plt.plot(
    received_bpsk[:100],
    label="Received BPSK Signal"
)

plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.title("Transmitted vs Received BPSK Signal")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("bpsk_transmitted_received.png", dpi=300, bbox_inches="tight")
plt.show()


# --------------------------------------------------
# 12. Transmitted vs Received QPSK Signal
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    qpsk_signal.real[:100],
    label="Transmitted QPSK Signal"
)

plt.plot(
    received_qpsk.real[:100],
    label="Received QPSK Signal"
)

plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.title("Transmitted vs Received QPSK Signal")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("qpsk_transmitted_received.png", dpi=300, bbox_inches="tight")
plt.show()


# --------------------------------------------------
# 13. Completion Message
# --------------------------------------------------

print("\n" + "=" * 45)
print("SIMULATION COMPLETED SUCCESSFULLY!")
print("All 7 graphs have been saved as PNG files.")
print("=" * 45)