import marimo

__generated_with = "0.11.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


@app.cell
def _(np):
    '''
    This example uses a list to calculate the parameters for the projectile.
    Note for  values equally distant from 45, the distance travelled is the same
    but the time of flight is longer.

    '''

    theta_list = [25, 35, 45, 55, 65]  # Launch angles
    v0 = 50
    G = 9.81

    for theta in theta_list:
        angle_rad_r = np.radians(2 * theta)  # Convert 2*theta to radians
        r = (v0**2) * np.sin(angle_rad_r) / G
        print(f"Range for theta = {theta}°: {r:.3f} metres")
        angle_rad_t = np.radians(theta)
        t = 2 * v0 * np.sin(angle_rad_t) / G
        print(f"Flight time for theta = {theta}°: {t:.3f} seconds")
    return G, angle_rad_r, angle_rad_t, r, t, theta, theta_list, v0


if __name__ == "__main__":
    app.run()
