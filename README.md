# Kepler's Laws: Interactive Orbital Simulator

A Python animation demonstrating Kepler's laws of planetary motion for an idealized planet orbiting a Sun-mass star.

## Run

Install Python 3.10+ and run:

```bash
python -m pip install -r requirements.txt
python simulator.py
```

On macOS, use `python3` instead of `python` if needed.

## Controls

- **Semi-major axis:** changes orbit size and period.
- **Eccentricity:** changes how stretched the ellipse is.
- **Reset time:** restarts the simulated clock.

## Astronomy explained

1. **Elliptical orbits:** The Sun sits at one focus, not at the ellipse's center.
2. **Equal areas in equal times:** The planet moves faster near perihelion (closest approach) and slower near aphelion (farthest point). The simulation uses Kepler's equation, so its position advances in equal time steps rather than equal angular steps.
3. **Period-distance relationship:** For a small planet orbiting a one-solar-mass star, `P² = a³` with `P` in years and `a` in astronomical units.

The animation uses the ideal two-body model and ignores gravitational perturbations from other planets. The on-screen speed is expressed in AU/year and follows the vis-viva equation. The trail depicts recent motion, not equal-area sectors.

## Suggested class submission

Include a screenshot or short screen recording of the running program, the GitHub repository link, and a one-page explanation of how each law appears in the simulation. Credit external code, references, and images if added.
