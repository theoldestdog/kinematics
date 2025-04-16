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
    vi = 50
    g = 9.81
    theta_R = 45
    angle_rad_r = 2*theta_R
    angle_rad_R = np.radians(angle_rad_r)

    R = (vi**2) * np.sin(angle_rad_R)/g

    print(f"Range for this projectile at theta = 45 and vi = 50 (without drag) is: {R:.3f} metres")

    return R, angle_rad_R, angle_rad_r, g, theta_R, vi


@app.cell
def _(np):
    vt = 50
    gt = 9.81
    theta_t = 45
    angle_t = theta_t
    angle_rad_t = np.radians(angle_t)

    ty = 2 * vt * np.sin(angle_rad_t) / gt
    print(f"Flight time for this projectile at theta = 45 and vt = 50 (without drag) is: {ty:.3f} seconds")

    return angle_rad_t, angle_t, gt, theta_t, ty, vt


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
