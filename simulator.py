"""Interactive Kepler orbit simulator. Requires matplotlib and numpy."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

# Astronomical units (AU) and years; solar mass assumed to be 1.
fig, ax = plt.subplots(figsize=(9, 7))
fig.subplots_adjust(bottom=0.25)
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('#101728')
fig.patch.set_facecolor('#f7f8fa')
ax.set_title('Kepler Orbital Simulator | Sun at a focus')
ax.set_xlabel('Distance (AU)')
ax.set_ylabel('Distance (AU)')
ax.grid(alpha=0.15)

orbit_line, = ax.plot([], [], color='#66b3ff', lw=1.6)
planet, = ax.plot([], [], 'o', color='#49d5ff', markersize=10)
sun, = ax.plot([0], [0], 'o', color='#ffbc42', markersize=16)
trail, = ax.plot([], [], color='#8de2ff', lw=3, alpha=0.55)
info = ax.text(0.02, 0.97, '', transform=ax.transAxes, va='top', color='white', fontsize=10,
               bbox=dict(facecolor='#17233a', alpha=0.85, edgecolor='none'))

ax_a = fig.add_axes([0.2, 0.13, 0.65, 0.03])
ax_e = fig.add_axes([0.2, 0.08, 0.65, 0.03])
a_slider = Slider(ax_a, 'Semi-major axis (AU)', 0.5, 3.5, valinit=1.5, valstep=0.1)
e_slider = Slider(ax_e, 'Eccentricity', 0.0, 0.85, valinit=0.4, valstep=0.01)
ax_button = fig.add_axes([0.4, 0.015, 0.2, 0.045])
reset_button = Button(ax_button, 'Reset time')

state = {'t': 0.0, 'history': []}
DT = 0.012  # simulated years per animation frame

def solve_kepler(M, e):
    """Solve M = E - e sin(E) by Newton iteration."""
    E = M if e < 0.8 else np.pi
    for _ in range(15):
        E -= (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return E

def coordinates(t, a, e):
    period = a ** 1.5  # Kepler's third law for a solar-mass star
    M = (2 * np.pi * t / period) % (2 * np.pi)
    E = solve_kepler(M, e)
    # Focus at the origin, perihelion to the right.
    x = a * (np.cos(E) - e)
    y = a * np.sqrt(1 - e**2) * np.sin(E)
    return x, y, period

def refresh_orbit(_=None):
    a, e = a_slider.val, e_slider.val
    theta = np.linspace(0, 2 * np.pi, 600)
    orbit_line.set_data(a * (np.cos(theta) - e), a * np.sqrt(1-e*e) * np.sin(theta))
    state['history'].clear()


def reset(_):
    state['t'] = 0.0
    state['history'].clear()


def animate(_):
    state['t'] += DT
    a, e = a_slider.val, e_slider.val
    x, y, period = coordinates(state['t'], a, e)
    planet.set_data([x], [y])
    state['history'].append((x, y))
    state['history'] = state['history'][-65:]
    trail.set_data([p[0] for p in state['history']], [p[1] for p in state['history']])
    r = np.hypot(x, y)
    # Vis-viva equation, with Earth's circular orbital speed = 2*pi AU/year.
    speed = 2 * np.pi * np.sqrt(2/r - 1/a)
    info.set_text(f'Period: {period:.2f} years (P² = a³)\n'
                  f'Distance to Sun: {r:.2f} AU\n'
                  f'Orbital speed: {speed:.2f} AU/year\n'
                  f'Simulated time: {state["t"]:.2f} years')
    return planet, trail, info

a_slider.on_changed(refresh_orbit)
e_slider.on_changed(refresh_orbit)
reset_button.on_clicked(reset)
refresh_orbit()
ani = FuncAnimation(fig, animate, interval=30, blit=False, cache_frame_data=False)
plt.show()
