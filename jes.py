from jes_sim import Sim
from jes_ui import UI

c_input = input("How many creatures do you want?\n100: Lightweight\n250: Standard (if you don't type anything, I'll go with this)\n500: Strenuous (this is what my carykh video used)\n")
if c_input == "":
    c_input = "250"

# Simulation (unchanged, as it’s not resolution-dependent)
sim = Sim(_c_count=int(c_input), _stabilization_time=200, _trial_time=300,
_beat_time=20, _beat_fade_time=5, _c_dim=[4,4],
_beats_per_cycle=3, _node_coor_count=4, # x_position, y_position, x_velocity, y_velocity
_y_clips=[-10000000,0], _ground_friction_coef=25,
_gravity_acceleration_coef=0.002, _calming_friction_coef=0.7,
_typical_friction_coef=0.8, _muscle_coef=0.08,
_traits_per_box=3, # desired width, desired height, rigidity
_traits_extra=1, # heartbeat (time)
_mutation_rate=0.07, _big_mutation_rate=0.025,
_UNITS_PER_METER=0.05)

# Cosmetic UI variables (scaled to effective resolution)
scaling_factor = 1200 / 1920  # Approximately 0.7140625
ui = UI(
    _W_W=int(1920 * 0.72),  # 1371
    _W_H=int(1080 * 0.64),  # 771 (adjusted to match 1920x1080 target)
    _MOVIE_SINGLE_DIM=(int(650 * scaling_factor), int(650 * scaling_factor)),  # (464, 464)
    _GRAPH_COOR=(int(850 * scaling_factor), int(50 * scaling_factor), int(900 * scaling_factor), int(500 * scaling_factor)),  # (607, 36, 643, 357)
    _SAC_COOR=(int(850 * scaling_factor), int(560 * scaling_factor), int(900 * scaling_factor), int(300 * scaling_factor)),  # (607, 400, 643, 214)
    _GENEALOGY_COOR=(int(20 * scaling_factor), int(105 * scaling_factor), int(530 * scaling_factor), int(802 * scaling_factor), int(42 * scaling_factor)),  # (14, 75, 378, 572, 30)
    _COLUMN_MARGIN=int(330 * scaling_factor),  # 236
    _MOSAIC_DIM=[int(10 * scaling_factor), int(24 * scaling_factor), int(24 * scaling_factor), int(30 * scaling_factor)],  # [7, 17, 17, 21]
    _MENU_TEXT_UP=int(180 * scaling_factor),  # 128
    _CM_MARGIN1=int(20 * scaling_factor),  # 14
    _CM_MARGIN2=int(1 * scaling_factor)  # 1 (rounded)
)

sim.ui = ui
ui.sim = sim
ui.addButtonsAndSliders()
    
sim.initializeUniverse()
while ui.running:
    sim.checkALAP()
    ui.detectMouseMotion()
    ui.detectEvents()
    ui.detectSliders()
    ui.doMovies()
    ui.drawMenu()
    ui.show()
