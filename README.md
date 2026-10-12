# Kepler's Laws: Interactive Orbital Simulator

A Python animation demonstrating Kepler's laws of planetary motion for an idealized planet orbiting a Sun-mass star.

## Run on macOS

1. Open **Terminal** (Applications → Utilities → Terminal) and check whether Python 3 is installed:

   ```bash
   python3 --version
   ```

   If Python 3.10 or newer is installed, skip to step 3.

2. If Terminal says `python3` is not found, install Homebrew:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   Follow the prompts. Then install Python:

   ```bash
   brew install python
   ```

   If the Homebrew installer gives you extra setup instructions, follow them. Check that Python installed:

   ```bash
   python3 --version
   ```

3. Download or clone this repository. To clone it from Terminal, run:

   ```bash
   git clone https://github.com/timothyleedoyun/keplers-laws-orbital-simulator.git
   cd keplers-laws-orbital-simulator
   ```

4. Create a virtual environment and install the project packages:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   ```

5. Start the simulator:

   ```bash
   python simulator.py
   ```

   To run it again later, open Terminal, go to the project folder, activate the environment with `source .venv/bin/activate`, and run `python simulator.py`.

## Controls

- **Semi-major axis:** changes the orbit's size and period.
- **Eccentricity:** changes how stretched the ellipse is.
- **Reset time:** restarts the simulated clock.

## Astronomy explained

1. **Elliptical orbits:** The Sun sits at one focus of the ellipse, not at its center.
2. **Equal areas in equal times:** The planet moves faster near perihelion, its closest point to the Sun, and slower near aphelion, its farthest point. The simulation uses Kepler's equation, so the planet advances in equal time steps rather than equal angular steps.
3. **Period-distance relationship:** For a small planet orbiting a one-solar-mass star, `P² = a³`, where `P` is measured in years and `a` in astronomical units (AU).

The displayed speed is measured in AU/year and calculated with the vis-viva equation. The trail shows recent motion; it does not draw equal-area sectors.

## Why I chose this project

I enjoy using Python to explore mathematical ideas, and I am interested in how changing inputs affects a model's results. This project connects that interest in computational modeling with astronomy by letting me change an orbit and observe how its shape, speed, and period respond.

## Model limits

This is an idealized two-body model of one planet orbiting a Sun-mass star. It does not include gravitational effects from other planets, and the plotted object sizes are symbolic.

## Files

- `simulator.py` — the interactive simulation
- `requirements.txt` — the Python packages needed to run it

## Reference

NASA Science, [Orbits and Kepler's Laws](https://science.nasa.gov/solar-system/orbits-and-keplers-laws/).
