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
    def no_drag_range_displacement():
        v0 = 50
        G = 9.81
        theta_0 = 45
        angle_0 = 2*theta_0
        angle_rad_r = np.radians(angle_0)
        angle_t = theta_0
        angle_rad_t = np.radians(angle_t)
    
        r = (v0**2) * np.sin(angle_rad_r)/G
        t = 2 * v0 * np.sin(angle_rad_t) / G
        return t, r

    def main():
        t, r = no_drag_range_displacement()
        print(f"Flight time for this projectile at theta = 45 and v0 = 50 (without drag) is: {t:.3f} seconds")
        print(f"Range for this projectile at theta = 45 and v0 = 50 (without drag) is: {r:.3f} metres")

    if __name__ == '__main__':
        main()

    

    return main, no_drag_range_displacement


if __name__ == "__main__":
    app.run()
