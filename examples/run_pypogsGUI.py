# -*- coding: utf-8 -*-
"""
Run the pypogs GUI
==================

Run this script (i.e. type python run_pypogsGUI.py in a termnial window) to start the pypogs Graphical User Interface.
"""
import sys
from pathlib import Path
sys.path.append('..')
import pypogs

# PRECONFIGURE TRACKING SETTINGS:
#pypogs.tracking.ControlLoopThread.CCL_transition_th = 200
"""
  Note: Changing SpotTracker class properties affects boath coarse and fine control configurations.
        To modify coarse and fine configurations individually, set instance (sys._coarse_track_thread.spot_tracker.*)
        properties instead, after loading requisite hardware (mount + associated coarse or fine camera).
"""
#pypogs.tracking.SpotTracker.smoothing_parameter = 4
#pypogs.tracking.SpotTracker.sigma_mode = 'global_root_square'
#pypogs.tracking.SpotTracker.bg_subtract_mode = 'local_mean'
#pypogs.tracking.SpotTracker.filtsize = 25


# INITIALIZE PYPOGS SYSTEM:
sys = pypogs.System()


# ADD MOUNT:
#sys.add_mount(model="ASCOM", identity="Simulator")
#sys.add_mount(model="ASCOM", identity="DeviceHub", axis_directions=(1, -1))
#sys.add_mount(model="iOptron AZMP", identity="COM2")
#sys.add_mount(model="Celestron", identity="COM2")

# CONFIGURE GROUND STATION SITE:
# class MySite:
#  lat  =  0  # degrees N
#  lon  =  0  # degrees E
#  elev =  500 # meters above MSL
#sys.alignment.set_location_lat_lon(lat=MySite.lat, lon=MySite.lon, height=MySite.elev)
#sys.alignment.set_alignment_enu()


# ADD COARSE CAMERA:
'''
coarsePlateScale = 206 * 5.86 / (400*0.65) # arcsec/pixel,  206 * pixel_pitch_um / focal_length_mm
sys.add_coarse_camera(
  model="ASCOM", 
  #identity="ASICamera2",
  #identity="ASICamera2_2",
  #identity="Simulator",
  identity="QHYCCD_GUIDER",
  exposure_time = 100,
  #gain = 400,
  plate_scale = round(coarsePlateScale, 3),  
  binning = 2
)
'''

# ADD STAR CAMERA:
#sys.add_star_camera_from_coarse()


# ADD FINE CAMERA:
#finePlateScale = 206 * 5.86 / 2350 # arcsec/pixel,  206 * pixel_pitch_um / focal_length_mm
#sys.add_fine_camera(model="ASCOM", identity="ASICamera2", exposure_time=500, gain=260, plate_scale=finePlateScale)


# CHANGE COARSE/FINE TRACKING SETTINGS INDIVIDUALLY:
# (MOUNT AND RESPECTIVE COARSE/FINE CAMERA MUST BE DEFINED PREVIOUSLY)
#sys.coarse_track_thread.spot_tracker.smoothing_parameter = 4
#sys.coarse_track_thread.spot_tracker.sigma_mode = 'global_root_square'
#sys.coarse_track_thread.spot_tracker.bg_subtract_mode = 'local_mean'
#sys.coarse_track_thread.spot_tracker.filtsize = 25

# ENABLE SAVING IMAGES DURING TRACKING:
# (MOUNT AND RESPECTIVE COARSE/FINE CAMERA MUST BE DEFINED PREVIOUSLY)
#sys.coarse_track_thread.img_save_frequency = 1
#sys.coarse_track_thread.image_folder = Path('D:\pypogs')
#sys.fine_track_thread.img_save_frequency = 1
#sys.fine_track_thread.image_folder = Path('D:\pypogs')



# SET TARGET:
#sys.target.get_and_set_tle_from_sat_id(23712)  # ISS = 25544
sys.target.get_and_set_tle_from_sat_id(25544)  # ISS = 25544
#sys.target.get_ephem(obj_id='-48', lat=MySite.lat, lon=MySite.lon, height=MySite.elev)
#sys.target.get_ephem(obj_id='7', lat=MySite.lat, lon=MySite.lon, height=MySite.elev)
#sys.target.get_ephem(obj_id='-170', lat=MySite.lat, lon=MySite.lon, height=MySite.elev)


# START GUI:
try:
    #sys.do_auto_star_alignment(max_trials=2, rate_control=True, pos_list=[(40, -135), (60, -135)])
    pypogs.GUI(sys, 500)
    

except Exception:
    raise
finally:
    sys.deinitialize()