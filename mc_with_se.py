import numpy as np

# Define parameters
mean_20_yards = 0.9905878  # Observed mean probability of kicking an xp when it was 20 yards
standard_error_20_yards = 0.0009099199  # Standard error for above
mean_33_yards = 0.9422206  # Observed mean probability of kicking an xp when it was 33 yards
standard_error_33_yards = 0.002198254  # Standard error for above
distance_to_interpolate = 22  # Distance to interpolate
twopc_exp_outcome = 0.4917695*2
# Generate random samples
num_samples = 10000

# Compute slope for linear interpolation
slope = (mean_33_yards - mean_20_yards) / (33 - 20)

# Store results of interpolation
results = []

# Perform Monte Carlo simulation
for i in range(num_samples):
    # Generate random sample of success probability at 20 yards
    sample_20_yards = np.random.normal(mean_20_yards, standard_error_20_yards)
    # Generate random sample of success probability at 33 yards
    sample_33_yards = np.random.normal(mean_33_yards, standard_error_33_yards)
    
    # Interpolate to estimate success probability at 30 yards
    interpolated_mean = sample_20_yards + slope * (distance_to_interpolate - 20)
    
    # Store the result for analysis
    results.append(interpolated_mean)

# Compute mean and standard error of the results
mean_estimate = np.mean(results)
standard_error = np.std(results) / np.sqrt(len(results))

print("Mean Estimate:", mean_estimate)
print("Standard Error:", standard_error)
print("Difference in expected value:", mean_estimate - twopc_exp_outcome)