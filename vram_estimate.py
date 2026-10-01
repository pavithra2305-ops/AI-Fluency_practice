def estimate(parameters_b, bytes_per_parameter, context_k, available_gb):
    weights_gb = parameters_b * bytes_per_parameter
    kv_gb = parameters_b * context_k * 0.02
    total_gb = (weights_gb + kv_gb) * 1.10

    if total_gb <= available_gb:
        status = "Fits"
    else:
        status = "Does NOT fit"

    return weights_gb, kv_gb, total_gb, status


def report(model, quantization, parameters, context, bytes_per_parameter, available_gb):
    weights, kv, total, status = estimate(
        parameters,
        bytes_per_parameter,
        context,
        available_gb
    )

    print(f"\nModel: {model}")
    print(f"Quantization: {quantization}")
    print(f"Parameters: {parameters}B")
    print(f"Context: {context}K")
    print(f"Weights VRAM: {weights:.2f} GB")
    print(f"KV Cache VRAM: {kv:.2f} GB")
    print(f"Total VRAM: {total:.2f} GB")
    print(f"Status: {status}")


AVAILABLE_GB = 16.0

print("=" * 50)
print("VRAM ESTIMATION")
print("=" * 50)
print(f"Available Memory: {AVAILABLE_GB} GB")


# Part A - Different model sizes

report("Qwen Small", "Q4", 1.5, 8, 0.57, AVAILABLE_GB)

report("8B Model", "Q4", 8, 8, 0.57, AVAILABLE_GB)

report("8B Model", "FP16", 8, 8, 2.0, AVAILABLE_GB)

report("30B Model", "Q4", 30, 8, 0.57, AVAILABLE_GB)

report("70B Model", "Q4", 70, 8, 0.57, AVAILABLE_GB)


# Part B - Same 8B model with different context sizes

print("\n" + "=" * 50)
print("8B MODEL - CONTEXT COMPARISON")
print("=" * 50)

for context in [4, 8, 32, 128]:
    report("8B Agent", "Q4", 8, context, 0.57, AVAILABLE_GB)


# Part C - Same 8B model with different quantization

print("\n" + "=" * 50)
print("8B MODEL - QUANTIZATION COMPARISON")
print("=" * 50)

quantizations = [
    ("Q3", 0.43),
    ("Q4", 0.57),
    ("Q5", 0.68),
    ("Q8", 1.0),
    ("FP16", 2.0)
]

for quantization, bytes_per_parameter in quantizations:
    report(
        "8B Agent",
        quantization,
        8,
        8,
        bytes_per_parameter,
        AVAILABLE_GB
    )