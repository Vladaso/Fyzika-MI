import numpy as np
import matplotlib.pyplot as plt

def mag_pole_dipole(r_x, r_y, r0_x=0.0, r0_y=0.0, m_x=0, m_y=1):
    r_x = r_x - r0_x
    r_y = r_y - r0_y
    r = np.sqrt(r_x * r_x + r_y * r_y)
    B_x = 3 * r_x * (m_x * r_x + m_y * r_y) / r**5 - m_x / r**3
    B_y = 3 * r_y * (m_x * r_x + m_y * r_y) / r**5 - m_y / r**3
    return B_x, B_y

def get_B_specific_point(x, y, m_x=0.0, m_y=1, r0_x=0.0, r0_y=0.0):
    r_x = x - r0_x
    r_y = y - r0_y
    r = np.sqrt(r_x * r_x + r_y * r_y)
    B_x = 3 * r_x * (m_x * r_x + m_y * r_y) / r**5 - m_x / r**3
    B_y = 3 * r_y * (m_x * r_x + m_y * r_y) / r**5 - m_y / r**3
    return np.sqrt(B_x**2 + B_y**2), B_x, B_y

# Function to calculate force on a segment of wire in the magnetic field
def calculate_force(I, B_x, B_y, length_x, length_y):
    force_x = I * (length_y * B_x)
    force_y = I * (-length_x * B_y)
    return force_x, force_y

# Function to calculate total torque for a given wire shape
def calculate_total_torque(wire_x, wire_y, I):
    total_torque = 0
    forces_x = []
    forces_y = []
    num_segments = len(wire_x)
    for i in range(num_segments - 1):
        B_mag, B_x_val, B_y_val = get_B_specific_point(wire_x[i], wire_y[i])
        length_x = wire_x[i+1] - wire_x[i]
        length_y = wire_y[i+1] - wire_y[i]
        force_x, force_y = calculate_force(I, B_x_val, B_y_val, length_x, length_y)
        forces_x.append(force_x)
        forces_y.append(force_y)
        
        # Position vector (from center to current segment)
        r_x = (wire_x[i] + wire_x[i+1]) / 2
        r_y = (wire_y[i] + wire_y[i+1]) / 2
        
        # Torque = r x F
        torque = r_x * force_y - r_y * force_x
        total_torque += np.abs(torque)
    return total_torque, forces_x, forces_y

# Function to generate wire shapes (ellipse)
def generate_wire_shape(a, b, num_segments=100):
    theta = np.linspace(0, 2 * np.pi, num_segments)
    wire_x = a * np.cos(theta)
    wire_y = b * np.sin(theta)
    return wire_x, wire_y

# Define the current
I = 1  # current through the wire

# Define the range of parameters to search
a_values = np.linspace(1, 10, 20)
b_values = np.linspace(1, 10, 20)

# Grid search for optimal ellipse parameters
max_torque = -np.inf
optimal_a = None
optimal_b = None
optimal_forces_x = None
optimal_forces_y = None
optimal_wire_x = None
optimal_wire_y = None

for a in a_values:
    for b in b_values:
        wire_x, wire_y = generate_wire_shape(a, b)
        total_torque, forces_x, forces_y = calculate_total_torque(wire_x, wire_y, I)
        print(f"Ellipse Parameters: a={a}, b={b}, Total Torque: {total_torque}")
        if total_torque > max_torque:
            max_torque = total_torque
            optimal_a = a
            optimal_b = b
            optimal_forces_x = forces_x
            optimal_forces_y = forces_y
            optimal_wire_x = wire_x
            optimal_wire_y = wire_y

print(f"Optimal Ellipse Parameters: a={optimal_a}, b={optimal_b}, Max Torque: {max_torque}")

# Plot the optimal wire shape and forces acting on it
plt.figure(figsize=(10, 10))
plt.plot(optimal_wire_x, optimal_wire_y, label="Wire Shape")
plt.quiver(optimal_wire_x[:-1], optimal_wire_y[:-1], optimal_forces_x, optimal_forces_y, color='r', pivot='mid', label="Forces")
plt.title("Optimal Ellipse Shape and Forces in Homopolar Motor")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
