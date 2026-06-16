"""
Halo 2 Xbox Object Monitor - Scripts tab mixin.
"""
import tkinter as tk
from tkinter import ttk

SCRIPT_DATABASE = {
    'scenarios/solo/00a_introduction/00a_introduction': {
        "objects": {
            'armory': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['introduction_cinematics']},
            'athens': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'banshee_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'banshee_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'banshee_03': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'banshee_04': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'banshee_05': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'banshee_06': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'banshee_07': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'banshee_08': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'banshee_09': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'banshee_10': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'brute_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'brute_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cairo': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'carrier_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cart': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['introduction_cinematics']},
            'chief': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'cruiser_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cruiser_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cruiser_03': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cruiser_04': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cruiser_05': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cruiser_06': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cruiser_07': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cruiser_08': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'cruiser_09': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'dervish': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'elc_26': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['introduction_cinematics']},
            'elc_27': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['introduction_cinematics']},
            'elite_counc_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'elite_counc_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'halo_exploding': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'halo_whole': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['introduction_cinematics']},
            'hammer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'helmet': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'iac_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'malta': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'master_guns': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['introduction_cinematics']},
            'mercy': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'optics': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['introduction_cinematics']},
            'pcc_33': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['introduction_cinematics']},
            'pcc_34': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['introduction_cinematics']},
            'poa_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['introduction_cinematics']},
            'poa_02': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['introduction_cinematics']},
            'poa_03': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['introduction_cinematics']},
            'power_supply': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['introduction_cinematics']},
            'prophet_counc_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'prophet_counc_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'prophet_counc_03': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['introduction_cinematics']},
            'prophet_counc_04': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['introduction_cinematics']},
            'regret': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'tartarus': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'throne_mercy': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'throne_regret': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'throne_truth': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['introduction_cinematics']},
            'truth': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['introduction_cinematics']},
            'x01_fleet': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['introduction_cinematics']},
        },
        "scripts": [('x01_01_predict', 'dormant', '00a_introduction_prediction'), ('x01_01b_predict', 'dormant', '00a_introduction_prediction'), ('x01_02_predict', 'dormant', '00a_introduction_prediction'), ('x01_03_predict', 'dormant', '00a_introduction_prediction'), ('x01_04_predict', 'dormant', '00a_introduction_prediction'), ('x01_05_predict', 'dormant', '00a_introduction_prediction'), ('x01_06_predict', 'dormant', '00a_introduction_prediction'), ('x01_07_predict', 'dormant', '00a_introduction_prediction'), ('x01_08_predict', 'dormant', '00a_introduction_prediction'), ('x01_09_predict', 'dormant', '00a_introduction_prediction'), ('x01_10_predict', 'dormant', '00a_introduction_prediction'), ('01_intro_01_predict', 'dormant', '00a_introduction_prediction'), ('01_intro_02_predict', 'dormant', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'static', '00a_introduction_prediction'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('void', 'stub', 'introduction_cinematics'), ('x01_score_01a', 'dormant', 'introduction_cinematics'), ('x01_foley_01a', 'dormant', 'introduction_cinematics'), ('x01_supratitle_01', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_01a', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_foley_01b', 'dormant', 'introduction_cinematics'), ('x01_0010_der', 'dormant', 'introduction_cinematics'), ('banshee_audio', 'dormant', 'introduction_cinematics'), ('banshee_hotness', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_01b', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_foley_02', 'dormant', 'introduction_cinematics'), ('x01_0020_pot', 'dormant', 'introduction_cinematics'), ('x01_0030_der', 'dormant', 'introduction_cinematics'), ('x01_0040_pcc', 'dormant', 'introduction_cinematics'), ('x01_0050_pom', 'dormant', 'introduction_cinematics'), ('x01_0060_der', 'dormant', 'introduction_cinematics'), ('x01_02_fov', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_02', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('create_councillors_01', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_foley_03', 'dormant', 'introduction_cinematics'), ('x01_0070_der', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_03', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_0080_por', 'dormant', 'introduction_cinematics'), ('x01_0090_der', 'dormant', 'introduction_cinematics'), ('x01_0100_por', 'dormant', 'introduction_cinematics'), ('x01_0110_der', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_04', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_04_cleanup', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_foley_05', 'dormant', 'introduction_cinematics'), ('x01_0120_por', 'dormant', 'introduction_cinematics'), ('x01_0130_por', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_05', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_foley_06', 'dormant', 'introduction_cinematics'), ('x01_0140_der', 'dormant', 'introduction_cinematics'), ('x01_0150_cch', 'dormant', 'introduction_cinematics'), ('x01_0160_pom', 'dormant', 'introduction_cinematics'), ('x01_0170_pot', 'dormant', 'introduction_cinematics'), ('x01_0180_der', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_06', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_foley_07', 'dormant', 'introduction_cinematics'), ('x01_0190_der', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_07', 'dormant', 'introduction_cinematics'), ('halo_explosion', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_0200_pcc', 'dormant', 'introduction_cinematics'), ('x01_0210_tar', 'dormant', 'introduction_cinematics'), ('x01_0220_por', 'dormant', 'introduction_cinematics'), ('x01_0230_pot', 'dormant', 'introduction_cinematics'), ('x01_0240_pot', 'dormant', 'introduction_cinematics'), ('x01_08_fov', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_08', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_0250_pc1', 'dormant', 'introduction_cinematics'), ('x01_0260_pcc', 'dormant', 'introduction_cinematics'), ('x01_0270_der', 'dormant', 'introduction_cinematics'), ('x01_0280_pot', 'dormant', 'introduction_cinematics'), ('x01_0290_tar', 'dormant', 'introduction_cinematics'), ('x01_09_fov', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_09', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('x01_score_10', 'dormant', 'introduction_cinematics'), ('x01_0300_pot', 'dormant', 'introduction_cinematics'), ('x01_0310_cch', 'dormant', 'introduction_cinematics'), ('x01_0320_pot', 'dormant', 'introduction_cinematics'), ('x01_0330_pot', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_scene_10', 'dormant', 'introduction_cinematics'), ('improve_framerate', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('c01_intro_foley_01', 'dormant', 'introduction_cinematics'), ('c01_1010_qtm', 'dormant', 'introduction_cinematics'), ('c01_intro_supratitle_01', 'dormant', 'introduction_cinematics'), ('lens_flares', 'dormant', 'introduction_cinematics'), ('c01_intro_dof_01', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_c01_scene_01', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('ships_unhide', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('c01_intro_foley_02', 'dormant', 'introduction_cinematics'), ('c01_1020_qtm', 'dormant', 'introduction_cinematics'), ('c01_1030_qtm', 'dormant', 'introduction_cinematics'), ('c01_1040_qtm', 'dormant', 'introduction_cinematics'), ('c01_1050_mas', 'dormant', 'introduction_cinematics'), ('cinematic_lighting_c01_scene_02', 'dormant', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('void', 'static', 'introduction_cinematics'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/01a_tutorial/01a_tutorial': {
        "objects": {
            'atr1_mar': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01a_tutorial_mission']},
            'atr2_mar': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01a_tutorial_mission']},
            'door_elevator_tram_bot': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['01a_tutorial_mission']},
            'door_tram_2': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01a_tutorial_mission']},
            'door_tram_3': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01a_tutorial_mission']},
            'door_tram_4': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01a_tutorial_mission']},
            'elevator_tram': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['01a_tutorial_mission']},
            'guns': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['01a_tutorial_mission']},
            'inhibitor': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['01a_tutorial_mission']},
            'johnson': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['01a_tutorial_mission']},
            'looker_light_bottom_green': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01a_tutorial_mission']},
            'looker_light_bottom_red': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01a_tutorial_mission']},
            'looker_light_left_green': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01a_tutorial_mission']},
            'looker_light_left_red': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01a_tutorial_mission']},
            'looker_light_right_green': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01a_tutorial_mission']},
            'looker_light_right_red': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01a_tutorial_mission']},
            'looker_light_top_green': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01a_tutorial_mission']},
            'looker_light_top_red': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01a_tutorial_mission']},
            'mid_mar': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01a_tutorial_mission']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['01a_tutorial_mission']},
            'tram': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['01a_tutorial_mission']},
            'tv_start_spot': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01a_tutorial_mission']},
            'tv_tram': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['01a_tutorial_mission']},
            'tv_zapper': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01a_tutorial_mission']},
            'zapper': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['01a_tutorial_mission']},
            'zapper_cage': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['01a_tutorial_mission']},
            'zapper_control': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['01a_tutorial_mission']},
            'zapper_control_group': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['01a_tutorial_mission']},
        },
        "scripts": [('save_look_start', 'static', '01a_tutorial_mission'), ('save_move_start', 'static', '01a_tutorial_mission'), ('save_shield_start', 'static', '01a_tutorial_mission'), ('save_tram_start', 'static', '01a_tutorial_mission'), ('cs_lookat_player', 'command_script', '01a_tutorial_mission'), ('cs_lookat_guns', 'command_script', '01a_tutorial_mission'), ('cs_johnson_glanceat_guns', 'command_script', '01a_tutorial_mission'), ('cs_lookat_johnson', 'command_script', '01a_tutorial_mission'), ('cs_lookat_console_zapper', 'command_script', '01a_tutorial_mission'), ('cs_lookat_console_toplight', 'command_script', '01a_tutorial_mission'), ('cs_lookat_console_bottomlight', 'command_script', '01a_tutorial_mission'), ('cs_lookat_console_inhibitor', 'command_script', '01a_tutorial_mission'), ('cs_guns_start', 'command_script', '01a_tutorial_mission'), ('cs_guns_zapper_halfway', 'command_script', '01a_tutorial_mission'), ('cs_guns_zapper_wait', 'command_script', '01a_tutorial_mission'), ('cs_guns_zapper', 'command_script', '01a_tutorial_mission'), ('cs_guns_zapper_prompt', 'command_script', '01a_tutorial_mission'), ('cs_johnson_start', 'command_script', '01a_tutorial_mission'), ('cs_johnson_elevator', 'command_script', '01a_tutorial_mission'), ('cs_johnson_elevator_face_guns', 'command_script', '01a_tutorial_mission'), ('cs_guns_elevator', 'command_script', '01a_tutorial_mission'), ('cs_johnson_tram', 'command_script', '01a_tutorial_mission'), ('cs_lookat_macgun', 'command_script', '01a_tutorial_mission'), ('cs_lookat_malta', 'command_script', '01a_tutorial_mission'), ('cs_lookat_fleet', 'command_script', '01a_tutorial_mission'), ('cs_johnson_lookat_station', 'command_script', '01a_tutorial_mission'), ('cs_johnson_station', 'command_script', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('icecream', 'startup', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void_mindread_down', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('boolean', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('training_done_tram', 'dormant', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('void', 'static', '01a_tutorial_mission'), ('training_fade', 'dormant', '01a_tutorial_mission'), ('mission_01a', 'startup', '01a_tutorial_mission'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/01b_spacestation/01b_spacestation': {
        "objects": {
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['01b_spacestation_mission']},
            'arm_cov': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'arm_cov_elt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'arm_cov_stl': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'arm_door_charger_1': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['01b_spacestation_mission']},
            'arm_door_charger_2': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['01b_spacestation_mission']},
            'arm_hum_guns': {'category': 'human', 'funcs': ['ai_kill', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov_bbalcony': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov_fbalcony': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov_sec_back': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov_sec_back_elt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov_sec_front': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov_stairs': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_strength'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov_stairs_back': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov_stairs_back_elt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr1_cov_stairs_front': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr1_hum': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['01b_spacestation_mission']},
            'atr2_cov': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_strength'], 'sources': ['01b_spacestation_mission']},
            'atr2_cov_bbalcony_grt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr2_cov_floor': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr2_cov_fnl': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr2_cov_fnl_elt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr2_cov_lstair': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr2_cov_lstair_elt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr2_cov_lstair_rear_elt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr2_cov_re': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'atr2_door_re': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_mission']},
            'atr2_hum': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay1_boarding_door': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_catwalk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_floor': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_floor_elt': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_fnl': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_wv2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_wv2_elt': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_wv3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_wv3_elt': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_wv4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay1_cov_wv5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay1_door_exit': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_mission']},
            'bay1_hum': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay2_boarding_door': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_catwalk': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_floor': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_floor_elt': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_fnl': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_wv2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_wv2_elt': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_wv3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_wv3_elt': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_wv4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay2_cov_wv5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'bay2_hum': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'bigrack_bsp0a_5': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_mission']},
            'bigrack_bsp0a_6': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_mission']},
            'blast_base': {'category': 'object', 'funcs': ['object_cinematic_visibility', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'bloom_quad': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'branding_iron_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'branding_iron_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'brute_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'brute_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'cairo_bridge': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'carrier_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['01b_spacestation_cinematics', '01b_spacestation_mission']},
            'carrier_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics', '01b_spacestation_mission']},
            'chief': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'chief_x02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'chief_x02_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'cortana': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'cortana_x02': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'covenant': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['01b_spacestation_mission']},
            'covenant_battery': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'dck_cov': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count', 'ai_strength'], 'sources': ['01b_spacestation_mission']},
            'dck_cov_arm1_elt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'dck_cov_arm2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'dck_cov_enter_elt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'dck_door_arm_1': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_mission']},
            'dck_door_arm_2': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_mission']},
            'dck_hog': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_mission']},
            'dck_hog_rail': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_mission']},
            'dervish': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'dervish_nude': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'elevator_light_top': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'elv_cov': {'category': 'covenant', 'funcs': ['ai_strength'], 'sources': ['01b_spacestation_mission']},
            'elv_cov_elevator': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'elv_cov_top': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'elv_elevator': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['01b_spacestation_mission']},
            'elv_elevator_control_1': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['01b_spacestation_mission']},
            'elv_elevator_control_2': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['01b_spacestation_mission']},
            'elv_elevator_position': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['01b_spacestation_mission']},
            'elv_hum_mar': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'fighter_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'fighter_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'fighter_x02_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'fighter_x02_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'fighter_x02_03': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'fighter_x02_04': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'fighter_x02_05': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'fighter_x02_06': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'fighter_x02_07': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'fighter_x02_08': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'grunt_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'grunt_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'grunt_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'gun_cortana': {'category': 'human', 'funcs': ['ai_living_count'], 'sources': ['01b_spacestation_mission']},
            'gun_cortana_1': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'gun_cortana_2': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'gun_cortana_3': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'gun_cortana_4': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'gun_cov': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'gun_elevator': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_mission']},
            'gun_hum_mar': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'gun_loader': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['01b_spacestation_mission']},
            'hammer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'hood': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'hood_x02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'hunter_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'hunter_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'hunter_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'iac': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'iac_bridge_outro_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'iac_bridge_outro_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'jackal_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'jackal_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'johnson': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'johnson_x02': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'johnson_x02_01': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_set_permutation'], 'sources': ['01b_spacestation_cinematics']},
            'lvr_airlock_blower': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['01b_spacestation_mission']},
            'lvr_cov': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['01b_spacestation_mission']},
            'lvr_cov_air': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'lvr_cov_wv1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'lvr_cov_wv2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_mission']},
            'lvr_door_enter_1': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['01b_spacestation_mission']},
            'lvr_door_enter_2': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_mission']},
            'macgun': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['01b_spacestation_mission']},
            'marine_01': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide', 'object_set_permutation'], 'sources': ['01b_spacestation_cinematics']},
            'marine_02': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_set_permutation'], 'sources': ['01b_spacestation_cinematics']},
            'marine_03': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_set_permutation'], 'sources': ['01b_spacestation_cinematics']},
            'marine_04': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_set_permutation'], 'sources': ['01b_spacestation_cinematics']},
            'marine_05': {'category': 'human', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'marine_06': {'category': 'human', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'marine_07': {'category': 'human', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'marine_08': {'category': 'human', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'marine_door_01': {'category': 'human', 'funcs': ['object_set_permutation'], 'sources': ['01b_spacestation_cinematics']},
            'marine_door_02': {'category': 'human', 'funcs': ['object_set_permutation'], 'sources': ['01b_spacestation_cinematics']},
            'marine_plant_01': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'marine_plant_02': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'marine_plant_03': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'marine_plant_04': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'marine_plant_05': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'marine_plant_06': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'marine_plant_07': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'marine_x02_01': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'marine_x02_02': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'marine_x02_03': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'marine_x02_04': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'marine_x02_05': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'marine_x02_06': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'marine_x02_07': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'marine_x02_08': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'matte_africa': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'matte_africa_coast': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'matte_carrier_core': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'matte_carrier_hull': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'matte_carrier_side': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'matte_earth': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'medal_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'miranda': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['01b_spacestation_cinematics']},
            'miranda_x02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'offending_light': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'outro_cortana_base': {'category': 'human', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'outro_cortana_stand': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'outro_door_01': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_cinematics']},
            'outro_door_02': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_cinematics']},
            'outro_door_03': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_cinematics']},
            'outro_elevator': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['01b_spacestation_cinematics']},
            'outro_fighter_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'outro_fighter_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'outro_fleet': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'outro_lever': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_cinematics']},
            'outro_seraph': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'pickle': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'pickle2': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['01b_spacestation_mission']},
            'poa': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'poa_x02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'problem_guard': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'prophet': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['01b_spacestation_mission']},
            'tartarus': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'tram': {'category': 'object', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['01b_spacestation_mission']},
            'trm1_cov_alock': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'trm1_cov_block': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['01b_spacestation_mission']},
            'trm1_door_exit': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['01b_spacestation_mission']},
            'trm1_hum_alock': {'category': 'human', 'funcs': ['ai_erase', 'ai_place', 'ai_set_orders'], 'sources': ['01b_spacestation_mission']},
            'trm1_hum_block': {'category': 'human', 'funcs': ['ai_erase', 'ai_place', 'ai_set_orders'], 'sources': ['01b_spacestation_mission']},
            'tv_1st_all': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_1st_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_1st_halla': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_1st_hallb': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_arm_save': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_arm_stairs': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_arm_start': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_atr1_floor': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_atr1_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_atr1_sec': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_atr1_stairs': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_atr2_floor_front': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_atr2_floor_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_atr2_lstair': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_atr2_security_r': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_bay1_boarding_tube': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_bay1_stairs': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_bay2_boarding_tube': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_bay2_hall': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_dck_arm1_back': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_dck_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_dck_start': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_elv_start': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_lvr_back': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_trm1_alock': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_trm1_block': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_trm1_floor': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'tv_trm1_start': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['01b_spacestation_mission']},
            'x02_bridge_door': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_cinematics']},
            'x02_cortana_stand': {'category': 'human', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'x02_door_02': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['01b_spacestation_cinematics']},
            'x02_elite_helmet': {'category': 'covenant', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
            'x02_panic_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_cinematics']},
            'x02_panic_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_cinematics']},
            'x02_panic_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_cinematics']},
            'x02_panic_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['01b_spacestation_cinematics']},
            'x02_tactical_display': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['01b_spacestation_cinematics']},
        },
        "scripts": [('title_training', 'dormant', '01b_spacestation_base'), ('title_bridge', 'dormant', '01b_spacestation_base'), ('title_escape', 'dormant', '01b_spacestation_base'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('void', 'stub', '01b_spacestation_cinematics'), ('x02_score_01', 'dormant', '01b_spacestation_cinematics'), ('x02_foley_01', 'dormant', '01b_spacestation_cinematics'), ('x02_0010_mas', 'dormant', '01b_spacestation_cinematics'), ('x02_0020_jon', 'dormant', '01b_spacestation_cinematics'), ('x02_0030_jon', 'dormant', '01b_spacestation_cinematics'), ('x02_0040_jon', 'dormant', '01b_spacestation_cinematics'), ('x02_0050_jon', 'dormant', '01b_spacestation_cinematics'), ('x02_01_dof', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_01', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_hum_crowd_01a', 'dormant', '01b_spacestation_cinematics'), ('x02_hum_crowd_01b', 'dormant', '01b_spacestation_cinematics'), ('open_bridge_door', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_foley_02', 'dormant', '01b_spacestation_cinematics'), ('x02_0070_gch', 'dormant', '01b_spacestation_cinematics'), ('x02_fov_02', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_02', 'dormant', '01b_spacestation_cinematics'), ('place_cov_crowd_01a', 'dormant', '01b_spacestation_cinematics'), ('place_cov_crowd_01b', 'dormant', '01b_spacestation_cinematics'), ('place_cov_crowd_01c', 'dormant', '01b_spacestation_cinematics'), ('place_cov_crowd_01d', 'dormant', '01b_spacestation_cinematics'), ('place_cov_crowd_distant', 'dormant', '01b_spacestation_cinematics'), ('activate_manacles', 'dormant', '01b_spacestation_cinematics'), ('create_columns', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_foley_03', 'dormant', '01b_spacestation_cinematics'), ('x02_0090_tar', 'dormant', '01b_spacestation_cinematics'), ('x02_0100_der', 'dormant', '01b_spacestation_cinematics'), ('x02_0110_tar', 'dormant', '01b_spacestation_cinematics'), ('effect_beam_01_start', 'dormant', '01b_spacestation_cinematics'), ('effect_beams', 'dormant', '01b_spacestation_cinematics'), ('place_cov_crowd_02', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_foley_04a', 'dormant', '01b_spacestation_cinematics'), ('x02_0140_lhd', 'dormant', '01b_spacestation_cinematics'), ('marine_whisper', 'dormant', '01b_spacestation_cinematics'), ('x02_0150_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0160_cor', 'dormant', '01b_spacestation_cinematics'), ('effect_cortana_on', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_04a', 'dormant', '01b_spacestation_cinematics'), ('x02_marine_crowd_01', 'dormant', '01b_spacestation_cinematics'), ('x02_marine_crowd_02', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_foley_04b', 'dormant', '01b_spacestation_cinematics'), ('x02_0170_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0180_cor', 'dormant', '01b_spacestation_cinematics'), ('x02_0190_mas', 'dormant', '01b_spacestation_cinematics'), ('x02_0200_jon', 'dormant', '01b_spacestation_cinematics'), ('x02_0210_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0220_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0230_lhd', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_04b', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_score_05', 'dormant', '01b_spacestation_cinematics'), ('x02_foley_05', 'dormant', '01b_spacestation_cinematics'), ('x02_0240_tar', 'dormant', '01b_spacestation_cinematics'), ('x02_0250_tar', 'dormant', '01b_spacestation_cinematics'), ('x02_0270_tar', 'dormant', '01b_spacestation_cinematics'), ('effect_body_smoke', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_05', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_foley_06', 'dormant', '01b_spacestation_cinematics'), ('x02_0280_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0290_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0300_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0310_lhd', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_06', 'dormant', '01b_spacestation_cinematics'), ('x02_marine_crowd_03', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_score_08', 'dormant', '01b_spacestation_cinematics'), ('x02_foley_07', 'dormant', '01b_spacestation_cinematics'), ('x02_0320_der', 'dormant', '01b_spacestation_cinematics'), ('x02_07_dof_01', 'dormant', '01b_spacestation_cinematics'), ('effect_helmet_smoke', 'dormant', '01b_spacestation_cinematics'), ('effect_brand', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_07', 'dormant', '01b_spacestation_cinematics'), ('backup_brand', 'dormant', '01b_spacestation_cinematics'), ('bring_back_brand', 'dormant', '01b_spacestation_cinematics'), ('delete_brand', 'dormant', '01b_spacestation_cinematics'), ('emotion_tartarus_07', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_foley_08', 'dormant', '01b_spacestation_cinematics'), ('x02_0330_cor', 'dormant', '01b_spacestation_cinematics'), ('x02_0340_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0350_cor', 'dormant', '01b_spacestation_cinematics'), ('x02_0360_ahp', 'dormant', '01b_spacestation_cinematics'), ('x02_0370_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0380_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0390_mir', 'dormant', '01b_spacestation_cinematics'), ('x02_0400_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0405_cor', 'dormant', '01b_spacestation_cinematics'), ('x02_0410_lhd', 'dormant', '01b_spacestation_cinematics'), ('effect_cortana_off', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_08', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('cs_x02_panic_01', 'command_script', '01b_spacestation_cinematics'), ('cs_x02_panic_02', 'command_script', '01b_spacestation_cinematics'), ('cs_x02_panic_03', 'command_script', '01b_spacestation_cinematics'), ('cs_x02_panic_04', 'command_script', '01b_spacestation_cinematics'), ('x02_foley_09', 'dormant', '01b_spacestation_cinematics'), ('x02_0420_to1', 'dormant', '01b_spacestation_cinematics'), ('x02_0430_to1', 'dormant', '01b_spacestation_cinematics'), ('x02_0440_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0450_lhd', 'dormant', '01b_spacestation_cinematics'), ('x02_0460_mas', 'dormant', '01b_spacestation_cinematics'), ('x02_0480_mas', 'dormant', '01b_spacestation_cinematics'), ('x02_0490_jon', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_09', 'dormant', '01b_spacestation_cinematics'), ('x02_fov_09_01', 'dormant', '01b_spacestation_cinematics'), ('x02_fov_09_02', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_09_setup', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('x02_foley_10', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_x02_10', 'dormant', '01b_spacestation_cinematics'), ('fighters_unhide', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_score_01', 'dormant', '01b_spacestation_cinematics'), ('c01_outro_foley_01', 'dormant', '01b_spacestation_cinematics'), ('c01_9010_cor', 'dormant', '01b_spacestation_cinematics'), ('c01_9050_mas', 'dormant', '01b_spacestation_cinematics'), ('c01_9060_cor', 'dormant', '01b_spacestation_cinematics'), ('c01_9070_mir', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_outro_01', 'dormant', '01b_spacestation_cinematics'), ('effects_cortana_transfer', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('bomb_deactivate', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('upload_cortana', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_foley_02', 'dormant', '01b_spacestation_cinematics'), ('c01_9080_mir', 'dormant', '01b_spacestation_cinematics'), ('c01_9090_lhd', 'dormant', '01b_spacestation_cinematics'), ('c01_9100_mas', 'dormant', '01b_spacestation_cinematics'), ('c01_9110_mas', 'dormant', '01b_spacestation_cinematics'), ('c01_9120_lhd', 'dormant', '01b_spacestation_cinematics'), ('c01_9130_mas', 'dormant', '01b_spacestation_cinematics'), ('c01_9140_lhd', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_bridges_01a', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_bridges_01b', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_chief_01', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_bridges_02', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_foley_03', 'dormant', '01b_spacestation_cinematics'), ('doors_outro_03', 'dormant', '01b_spacestation_cinematics'), ('outro_sparks_03', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_chief_02', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_foley_04', 'dormant', '01b_spacestation_cinematics'), ('c01_9150_cor', 'dormant', '01b_spacestation_cinematics'), ('c01_9160_mas', 'dormant', '01b_spacestation_cinematics'), ('c01_9170_cor', 'dormant', '01b_spacestation_cinematics'), ('c01_9180_cor', 'dormant', '01b_spacestation_cinematics'), ('c01_outro_shake_04_01', 'dormant', '01b_spacestation_cinematics'), ('c01_outro_shake_04_02', 'dormant', '01b_spacestation_cinematics'), ('c01_outro_shake_04_03', 'dormant', '01b_spacestation_cinematics'), ('outro_sparks_03_04', 'dormant', '01b_spacestation_cinematics'), ('doors_outro_04', 'dormant', '01b_spacestation_cinematics'), ('create_bloom_quad', 'dormant', '01b_spacestation_cinematics'), ('top_light', 'dormant', '01b_spacestation_cinematics'), ('bottom_light', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_foley_05', 'dormant', '01b_spacestation_cinematics'), ('c01_9190_cor', 'dormant', '01b_spacestation_cinematics'), ('c01_9200_cor', 'dormant', '01b_spacestation_cinematics'), ('c01_9210_mas', 'dormant', '01b_spacestation_cinematics'), ('c01_outro_shake_05_01', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_bay_01', 'dormant', '01b_spacestation_cinematics'), ('lever', 'dormant', '01b_spacestation_cinematics'), ('airlock', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_music_06', 'dormant', '01b_spacestation_cinematics'), ('c01_outro_foley_06', 'dormant', '01b_spacestation_cinematics'), ('c01_outro_shake_06_01', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_bay_02', 'dormant', '01b_spacestation_cinematics'), ('final_sparks', 'dormant', '01b_spacestation_cinematics'), ('destroy_fleet', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_foley_07', 'dormant', '01b_spacestation_cinematics'), ('effect_covenant_beams', 'dormant', '01b_spacestation_cinematics'), ('effect_poa_explosions', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_outro_07', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_poa_reverse', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_foley_08', 'dormant', '01b_spacestation_cinematics'), ('effect_cluster_bombs', 'dormant', '01b_spacestation_cinematics'), ('effect_interior_blast', 'dormant', '01b_spacestation_cinematics'), ('x02_08_dof', 'dormant', '01b_spacestation_cinematics'), ('bomb_reactivate', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_scene_08', 'dormant', '01b_spacestation_cinematics'), ('cinematic_light_carrier_int', 'dormant', '01b_spacestation_cinematics'), ('save_framerate_08', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_foley_09', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_scene_09', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('c01_outro_foley_10', 'dormant', '01b_spacestation_cinematics'), ('c01_9220_jon', 'dormant', '01b_spacestation_cinematics'), ('c01_9230_jon', 'dormant', '01b_spacestation_cinematics'), ('c01_9240_mir', 'dormant', '01b_spacestation_cinematics'), ('c01_9250_mir', 'dormant', '01b_spacestation_cinematics'), ('carrier_explosion_tiny', 'dormant', '01b_spacestation_cinematics'), ('carrier_explosion_medium', 'dormant', '01b_spacestation_cinematics'), ('carrier_explosion_large', 'dormant', '01b_spacestation_cinematics'), ('white_flash', 'dormant', '01b_spacestation_cinematics'), ('effect_africa_explosions', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_outro_10', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_iac_ext_01', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_iac_interior', 'dormant', '01b_spacestation_cinematics'), ('cinematic_lighting_iac_ext_02', 'dormant', '01b_spacestation_cinematics'), ('emotion_10', 'dormant', '01b_spacestation_cinematics'), ('save_framerate_10', 'dormant', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('void', 'static', '01b_spacestation_cinematics'), ('megg_check', 'dormant', '01b_spacestation_mission'), ('ice_cream_check', 'dormant', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('save_bay2_retreat', 'dormant', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('save_bay2_fnl', 'dormant', '01b_spacestation_mission'), ('save_arm_start', 'dormant', '01b_spacestation_mission'), ('save_atr1_start', 'dormant', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('title_1st', 'dormant', '01b_spacestation_mission'), ('title_bay2', 'dormant', '01b_spacestation_mission'), ('title_dck', 'dormant', '01b_spacestation_mission'), ('title_gun', 'dormant', '01b_spacestation_mission'), ('short', 'static', '01b_spacestation_mission'), ('short', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('flavor_mission', 'dormant', '01b_spacestation_mission'), ('cs_clear', 'command_script', '01b_spacestation_mission'), ('cs_1st_hichief', 'command_script', '01b_spacestation_mission'), ('cs_weapons', 'command_script', '01b_spacestation_mission'), ('1st_tram', 'dormant', '01b_spacestation_mission'), ('cs_1st_fieldoffire', 'command_script', '01b_spacestation_mission'), ('cs_1st_johnson_deploy', 'command_script', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('1st_waves', 'dormant', '01b_spacestation_mission'), ('boolean', 'static', '01b_spacestation_mission'), ('1st_mission', 'dormant', '01b_spacestation_mission'), ('atr2_mission', 'dormant', '01b_spacestation_mission'), ('cs_lookat_malta', 'command_script', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('bay1_mission', 'dormant', '01b_spacestation_mission'), ('cs_lookat_athens', 'command_script', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('bay2_mission', 'dormant', '01b_spacestation_mission'), ('cs_arm_guns_grate', 'command_script', '01b_spacestation_mission'), ('arm_mission', 'dormant', '01b_spacestation_mission'), ('cs_atr1_turret_fbalcony', 'command_script', '01b_spacestation_mission'), ('cs_atr1_turret_bbalcony', 'command_script', '01b_spacestation_mission'), ('atr1_mission', 'dormant', '01b_spacestation_mission'), ('cs_trm1_bunker', 'command_script', '01b_spacestation_mission'), ('cs_trm1_lookat_player_crouch', 'command_script', '01b_spacestation_mission'), ('cs_trm1_lookat_miranda_crouch', 'command_script', '01b_spacestation_mission'), ('cs_trm1_lookat_johnson_crouch', 'command_script', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('cs_trm1_approach', 'command_script', '01b_spacestation_mission'), ('cs_trm1_moveto_alock', 'command_script', '01b_spacestation_mission'), ('cs_trm1_moveto_alock_miranda', 'command_script', '01b_spacestation_mission'), ('cs_trm1_moveto_alock_johnson', 'command_script', '01b_spacestation_mission'), ('cs_trm1_moveto_alock_block', 'command_script', '01b_spacestation_mission'), ('cs_trm1_lookat_block', 'command_script', '01b_spacestation_mission'), ('cs_trm1_lookat_player', 'command_script', '01b_spacestation_mission'), ('cs_trm1_lookat_miranda', 'command_script', '01b_spacestation_mission'), ('cs_trm1_lookat_johnson', 'command_script', '01b_spacestation_mission'), ('trm1_bugproblem', 'dormant', '01b_spacestation_mission'), ('trm1_cleanup', 'dormant', '01b_spacestation_mission'), ('trm1_mission', 'dormant', '01b_spacestation_mission'), ('dck_hog', 'dormant', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('dck_mission', 'dormant', '01b_spacestation_mission'), ('elv_goinloud', 'dormant', '01b_spacestation_mission'), ('boolean', 'static', '01b_spacestation_mission'), ('boolean', 'static', '01b_spacestation_mission'), ('elv_mission', 'dormant', '01b_spacestation_mission'), ('lvr_carrier_flyby', 'dormant', '01b_spacestation_mission'), ('lvr_carriers', 'dormant', '01b_spacestation_mission'), ('lvr_mission', 'dormant', '01b_spacestation_mission'), ('cs_expand_cortana', 'command_script', '01b_spacestation_mission'), ('cs_shrink_cortana', 'command_script', '01b_spacestation_mission'), ('gun_cortana', 'dormant', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('gun_flyby', 'dormant', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('mission_spacestation', 'startup', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('void', 'static', '01b_spacestation_mission'), ('x02_01_predict', 'dormant', '01b_spacestation_prediction'), ('x02_02_predict', 'dormant', '01b_spacestation_prediction'), ('x02_03_predict', 'dormant', '01b_spacestation_prediction'), ('x02_04a_predict', 'dormant', '01b_spacestation_prediction'), ('x02_04b_predict', 'dormant', '01b_spacestation_prediction'), ('x02_05_predict', 'dormant', '01b_spacestation_prediction'), ('x02_06_predict', 'dormant', '01b_spacestation_prediction'), ('x02_07_predict', 'dormant', '01b_spacestation_prediction'), ('x02_08_predict', 'dormant', '01b_spacestation_prediction'), ('x02_09_predict', 'dormant', '01b_spacestation_prediction'), ('x02_10_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_01_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_02_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_03_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_04_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_05_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_06_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_07_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_08_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_09_predict', 'dormant', '01b_spacestation_prediction'), ('01_outro_10_predict', 'dormant', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('void', 'static', '01b_spacestation_prediction'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/03a_oldmombasa/03a_oldmombasa': {
        "objects": {
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase', 'ai_migrate', 'ai_strength', 'ai_vehicle_enter', 'ai_vehicle_exit'], 'sources': ['03a_oldmombasa_cinematics', '03a_oldmombasa_mission']},
            'ai_current_squad': {'category': 'object', 'funcs': ['ai_erase', 'ai_magically_see', 'ai_set_orders', 'ai_strength'], 'sources': ['03a_oldmombasa_mission']},
            'battle_rifle_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'battle_rifle_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'carrier': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'chief': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'copilot': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_set_permutation'], 'sources': ['03a_oldmombasa_cinematics']},
            'covenant': {'category': 'object', 'funcs': ['ai_allegiance', 'ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'crashed_pelican': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e10_cov': {'category': 'covenant', 'funcs': ['ai_strength'], 'sources': ['03a_oldmombasa_mission']},
            'e10_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['03a_oldmombasa_mission']},
            'e10_cov_ghosts0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e10_cov_ghosts1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e10_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e10_cov_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e10_cov_phantom0': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e10_mars_inf0': {'category': 'human', 'funcs': ['ai_migrate'], 'sources': ['03a_oldmombasa_mission']},
            'e10_mars_test': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e10_mars_warthog0': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_ghosts0_0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_ghosts0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_inf1_0/elite0': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_inf1_0/elite1': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_inf1_0/elite2': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_inf1_1/elite0': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_inf1_1/elite1': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_inf1_1/elite2': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_inf1_1/elite3': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['03a_oldmombasa_mission']},
            'e11_cov_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e11_mars': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['03a_oldmombasa_mission']},
            'e11_mars_inf0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e11_mars_warthog0': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e11_pod0_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e11_pod1_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e11_pod2_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e11_pod3_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e11_pod4_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e11_pod5_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e11_pod6_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e12_cov_creep0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_cov_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_cov_inf0_4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_cov_inf0_5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_cov_inf0_6': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_mars_inf1': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_mars_warthog0': {'category': 'human', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_mars_warthog1': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e12_scarab_gun': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e12_warthog0': {'category': 'object', 'funcs': ['object_set_velocity'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_creep0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_creep0_0/creep0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_creep0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_creep0_1/creep0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_creep0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_creep0_2/creep0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_creep0_3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_creep0_6': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e13_cov_ghosts1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e13_mars_warthog0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf0_1/grunt0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf0_1/grunt1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf0_2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_magically_see', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf0_3': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_magically_see', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf2': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf2_1': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf2_2': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf2_3': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf2_4': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf2_5': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf2_6': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf2_7': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf3': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf3_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf3_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf3_2': {'category': 'covenant', 'funcs': ['ai_place', 'ai_strength'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf4': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_inf4_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_phantom0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_phantom0_1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_snipers0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_snipers0/sniper0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_snipers0/sniper1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_snipers0/sniper2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_snipers0/sniper3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_cov_snipers0/sniper4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_mars': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['03a_oldmombasa_mission']},
            'e1_mars_inf0': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e1_mars_inf1': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_mars_johnson': {'category': 'human', 'funcs': ['ai_magically_see', 'ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e1_mars_pelican0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e2_cov_hunters0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_strength'], 'sources': ['03a_oldmombasa_mission']},
            'e2_cov_hunters0_active': {'category': 'covenant', 'funcs': ['ai_trigger_test'], 'sources': ['03a_oldmombasa_mission']},
            'e2_cov_hunters0_bypassed': {'category': 'covenant', 'funcs': ['ai_trigger_test'], 'sources': ['03a_oldmombasa_mission']},
            'e2_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e2_hunter_door': {'category': 'covenant', 'funcs': ['device_set_position'], 'sources': ['03a_oldmombasa_mission']},
            'e2_hunter_smoke': {'category': 'covenant', 'funcs': ['object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e2_mars_inf0': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e2_mars_johnson': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e3_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e3_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e3_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e3_cov_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e3_mars_inf0': {'category': 'human', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e3_mars_inf1': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e3_mars_johnson': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place', 'ai_vehicle_enter'], 'sources': ['03a_oldmombasa_mission']},
            'e3_mars_pelican0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_inf1': {'category': 'covenant', 'funcs': ['ai_migrate'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_inf1_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_inf2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_snipers0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_snipers0_0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_snipers0_1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_snipers0_2': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_snipers0_2/sniper0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_snipers0_2/sniper1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_cov_snipers0_2/sniper2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e4_mars_inf0': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf0_0/sniper0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf0_0/sniper1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf0_0/sniper2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf0_0/sniper3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf0_ambush_sprung': {'category': 'covenant', 'funcs': ['ai_trigger_test'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf1': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf1_0': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf1_1': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e5_cov_inf3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e5_mars': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['03a_oldmombasa_mission']},
            'e5_mars_inf0': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e5b_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e6_cov': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e6_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e6_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e6_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e6_cov_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e6_cov_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e6_mars': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['03a_oldmombasa_mission']},
            'e6_mars_inf0': {'category': 'human', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e6_mars_inf0_1': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e6_mars_inf1': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e6_mars_inf1/marine0': {'category': 'human', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['03a_oldmombasa_mission']},
            'e6_mars_inf1/marine1': {'category': 'human', 'funcs': ['ai_migrate'], 'sources': ['03a_oldmombasa_mission']},
            'e7_cov': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['03a_oldmombasa_mission']},
            'e7_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e7_gun0': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'e7_mars': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['03a_oldmombasa_mission']},
            'e7_mars_inf0': {'category': 'human', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e8_cov': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e8_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['03a_oldmombasa_mission']},
            'e8_cov_ghosts0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e8_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e8_cov_inf1': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e8_cov_inf2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e8_cov_phantom0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e8_mars_inf0': {'category': 'human', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e8_mars_warthog0': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e8_mars_warthog0/warthog0': {'category': 'human', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e9_cov': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e9_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e9_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e9_cov_inf1': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'e9_cov_inf1_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e9_cov_inf1_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e9_cov_inf1_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e9_cov_shadow0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e9_mars': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['03a_oldmombasa_mission']},
            'e9_mars_test': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03a_oldmombasa_mission']},
            'e9_mars_warthog0': {'category': 'human', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place', 'ai_vehicle_enter'], 'sources': ['03a_oldmombasa_mission']},
            'g_e10_warthog': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['03a_oldmombasa_mission']},
            'g_e8_warthog': {'category': 'object', 'funcs': ['object_get_health', 'unit_get_health'], 'sources': ['03a_oldmombasa_mission']},
            'generic_player_fired': {'category': 'object', 'funcs': ['ai_trigger_test'], 'sources': ['03a_oldmombasa_mission']},
            'generic_player_within_4wu': {'category': 'object', 'funcs': ['ai_trigger_test'], 'sources': ['03a_oldmombasa_mission']},
            'helmet': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'iac': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility'], 'sources': ['03a_oldmombasa_cinematics']},
            'iac_bridge': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'intro_hog_01': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03a_oldmombasa_cinematics']},
            'intro_hog_02': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03a_oldmombasa_cinematics']},
            'intro_hog_03': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03a_oldmombasa_cinematics']},
            'intro_hog_04': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03a_oldmombasa_cinematics']},
            'intro_scarab_gun': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'intro_scarab_gun_turret': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'johnson': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'magazine': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'marines': {'category': 'human', 'funcs': ['ai_living_count'], 'sources': ['03a_oldmombasa_mission']},
            'miranda': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'odst_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide', 'object_set_permutation'], 'sources': ['03a_oldmombasa_cinematics']},
            'odst_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide', 'object_set_permutation'], 'sources': ['03a_oldmombasa_cinematics']},
            'odst_03': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide', 'object_set_permutation'], 'sources': ['03a_oldmombasa_cinematics']},
            'odst_04': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide', 'object_set_permutation'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_01': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_02': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_03': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_04': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_05': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_06': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_07': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_08': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_09': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_10': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_11': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_12': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_13': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_14': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_15': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_16': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_17': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_18': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_19': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'offending_palm_20': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['03a_oldmombasa_cinematics']},
            'pelican_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_set_velocity'], 'sources': ['03a_oldmombasa_cinematics']},
            'pelican_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_set_velocity'], 'sources': ['03a_oldmombasa_cinematics']},
            'pelican_03': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_hide', 'object_set_velocity'], 'sources': ['03a_oldmombasa_cinematics']},
            'pelican_04': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'pilot': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['03a_oldmombasa_mission']},
            'scarab': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['03a_oldmombasa_cinematics']},
            'scarab_turret': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['03a_oldmombasa_cinematics']},
            'scope': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'sniper': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'sniper_rifle': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'spotter': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'the_fiscal_year': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03a_oldmombasa_cinematics']},
            'tunnel_scarab': {'category': 'object', 'funcs': ['device_get_position', 'object_destroy'], 'sources': ['03a_oldmombasa_mission']},
            'tv_beach': {'category': 'object', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_dark_area0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_dark_area1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_dark_area2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_dark_area3': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e10_cov_phantom0_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e10_early_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e10_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e10_mars_warthog0_unsafe': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e10_music': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e11_area': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e11_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e11_mars_warthog0_unsafe': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e11_near_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e11_on_fort': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e11_tunnel_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_cov_ghosts0_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_cov_inf0_2_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_cov_inf0_3_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_cov_inf0_4_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_cov_inf0_5_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_cov_inf0_6_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_cov_inf0_6_migrate': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_mars_inf1_begin': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_mars_warthog0_preserve': {'category': 'human', 'funcs': ['volume_test_object'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_mars_warthog1_begin': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e12_scarab_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e13_cov_creep0_6_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e13_cov_creep0_reins0': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e13_creep0_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e13_dialog': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e13_end_area': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e13_end_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e13_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e13_waypoint0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e13_waypoint1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_inf0_1_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_inf0_2_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_inf1_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_inf2_1_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_inf2_2_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_inf2_3_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_inf2_4_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_inf2_5_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_inf4_1_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_sniper0_0_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_sniper0_1_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_sniper0_2_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_cov_sniper0_3_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_crash_area_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_crashed_pelican': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_ghost_key': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_main_area_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_on_building': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e1_prediction': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e2_hunters_bypassed': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e2_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e3_crossing_street': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e3_johnson_required': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e3_johnson_teleport_unsafe': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e3_main_begin0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e3_main_begin1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e3_mars_pelican0_begin': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e4_cov_inf1_main_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e4_cov_inf2_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e4_end_of_street': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e4_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e4_player_moved_up': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_advanced0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_advanced1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_ambush_trigger0': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_ambush_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_ambush_trigger2': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_cov_inf1_done': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_cov_inf1_unsafe0': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_cov_inf1_unsafe1': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_main_begin0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_main_begin1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_main_begin2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5_player_advanced': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5b_bounds': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e5b_main': {'category': 'object', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e6_hotel_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e6_hotel_vicinity': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e6_main_begin0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e6_main_begin1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e6_main_begin2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e7_cov_inf0_init': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e7_cov_inf0_spring_ambush': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e7_hall': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e7_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e8_area': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e8_cov_inf2_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e8_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e8_vehicle_spawn_area': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e9_bypass': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e9_dialogue': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e9_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e9_near_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_e9_retreat_checkpoint': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
            'tv_mission_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03a_oldmombasa_mission']},
        },
        "scripts": [('void', 'stub', '03a_oldmombasa_cinematics'), ('void', 'stub', '03a_oldmombasa_cinematics'), ('void', 'stub', '03a_oldmombasa_cinematics'), ('void', 'stub', '03a_oldmombasa_cinematics'), ('c03_intro_score_01', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_foley_01', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene1_01', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene1_02', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene1_03', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene1_04', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1010_cor', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1011_cor', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1020_mir', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1021_mir', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1030_jon', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1040_jon', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1050_och_1', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1050_och_2', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_shake_01_1', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_shake_01_2', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_shake_01_3', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_01_dof_1', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_light_01_city_01', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_light_01_pelican_01', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_light_01_iac_01', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_light_01_city_02', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_light_01_pelican_02', 'dormant', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('cs_hog_01', 'command_script', '03a_oldmombasa_cinematics'), ('cs_hog_02', 'command_script', '03a_oldmombasa_cinematics'), ('cs_hog_03', 'command_script', '03a_oldmombasa_cinematics'), ('cs_hog_04', 'command_script', '03a_oldmombasa_cinematics'), ('intro_hogs', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_foley_02', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene2_01', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene2_02', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene2_03', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene2_04', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene2_05', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1060_cor', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1070_cor', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1080_mrs', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1090_dp1', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_shake_02', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_fov_01', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_lighting_scene_02', 'dormant', '03a_oldmombasa_cinematics'), ('white_flash', 'dormant', '03a_oldmombasa_cinematics'), ('erase_hogs', 'dormant', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('c03_intro_foley_03', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene3_01', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene3_02', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_sound_scene3_03', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1100_dp1', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1110_jon', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1120_jon', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1130_lhd', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1140_lhd', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1150_dp2', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_shake_03', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_03_dof_1', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_03_dof_2', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_lighting_scene_03', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_light_troopbay_03_01', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_light_chief_03_01', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_light_street_03_01', 'dormant', '03a_oldmombasa_cinematics'), ('save_dof_01', 'dormant', '03a_oldmombasa_cinematics'), ('show_trees_pelican', 'dormant', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('intro_scarab_gun_charge', 'dormant', '03a_oldmombasa_cinematics'), ('intro_scarab_gun_fire', 'dormant', '03a_oldmombasa_cinematics'), ('intro_scarab_turret_fire', 'dormant', '03a_oldmombasa_cinematics'), ('effect_pelican_hit_01', 'dormant', '03a_oldmombasa_cinematics'), ('effect_pelican_impact_01', 'dormant', '03a_oldmombasa_cinematics'), ('effect_pelican_impact_02', 'dormant', '03a_oldmombasa_cinematics'), ('effect_blow_railings', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_foley_04', 'dormant', '03a_oldmombasa_cinematics'), ('c03_1160_dp2', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_fov_02', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_shake_04', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_04_dof_1', 'dormant', '03a_oldmombasa_cinematics'), ('c03_intro_04_dof_3', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_lighting_scene_04', 'dormant', '03a_oldmombasa_cinematics'), ('cinematic_light_street_04_01', 'dormant', '03a_oldmombasa_cinematics'), ('effect_big_foot', 'dormant', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'static', '03a_oldmombasa_cinematics'), ('void', 'stub', '03a_oldmombasa_mission'), ('void', 'stub', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('chapter_title0', 'dormant', '03a_oldmombasa_mission'), ('chapter_title1', 'dormant', '03a_oldmombasa_mission'), ('chapter_title2', 'dormant', '03a_oldmombasa_mission'), ('objective0_set', 'dormant', '03a_oldmombasa_mission'), ('objective0_clear', 'dormant', '03a_oldmombasa_mission'), ('objective1_set', 'dormant', '03a_oldmombasa_mission'), ('objective1_clear', 'dormant', '03a_oldmombasa_mission'), ('objective2_set', 'dormant', '03a_oldmombasa_mission'), ('objective2_clear', 'dormant', '03a_oldmombasa_mission'), ('objective3_set', 'dormant', '03a_oldmombasa_mission'), ('objective3_clear', 'dormant', '03a_oldmombasa_mission'), ('objective4_set', 'dormant', '03a_oldmombasa_mission'), ('objective4_clear', 'dormant', '03a_oldmombasa_mission'), ('music_03a_01_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_01_stop', 'dormant', '03a_oldmombasa_mission'), ('music_03a_02_stop_alt', 'dormant', '03a_oldmombasa_mission'), ('music_03a_02_stop', 'dormant', '03a_oldmombasa_mission'), ('music_03a_02_start_alt', 'dormant', '03a_oldmombasa_mission'), ('music_03a_02_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_03_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_03_stop', 'dormant', '03a_oldmombasa_mission'), ('music_03a_04_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_04_stop', 'dormant', '03a_oldmombasa_mission'), ('music_03a_05_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_05_stop', 'dormant', '03a_oldmombasa_mission'), ('music_03a_06_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_06_stop', 'dormant', '03a_oldmombasa_mission'), ('music_03a_065_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_065_stop', 'dormant', '03a_oldmombasa_mission'), ('music_03a_065_start_alt', 'dormant', '03a_oldmombasa_mission'), ('music_03a_066_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_067_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_067_stop', 'dormant', '03a_oldmombasa_mission'), ('music_03a_07_start', 'dormant', '03a_oldmombasa_mission'), ('music_03a_07_stop', 'dormant', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('flashlight_control', 'dormant', '03a_oldmombasa_mission'), ('loudspeakers', 'dormant', '03a_oldmombasa_mission'), ('cs_e13_mars_continue', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_unload', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_end0', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_end1', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_end2', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_drive1', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_drive0', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_drive0', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_0_decision', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_1_decision', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_cov_creep0_2_decision', 'command_script', '03a_oldmombasa_mission'), ('cs_e13_mars_warthog0_drive', 'command_script', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('e13_navpoints', 'dormant', '03a_oldmombasa_mission'), ('e13_cov_ghosts1_main', 'dormant', '03a_oldmombasa_mission'), ('e13_cov_creep0_ghost_aux', 'dormant', '03a_oldmombasa_mission'), ('e13_cov_creep0_main', 'dormant', '03a_oldmombasa_mission'), ('e13_mars_warthog0_main', 'dormant', '03a_oldmombasa_mission'), ('e13_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('cs_e12_mars_horrible_cleanup', 'command_script', '03a_oldmombasa_mission'), ('cs_e12_cov_inf0_ghost_drop', 'command_script', '03a_oldmombasa_mission'), ('cs_e12_cov_inf0_0_ghost0', 'command_script', '03a_oldmombasa_mission'), ('cs_e12_cov_inf0_0_patrol0', 'command_script', '03a_oldmombasa_mission'), ('cs_e12_scarab_gunner', 'command_script', '03a_oldmombasa_mission'), ('cs_e12_mars_warthog0_cleanup', 'command_script', '03a_oldmombasa_mission'), ('cs_e12_ghosts_entry', 'command_script', '03a_oldmombasa_mission'), ('e12_cov_ghosts0_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('e12_event_warthog', 'dormant', '03a_oldmombasa_mission'), ('e12_event_scarab_gun', 'dormant', '03a_oldmombasa_mission'), ('e12_event_scarab', 'dormant', '03a_oldmombasa_mission'), ('e12_cortana_dialog', 'dormant', '03a_oldmombasa_mission'), ('e12_cov_creep0_main', 'dormant', '03a_oldmombasa_mission'), ('e12_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e12_mars_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e12_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e12_mars_warthog1_main', 'dormant', '03a_oldmombasa_mission'), ('e12_mars_warthog0_main', 'dormant', '03a_oldmombasa_mission'), ('e12_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('cs_e11_cov_phantom0_exit', 'command_script', '03a_oldmombasa_mission'), ('cs_e11_cov_inf0_shoot0', 'command_script', '03a_oldmombasa_mission'), ('cs_e11_cov_inf0_shoot1', 'command_script', '03a_oldmombasa_mission'), ('cs_e11_cov_inf0_shoot2', 'command_script', '03a_oldmombasa_mission'), ('cs_e11_cov_ghosts0_entry', 'command_script', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('e11_cov_inf1_0_insertion0', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_inf1_0_insertion1', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_inf1_0_insertion2', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_inf1_1_insertion0', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_inf1_1_insertion1', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_inf1_1_insertion2', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_inf1_1_insertion3', 'dormant', '03a_oldmombasa_mission'), ('e11_warthog_approach_horn', 'dormant', '03a_oldmombasa_mission'), ('cs_e11_warthog_approach', 'command_script', '03a_oldmombasa_mission'), ('e11_miranda_dialog', 'dormant', '03a_oldmombasa_mission'), ('e11_dialog', 'dormant', '03a_oldmombasa_mission'), ('e11_navpoint', 'dormant', '03a_oldmombasa_mission'), ('e11_navpoint_kill', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_phantom0_main', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_ghosts0_main', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_inf2_main', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e11_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e11_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e11_mars_warthog0_main', 'dormant', '03a_oldmombasa_mission'), ('e11_warthog_for_the_masses', 'dormant', '03a_oldmombasa_mission'), ('e11_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('cs_e10_cov_guntower_shoot', 'command_script', '03a_oldmombasa_mission'), ('cs_e10_cov_phantom0_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e10_cov_phantom0_exit', 'command_script', '03a_oldmombasa_mission'), ('cs_e10_cov_inf0_patrol1', 'command_script', '03a_oldmombasa_mission'), ('cs_e10_cov_inf0_patrol0', 'command_script', '03a_oldmombasa_mission'), ('e10_warthog_approach_horn', 'dormant', '03a_oldmombasa_mission'), ('cs_e10_warthog_approach', 'command_script', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('e10_cov_phantom0_main', 'dormant', '03a_oldmombasa_mission'), ('e10_cov_ghosts0_main', 'dormant', '03a_oldmombasa_mission'), ('e10_cov_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e10_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e10_mars_warthog0_main', 'dormant', '03a_oldmombasa_mission'), ('e10_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('cs_e9_cov_guntower_shoot', 'command_script', '03a_oldmombasa_mission'), ('cs_e9_cov_guntower_abort', 'command_script', '03a_oldmombasa_mission'), ('cs_e9_beach_chatter_scene', 'command_script', '03a_oldmombasa_mission'), ('cs_e9_cov_inf1_2_patrol', 'command_script', '03a_oldmombasa_mission'), ('cs_e9_cov_inf1_0_patrol', 'command_script', '03a_oldmombasa_mission'), ('cs_e9_warthog_abort', 'command_script', '03a_oldmombasa_mission'), ('e9_warthog_approach_horn', 'dormant', '03a_oldmombasa_mission'), ('cs_e9_warthog_follow', 'command_script', '03a_oldmombasa_mission'), ('e9_cortana_dialog', 'dormant', '03a_oldmombasa_mission'), ('e9_warthog_navpoint', 'dormant', '03a_oldmombasa_mission'), ('e9_warthog_navpoint_kill', 'dormant', '03a_oldmombasa_mission'), ('e9_retreat_checkpoint0', 'dormant', '03a_oldmombasa_mission'), ('e9_retreat_checkpoint1', 'dormant', '03a_oldmombasa_mission'), ('e9_music', 'dormant', '03a_oldmombasa_mission'), ('e9_cov_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e9_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e9_cov_shadow0_main', 'dormant', '03a_oldmombasa_mission'), ('e9_cov_ghosts0_main', 'dormant', '03a_oldmombasa_mission'), ('e9_mars_warthog0_main', 'dormant', '03a_oldmombasa_mission'), ('e9_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('cs_e8_warthog_intro_scene', 'command_script', '03a_oldmombasa_mission'), ('cs_e8_mars_warthog0_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e8_cov_phantom0_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e8_cov_ghosts0_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e8_mars_inf0_no_assholes', 'command_script', '03a_oldmombasa_mission'), ('cs_e8_cov_inf2_patrol2', 'command_script', '03a_oldmombasa_mission'), ('cs_e8_cov_inf2_patrol1', 'command_script', '03a_oldmombasa_mission'), ('cs_e8_cov_inf2_patrol0', 'command_script', '03a_oldmombasa_mission'), ('e8_warthog_scene', 'dormant', '03a_oldmombasa_mission'), ('e8_cov_ghosts0_main', 'dormant', '03a_oldmombasa_mission'), ('e8_cov_phantom0_main', 'dormant', '03a_oldmombasa_mission'), ('e8_cov_inf2_main', 'dormant', '03a_oldmombasa_mission'), ('e8_cov_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e8_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e8_mars_warthog0_main', 'dormant', '03a_oldmombasa_mission'), ('e8_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e8_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('cs_e7_hide', 'command_script', '03a_oldmombasa_mission'), ('cs_e7_cov_inf0_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e7_abort', 'command_script', '03a_oldmombasa_mission'), ('cs_e7_hotel_hall_scene0', 'command_script', '03a_oldmombasa_mission'), ('cs_e7_hotel_hall_scene1', 'command_script', '03a_oldmombasa_mission'), ('e7_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e7_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e7_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('cs_e6_mars_inf1_odst', 'command_script', '03a_oldmombasa_mission'), ('cs_e6_mars_inf1_cower', 'command_script', '03a_oldmombasa_mission'), ('cs_e6_mars_inf0_1_cower', 'command_script', '03a_oldmombasa_mission'), ('cs_e6_mars_inf1_abort', 'command_script', '03a_oldmombasa_mission'), ('cs_e6_mars_inf1_lead', 'command_script', '03a_oldmombasa_mission'), ('cs_e6_hotel_greeting_scene', 'command_script', '03a_oldmombasa_mission'), ('cs_e6_hotel_grunt_scene', 'command_script', '03a_oldmombasa_mission'), ('cs_e6_hotel_rescue_scene', 'command_script', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('e6_cov_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e6_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e6_mars_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e6_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e6_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('e5b_resetter', 'dormant', '03a_oldmombasa_mission'), ('e5b_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e5b_main', 'dormant', '03a_oldmombasa_mission'), ('cs_e5_cov_inf0_guard0', 'command_script', '03a_oldmombasa_mission'), ('cs_e5_cov_inf0_wait', 'command_script', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('e5_cov_inf4_main', 'dormant', '03a_oldmombasa_mission'), ('e5_cov_inf3_main', 'dormant', '03a_oldmombasa_mission'), ('e5_cov_inf2_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('e5_cov_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e5_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e5_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e5_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('cs_e4_cov_inf0_0_patrol0', 'command_script', '03a_oldmombasa_mission'), ('cs_e4_cov_inf0_0_patrol1', 'command_script', '03a_oldmombasa_mission'), ('cs_e4_cov_inf0_2_patrol0', 'command_script', '03a_oldmombasa_mission'), ('cs_e4_cov_inf0_1_patrol0', 'command_script', '03a_oldmombasa_mission'), ('cs_e4_cov_inf2_lurk', 'command_script', '03a_oldmombasa_mission'), ('e4_cov_snipers0_main', 'dormant', '03a_oldmombasa_mission'), ('e4_cov_inf2_main', 'dormant', '03a_oldmombasa_mission'), ('e4_cov_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e4_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e4_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e4_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('cs_e3_sniper_intro_scene', 'command_script', '03a_oldmombasa_mission'), ('e3_mars_sniper_scene', 'dormant', '03a_oldmombasa_mission'), ('cs_e3_cov_inf0_1_intro', 'command_script', '03a_oldmombasa_mission'), ('cs_e3_cov_inf0_1_patrol0', 'command_script', '03a_oldmombasa_mission'), ('cs_e3_mars_pelican0_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e3_mars_pelican0_exit', 'command_script', '03a_oldmombasa_mission'), ('cs_e3_mars_johnson_exit', 'command_script', '03a_oldmombasa_mission'), ('cs_e3_mars_johnson_slam', 'command_script', '03a_oldmombasa_mission'), ('cs_e3_mars_inf1_ride', 'command_script', '03a_oldmombasa_mission'), ('cs_e3_mars_johnson_teleport', 'command_script', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('e3_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e3_mars_pelican0_main', 'dormant', '03a_oldmombasa_mission'), ('e3_mars_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e3_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e3_mars_johnson_main', 'dormant', '03a_oldmombasa_mission'), ('e3_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('cs_e2_cov_hunters0_taunt', 'command_script', '03a_oldmombasa_mission'), ('cs_e2_cov_hunters0_0_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e2_cov_hunters0_1_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e2_cov_inf0_watch', 'command_script', '03a_oldmombasa_mission'), ('cs_e2_mars_johnson0_dialogue0', 'command_script', '03a_oldmombasa_mission'), ('cs_e2_mars_johnson0_watch', 'command_script', '03a_oldmombasa_mission'), ('cs_e2_mars_inf0_watch', 'command_script', '03a_oldmombasa_mission'), ('cs_e2_mars_continue', 'command_script', '03a_oldmombasa_mission'), ('e2_dialog', 'dormant', '03a_oldmombasa_mission'), ('e2_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e2_cov_hunters0_main', 'dormant', '03a_oldmombasa_mission'), ('e2_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e2_mars_johnson_main', 'dormant', '03a_oldmombasa_mission'), ('e2_main', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('cs_e1_mars_pelican0_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_mars_johnson_finale', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_mars_johnson_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_mars_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_mars_entry0', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_cov_phantom0_0_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_cov_phantom0_1_entry', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_cov_inf0_grunt0', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_cov_inf0_0_patrol0', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_cov_inf0_0_patrol1', 'command_script', '03a_oldmombasa_mission'), ('cs_e1_cov_inf0_3_patrol0', 'command_script', '03a_oldmombasa_mission'), ('e1_crashed_pelican', 'continuous', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('boolean', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('e1_mars_pelican0_main', 'dormant', '03a_oldmombasa_mission'), ('e1_cov_phantom0_main', 'dormant', '03a_oldmombasa_mission'), ('e1_cov_snipers0_main', 'dormant', '03a_oldmombasa_mission'), ('e1_cov_inf4_main', 'dormant', '03a_oldmombasa_mission'), ('e1_cov_inf3_main', 'dormant', '03a_oldmombasa_mission'), ('e1_cov_inf2_main', 'dormant', '03a_oldmombasa_mission'), ('e1_cov_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e1_cov_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e1_mars_inf1_main', 'dormant', '03a_oldmombasa_mission'), ('e1_mars_inf0_main', 'dormant', '03a_oldmombasa_mission'), ('e1_mars_johnson_main', 'dormant', '03a_oldmombasa_mission'), ('e1_key', 'dormant', '03a_oldmombasa_mission'), ('e1_main', 'dormant', '03a_oldmombasa_mission'), ('mission_start', 'dormant', '03a_oldmombasa_mission'), ('void', 'static', '03a_oldmombasa_mission'), ('mission_main', 'startup', '03a_oldmombasa_mission'), ('03_intro_01_predict', 'dormant', '03a_oldmombasa_prediction'), ('03_intro_02_predict', 'dormant', '03a_oldmombasa_prediction'), ('03_intro_03_predict', 'dormant', '03a_oldmombasa_prediction'), ('03_intro_04_predict', 'dormant', '03a_oldmombasa_prediction'), ('void', 'static', '03a_oldmombasa_prediction'), ('void', 'static', '03a_oldmombasa_prediction'), ('void', 'static', '03a_oldmombasa_prediction'), ('void', 'static', '03a_oldmombasa_prediction'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/06b_floodzone/06b_floodzone': {
        "objects": {
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase', 'ai_migrate'], 'sources': ['floodzone_mission']},
            'ai_current_squad': {'category': 'object', 'funcs': ['ai_erase', 'ai_set_orders'], 'sources': ['floodzone_mission']},
            'brute_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'brute_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'brute_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'brute_04': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'brute_rifle_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'brute_rifle_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'brute_shot_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'brute_shot_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'commander': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['floodzone_cinematics']},
            'commander_intra1': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'cov_def_enf': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'covenant': {'category': 'object', 'funcs': ['ai_allegiance', 'ai_living_count', 'ai_magically_see', 'ai_migrate', 'ai_set_orders', 'ai_vehicle_exit'], 'sources': ['floodzone_mission']},
            'covenant_infantry': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['floodzone_mission']},
            'covenant_vehicles': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['floodzone_mission']},
            'dam_door_a': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['floodzone_mission']},
            'dam_door_b': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['floodzone_mission']},
            'dervish': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['floodzone_cinematics']},
            'dervish_intra1': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'e20_cov': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['floodzone_mission']},
            'e20_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e20_fld': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['floodzone_mission']},
            'e21_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'e21_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['floodzone_mission']},
            'e21_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['floodzone_mission']},
            'e21_fld_carriers0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['floodzone_mission']},
            'e21_fld_carriers1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e21_fld_inf0': {'category': 'covenant', 'funcs': ['ai_migrate'], 'sources': ['floodzone_mission']},
            'e21_fld_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e21_fld_inf0_1': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['floodzone_mission']},
            'e21_fld_inf0_2': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['floodzone_mission']},
            'e21_fld_inf1_1': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['floodzone_mission']},
            'e21_fld_inf1_2': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['floodzone_mission']},
            'e22_cov_inf1_0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'e22_fld_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e23_fld_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e23_fld_inf0_0': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['floodzone_mission']},
            'e23_fld_inf0_1': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['floodzone_mission']},
            'e24_fld_inf1_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e25_fld_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e25_fld_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e25_fld_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e25_fld_inf1_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e25_fld_inf1_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e25_fld_inf1_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e26_fld_infection_forms0/swarm0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e26_fld_infection_forms0/swarm1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e26_fld_infection_forms0/swarm2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e26_fld_infection_forms0/swarm3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'e26_smg0': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['floodzone_mission']},
            'e26_smg1': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['floodzone_mission']},
            'elite_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'elite_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'elite_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'elite_04': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'energy_blade': {'category': 'object', 'funcs': ['object_set_permutation'], 'sources': ['floodzone_cinematics']},
            'ext_a_flood_a': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_flood_b': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_flood_c': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_flood_d': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_flood_dam_a': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_flood_dam_b': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_flood_e': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_flood_f': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_flood_ghost_fr': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'ext_a_sen_a': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_sen_b': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_sen_c': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_sen_d': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_sen_dam_a': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_sen_dam_b': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_sen_e': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_a_sen_elim_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'ext_a_sen_f': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_b_flood': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_b_flood_a': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_b_flood_b': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_b_flood_c': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_b_flood_d': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_b_sentinels_a': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_b_sentinels_b': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_b_sentinels_c': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'ext_b_sentinels_d': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'fact_ent_enf': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'fact_ent_flood': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'fact_ent_flood_scorpion': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'fact_ent_flood_turrets': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'fact_ent_flood_wraith_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'fact_ent_flood_wraith_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'fact_ent_sen': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'fact_ent_sentinels': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'factory1_flood': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['floodzone_mission']},
            'factory1_sentinels': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'factory2_flood': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'factory2_flood_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory2_flood_bk_tunnel': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory2_flood_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory2_flood_mid': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory2_sen_bk_tunnel': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_flood_alcove': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_flood_end': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_flood_initial_end': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_flood_initial_mid': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_flood_intro': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_flood_tubes_far': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_flood_tubes_near': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_major': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_sentinels_01_high': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_sentinels_01_low': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_sentinels_02_high': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_sentinels_02_low': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_sentinels_03_high': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_sentinels_03_low': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_sentinels_initial_end': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_sentinels_initial_mid': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'factory_1_sentinels_intro': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'gorge_enf': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'gorge_flood_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'gorge_flood_bk_cave': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'gorge_flood_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'gorge_jugg_a': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'gorge_jugg_b': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'gorge_sen': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'hammer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['floodzone_cinematics']},
            'human_key_door2': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['floodzone_mission']},
            'index_container': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['floodzone_cinematics']},
            'johnson': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['floodzone_cinematics']},
            'johnson_rifle': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['floodzone_cinematics']},
            'key': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['floodzone_cinematics', 'floodzone_mission']},
            'key_human': {'category': 'human', 'funcs': ['device_get_position', 'object_destroy'], 'sources': ['floodzone_mission']},
            'key_intra2_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['floodzone_cinematics']},
            'key_intra2_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'key_ride_door0': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['floodzone_cinematics', 'floodzone_mission']},
            'key_ride_door1': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['floodzone_mission']},
            'key_ride_door2': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['floodzone_mission']},
            'key_ride_door3': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['floodzone_mission']},
            'key_ride_tartarus': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'key_switch': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['floodzone_cinematics']},
            'miranda': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['floodzone_cinematics']},
            'miranda_smg_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'miranda_smg_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'phantom_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['floodzone_cinematics']},
            'phantom_intra1': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['floodzone_mission']},
            'prophet': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['floodzone_mission']},
            'qz_cov_def_enforcer_a': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['floodzone_mission']},
            'qz_cov_def_enforcer_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_cov_def_ghosts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_cov_def_phantom': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_cov_def_sen_elim': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_cov_def_spec_ops': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_cov_def_spectre': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_dam_door_a': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['floodzone_mission']},
            'qz_door_a': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['floodzone_mission']},
            'qz_ext_a_dam_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'qz_ext_a_dam_enf/a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_dam_enf_door': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_dam_flood_cliff_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_dam_flood_cliff_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_dam_flood_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_dam_human': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_dam_sen': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_dam_sen_elim': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_enf_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_enf_bk': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_flood_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_flood_c2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_flood_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_flood_ghosts': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_flood_rocket': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_flood_wraith_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_flood_wraith_fr': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_flood_wraith_ledge': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_ghosts': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_phantom': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_a_spec_ops': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_cov_ghosts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_cov_phantom': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_cov_spec_ops': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_enter'], 'sources': ['floodzone_mission']},
            'qz_ext_b_cov_spectre': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_enf_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_enf_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ent_cov_phantom': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ent_enf': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ent_flood_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ent_flood_tube_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ent_flood_tube_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ent_ghost_bk': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ent_scorpion': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ent_turrets': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ent_wraith_a': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_fact_flood': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_fact_ghost_bk': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_fact_ghosts': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_fact_ghosts_spare': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_fact_humans': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_fact_scorpion': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_fact_warthog': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_fact_wraith': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ghosts_a': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_ghosts_b': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_warthog': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_warthog_gauss': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_wraith_a': {'category': 'object', 'funcs': ['ai_magically_see', 'ai_place'], 'sources': ['floodzone_mission']},
            'qz_ext_b_wraith_b': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'sentinels': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'spectre_intra1': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['floodzone_cinematics']},
            'tartarus': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['floodzone_cinematics']},
            'tv_bsp_swap_bullshit': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['floodzone_mission']},
            'tv_cutscene_key_boarding': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_dam_door_a': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_dam_door_b': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_e20_dock_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_e26_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_a_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_a_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_a_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_a_d': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_a_dam_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_a_e': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_a_f': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_a_fact_ent': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_a_ghosts_off': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_b_back': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_b_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_b_exit_door': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_b_exit_tube_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_b_exit_tube_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_b_fact_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_b_gate': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_ext_b_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_fact_ent_follow': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_factory': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission', 'floodzone_teleport']},
            'tv_factory2_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_factory2_enter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_factory2_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_gorge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_gorge_bk_cave': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_gorge_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_key_near_lower_spawner': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_key_ride': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission', 'floodzone_teleport']},
            'tv_key_ride_cinematic': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_key_upper_left_side': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_mission_end0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_mission_end1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_music_06b_07': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_qz_ext_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission', 'floodzone_teleport']},
            'tv_qz_ext_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission', 'floodzone_teleport']},
            'tv_veh_int_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_veh_int_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_veh_int_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_veh_int_d': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_vehicle_int': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'tv_x07': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission', 'floodzone_teleport']},
            'veh_int_door_a': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['floodzone_mission']},
            'veh_int_door_b': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['floodzone_mission']},
            'veh_int_enf_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_enf_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_enf_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_flood_b': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'veh_int_flood_bk/runner': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_flood_c': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'veh_int_flood_d': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'veh_int_flood_ghosts_bk': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_flood_ghosts_ini': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_flood_hog_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_ghost_ab': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_hog_ab': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_scorpion': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_sen_a': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'veh_int_sen_b': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'veh_int_sen_c': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'veh_int_sen_d': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['floodzone_mission']},
            'veh_int_sen_elim_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_sen_elim_lt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_sen_elim_rt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_turrets': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_wraith': {'category': 'object', 'funcs': ['ai_magically_see'], 'sources': ['floodzone_mission']},
            'veh_int_wraith/driver': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'veh_int_wraith/wraith': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['floodzone_mission']},
            'vol_factory_1_enter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'vol_factory_1_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'vol_factory_1_mid_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'vol_factory_1_mid_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'vol_factory_1_mid_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_mission']},
            'vol_factory_2_enter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['floodzone_teleport']},
            'x07_tentacle': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['floodzone_cinematics']},
        },
        "scripts": [('void', 'stub', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_cinematics'), ('c06_intra1_score_01', 'dormant', 'floodzone_cinematics'), ('c06_intra1_foley_01', 'dormant', 'floodzone_cinematics'), ('c06_2070_der', 'dormant', 'floodzone_cinematics'), ('c06_2090_soc', 'dormant', 'floodzone_cinematics'), ('c06_2101_elc', 'dormant', 'floodzone_cinematics'), ('c06_2110_soc', 'dormant', 'floodzone_cinematics'), ('c06_2120_soc', 'dormant', 'floodzone_cinematics'), ('c06_intra1_dof_01', 'dormant', 'floodzone_cinematics'), ('c06_intra1_dof_02', 'dormant', 'floodzone_cinematics'), ('c06_intra1_cinematic_light', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('c06_intra2_score_01', 'dormant', 'floodzone_cinematics'), ('c06_intra2_foley_01', 'dormant', 'floodzone_cinematics'), ('c06_3010_soc', 'dormant', 'floodzone_cinematics'), ('c06_intra2_cinematic_light', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('c06_intra2_foley_02', 'dormant', 'floodzone_cinematics'), ('c06_3030_soc', 'dormant', 'floodzone_cinematics'), ('blade_activate', 'dormant', 'floodzone_cinematics'), ('kill_switch', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('c06_intra2_foley_03', 'dormant', 'floodzone_cinematics'), ('l06_0300_tar', 'dormant', 'floodzone_cinematics'), ('l06_0310_tar', 'dormant', 'floodzone_cinematics'), ('key_door_open', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('x07_foley_01', 'dormant', 'floodzone_cinematics'), ('x07_cinematic_light_01', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('x07_score_02', 'dormant', 'floodzone_cinematics'), ('x07_foley_02', 'dormant', 'floodzone_cinematics'), ('x07_0010_mir', 'dormant', 'floodzone_cinematics'), ('x07_0020_jon', 'dormant', 'floodzone_cinematics'), ('x07_0030_mir', 'dormant', 'floodzone_cinematics'), ('x07_emotion_miranda_01', 'dormant', 'floodzone_cinematics'), ('x07_emotion_miranda_02', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('x07_score_03', 'dormant', 'floodzone_cinematics'), ('x07_foley_03', 'dormant', 'floodzone_cinematics'), ('x07_0040_jon', 'dormant', 'floodzone_cinematics'), ('x07_0050_jon', 'dormant', 'floodzone_cinematics'), ('x07_0060_jon', 'dormant', 'floodzone_cinematics'), ('x07_0070_jon', 'dormant', 'floodzone_cinematics'), ('x07_0080_jon', 'dormant', 'floodzone_cinematics'), ('x07_0090_mir', 'dormant', 'floodzone_cinematics'), ('x07_0100_mir', 'dormant', 'floodzone_cinematics'), ('miranda_smgs_fire_1', 'dormant', 'floodzone_cinematics'), ('johnson_rifle_fire', 'dormant', 'floodzone_cinematics'), ('dervish_cammo', 'dormant', 'floodzone_cinematics'), ('x07_cinematic_light_03', 'dormant', 'floodzone_cinematics'), ('johnson_rifle_arm', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('x07_foley_04', 'dormant', 'floodzone_cinematics'), ('x07_0110_mir', 'dormant', 'floodzone_cinematics'), ('x07_0120_mir', 'dormant', 'floodzone_cinematics'), ('x07_0130_tar', 'dormant', 'floodzone_cinematics'), ('x07_0140_der', 'dormant', 'floodzone_cinematics'), ('effect_miranda_hit', 'dormant', 'floodzone_cinematics'), ('x07_cinematic_light_04', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('x07_emotion_miranda_03', 'dormant', 'floodzone_cinematics'), ('tartarus_hide_seek', 'dormant', 'floodzone_cinematics'), ('miranda_smgs_destroy', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('x07_foley_05', 'dormant', 'floodzone_cinematics'), ('x07_0150_tar', 'dormant', 'floodzone_cinematics'), ('x07_0160_tar', 'dormant', 'floodzone_cinematics'), ('x07_0170_tar', 'dormant', 'floodzone_cinematics'), ('x07_0180_tar', 'dormant', 'floodzone_cinematics'), ('x07_0190_der', 'dormant', 'floodzone_cinematics'), ('destroy_miranda', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('x07_foley_06', 'dormant', 'floodzone_cinematics'), ('x07_0200_tar', 'dormant', 'floodzone_cinematics'), ('tartarus_bruteshot_fire', 'dormant', 'floodzone_cinematics'), ('tartarus_bruteshot_hit', 'dormant', 'floodzone_cinematics'), ('x07_predict_shaft_01', 'dormant', 'floodzone_cinematics'), ('x07_predict_shaft_02', 'dormant', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'static', 'floodzone_cinematics'), ('void', 'stub', 'floodzone_mission'), ('void', 'stub', 'floodzone_mission'), ('void', 'stub', 'floodzone_mission'), ('cs_invulnerable', 'command_script', 'floodzone_mission'), ('cs_invul_8', 'command_script', 'floodzone_mission'), ('cs_kill', 'command_script', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('ice_cream_superman', 'dormant', 'floodzone_mission'), ('music_06b_01', 'dormant', 'floodzone_mission'), ('music_06b_02', 'dormant', 'floodzone_mission'), ('music_06b_03', 'dormant', 'floodzone_mission'), ('music_06b_04', 'dormant', 'floodzone_mission'), ('music_06b_05', 'dormant', 'floodzone_mission'), ('music_06b_06', 'dormant', 'floodzone_mission'), ('music_06b_07', 'dormant', 'floodzone_mission'), ('chapter_mirror', 'dormant', 'floodzone_mission'), ('chapter_competition', 'dormant', 'floodzone_mission'), ('chapter_gallery', 'dormant', 'floodzone_mission'), ('chapter_familiar', 'dormant', 'floodzone_mission'), ('objective_push_set', 'dormant', 'floodzone_mission'), ('objective_push_clear', 'dormant', 'floodzone_mission'), ('objective_link_set', 'dormant', 'floodzone_mission'), ('objective_link_clear', 'dormant', 'floodzone_mission'), ('objective_retrieve_set', 'dormant', 'floodzone_mission'), ('objective_retrieve_clear', 'dormant', 'floodzone_mission'), ('sc_cov_charge', 'dormant', 'floodzone_mission'), ('sc_cov_charge', 'dormant', 'floodzone_mission'), ('cs_sc_qz_veh_int', 'command_script', 'floodzone_mission'), ('sc_qz_veh_int', 'dormant', 'floodzone_mission'), ('sc_ext_a', 'dormant', 'floodzone_mission'), ('sc_factory_approach', 'dormant', 'floodzone_mission'), ('sc_factory_exit', 'dormant', 'floodzone_mission'), ('sc_human_fools', 'dormant', 'floodzone_mission'), ('sc_ext_b', 'dormant', 'floodzone_mission'), ('sc_chasm', 'dormant', 'floodzone_mission'), ('sc_outer_wall', 'dormant', 'floodzone_mission'), ('sc_dock', 'dormant', 'floodzone_mission'), ('boolean', 'static', 'floodzone_mission'), ('boolean', 'static', 'floodzone_mission'), ('cov_def_spec_tele_a', 'command_script', 'floodzone_mission'), ('cov_def_spec_tele_b', 'command_script', 'floodzone_mission'), ('cov_def_spec_tele_c', 'command_script', 'floodzone_mission'), ('cov_def_spec_tele_d', 'command_script', 'floodzone_mission'), ('cs_fact_ent_exit_veh', 'command_script', 'floodzone_mission'), ('ext_a_vehicle_orders', 'dormant', 'floodzone_mission'), ('cs_ext_b_exit', 'command_script', 'floodzone_mission'), ('ext_b_vehicle_orders', 'dormant', 'floodzone_mission'), ('cs_cov_def_phantom', 'command_script', 'floodzone_mission'), ('cs_cov_def_spec_ops_a', 'command_script', 'floodzone_mission'), ('cs_cov_def_spec_ops_b', 'command_script', 'floodzone_mission'), ('cs_cov_def_spec_ops_c', 'command_script', 'floodzone_mission'), ('cs_cov_def_spec_ops_d', 'command_script', 'floodzone_mission'), ('cs_go_to_scorpion', 'command_script', 'floodzone_mission'), ('cs_go_to_wraith', 'command_script', 'floodzone_mission'), ('ai_veh_int_ghost_spawn', 'dormant', 'floodzone_mission'), ('dam_door_a', 'dormant', 'floodzone_mission'), ('dam_door_b', 'dormant', 'floodzone_mission'), ('cs_ext_a_enf_ini', 'command_script', 'floodzone_mission'), ('cs_ext_a_pelican', 'command_script', 'floodzone_mission'), ('cs_boost_1_5', 'command_script', 'floodzone_mission'), ('cs_ext_a_phantom', 'command_script', 'floodzone_mission'), ('cs_wraiths_shoot', 'command_script', 'floodzone_mission'), ('ai_ext_a_dam_enforcers', 'dormant', 'floodzone_mission'), ('ai_qz_ext_a_wraiths', 'dormant', 'floodzone_mission'), ('ai_qz_ext_a_ghosts', 'dormant', 'floodzone_mission'), ('ai_fact_ent_sen_spawn', 'dormant', 'floodzone_mission'), ('ai_fact_ent_enf_spawn', 'dormant', 'floodzone_mission'), ('ai_qz_ext_a_d_spawn', 'dormant', 'floodzone_mission'), ('factory_1_flood_respawn', 'dormant', 'floodzone_mission'), ('factory_1_sentinel_respawn_01', 'dormant', 'floodzone_mission'), ('factory_1_sentinel_respawn_02', 'dormant', 'floodzone_mission'), ('factory_1_sentinel_enders', 'dormant', 'floodzone_mission'), ('factory_1_flood_surge', 'dormant', 'floodzone_mission'), ('sent_factory_1_start', 'dormant', 'floodzone_mission'), ('ai_sentinel_spawn', 'dormant', 'floodzone_mission'), ('ai_gorge', 'dormant', 'floodzone_mission'), ('ai_factory2', 'dormant', 'floodzone_mission'), ('ai_constructor_flock', 'dormant', 'floodzone_mission'), ('cs_ext_b_phantom', 'command_script', 'floodzone_mission'), ('cs_ext_b_ent_phantom', 'command_script', 'floodzone_mission'), ('ai_ext_b_exit_tube_a', 'dormant', 'floodzone_mission'), ('ai_ext_b_exit_tube_b', 'dormant', 'floodzone_mission'), ('ai_ext_b_enf_spawn', 'dormant', 'floodzone_mission'), ('ai_ext_b_bk_ghost_spawn', 'dormant', 'floodzone_mission'), ('key_ride_door3_main', 'dormant', 'floodzone_mission'), ('key_ride_human_door2_main', 'dormant', 'floodzone_mission'), ('key_ride_door2_main', 'dormant', 'floodzone_mission'), ('key_ride_door1_main', 'dormant', 'floodzone_mission'), ('key_ride_door0_main', 'dormant', 'floodzone_mission'), ('key_main', 'dormant', 'floodzone_mission'), ('key_ride_human_key_main', 'dormant', 'floodzone_mission'), ('cs_e21_tartarus', 'command_script', 'floodzone_mission'), ('cs_e22_tartarus', 'command_script', 'floodzone_mission'), ('cs_e23_tartarus', 'command_script', 'floodzone_mission'), ('cs_e24_tartarus', 'command_script', 'floodzone_mission'), ('cs_e25_tartarus', 'command_script', 'floodzone_mission'), ('cs_e26_tartarus', 'command_script', 'floodzone_mission'), ('key_ride_tartarus_main', 'dormant', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('cs_e26_fld_infections_entry3', 'command_script', 'floodzone_mission'), ('cs_e26_fld_infections_entry2', 'command_script', 'floodzone_mission'), ('cs_e26_fld_infections_entry1', 'command_script', 'floodzone_mission'), ('cs_e26_fld_infections_entry0', 'command_script', 'floodzone_mission'), ('e26_smg1', 'dormant', 'floodzone_mission'), ('e26_smg0', 'dormant', 'floodzone_mission'), ('e26_fld_infections_main', 'dormant', 'floodzone_mission'), ('e26_main', 'dormant', 'floodzone_mission'), ('cs_e25_scene3', 'command_script', 'floodzone_mission'), ('cs_e25_scene1', 'command_script', 'floodzone_mission'), ('cs_e25_scene0', 'command_script', 'floodzone_mission'), ('e25_dialogue', 'dormant', 'floodzone_mission'), ('e25_fld_inf1_main', 'dormant', 'floodzone_mission'), ('e25_fld_inf0_main', 'dormant', 'floodzone_mission'), ('e25_main', 'dormant', 'floodzone_mission'), ('cs_e24_fld_inf1_load', 'command_script', 'floodzone_mission'), ('e24_fld_inf2_main', 'dormant', 'floodzone_mission'), ('e24_fld_inf1_main', 'dormant', 'floodzone_mission'), ('e24_fld_inf0_main', 'dormant', 'floodzone_mission'), ('e24_main', 'dormant', 'floodzone_mission'), ('cs_e23_fld_inf0_0_load', 'command_script', 'floodzone_mission'), ('cs_e23_fld_inf0_1_load', 'command_script', 'floodzone_mission'), ('cs_e23_scene0', 'command_script', 'floodzone_mission'), ('e23_dialogue', 'dormant', 'floodzone_mission'), ('e23_fld_inf0_main', 'dormant', 'floodzone_mission'), ('e23_main', 'dormant', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('cs_e22_hack_divide', 'command_script', 'floodzone_mission'), ('cs_e22_fld_inf0_0_load', 'command_script', 'floodzone_mission'), ('cs_e22_scene0', 'command_script', 'floodzone_mission'), ('e22_dialogue', 'dormant', 'floodzone_mission'), ('e22_fld_inf0_main', 'dormant', 'floodzone_mission'), ('e22_main', 'dormant', 'floodzone_mission'), ('cs_e21_fld_inf1_low_entry', 'command_script', 'floodzone_mission'), ('cs_e21_fld_inf1_high_entry', 'command_script', 'floodzone_mission'), ('cs_e21_fld_inf0_low_entry', 'command_script', 'floodzone_mission'), ('cs_e21_fld_inf0_high_entry', 'command_script', 'floodzone_mission'), ('cs_e21_fld_inf0_0_load', 'command_script', 'floodzone_mission'), ('cs_e21_scene0', 'command_script', 'floodzone_mission'), ('cs_e21_scene1', 'command_script', 'floodzone_mission'), ('boolean', 'static', 'floodzone_mission'), ('e21_fld_carriers1_main', 'dormant', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('e21_fld_inf1_main', 'dormant', 'floodzone_mission'), ('e21_fld_carriers0_main', 'dormant', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('e21_fld_inf0_main', 'dormant', 'floodzone_mission'), ('e21_cov_inf0_main', 'dormant', 'floodzone_mission'), ('e21_main', 'dormant', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('cinematic_key_boarding', 'dormant', 'floodzone_mission'), ('e20_cov_inf0_main', 'dormant', 'floodzone_mission'), ('e20_main', 'dormant', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('begin_key_ride_main', 'dormant', 'floodzone_mission'), ('enc_cov_charge', 'dormant', 'floodzone_mission'), ('enc_vehicle_int', 'dormant', 'floodzone_mission'), ('enc_qz_ext_a', 'dormant', 'floodzone_mission'), ('enc_crashed_factory', 'dormant', 'floodzone_mission'), ('enc_qz_ext_b', 'dormant', 'floodzone_mission'), ('enc_key_ride', 'dormant', 'floodzone_mission'), ('enc_library', 'dormant', 'floodzone_mission'), ('mission_floodzone', 'dormant', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('mission_main', 'startup', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('void', 'static', 'floodzone_mission'), ('06_intra1_01_predict', 'dormant', 'floodzone_prediction'), ('06_intra2_01_predict', 'dormant', 'floodzone_prediction'), ('06_intra2_02_predict', 'dormant', 'floodzone_prediction'), ('06_intra2_03_predict', 'dormant', 'floodzone_prediction'), ('x07_01_predict', 'dormant', 'floodzone_prediction'), ('x07_02_predict', 'dormant', 'floodzone_prediction'), ('x07_03_predict', 'dormant', 'floodzone_prediction'), ('x07_04_predict', 'dormant', 'floodzone_prediction'), ('x07_05_predict', 'dormant', 'floodzone_prediction'), ('x07_06_predict', 'dormant', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_prediction'), ('void', 'static', 'floodzone_teleport'), ('void', 'static', 'floodzone_teleport'), ('void', 'static', 'floodzone_teleport'), ('void', 'static', 'floodzone_teleport'), ('void', 'static', 'floodzone_teleport'), ('void', 'static', 'floodzone_teleport'), ('void', 'static', 'floodzone_teleport'), ('void', 'static', 'floodzone_teleport'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/03b_newmombasa/03b_newmombasa': {
        "objects": {
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase', 'ai_migrate', 'ai_strength', 'ai_vehicle_exit'], 'sources': ['03b_newmombasa_mission']},
            'ai_current_squad': {'category': 'object', 'funcs': ['ai_erase', 'ai_strength'], 'sources': ['03b_newmombasa_mission']},
            'carrier': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'carrier_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['03b_newmombasa_cinematics']},
            'chief': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'cigar': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'covenant': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['03b_newmombasa_mission']},
            'e14_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e14_cov_ghosts0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e14_cov_ghosts0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e14_cov_wraiths0/wraith0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e14_mars_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e14_mars_inf0/warthog0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e14_mars_inf0/warthog1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e14_mars_pelican0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e15_cov': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e15_cov_banshees0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e15_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e15_cov_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e15_cov_inf2_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e15_cov_inf2_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e15_cov_phantom0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e15_cov_phantom0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e15_cov_phantom1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e15_mars_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_banshees0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_banshees0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_ghosts0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_ghosts0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_ghosts1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_phantom0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_wraiths0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_wraiths0_0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_wraiths0_0/wraith0': {'category': 'covenant', 'funcs': ['ai_braindead', 'ai_living_count', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_wraiths0_0/wraith1': {'category': 'covenant', 'funcs': ['ai_braindead', 'ai_living_count', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_cov_wraiths1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e16_mars': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['03b_newmombasa_mission']},
            'e16_mars_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf0_3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf1_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf2': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf2_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf2_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf2_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_cov_inf2_3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_door0': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['03b_newmombasa_mission']},
            'e17_door1': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['03b_newmombasa_mission']},
            'e17_mars_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e17_mars_inf0/passenger0': {'category': 'covenant', 'funcs': ['ai_vehicle_exit'], 'sources': ['03b_newmombasa_mission']},
            'e17_mars_inf0/warthog0': {'category': 'covenant', 'funcs': ['ai_vehicle_exit'], 'sources': ['03b_newmombasa_mission']},
            'e18_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e18_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e18_cov_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e18_cov_inf1_1': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e18_cov_inf2': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e18_cov_inf2_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e18_cov_inf2_1/sniper0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e18_cov_inf2_1/sniper1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e18_mars_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e18_mars_warthog0': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e19_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['03b_newmombasa_mission']},
            'e19_cov_ghosts0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e19_cov_ghosts0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e19_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e19_cov_wraiths0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e19_mars_warthog0': {'category': 'human', 'funcs': ['ai_migrate'], 'sources': ['03b_newmombasa_mission']},
            'e19_tree0': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_mission']},
            'e19_tree1': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_mission']},
            'e20_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e20_mars_warthog0': {'category': 'human', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e20_mars_warthog1': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e20_mars_warthog1/spare': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_creep0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_ghosts0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_phantom0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_phantom1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_wraiths0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_wraiths0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_wraiths0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_cov_wraiths0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_mars_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_mars_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_mars_pelican0/pelican0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_mars_pelican0/scorpion0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_mars_pelican1': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e21_mars_warthog0': {'category': 'human', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_door0': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['03b_newmombasa_mission']},
            'e22_door1': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['03b_newmombasa_mission']},
            'e22_door2': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['03b_newmombasa_mission']},
            'e22_door3': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf0': {'category': 'covenant', 'funcs': ['ai_set_orders', 'ai_vehicle_exit'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf0/guard0': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf0/guard1': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf0/guard2': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf0/medic0': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf0/perez': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf1': {'category': 'covenant', 'funcs': ['ai_migrate'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf1/lieutenant': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf1/marine0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf1/marine1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_mars_scorpions0': {'category': 'human', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e22_scarab_gun': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf0_3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf0_4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf1': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf1_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf1_0/ultra0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e23_cov_inf1_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_gun': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_pelican0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_pelican1_0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_pelican1_1': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_pelican2': {'category': 'human', 'funcs': ['ai_living_count'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_pelican2/gunner0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_pelican2/gunner1': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_pelican2/pelican0': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_pelican2/pelican1': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'e23_mars_pelican2/pelican2': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'g_target': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['03b_newmombasa_mission']},
            'generic_player_sighted': {'category': 'object', 'funcs': ['ai_trigger_test'], 'sources': ['03b_newmombasa_mission']},
            'hood': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['03b_newmombasa_cinematics']},
            'iac': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['03b_newmombasa_cinematics']},
            'iac_bridge': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['03b_newmombasa_cinematics']},
            'johnson': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'johnson_02': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'johnson_03': {'category': 'human', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'marine_01': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'marine_02': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_set_permutation'], 'sources': ['03b_newmombasa_cinematics']},
            'miranda': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['03b_newmombasa_cinematics']},
            'nav_officer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['03b_newmombasa_cinematics']},
            'pelican_01a': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'pelican_01b': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'pelican_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'pilot': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'pilot_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['03b_newmombasa_mission']},
            'rear_gun': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'rifle_01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'rifle_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'rifle_03': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'scarab': {'category': 'object', 'funcs': ['device_get_position', 'object_destroy', 'object_teleport'], 'sources': ['03b_newmombasa_mission']},
            'scarab_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'scarab_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'scarab_gunners/left_gunner0': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'scarab_gunners/left_gunner1': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'scarab_gunners/main_gunner': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'scarab_gunners/right_gunner0': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'scarab_gunners/right_gunner1': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['03b_newmombasa_mission']},
            'scarab_gunners/upper_gunner': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['03b_newmombasa_mission']},
            'scorpion_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'scorpion_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'tv_dark_area0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e14_blockade0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e14_blockade1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e14_blockade2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e14_blockade3': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e14_blockade4': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e14_blockade5': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e14_mars_inf0_advance': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e15_cov_inf1_spring': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e15_cov_phantoms0_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e15_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e15_phantom_drop_zone0': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e15_phantom_drop_zone1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e16_bridge_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e16_cov_inf0_1_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e16_cov_inf0_2_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e16_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e16_toll_plaza': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e16_tunnel': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_cov_inf0_2_init': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_cov_inf2_1_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_first_wall_approach': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_migration_area': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_near_first_wall': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_near_second_wall': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_objectives': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_on_first_wall': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_section0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_section1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_section2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e17_section3': {'category': 'object', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e18_cov_inf2_1_unsafe0': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e18_cov_inf2_1_unsafe1': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e18_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e18_second_half': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e19_cov_ghosts0_1_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e19_main_begin0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e19_main_begin1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e19_player_advanced': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e19_scarab_withdraws': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e20_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e21_boulevard1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e21_cov_creep0_main': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e21_cov_inf0_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e21_cov_wraith0_2_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e21_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e21_mars_inf0_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e22_away_from_building': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e22_begin_scarab_sequence': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e22_doorway': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e22_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e22_mars_inf0_visible': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e22_mars_inf3_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e22_near_building': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e22_scarab_entry_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e22_stairwell': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e23_entry_door': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e23_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e23_mars_pelican0_begin': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e23_mars_pelican1_begin': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_e23_scarab_corner_continue': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_scarab': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_scarab_interior': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_scarab_no_save': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'tv_scarab_stairwell': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['03b_newmombasa_mission']},
            'x03_bus': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'x03_dumpster': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'x03_generator': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'x03_shockwave_close': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'x03_shockwave_far': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'x03_shockwave_start': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'x03_slipspace_collapse': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'x03_smoke': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
            'x03_truck': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['03b_newmombasa_cinematics']},
        },
        "scripts": [('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_cinematics'), ('c03_intra1_sound_scene1_01', 'dormant', '03b_newmombasa_cinematics'), ('c03_intra1_score_01', 'dormant', '03b_newmombasa_cinematics'), ('c03_intra1_foley_01', 'dormant', '03b_newmombasa_cinematics'), ('c03_2010_mr3', 'dormant', '03b_newmombasa_cinematics'), ('c03_2020_mr4', 'dormant', '03b_newmombasa_cinematics'), ('c03_2030_mr4', 'dormant', '03b_newmombasa_cinematics'), ('c03_intra1_fov_01', 'dormant', '03b_newmombasa_cinematics'), ('drop_tank', 'dormant', '03b_newmombasa_cinematics'), ('destroy_scarab', 'dormant', '03b_newmombasa_cinematics'), ('c03_intra1_cinematic_light_01', 'dormant', '03b_newmombasa_cinematics'), ('c03_intra1_problem_actors', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('c03_intra1_foley_02a', 'dormant', '03b_newmombasa_cinematics'), ('c03_2040_jon', 'dormant', '03b_newmombasa_cinematics'), ('c03_2050_mr4', 'dormant', '03b_newmombasa_cinematics'), ('c03_2060_mr3', 'dormant', '03b_newmombasa_cinematics'), ('c03_2070_jon', 'dormant', '03b_newmombasa_cinematics'), ('c03_2080_mr3', 'dormant', '03b_newmombasa_cinematics'), ('c03_2090_jon', 'dormant', '03b_newmombasa_cinematics'), ('swap_tanks', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('c03_intra1_speech_easy', 'dormant', '03b_newmombasa_cinematics'), ('c03_intra1_speech_normal', 'dormant', '03b_newmombasa_cinematics'), ('c03_intra1_speech_heroic', 'dormant', '03b_newmombasa_cinematics'), ('c03_intra1_speech_legendary', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('c03_intra1_foley_02c', 'dormant', '03b_newmombasa_cinematics'), ('c03_2092_jon', 'dormant', '03b_newmombasa_cinematics'), ('c03_2094_jon', 'dormant', '03b_newmombasa_cinematics'), ('c03_2096_jon', 'dormant', '03b_newmombasa_cinematics'), ('c03_2098_jon', 'dormant', '03b_newmombasa_cinematics'), ('c03_2100_mr4', 'dormant', '03b_newmombasa_cinematics'), ('c03_2100_mr4_hard', 'dormant', '03b_newmombasa_cinematics'), ('c03_2100_mr4_leg', 'dormant', '03b_newmombasa_cinematics'), ('c03_2110_jon', 'dormant', '03b_newmombasa_cinematics'), ('c03_2110_jon_leg', 'dormant', '03b_newmombasa_cinematics'), ('c03_2120_jon', 'dormant', '03b_newmombasa_cinematics'), ('c03_2120_jon_leg', 'dormant', '03b_newmombasa_cinematics'), ('c03_2130_mr4', 'dormant', '03b_newmombasa_cinematics'), ('c03_2130_mr4_leg', 'dormant', '03b_newmombasa_cinematics'), ('c03_2140_cor', 'dormant', '03b_newmombasa_cinematics'), ('c03_2140_cor_leg', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('c03_intra1_foley_03', 'dormant', '03b_newmombasa_cinematics'), ('c03_2150_jon', 'dormant', '03b_newmombasa_cinematics'), ('c03_intra1_cinematic_light_03', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('x03_foley_01', 'dormant', '03b_newmombasa_cinematics'), ('x03_0010_jon', 'dormant', '03b_newmombasa_cinematics'), ('x03_0020_mir', 'dormant', '03b_newmombasa_cinematics'), ('x03_fov_01', 'dormant', '03b_newmombasa_cinematics'), ('x03_01_dof_1', 'dormant', '03b_newmombasa_cinematics'), ('scarab_shake_1', 'dormant', '03b_newmombasa_cinematics'), ('scarab_shake_2', 'dormant', '03b_newmombasa_cinematics'), ('effect_scarab_death', 'dormant', '03b_newmombasa_cinematics'), ('effect_smoke_start', 'dormant', '03b_newmombasa_cinematics'), ('effect_smoke_stop', 'dormant', '03b_newmombasa_cinematics'), ('effect_grav_lift', 'dormant', '03b_newmombasa_cinematics'), ('x03_cinematic_lighting_01', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('c03_intra1_sound_scene2_01', 'dormant', '03b_newmombasa_cinematics'), ('x03_foley_02', 'dormant', '03b_newmombasa_cinematics'), ('x03_0030_mir', 'dormant', '03b_newmombasa_cinematics'), ('x03_0040_jon', 'dormant', '03b_newmombasa_cinematics'), ('x03_0050_lhd', 'dormant', '03b_newmombasa_cinematics'), ('x03_0060_mir', 'dormant', '03b_newmombasa_cinematics'), ('x03_texture_camera_scene_02', 'dormant', '03b_newmombasa_cinematics'), ('x03_cinematic_lighting_02', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('delete_johnson', 'dormant', '03b_newmombasa_cinematics'), ('x03_emotion_02', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('x03_score_03', 'dormant', '03b_newmombasa_cinematics'), ('x03_foley_03', 'dormant', '03b_newmombasa_cinematics'), ('x03_0070_lhd', 'dormant', '03b_newmombasa_cinematics'), ('x03_0080_lhd', 'dormant', '03b_newmombasa_cinematics'), ('x03_0090_nv1', 'dormant', '03b_newmombasa_cinematics'), ('x03_fov_03', 'dormant', '03b_newmombasa_cinematics'), ('effect_slipspace_open', 'dormant', '03b_newmombasa_cinematics'), ('x03_cinematic_lighting_03', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('hide_iac_crew_03', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('x03_foley_04', 'dormant', '03b_newmombasa_cinematics'), ('x03_0100_nv1', 'dormant', '03b_newmombasa_cinematics'), ('x03_0110_mir', 'dormant', '03b_newmombasa_cinematics'), ('x03_0120_lhd', 'dormant', '03b_newmombasa_cinematics'), ('x03_texture_camera_scene_04', 'dormant', '03b_newmombasa_cinematics'), ('x03_cinematic_lighting_04', 'dormant', '03b_newmombasa_cinematics'), ('x03_emotion_04', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('x03_foley_05', 'dormant', '03b_newmombasa_cinematics'), ('x03_0130_mir', 'dormant', '03b_newmombasa_cinematics'), ('effect_iac_engines', 'dormant', '03b_newmombasa_cinematics'), ('effect_slipspace_widen', 'dormant', '03b_newmombasa_cinematics'), ('x03_cinematic_lighting_05', 'dormant', '03b_newmombasa_cinematics'), ('delete_pelican', 'dormant', '03b_newmombasa_cinematics'), ('hide_iac_crew_05', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('x03_foley_06', 'dormant', '03b_newmombasa_cinematics'), ('x03_0140_nv1', 'dormant', '03b_newmombasa_cinematics'), ('x03_0150_mir', 'dormant', '03b_newmombasa_cinematics'), ('x03_fov_06', 'dormant', '03b_newmombasa_cinematics'), ('x03_texture_camera_scene_06', 'dormant', '03b_newmombasa_cinematics'), ('x03_cinematic_lighting_06', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('x03_foley_07', 'dormant', '03b_newmombasa_cinematics'), ('effect_slipspace_collapse', 'dormant', '03b_newmombasa_cinematics'), ('effect_shockwave_start', 'dormant', '03b_newmombasa_cinematics'), ('shockwave_shake_01', 'dormant', '03b_newmombasa_cinematics'), ('x03_cinematic_lighting_07', 'dormant', '03b_newmombasa_cinematics'), ('delete_iac', 'dormant', '03b_newmombasa_cinematics'), ('delete_carrier', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('effect_ease_on_down_the_road', 'dormant', '03b_newmombasa_cinematics'), ('effect_akira', 'dormant', '03b_newmombasa_cinematics'), ('shockwave_shake_02', 'dormant', '03b_newmombasa_cinematics'), ('shockwave_shake_03', 'dormant', '03b_newmombasa_cinematics'), ('final_fade', 'dormant', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'static', '03b_newmombasa_cinematics'), ('void', 'stub', '03b_newmombasa_mission'), ('void', 'stub', '03b_newmombasa_mission'), ('chapter_title0', 'dormant', '03b_newmombasa_mission'), ('chapter_title1', 'dormant', '03b_newmombasa_mission'), ('chapter_title2', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('objective0_set', 'dormant', '03b_newmombasa_mission'), ('objective0_clear', 'dormant', '03b_newmombasa_mission'), ('objective1_set', 'dormant', '03b_newmombasa_mission'), ('objective1_clear', 'dormant', '03b_newmombasa_mission'), ('objective2_set', 'dormant', '03b_newmombasa_mission'), ('objective2_clear', 'dormant', '03b_newmombasa_mission'), ('objective3_set', 'dormant', '03b_newmombasa_mission'), ('music_03b_01_stop', 'dormant', '03b_newmombasa_mission'), ('music_03b_01_start_alt', 'dormant', '03b_newmombasa_mission'), ('music_03b_01_start', 'dormant', '03b_newmombasa_mission'), ('music_03b_02_stop', 'dormant', '03b_newmombasa_mission'), ('music_03b_02_start', 'dormant', '03b_newmombasa_mission'), ('music_03b_03_stop', 'dormant', '03b_newmombasa_mission'), ('music_03b_03_start', 'dormant', '03b_newmombasa_mission'), ('music_03b_04_stop', 'dormant', '03b_newmombasa_mission'), ('music_03b_04_start_alt', 'dormant', '03b_newmombasa_mission'), ('music_03b_04_start', 'dormant', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('flashlight_control', 'dormant', '03b_newmombasa_mission'), ('scarab_no_save', 'dormant', '03b_newmombasa_mission'), ('cs_scarab_load_main_gun', 'command_script', '03b_newmombasa_mission'), ('cs_scarab_load_upper_gun', 'command_script', '03b_newmombasa_mission'), ('cs_scarab_load_rear_gun', 'command_script', '03b_newmombasa_mission'), ('cs_scarab_load_right_gun0', 'command_script', '03b_newmombasa_mission'), ('cs_scarab_load_right_gun1', 'command_script', '03b_newmombasa_mission'), ('cs_scarab_load_left_gun0', 'command_script', '03b_newmombasa_mission'), ('cs_scarab_load_left_gun1', 'command_script', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('cs_e23_mars_pelican1_0_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican1_1_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican0_entry0', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican0_evade0', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican0_entry1', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican0_evade1', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican0_gunners0', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican0_gunners1', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican2_0_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican2_1_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican2_gunners0', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican2_gunners1', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_pelican2_2_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_inf1_shoot', 'command_script', '03b_newmombasa_mission'), ('cs_e23_mars_inf0_shoot', 'command_script', '03b_newmombasa_mission'), ('cs_e23_cov_inf1_pilot_exit', 'command_script', '03b_newmombasa_mission'), ('cs_e23_cov_inf1_pilot0', 'command_script', '03b_newmombasa_mission'), ('cs_e23_cov_inf1_pilot1', 'command_script', '03b_newmombasa_mission'), ('cs_e23_scarab_shoot_pelican0', 'command_script', '03b_newmombasa_mission'), ('cs_e23_scarab_shoot_pelican1', 'command_script', '03b_newmombasa_mission'), ('cs_e23_scarab_upper_gun', 'command_script', '03b_newmombasa_mission'), ('cs_best_cs_ever', 'command_script', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('scarab_left_gunner0_main', 'dormant', '03b_newmombasa_mission'), ('scarab_left_gunner1_main', 'dormant', '03b_newmombasa_mission'), ('scarab_right_gunner0_main', 'dormant', '03b_newmombasa_mission'), ('scarab_right_gunner1_main', 'dormant', '03b_newmombasa_mission'), ('scarab_upper_gunner_main', 'dormant', '03b_newmombasa_mission'), ('e23_scarab', 'dormant', '03b_newmombasa_mission'), ('e23_ultra_dialogue', 'dormant', '03b_newmombasa_mission'), ('e23_ultra_dialogue_kill', 'dormant', '03b_newmombasa_mission'), ('e23_dialogue_boarding', 'dormant', '03b_newmombasa_mission'), ('e23_dialogue_boarding_kill', 'dormant', '03b_newmombasa_mission'), ('e23_best_cs_ever', 'dormant', '03b_newmombasa_mission'), ('e23_cov_inf1_main', 'dormant', '03b_newmombasa_mission'), ('e23_cov_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e23_mars_pelican2_main', 'dormant', '03b_newmombasa_mission'), ('e23_mars_pelican1_main', 'dormant', '03b_newmombasa_mission'), ('e23_mars_pelican0_main', 'dormant', '03b_newmombasa_mission'), ('e23_mars_inf1_main', 'dormant', '03b_newmombasa_mission'), ('e23_mars_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e23_main', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('cs_e22_mars1_go', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars1_lieutenant', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars0_crouch', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars0_stand', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars0_perez', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars_inf1_crouch', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars_inf1_marine1', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars_inf2_marine_end', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars_inf2_marine0', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars_inf2_marine1', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars_inf2_marine2', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars_inf2_marine3', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars_inf2_marine4', 'command_script', '03b_newmombasa_mission'), ('cs_e22_mars_scorpion0', 'command_script', '03b_newmombasa_mission'), ('cs_e22_scarab_main_gun', 'command_script', '03b_newmombasa_mission'), ('e22_scarab_climbing_events', 'dormant', '03b_newmombasa_mission'), ('e22_scarab_advancing_events', 'dormant', '03b_newmombasa_mission'), ('e22_scarab_appearance_events', 'dormant', '03b_newmombasa_mission'), ('e22_scarab_intro_gun', 'dormant', '03b_newmombasa_mission'), ('e22_scarab', 'dormant', '03b_newmombasa_mission'), ('e22_nasty_player_synch', 'dormant', '03b_newmombasa_mission'), ('e22_objective', 'dormant', '03b_newmombasa_mission'), ('e22_dialogue', 'dormant', '03b_newmombasa_mission'), ('e22_dialogue_kill', 'dormant', '03b_newmombasa_mission'), ('e22_mars_inf3_main', 'dormant', '03b_newmombasa_mission'), ('e22_mars_inf2_main', 'dormant', '03b_newmombasa_mission'), ('e22_mars_inf1_main', 'dormant', '03b_newmombasa_mission'), ('e22_mars_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e22_mars_scorpions0_main', 'dormant', '03b_newmombasa_mission'), ('e22_main', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('cs_e21_cov_phantom0_bombard', 'command_script', '03b_newmombasa_mission'), ('cs_e21_cov_wraiths0_bombard', 'command_script', '03b_newmombasa_mission'), ('cs_e21_cov_abort_bombard', 'command_script', '03b_newmombasa_mission'), ('cs_e21_cov_phantom1_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e21_cov_phantom_exit', 'command_script', '03b_newmombasa_mission'), ('cs_e21_mars_pelican0_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e21_mars_pelican0_exit', 'command_script', '03b_newmombasa_mission'), ('cs_e21_mars_pelican1_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e21_mars_inf1_exit', 'command_script', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('e21_dialog', 'dormant', '03b_newmombasa_mission'), ('e21_cov_creep0_main', 'dormant', '03b_newmombasa_mission'), ('e21_cov_phantom1_main', 'dormant', '03b_newmombasa_mission'), ('e21_cov_phantom0_main', 'dormant', '03b_newmombasa_mission'), ('e21_cov_wraiths0_main', 'dormant', '03b_newmombasa_mission'), ('e21_cov_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e21_mars_pelican1_main', 'dormant', '03b_newmombasa_mission'), ('e21_mars_pelican0_main', 'dormant', '03b_newmombasa_mission'), ('e21_mars_warthog0_main', 'dormant', '03b_newmombasa_mission'), ('e21_mars_inf1_main', 'dormant', '03b_newmombasa_mission'), ('e21_mars_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e21_main_end_condition', 'dormant', '03b_newmombasa_mission'), ('e21_main', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('e20_cov_ghosts0_main', 'dormant', '03b_newmombasa_mission'), ('e20_mars_warthog1_main', 'dormant', '03b_newmombasa_mission'), ('e20_mars_warthog0_main', 'dormant', '03b_newmombasa_mission'), ('e20_main', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('cs_e19_cov_ghosts0_1_entry1', 'command_script', '03b_newmombasa_mission'), ('cs_e19_cov_ghosts0_1_entry0', 'command_script', '03b_newmombasa_mission'), ('e19_cov_ghosts0_main', 'dormant', '03b_newmombasa_mission'), ('e19_cov_wraiths0_main', 'dormant', '03b_newmombasa_mission'), ('e19_cov_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e19_mars_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e19_main', 'dormant', '03b_newmombasa_mission'), ('cs_e18_mars_warthog0_orbit', 'command_script', '03b_newmombasa_mission'), ('cs_e18_mars_warthog0_approach0', 'command_script', '03b_newmombasa_mission'), ('cs_e18_mars_warthog0_approach1', 'command_script', '03b_newmombasa_mission'), ('cs_e18_mars_warthog0_abort', 'command_script', '03b_newmombasa_mission'), ('cs_e18_cov_inf0_sniper0', 'command_script', '03b_newmombasa_mission'), ('cs_e18_cov_inf2_1_entry0', 'command_script', '03b_newmombasa_mission'), ('e18_scarab_main', 'dormant', '03b_newmombasa_mission'), ('e18_cov_ghosts0_main', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('e18_cov_inf2_main', 'dormant', '03b_newmombasa_mission'), ('e18_cov_inf1_main', 'dormant', '03b_newmombasa_mission'), ('e18_cov_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e18_mars_warthog0_main', 'dormant', '03b_newmombasa_mission'), ('e18_mars_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e18_key', 'dormant', '03b_newmombasa_mission'), ('e18_main', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('cs_e17_mars_inf0_drive', 'command_script', '03b_newmombasa_mission'), ('cs_e17_shotgun_scene', 'command_script', '03b_newmombasa_mission'), ('cs_e17_cov_inf0_0_turret0', 'command_script', '03b_newmombasa_mission'), ('cs_e17_cov_ghost0_entry0', 'command_script', '03b_newmombasa_mission'), ('cs_e17_mars_selective_migrate', 'command_script', '03b_newmombasa_mission'), ('cs_e17_cov_inf0_2_ambush', 'command_script', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('boolean', 'static', '03b_newmombasa_mission'), ('e17_doors_main', 'dormant', '03b_newmombasa_mission'), ('e17_shotgun_scene', 'dormant', '03b_newmombasa_mission'), ('e17_dialog', 'dormant', '03b_newmombasa_mission'), ('e17_cov_inf2_main', 'dormant', '03b_newmombasa_mission'), ('e17_cov_inf1_main', 'dormant', '03b_newmombasa_mission'), ('e17_cov_inf0_aux', 'dormant', '03b_newmombasa_mission'), ('e17_cov_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e17_mars_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e17_main', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('cs_e16_cov_ghosts0_advance1', 'command_script', '03b_newmombasa_mission'), ('cs_e16_cov_ghosts0_advance0', 'command_script', '03b_newmombasa_mission'), ('cs_e16_cov_banshee_boost0', 'command_script', '03b_newmombasa_mission'), ('cs_e16_cov_banshee_boost1', 'command_script', '03b_newmombasa_mission'), ('cs_e16_cov_inf0_last_stand', 'command_script', '03b_newmombasa_mission'), ('cs_e16_cov_phantom0_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e16_cov_phantom0_exit', 'command_script', '03b_newmombasa_mission'), ('cs_e16_cov_wraiths1_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e16_cov_ghosts1_entry', 'command_script', '03b_newmombasa_mission'), ('e16_cov_phantom0_main', 'dormant', '03b_newmombasa_mission'), ('e16_cov_wraiths1_main', 'dormant', '03b_newmombasa_mission'), ('e16_cov_ghosts1_main', 'dormant', '03b_newmombasa_mission'), ('e16_cov_banshees0_main', 'dormant', '03b_newmombasa_mission'), ('e16_cov_ghosts0_main', 'dormant', '03b_newmombasa_mission'), ('e16_cov_wraiths0_main', 'dormant', '03b_newmombasa_mission'), ('e16_cov_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e16_mars_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e16_main', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('cs_e15_cov_phantom0_1_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e15_cov_phantom0_1_exit', 'command_script', '03b_newmombasa_mission'), ('cs_e15_cov_phantom0_0_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e15_cov_phantom0_0_exit', 'command_script', '03b_newmombasa_mission'), ('cs_e15_cov_phantom1_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e15_cov_banshee0_0_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e15_cov_banshee0_1_entry', 'command_script', '03b_newmombasa_mission'), ('cs_e15_mars_inf0_unload', 'command_script', '03b_newmombasa_mission'), ('cs_e15_mars_inf0_init', 'command_script', '03b_newmombasa_mission'), ('cs_e15_mars_inf0_abort', 'command_script', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('e15_cov_banshees0_main', 'dormant', '03b_newmombasa_mission'), ('e15_cov_wraith1_main', 'dormant', '03b_newmombasa_mission'), ('e15_cov_wraith0_main', 'dormant', '03b_newmombasa_mission'), ('e15_cov_phantom1_main', 'dormant', '03b_newmombasa_mission'), ('e15_cov_phantom0_main', 'dormant', '03b_newmombasa_mission'), ('e15_cov_inf2_main', 'dormant', '03b_newmombasa_mission'), ('e15_cov_inf1_main', 'dormant', '03b_newmombasa_mission'), ('e15_cov_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e15_mars_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e15_main', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('cs_e14_cov_wraiths0_bombard', 'command_script', '03b_newmombasa_mission'), ('cs_e14_mars_pelican0', 'command_script', '03b_newmombasa_mission'), ('cs_e14_cov_ghosts0_advance0', 'command_script', '03b_newmombasa_mission'), ('cs_e14_cov_ghosts0_advance1', 'command_script', '03b_newmombasa_mission'), ('e14_cov_snipers0_main', 'dormant', '03b_newmombasa_mission'), ('e14_cov_wraiths0_main', 'dormant', '03b_newmombasa_mission'), ('e14_cov_ghosts1_main', 'dormant', '03b_newmombasa_mission'), ('e14_cov_ghosts0_main', 'dormant', '03b_newmombasa_mission'), ('e14_mars_pelican0_main', 'dormant', '03b_newmombasa_mission'), ('e14_mars_inf0_main', 'dormant', '03b_newmombasa_mission'), ('e14_main', 'dormant', '03b_newmombasa_mission'), ('mission_start', 'dormant', '03b_newmombasa_mission'), ('void', 'static', '03b_newmombasa_mission'), ('mission_main', 'startup', '03b_newmombasa_mission'), ('03_intra1_01_predict', 'dormant', '03b_newmombasa_prediction'), ('03_intra1_02a_predict', 'dormant', '03b_newmombasa_prediction'), ('03_intra1_02b_predict', 'dormant', '03b_newmombasa_prediction'), ('03_intra1_02c_predict', 'dormant', '03b_newmombasa_prediction'), ('03_intra1_03_predict', 'dormant', '03b_newmombasa_prediction'), ('x03_01_predict', 'dormant', '03b_newmombasa_prediction'), ('x03_02_predict', 'dormant', '03b_newmombasa_prediction'), ('x03_03_predict', 'dormant', '03b_newmombasa_prediction'), ('x03_04_predict', 'dormant', '03b_newmombasa_prediction'), ('x03_05_predict', 'dormant', '03b_newmombasa_prediction'), ('x03_06_predict', 'dormant', '03b_newmombasa_prediction'), ('x03_07_predict', 'dormant', '03b_newmombasa_prediction'), ('x03_08_predict', 'dormant', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('void', 'static', '03b_newmombasa_prediction'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/04a_gasgiant/04a_gasgiant': {
        "objects": {
            'Big_filthy_audio1': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'a50_high': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'a50_low': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['04a_gasgiant_mission']},
            'all_allies': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['04a_gasgiant_mission']},
            'allied_phantom_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['04a_gasgiant_mission']},
            'allies_elites': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'allies_elites_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'allies_elites_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'allies_grunts': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'allies_grunts_01': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders', 'ai_vehicle_exit'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'allies_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'alpha_gas_exterior': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'arm01_allies': {'category': 'object', 'funcs': ['ai_living_count', 'ai_set_orders', 'ai_suppress_combat'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'arm02_final_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'arm02_final_heretics': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bday_party': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_05/L1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_05/L2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_05/L3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_05/R1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_05/R2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_grunts_05/R3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_heretics': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'bottling_heretics_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_heretics_02': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_heretics_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_heretics_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_heretics_05': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['04a_gasgiant_mission']},
            'bottling_heretics_start': {'category': 'object', 'funcs': ['ai_migrate'], 'sources': ['04a_gasgiant_mission']},
            'bottling_sentinels': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'bottling_sentinels_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_sentinels_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_sentinels_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'bottling_sentinels_03/a': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['04a_gasgiant_mission']},
            'bottling_sentinels_03/b': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['04a_gasgiant_mission']},
            'brute_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'brute_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'chasers': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['04a_gasgiant_mission']},
            'commander': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'dervish': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'dervish02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'dog_flak_02': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_flak_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_flak_07': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_obj_emplaced_01': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'dog_obj_emplaced_02': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'dog_obj_emplaced_03': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'dog_obj_emplaced_04': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'dog_obj_emplaced_05': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'dog_obj_emplaced_06': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'dog_obj_emplaced_07': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'dog_sen_03': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_sen_05': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_sen_06': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turret_men_01': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turret_men_02': {'category': 'device', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turret_men_03': {'category': 'device', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turret_men_04': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turret_men_06': {'category': 'device', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turret_men_07': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turrets_01': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'dog_turrets_02': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turrets_03': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turrets_04': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turrets_06': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dog_turrets_07': {'category': 'device', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_enemies': {'category': 'object', 'funcs': ['ai_magically_see', 'ai_set_orders'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_enemies/pt_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_enemies/pt_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_enemies/pt_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_enemies/pt_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_enemies/pt_05': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_enemies/pt_06': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_enemies/pt_07': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_enemies/pt_08': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfight_initial_enemies': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'dogfighters_01': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'elev_hangar': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['04a_gasgiant_mission']},
            'elite01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'elite02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'elite03': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'elite04': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'elite05': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'elite06': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'elite07': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'energy_blade01': {'category': 'object', 'funcs': ['object_set_permutation'], 'sources': ['04a_gasgiant_cinematics']},
            'filthy_audio1': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'filthy_audio2': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'first_hall_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'first_hall_heretic_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'first_hall_heretic_02': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'first_hall_heretic_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'first_hall_heretics': {'category': 'object', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['04a_gasgiant_mission']},
            'gas01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'gas02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'gas03': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'gas04': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'gas05': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'gas06': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'gas07': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'gas08': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'gas09': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'gas10': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'grunt01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'grunt02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'grunt03': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'grunt04': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'hacker': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'hammer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'hang_01l': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'hang_01r': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'hang_02l': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'hang_02r': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'hang_03l': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'hang_03r': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_01l_high': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_01l_low': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_01r_high': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_01r_low': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_02l_high': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_02l_low': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_02r_high': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_02r_low': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_03l_high': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_03l_low': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_03r_high': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_a50_03r_low': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_door_cinematic': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'hangar_exit': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'hangar_grunts_01L': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_grunts_01R': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_grunts_04L': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_grunts_04R': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_grunts_end': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_helper_01': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_helper_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_helper_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_01L': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_01R': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_02L': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_02R': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_05': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_06C': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_06L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_06R': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_heavies_L/02a': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_heavies_L/02b': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_heavies_L/03a': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_heavies_L/03b': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_heavies_R/02a': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_heavies_R/02b': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_heavies_R/03a': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretic_heavies_R/03b': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretics': {'category': 'object', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['04a_gasgiant_mission']},
            'hangar_heretics_init': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['04a_gasgiant_mission']},
            'hangar_phantom': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_rein_her_01L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_rein_her_01R': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_rein_her_02L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_rein_her_02R': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_rein_her_03L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_rein_her_03R': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_sentinel_swarm': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_sentinels': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'hangar_sentinels_flit': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'hangar_sentinels_flit/c1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_sentinels_flit/c2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_sentinels_flit/l1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_sentinels_flit/l2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_sentinels_flit/r1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'hangar_sentinels_flit/r2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'help_can_01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'help_can_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_mission']},
            'heretic': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['04a_gasgiant_mission']},
            'heretic_leader_02': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'heretic_leader_03': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'heretic_leader_holo_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'hl_escort_sentinels': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'intro_elites': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place', 'ai_set_orders'], 'sources': ['04a_gasgiant_mission']},
            'intro_fleet': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'intro_phantom': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'jackal_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['04a_gasgiant_cinematics']},
            'jackal_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['04a_gasgiant_cinematics']},
            'jackal_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['04a_gasgiant_cinematics']},
            'jail_ledge': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'ledge_banshees_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'ledge_banshees_01/left': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'ledge_banshees_01/right': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'matte_structure_top': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'mercy': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'phantom01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_set_velocity'], 'sources': ['04a_gasgiant_cinematics']},
            'phantom02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_set_velocity'], 'sources': ['04a_gasgiant_cinematics']},
            'phantom03': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_set_velocity'], 'sources': ['04a_gasgiant_cinematics']},
            'phantom_01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'phantom_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'phantom_03': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'phantom_int': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['04a_gasgiant_cinematics']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['04a_gasgiant_mission']},
            'rec_cen_rein_grt_01L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_cen_rein_grt_01R': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_cen_rein_her_01L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_cen_rein_her_01R': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_entry_ext': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_entry_int': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_grunts_02L': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_grunts_02R': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_grunts_03': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_grunts_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_grunts_05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_grunts_06': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_grunts_07': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_heretic_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_heretic_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_heretic_03': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_heretic_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_heretic_05': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_heretic_06': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'rec_center_heretics': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04a_gasgiant_mission']},
            'reinforce_elites_01': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['04a_gasgiant_mission']},
            'reinforce_elites_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'reinforce_elites_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'reinforce_grunts_01': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['04a_gasgiant_mission']},
            'reinforce_grunts_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'reinforce_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'sarcophagus': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'second_hall_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_grunts_02/1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_grunts_02/2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_grunts_02/3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_grunts_02/4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_heretic_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_heretic_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_heretic_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_heretic_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_heretic_05': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_heretic_06': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'second_hall_heretics': {'category': 'object', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['04a_gasgiant_mission']},
            'sentinel': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['04a_gasgiant_mission']},
            'tartarus': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'throne_mercy': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04a_gasgiant_cinematics']},
            'throne_truth': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04a_gasgiant_cinematics']},
            'truth': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'underhangar_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'underhangar_grunts_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'underhangar_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'underhangar_heretic_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'underhangar_heretic_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'underhangar_heretics': {'category': 'object', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['04a_gasgiant_mission']},
            'underhangar_rein_her_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'underhangar_rein_her_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04a_gasgiant_mission']},
            'vol_04a_game_won': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_2nd_hall_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_2nd_hall_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_2nd_hall_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_arm02_air': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_arm_02_lz': {'category': 'object', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_bottling_back': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_bottling_back_top': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_bottling_enter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'vol_bottling_exit_l': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_bottling_exit_r': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_bottling_mid01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_bottling_mid02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_bottling_really_inside': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_bottling_reinforce': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_dog_obj_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_dog_obj_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_dog_obj_04': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_dog_obj_05': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_dog_obj_06': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_dog_obj_07': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_entering_facility': {'category': 'object', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_entry_landing': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_first_hall_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_grunt_bday': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_by_door': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_can_all': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_center': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_center_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_elev_left': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_elev_right': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_end_left': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_end_right': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_left': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_lift_top': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_mid_left': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_mid_right': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_reenter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_right': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_spawn_01L': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_spawn_01R': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_spawn_02L': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_spawn_02R': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_spawn_03L': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hangar_spawn_03R': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_hl_delete_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_leaving_hangar': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_leaving_lz': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_leaving_rec_center': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_on_banshee_ledge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_on_hangar_lift_top': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'vol_real_win': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_rec_slope_top': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_recycling_mid_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_recycling_mid_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_starting_locations': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_01': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_02': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_03': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_04': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_05': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_06': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_07': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_08': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_09': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_10': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_11': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_12': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_13': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_14': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_stuck_15': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04a_gasgiant_mission']},
            'vol_trigger_helpers': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_underhangar_can_all': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_underhangar_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_underhangar_from_bottom': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_underhangar_from_top': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission', '04a_gasgiant_teleport']},
            'vol_underhangar_halfway': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'vol_underhangar_reinforce': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04a_gasgiant_mission']},
            'x04_button': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
            'x04_door_01': {'category': 'device', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['04a_gasgiant_cinematics']},
        },
        "scripts": [('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_cinematics'), ('x04_score_01', 'dormant', '04a_gasgiant_cinematics'), ('x04_foley_01', 'dormant', '04a_gasgiant_cinematics'), ('x04_0010_bgr', 'dormant', '04a_gasgiant_cinematics'), ('x04_0020_bgl', 'dormant', '04a_gasgiant_cinematics'), ('x04_0040_jcr', 'dormant', '04a_gasgiant_cinematics'), ('x04_0030_bgl', 'dormant', '04a_gasgiant_cinematics'), ('x04_0050_bgr', 'dormant', '04a_gasgiant_cinematics'), ('x04_cinematic_lighting_scene_01', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_foley_02a', 'dormant', '04a_gasgiant_cinematics'), ('x04_0060_tar', 'dormant', '04a_gasgiant_cinematics'), ('x04_0070_tar', 'dormant', '04a_gasgiant_cinematics'), ('x04_0080_tar', 'dormant', '04a_gasgiant_cinematics'), ('x04_button_delete', 'dormant', '04a_gasgiant_cinematics'), ('x04_door_open', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_foley_2b', 'dormant', '04a_gasgiant_cinematics'), ('x04_02b_fov', 'dormant', '04a_gasgiant_cinematics'), ('x04_cinematic_lighting_02b', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_foley_03b', 'dormant', '04a_gasgiant_cinematics'), ('x04_03b_dof_1', 'dormant', '04a_gasgiant_cinematics'), ('x04_cinematic_lighting_03b', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_foley_04', 'dormant', '04a_gasgiant_cinematics'), ('x04_cinematic_lighting_scene_04', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_foley_05', 'dormant', '04a_gasgiant_cinematics'), ('x04_0090_tar', 'dormant', '04a_gasgiant_cinematics'), ('x04_0100_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0110_tar', 'dormant', '04a_gasgiant_cinematics'), ('x04_0120_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0130_tar', 'dormant', '04a_gasgiant_cinematics'), ('x04_0140_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0150_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_05_dof_1', 'dormant', '04a_gasgiant_cinematics'), ('x04_cinematic_lighting_scene_05', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_score_06', 'dormant', '04a_gasgiant_cinematics'), ('x04_foley_06', 'dormant', '04a_gasgiant_cinematics'), ('x04_0160_der', 'dormant', '04a_gasgiant_cinematics'), ('x04_0170_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0180_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0190_der', 'dormant', '04a_gasgiant_cinematics'), ('x04_0200_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0210_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0220_pom', 'dormant', '04a_gasgiant_cinematics'), ('x04_0230_der', 'dormant', '04a_gasgiant_cinematics'), ('x04_0240_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_06_dof_1', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_foley_07', 'dormant', '04a_gasgiant_cinematics'), ('x04_0250_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0260_hld', 'dormant', '04a_gasgiant_cinematics'), ('x04_0270_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0280_pom', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_score_08', 'dormant', '04a_gasgiant_cinematics'), ('x04_foley_08', 'dormant', '04a_gasgiant_cinematics'), ('x04_0290_der', 'dormant', '04a_gasgiant_cinematics'), ('x04_0300_pot', 'dormant', '04a_gasgiant_cinematics'), ('x04_0310_pot', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_foley_09', 'dormant', '04a_gasgiant_cinematics'), ('x04_0320_der', 'dormant', '04a_gasgiant_cinematics'), ('x04_0330_pom', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('x04_score_10', 'dormant', '04a_gasgiant_cinematics'), ('x04_foley_10', 'dormant', '04a_gasgiant_cinematics'), ('x04_0370_der', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene1_01', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_foley_01', 'dormant', '04a_gasgiant_cinematics'), ('c04_1010_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_1020_sec', 'dormant', '04a_gasgiant_cinematics'), ('c04_1030_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_cinematic_lighting_01', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene2a_01', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene2a_02', 'dormant', '04a_gasgiant_cinematics'), ('c04_1040_sec', 'dormant', '04a_gasgiant_cinematics'), ('c04_1050_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_1060_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_1070_sog', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_02a_fov', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_cinematic_light_02a', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('c04_1080_sec', 'dormant', '04a_gasgiant_cinematics'), ('c04_1090_soc', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene2c_01', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene2c_02', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_score_02c', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_foley_02c', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_cinematic_light_02c', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene2d_01', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_foley_02d', 'dormant', '04a_gasgiant_cinematics'), ('c04_1100_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_1110_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_1120_der', 'dormant', '04a_gasgiant_cinematics'), ('c04_1130_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_1140_der', 'dormant', '04a_gasgiant_cinematics'), ('c04_1150_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_cinematic_light_02d', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene3_01', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene3_02', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene3_03', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_foley_03', 'dormant', '04a_gasgiant_cinematics'), ('c04_1170_elp', 'dormant', '04a_gasgiant_cinematics'), ('c04_1180_ecp', 'dormant', '04a_gasgiant_cinematics'), ('c04_1190_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_cinematic_light_03', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_shake_03', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene5_01', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_05_shake_1', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene6b_01', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene6b_02', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene6b_03', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene6b_04', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene6b_05', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene6b_06', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_sound_scene6b_07', 'dormant', '04a_gasgiant_cinematics'), ('c04_1200_soc', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_06b_fov', 'dormant', '04a_gasgiant_cinematics'), ('c04_06b_shake_1', 'dormant', '04a_gasgiant_cinematics'), ('c04_intro_cinematic_light_06b', 'dormant', '04a_gasgiant_cinematics'), ('grunt_insertion', 'dormant', '04a_gasgiant_cinematics'), ('elite_insertion', 'dormant', '04a_gasgiant_cinematics'), ('dervish_insertion', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('elite_01_insertion', 'dormant', '04a_gasgiant_cinematics'), ('elite_02_insertion', 'dormant', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'static', '04a_gasgiant_cinematics'), ('void', 'stub', '04a_gasgiant_mission'), ('void', 'stub', '04a_gasgiant_mission'), ('active_camo_drop', 'continuous', '04a_gasgiant_mission'), ('abort', 'command_script', '04a_gasgiant_mission'), ('long_pause', 'command_script', '04a_gasgiant_mission'), ('forever_pause', 'command_script', '04a_gasgiant_mission'), ('snap_alert', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_01', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_02', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_03', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_04', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_05', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_06', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_07', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_08', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_09', 'command_script', '04a_gasgiant_mission'), ('stealth_comment_10', 'command_script', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('04a_title0', 'dormant', '04a_gasgiant_mission'), ('04a_title1', 'dormant', '04a_gasgiant_mission'), ('objective_hl_set', 'dormant', '04a_gasgiant_mission'), ('objective_hl_clear', 'dormant', '04a_gasgiant_mission'), ('objective_dogfight_set', 'dormant', '04a_gasgiant_mission'), ('objective_dogfight_clear', 'dormant', '04a_gasgiant_mission'), ('music_04a_01_start', 'dormant', '04a_gasgiant_mission'), ('music_04a_01_stop', 'dormant', '04a_gasgiant_mission'), ('music_04a_02_start', 'dormant', '04a_gasgiant_mission'), ('music_04a_02_stop', 'dormant', '04a_gasgiant_mission'), ('music_04a_03_start', 'dormant', '04a_gasgiant_mission'), ('music_04a_04_start', 'dormant', '04a_gasgiant_mission'), ('music_04a_04_stop', 'dormant', '04a_gasgiant_mission'), ('kill_volumes', 'dormant', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('wind', 'dormant', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('lz_phantom_01_away', 'command_script', '04a_gasgiant_mission'), ('lz_phantom_02_away', 'command_script', '04a_gasgiant_mission'), ('lz_phantom_03_away', 'command_script', '04a_gasgiant_mission'), ('commander_entry_reminder', 'dormant', '04a_gasgiant_mission'), ('commander_comment_03', 'dormant', '04a_gasgiant_mission'), ('lz_active_camo_call', 'command_script', '04a_gasgiant_mission'), ('inner_aim_elites', 'command_script', '04a_gasgiant_mission'), ('inner_aim_hacker', 'command_script', '04a_gasgiant_mission'), ('inner_aim_grunts', 'command_script', '04a_gasgiant_mission'), ('production_arm_bsp_swap', 'dormant', '04a_gasgiant_mission'), ('commander_comment_01', 'dormant', '04a_gasgiant_mission'), ('commander_comment_02', 'dormant', '04a_gasgiant_mission'), ('lz_phantom_leaves', 'command_script', '04a_gasgiant_mission'), ('landing_zone_follow_01', 'command_script', '04a_gasgiant_mission'), ('landing_zone_follow_02', 'command_script', '04a_gasgiant_mission'), ('SWAT_hack', 'command_script', '04a_gasgiant_mission'), ('SWAT_aim', 'command_script', '04a_gasgiant_mission'), ('SWAT_deploy', 'dormant', '04a_gasgiant_mission'), ('recycling_can_spawner', 'dormant', '04a_gasgiant_mission'), ('recycling_killer_new', 'dormant', '04a_gasgiant_mission'), ('heretic_chat', 'command_script', '04a_gasgiant_mission'), ('heretic_uplink_01', 'dormant', '04a_gasgiant_mission'), ('rec_center_reminder', 'dormant', '04a_gasgiant_mission'), ('get_on_e1', 'command_script', '04a_gasgiant_mission'), ('get_on_e2', 'command_script', '04a_gasgiant_mission'), ('get_on_g1', 'command_script', '04a_gasgiant_mission'), ('get_on_g2', 'command_script', '04a_gasgiant_mission'), ('rec_center_turret', 'command_script', '04a_gasgiant_mission'), ('recycling_center_start', 'dormant', '04a_gasgiant_mission'), ('hangar_extra_save', 'dormant', '04a_gasgiant_mission'), ('hangar_can_spawner', 'dormant', '04a_gasgiant_mission'), ('hangar_killer_new', 'dormant', '04a_gasgiant_mission'), ('hangar_help_01', 'command_script', '04a_gasgiant_mission'), ('hangar_help_02', 'command_script', '04a_gasgiant_mission'), ('hangar_help_03', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_out_l1', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_out_l2', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_out_r1', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_out_r2', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_out_c1', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_out_c2', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_l1', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_l2', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_r1', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_r2', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_c1', 'command_script', '04a_gasgiant_mission'), ('hangar_fly_c2', 'command_script', '04a_gasgiant_mission'), ('hangar_sentinels_flitting', 'dormant', '04a_gasgiant_mission'), ('hangar_sentinel_comment', 'command_script', '04a_gasgiant_mission'), ('hangar_helpers', 'dormant', '04a_gasgiant_mission'), ('hangar_phantom_arrives', 'command_script', '04a_gasgiant_mission'), ('hangar_allies_reinforce', 'dormant', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('hangar_door_monitor', 'dormant', '04a_gasgiant_mission'), ('hangar_objective', 'dormant', '04a_gasgiant_mission'), ('hangar_door_reminder', 'dormant', '04a_gasgiant_mission'), ('hangar_sentinel_call', 'command_script', '04a_gasgiant_mission'), ('hangar_alerted_call', 'dormant', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('hangar_exit_comment', 'command_script', '04a_gasgiant_mission'), ('hangar_exit_warn', 'dormant', '04a_gasgiant_mission'), ('hangar_reminder', 'dormant', '04a_gasgiant_mission'), ('hangar_exterior_toggle', 'dormant', '04a_gasgiant_mission'), ('deploy_hangar_right', 'command_script', '04a_gasgiant_mission'), ('deploy_hangar_left', 'command_script', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('hangar_firsttime_start', 'dormant', '04a_gasgiant_mission'), ('first_hall_reinforce', 'dormant', '04a_gasgiant_mission'), ('to_underhangar_firsttime', 'dormant', '04a_gasgiant_mission'), ('underhangar_can_spawner', 'dormant', '04a_gasgiant_mission'), ('underhangar_killer_new', 'dormant', '04a_gasgiant_mission'), ('new_allies_02', 'dormant', '04a_gasgiant_mission'), ('underhangar_reinforce', 'dormant', '04a_gasgiant_mission'), ('underhangar_comment', 'command_script', '04a_gasgiant_mission'), ('underhangar_reminder', 'dormant', '04a_gasgiant_mission'), ('underhangar_firsttime_start', 'dormant', '04a_gasgiant_mission'), ('second_hall_reinforce_01', 'dormant', '04a_gasgiant_mission'), ('second_hall_reinforce_02', 'dormant', '04a_gasgiant_mission'), ('second_hall_reinforce_03', 'dormant', '04a_gasgiant_mission'), ('to_bottling', 'dormant', '04a_gasgiant_mission'), ('bottling_can_spawner', 'dormant', '04a_gasgiant_mission'), ('bottling_killer_new', 'dormant', '04a_gasgiant_mission'), ('bottling_sentinel_call', 'command_script', '04a_gasgiant_mission'), ('new_allies_03', 'dormant', '04a_gasgiant_mission'), ('bottling_firsttime_start', 'dormant', '04a_gasgiant_mission'), ('hl_retreat_01', 'command_script', '04a_gasgiant_mission'), ('hl_retreat_backup', 'command_script', '04a_gasgiant_mission'), ('sentinel_wingmen_a', 'command_script', '04a_gasgiant_mission'), ('sentinel_wingmen_b', 'command_script', '04a_gasgiant_mission'), ('hl_retreat_02', 'command_script', '04a_gasgiant_mission'), ('hl_retreat_react', 'command_script', '04a_gasgiant_mission'), ('bottling_overlook_reinforce', 'dormant', '04a_gasgiant_mission'), ('phantom_to_ledge', 'command_script', '04a_gasgiant_mission'), ('bottling_elites_secure', 'command_script', '04a_gasgiant_mission'), ('bottling_grunts_secure', 'command_script', '04a_gasgiant_mission'), ('bottling_allies_secure', 'dormant', '04a_gasgiant_mission'), ('big_filth_toggle', 'dormant', '04a_gasgiant_mission'), ('bring_in_da_phantom', 'dormant', '04a_gasgiant_mission'), ('bottling_plant_end', 'dormant', '04a_gasgiant_mission'), ('partytime', 'command_script', '04a_gasgiant_mission'), ('grunt_birthday_party', 'dormant', '04a_gasgiant_mission'), ('banshee_stuck_spawner_01', 'dormant', '04a_gasgiant_mission'), ('banshee_stuck_spawner_02', 'dormant', '04a_gasgiant_mission'), ('phantom_path', 'command_script', '04a_gasgiant_mission'), ('arm02_SWAT_aim_00', 'command_script', '04a_gasgiant_mission'), ('arm02_SWAT_aim_01', 'command_script', '04a_gasgiant_mission'), ('arm02_SWAT_aim_02', 'command_script', '04a_gasgiant_mission'), ('arm02_SWAT_aim_03', 'command_script', '04a_gasgiant_mission'), ('arm02_final_approach', 'command_script', '04a_gasgiant_mission'), ('dogfight_search_reminder', 'dormant', '04a_gasgiant_mission'), ('dogfight_ph_pilot_talk', 'dormant', '04a_gasgiant_mission'), ('boost_test', 'command_script', '04a_gasgiant_mission'), ('banshee_fight_saving', 'dormant', '04a_gasgiant_mission'), ('phantom_path_w_orders', 'dormant', '04a_gasgiant_mission'), ('goto_dog_turret_01l', 'command_script', '04a_gasgiant_mission'), ('goto_dog_turret_01r', 'command_script', '04a_gasgiant_mission'), ('goto_dog_turret_02l', 'command_script', '04a_gasgiant_mission'), ('goto_dog_turret_02r', 'command_script', '04a_gasgiant_mission'), ('goto_dog_turret_03l', 'command_script', '04a_gasgiant_mission'), ('goto_dog_turret_03r', 'command_script', '04a_gasgiant_mission'), ('goto_dog_turret_04l', 'command_script', '04a_gasgiant_mission'), ('goto_dog_turret_04r', 'command_script', '04a_gasgiant_mission'), ('goto_dog_turret_06l', 'command_script', '04a_gasgiant_mission'), ('goto_dog_turret_06r', 'command_script', '04a_gasgiant_mission'), ('lz_turret_01', 'command_script', '04a_gasgiant_mission'), ('lz_turret_02', 'command_script', '04a_gasgiant_mission'), ('lz_turret_03', 'command_script', '04a_gasgiant_mission'), ('lz_turret_04', 'command_script', '04a_gasgiant_mission'), ('near_dog_obj_01', 'dormant', '04a_gasgiant_mission'), ('near_dog_obj_02', 'dormant', '04a_gasgiant_mission'), ('near_dog_obj_03', 'dormant', '04a_gasgiant_mission'), ('near_dog_obj_04', 'dormant', '04a_gasgiant_mission'), ('near_dog_obj_05', 'dormant', '04a_gasgiant_mission'), ('near_dog_obj_06', 'dormant', '04a_gasgiant_mission'), ('final_dogfight_reminder', 'dormant', '04a_gasgiant_mission'), ('ally_final_run', 'dormant', '04a_gasgiant_mission'), ('near_dog_obj_07', 'dormant', '04a_gasgiant_mission'), ('dogfight_flak_warn', 'dormant', '04a_gasgiant_mission'), ('dogfight_objectives', 'dormant', '04a_gasgiant_mission'), ('dogfight_nav_swap', 'dormant', '04a_gasgiant_mission'), ('always_get_banshee_01', 'dormant', '04a_gasgiant_mission'), ('always_get_banshee_02', 'dormant', '04a_gasgiant_mission'), ('dogfight_firsttime_start', 'dormant', '04a_gasgiant_mission'), ('arm_02_entry_win', 'dormant', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('void', 'static', '04a_gasgiant_mission'), ('mission', 'startup', '04a_gasgiant_mission'), ('x04_01_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_02a_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_02b_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_03b_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_04_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_05_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_06_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_07_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_08_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_09_predict', 'dormant', '04a_gasgiant_prediction'), ('x04_10_predict', 'dormant', '04a_gasgiant_prediction'), ('04_intro_01_predict', 'dormant', '04a_gasgiant_prediction'), ('04_intro_02a_predict', 'dormant', '04a_gasgiant_prediction'), ('04_intro_02b_predict', 'dormant', '04a_gasgiant_prediction'), ('04_intro_02c_predict', 'dormant', '04a_gasgiant_prediction'), ('04_intro_02d_predict', 'dormant', '04a_gasgiant_prediction'), ('04_intro_03_predict', 'dormant', '04a_gasgiant_prediction'), ('04_intro_05_predict', 'dormant', '04a_gasgiant_prediction'), ('04_intro_06b_predict', 'dormant', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_prediction'), ('void', 'static', '04a_gasgiant_teleport'), ('void', 'static', '04a_gasgiant_teleport'), ('void', 'static', '04a_gasgiant_teleport'), ('void', 'static', '04a_gasgiant_teleport'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/04b_floodlab/04b_floodlab': {
        "objects": {
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['04b_floodlab_mission']},
            'all_allies': {'category': 'object', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'all_enemies': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['04b_floodlab_mission']},
            'allied_phantom_02': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'allied_phantom_03': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'allies_elites': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count', 'ai_migrate'], 'sources': ['04b_floodlab_mission']},
            'allies_elites_03a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'allies_elites_03b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'allies_elites_04': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'allies_grunts_03': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'allies_grunts_04': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'arm02_allies': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'arm_02_entry_ext': {'category': 'object', 'funcs': ['device_set_position', 'device_set_power'], 'sources': ['04b_floodlab_cinematics']},
            'bait_bottling_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bait_bottling_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bait_hall_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bait_hall_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bait_hall_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'boss_fight_combatforms': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'boss_fight_heretic_leader': {'category': 'object', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'boss_fight_hl_hologram_01': {'category': 'object', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'boss_fight_hl_hologram_02': {'category': 'object', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'boss_fight_sentinels': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_plant_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_carriers_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_carriers_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_carriers_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_combatforms_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_combatforms_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_combatforms_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_flood_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_sentinels_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_sentinels_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bottling_return_sentinels_03': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_carriers': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_combatforms': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_h_grunts_L_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_h_grunts_R_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_h_grunts_final': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_h_grunts_init': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_heretics_L_02': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_heretics_L_04': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_heretics_R_02': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_heretics_R_04': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_heretics_final': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_infection': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_runners': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_sentinels_L_05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_sentinels_R_05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'bridge_strafer': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'cable_flood': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'cable_room_combatforms': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'cable_room_sentinels': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'cable_sentinels': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'cableroom': {'category': 'object', 'funcs': ['device_get_position', 'object_destroy'], 'sources': ['04b_floodlab_mission']},
            'cableroom2': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'cableroom_flood_init': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'cableroom_sentinels_init': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'cableroom_top': {'category': 'object', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['04b_floodlab_mission']},
            'cap_01_1': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_10': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_11': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_12': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_2': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_3': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_4': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_5': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_6': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_7': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_8': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_01_9': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_1': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_10': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_11': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_2': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_3': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_4': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_5': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_6': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_7': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_8': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_02_9': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_03_1': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_03_2': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_03_3': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_03_4': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_03_5': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_03_6': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_03_7': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_03_8': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_1': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_10': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_11': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_12': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_2': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_3': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_4': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_5': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_6': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_7': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_8': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'cap_04_9': {'category': 'object', 'funcs': ['object_cannot_take_damage'], 'sources': ['04b_floodlab_mission']},
            'commander': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'commander_intra0': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'control_bottom_spawnroom': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'control_commander_cinematic': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_down_switch_01': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['04b_floodlab_mission']},
            'control_down_switch_02': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['04b_floodlab_mission']},
            'control_elites_cinematic': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_entry_int': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'control_flood_wave_01_combat': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_flood_wave_02_carriers': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_flood_wave_02_combat': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_flood_wave_03_carriers': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_flood_wave_03_combat': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_infection': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_middle_spawnroom': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'control_peri_spawnroom': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_02/mid01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_02/mid02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_02/peri01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_02/peri02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_03/bott01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_03/bott02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_03/peri01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_03/peri02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_04/bott01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_04/bott02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_04/entry01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_carriers_04/entry02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_02/mid01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_02/mid02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_02/mid03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_02/mid04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_02/peri01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_02/peri02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_02/peri03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_02/peri04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_03/bott01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_03/bott02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_03/bott03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_03/bott04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_03/peri01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_03/peri02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_03/peri03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_03/peri04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_04/bott01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_04/bott02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_04/bott03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_04/bott04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_04/entry01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_04/entry02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_04/entry03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_flood_04/entry04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_h_grunts_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_h_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_heretics': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04b_floodlab_mission']},
            'control_return_heretics_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_heretics_02': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_heretics_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_return_sentinels_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_sentinels_wave_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_sentinels_wave_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'control_shield_door': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['04b_floodlab_cinematics']},
            'control_up_switch_01': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'control_up_switch_02': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'core_allies': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'dervish02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'dervish02b': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'dervish_01': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'dervish_02': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'dervish_03': {'category': 'object', 'funcs': ['ai_erase', 'ai_place', 'object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics', '04b_floodlab_mission']},
            'dervish_intra0': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'disposal_commander': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'disposal_entry_flood': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'disposal_entry_heretics': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'disposal_entry_int': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['04b_floodlab_mission']},
            'disposal_entry_juggernaut': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'disposal_infection_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'disposal_infection_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'dogfighters': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04b_floodlab_mission']},
            'dogfighters_finale/1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'dogfighters_finale/2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'dogfighters_finale/3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'dogfighters_finale/4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'dogfighters_finale/5': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'dogfighters_finale/6': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'dogfighters_init': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'dummy_can': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'eb_intra0_soc': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_set_permutation'], 'sources': ['04b_floodlab_cinematics']},
            'elev_control_up': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['04b_floodlab_mission']},
            'elev_silo': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'elite01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'elite02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'elite_intra0_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'elite_intra0_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'famine_cf': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'gas01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gas02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gas03': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gas04': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gas05': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gas06': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gas07': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gas08': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gas09': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gas10': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'gasmine_hologram': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'grunt_intra0_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'grunt_intra0_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'hall2_spawn_01': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'hall2_spawn_02': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'hall2_spawn_03': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'hammer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'hangar_door_cinematic': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['04b_floodlab_cinematics']},
            'hangar_door_ingame': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'heretic': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['04b_floodlab_mission']},
            'heretic_leader': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics', '04b_floodlab_mission']},
            'heretic_leader_04': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'heretic_leader_control': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'heretic_leader_hangar': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'hl_boss_holo_random_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'hl_boss_holo_random_02': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'hl_boss_holo_random_03': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'hl_boss_holo_random_04': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'hl_boss_random': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'hl_fake_banshee': {'category': 'object', 'funcs': ['object_cannot_take_damage', 'object_destroy'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'hl_hologram': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'hl_ledge_ext': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['04b_floodlab_mission']},
            'hl_rifle_01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'hl_rifle_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'holo1': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'holo2': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'holo3': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'holo4': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'holo_boy': {'category': 'object', 'funcs': ['object_cannot_take_damage', 'object_destroy', 'object_get_shield', 'object_set_shield'], 'sources': ['04b_floodlab_mission']},
            'holo_drone': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'holo_drone_1': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'holo_drone_2': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'holo_drones': {'category': 'object', 'funcs': ['ai_kill', 'ai_living_count'], 'sources': ['04b_floodlab_mission']},
            'hologram01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'hologram02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'intra1_blade': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'intra1_rifle_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'intra1_rifle_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'lab_carriers_01': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/5': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/6': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/init1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/init2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/init3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_01/init4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_02/r1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_02/r2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_02/r3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_02/r4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_carriers_02/r5': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_combatforms_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_combatforms_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_combatforms_02/r1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_combatforms_02/r2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_combatforms_02/r3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_combatforms_02/r4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_combatforms_02/r5': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_exit_int': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'lab_exit_turrets': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_flood': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'lab_grunts_02': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_enter'], 'sources': ['04b_floodlab_mission']},
            'lab_heretics': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04b_floodlab_mission']},
            'lab_heretics_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders', 'ai_strength'], 'sources': ['04b_floodlab_mission']},
            'lab_heretics_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_heretics_above': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'lab_infection_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'lab_juggernaut_above': {'category': 'object', 'funcs': ['ai_living_count', 'ai_strength'], 'sources': ['04b_floodlab_mission']},
            'lab_turret_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'ledge_banshees_02/left': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'ledge_banshees_02/right': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'monitor': {'category': 'object', 'funcs': ['ai_erase', 'ai_place', 'object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics', '04b_floodlab_mission']},
            'phantom_outro2': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'phantom_vol': {'category': 'volume', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['04b_floodlab_mission']},
            'player0_fake_banshee': {'category': 'object', 'funcs': ['object_cannot_take_damage', 'object_destroy'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'player1_fake_banshee': {'category': 'object', 'funcs': ['object_cannot_take_damage', 'object_destroy'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'power_core_carriers': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'power_core_combatforms': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'power_core_h_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'power_core_heretics': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04b_floodlab_mission']},
            'power_core_heretics_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'power_core_sentinels_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'power_core_swords': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'pp_intra0_sog_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'pp_intra0_sog_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'pr_intra0_der': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'pr_intra0_soe_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'pr_intra0_soe_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'pr_intra0_soe_03': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['04b_floodlab_cinematics']},
            'real_cable_a': {'category': 'object', 'funcs': ['device_set_position', 'object_can_take_damage', 'object_cannot_take_damage', 'object_get_health'], 'sources': ['04b_floodlab_mission']},
            'real_cable_b': {'category': 'object', 'funcs': ['device_set_position', 'object_can_take_damage', 'object_cannot_take_damage', 'object_get_health'], 'sources': ['04b_floodlab_mission']},
            'real_cable_c': {'category': 'object', 'funcs': ['device_set_position', 'object_can_take_damage', 'object_cannot_take_damage', 'object_get_health'], 'sources': ['04b_floodlab_mission']},
            'second_hall_carriers': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'second_hall_flood_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'second_hall_flood_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'second_hall_flood_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'second_hall_infection_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'second_hall_infection_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'sentinel': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['04b_floodlab_mission']},
            'seraph': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'silo_climbers_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_climbers_02': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_flood': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['04b_floodlab_mission']},
            'silo_flood_halls': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_flood_initial': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_heretics': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_sentinels_all': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['04b_floodlab_mission']},
            'silo_sentinels_below': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_sentinels_initial': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_sentinels_resupply/1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_sentinels_resupply/2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_sentinels_resupply/5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'silo_sentinels_resupply/6': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'stop_01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'stop_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'stop_03': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'stop_04': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'stop_05': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'stop_06': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['04b_floodlab_mission']},
            'tartarus': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['04b_floodlab_cinematics']},
            'tennis_ball': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['04b_floodlab_mission']},
            'trans_3': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04b_floodlab_mission']},
            'tray01': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['04b_floodlab_mission']},
            'tray02': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['04b_floodlab_mission']},
            'tray03': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['04b_floodlab_mission']},
            'tray04': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['04b_floodlab_mission']},
            'tray05': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['04b_floodlab_mission']},
            'tray06': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['04b_floodlab_mission']},
            'underhangar_carriers_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_carriers_init': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_combatforms_init': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_h_grunts_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_h_grunts_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_h_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_heretics_01': {'category': 'object', 'funcs': ['ai_place', 'ai_strength'], 'sources': ['04b_floodlab_mission']},
            'underhangar_heretics_02': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_heretics_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_return_flood_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_return_flood_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_return_flood_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_return_flood_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['04b_floodlab_mission']},
            'underhangar_return_heretics': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['04b_floodlab_mission']},
            'underhangar_spawn_01': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'underhangar_spawn_02': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['04b_floodlab_mission']},
            'vol_2nd_hall_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_2nd_hall_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_arm_01_return': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission', '04b_floodlab_teleport']},
            'vol_arm_02_lz': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_boss_delete_L': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_boss_delete_R': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_boss_delete_c1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_boss_delete_c2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_bottling_enter': {'category': 'object', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_bottling_mid02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_bottling_mid03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_bottling_return_01r': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_bottling_return_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_cableroom_pit_01': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04b_floodlab_mission']},
            'vol_cableroom_pit_02': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04b_floodlab_mission']},
            'vol_cableroom_pit_03': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04b_floodlab_mission']},
            'vol_control_bottom_spawnroom': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_enter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_entry_int': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_middle': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_middle_spawnroom': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_peri_spawnroom': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_perimeter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_return': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_return_middle': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_return_perimeter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_control_top': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_croom_kill_new': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04b_floodlab_mission']},
            'vol_croom_kill_new_too': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04b_floodlab_mission']},
            'vol_disposal_enter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_famine_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_famine_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_going_down': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_gusty': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_hall2_spawn_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_hall2_spawn_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_hall2_spawn_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_hall_to_lab': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_hangar_cutscene_start': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_hangar_reenter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_hl_killer': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['04b_floodlab_mission']},
            'vol_juggernaut_preview': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_lab_enter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_lab_floor': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_leaving_silo': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_near_shield': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_on_bridge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_plummet_fl': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_plummet_fr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_plummet_nl': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_plummet_nr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_power_core_bottom': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_power_core_enter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_power_core_ledge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_power_core_midway': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_silo_enter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_soc_post': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_soc_reborn': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_underhangar_from_bottom': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_underhangar_from_top': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_underhangar_music': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_underhangar_return_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_underhangar_return_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_underhangar_shaft_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_underhangar_shaft_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_underhangar_spawn_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_underhangar_spawn_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_wrap_final': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_wrap_left_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_wrap_left_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_wrap_left_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_wrap_right_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_wrap_right_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
            'vol_wrap_right_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['04b_floodlab_mission']},
        },
        "scripts": [('void', 'stub', '04b_floodlab_cinematics'), ('void', 'stub', '04b_floodlab_cinematics'), ('void', 'stub', '04b_floodlab_cinematics'), ('void', 'stub', '04b_floodlab_cinematics'), ('void', 'stub', '04b_floodlab_cinematics'), ('void', 'stub', '04b_floodlab_cinematics'), ('void', 'stub', '04b_floodlab_cinematics'), ('void', 'stub', '04b_floodlab_cinematics'), ('c04_intra0_score_01', 'dormant', '04b_floodlab_cinematics'), ('c04_intra0_foley_01', 'dormant', '04b_floodlab_cinematics'), ('c04_1230_der', 'dormant', '04b_floodlab_cinematics'), ('c04_1240_soc', 'dormant', '04b_floodlab_cinematics'), ('c04_intra0_cinematic_light_01', 'dormant', '04b_floodlab_cinematics'), ('soc_blade_activate', 'dormant', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('c04_intra1_foley_01', 'dormant', '04b_floodlab_cinematics'), ('c04_2010_her', 'dormant', '04b_floodlab_cinematics'), ('c04_2020_her', 'dormant', '04b_floodlab_cinematics'), ('c04_2030_soc', 'dormant', '04b_floodlab_cinematics'), ('scale_hologram', 'dormant', '04b_floodlab_cinematics'), ('effect_shield_impact', 'dormant', '04b_floodlab_cinematics'), ('c04_intra1_cinematic_light_01', 'dormant', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('c04_intra1_foley_02', 'dormant', '04b_floodlab_cinematics'), ('c04_2031_soc', 'dormant', '04b_floodlab_cinematics'), ('c04_2040_soc', 'dormant', '04b_floodlab_cinematics'), ('c04_2050_soc', 'dormant', '04b_floodlab_cinematics'), ('c04_2060_der', 'dormant', '04b_floodlab_cinematics'), ('c04_2070_soc', 'dormant', '04b_floodlab_cinematics'), ('c04_2080_der', 'dormant', '04b_floodlab_cinematics'), ('c04_2090_der', 'dormant', '04b_floodlab_cinematics'), ('c04_intra1_cinematic_light_02', 'dormant', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('c04_outro1_score_01', 'dormant', '04b_floodlab_cinematics'), ('c04_outro1_foley_01', 'dormant', '04b_floodlab_cinematics'), ('c04_3010_der', 'dormant', '04b_floodlab_cinematics'), ('c04_3020_her', 'dormant', '04b_floodlab_cinematics'), ('c04_3030_her', 'dormant', '04b_floodlab_cinematics'), ('c04_3040_der', 'dormant', '04b_floodlab_cinematics'), ('c04_outro1_01_dof', 'dormant', '04b_floodlab_cinematics'), ('c04_outro1_cinematic_light_01', 'dormant', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('c04_outro1_foley_02', 'dormant', '04b_floodlab_cinematics'), ('c04_3050_der', 'dormant', '04b_floodlab_cinematics'), ('c04_3060_gsp', 'dormant', '04b_floodlab_cinematics'), ('c04_3070_her', 'dormant', '04b_floodlab_cinematics'), ('c04_3080_gsp', 'dormant', '04b_floodlab_cinematics'), ('c04_outro1_cinematic_light_02', 'dormant', '04b_floodlab_cinematics'), ('heretic_leader_fire_rifles', 'dormant', '04b_floodlab_cinematics'), ('effect_jetpack', 'dormant', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('c04_outro1_foley_03', 'dormant', '04b_floodlab_cinematics'), ('c04_3090_her', 'dormant', '04b_floodlab_cinematics'), ('c04_3100_her', 'dormant', '04b_floodlab_cinematics'), ('effect_drone_activate', 'dormant', '04b_floodlab_cinematics'), ('effect_holograms_appear', 'dormant', '04b_floodlab_cinematics'), ('arm_holograms', 'dormant', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('c04_outro1_03_holo1', 'dormant', '04b_floodlab_cinematics'), ('c04_outro1_03_holo2', 'dormant', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('c04_outro2_score_01', 'dormant', '04b_floodlab_cinematics'), ('c04_outro2_foley_01', 'dormant', '04b_floodlab_cinematics'), ('c04_9110_gsp', 'dormant', '04b_floodlab_cinematics'), ('c04_9120_der', 'dormant', '04b_floodlab_cinematics'), ('c04_9130_gsp', 'dormant', '04b_floodlab_cinematics'), ('effect_monitor_scramble', 'dormant', '04b_floodlab_cinematics'), ('c04_outro2_cinematic_light_01', 'dormant', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('c04_outro2_foley_02', 'dormant', '04b_floodlab_cinematics'), ('c04_9140_gsp', 'dormant', '04b_floodlab_cinematics'), ('c04_9150_der', 'dormant', '04b_floodlab_cinematics'), ('c04_9160_tar', 'dormant', '04b_floodlab_cinematics'), ('c04_9170_tar', 'dormant', '04b_floodlab_cinematics'), ('effect_monitor_yank', 'dormant', '04b_floodlab_cinematics'), ('c04_outro2_cinematic_light_02', 'dormant', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'static', '04b_floodlab_cinematics'), ('void', 'stub', '04b_floodlab_mission'), ('void', 'stub', '04b_floodlab_mission'), ('void', 'stub', '04b_floodlab_mission'), ('void', 'stub', '04b_floodlab_mission'), ('abort', 'command_script', '04b_floodlab_mission'), ('long_pause', 'command_script', '04b_floodlab_mission'), ('forever_pause', 'command_script', '04b_floodlab_mission'), ('04b_title0', 'dormant', '04b_floodlab_mission'), ('04b_title1', 'dormant', '04b_floodlab_mission'), ('04b_title2', 'dormant', '04b_floodlab_mission'), ('objective_labs_set', 'dormant', '04b_floodlab_mission'), ('objective_labs_clear', 'dormant', '04b_floodlab_mission'), ('objective_control_set', 'dormant', '04b_floodlab_mission'), ('objective_control_clear', 'dormant', '04b_floodlab_mission'), ('objective_cables_set', 'dormant', '04b_floodlab_mission'), ('objective_cables_clear', 'dormant', '04b_floodlab_mission'), ('objective_dogfight_set', 'dormant', '04b_floodlab_mission'), ('objective_dogfight_clear', 'dormant', '04b_floodlab_mission'), ('objective_hl_set', 'dormant', '04b_floodlab_mission'), ('objective_hl_clear', 'dormant', '04b_floodlab_mission'), ('music_04b_01_start', 'dormant', '04b_floodlab_mission'), ('music_04b_01_stop', 'dormant', '04b_floodlab_mission'), ('music_04b_02_start', 'dormant', '04b_floodlab_mission'), ('music_04b_02_stop', 'dormant', '04b_floodlab_mission'), ('music_04b_03_start', 'dormant', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('music_04b_03_stop', 'dormant', '04b_floodlab_mission'), ('music_04b_04_start', 'dormant', '04b_floodlab_mission'), ('music_04b_04_start_alt', 'dormant', '04b_floodlab_mission'), ('music_04b_04_stop_alt', 'dormant', '04b_floodlab_mission'), ('music_04b_04_stop', 'dormant', '04b_floodlab_mission'), ('music_04b_05_start', 'dormant', '04b_floodlab_mission'), ('music_04b_06_start', 'dormant', '04b_floodlab_mission'), ('music_04b_07_start', 'dormant', '04b_floodlab_mission'), ('music_04b_08_start', 'dormant', '04b_floodlab_mission'), ('music_04b_08_start_alt', 'dormant', '04b_floodlab_mission'), ('music_04b_08_stop', 'dormant', '04b_floodlab_mission'), ('kill_volumes', 'dormant', '04b_floodlab_mission'), ('cableroom_killer', 'dormant', '04b_floodlab_mission'), ('cableroom_junk_killer', 'dormant', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('juggernaut_gosh', 'command_script', '04b_floodlab_mission'), ('juggernaut_whew', 'command_script', '04b_floodlab_mission'), ('disposal_juggernaut_exit', 'command_script', '04b_floodlab_mission'), ('arm_02_entry_start', 'dormant', '04b_floodlab_mission'), ('juggernaut_abort', 'dormant', '04b_floodlab_mission'), ('holo_drone_arrives', 'command_script', '04b_floodlab_mission'), ('disposal_ally_comment_01', 'command_script', '04b_floodlab_mission'), ('disposal_ally_comment_02', 'command_script', '04b_floodlab_mission'), ('hologram_face', 'command_script', '04b_floodlab_mission'), ('hologram_ally_01', 'command_script', '04b_floodlab_mission'), ('hologram_ally_02', 'command_script', '04b_floodlab_mission'), ('hologram_ally_03', 'command_script', '04b_floodlab_mission'), ('hologram_ally_04', 'command_script', '04b_floodlab_mission'), ('revive_aware', 'dormant', '04b_floodlab_mission'), ('disposal_after_react', 'command_script', '04b_floodlab_mission'), ('disposal_after_commander', 'command_script', '04b_floodlab_mission'), ('spec_ops_reborn', 'dormant', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('holo_cannot_die', 'dormant', '04b_floodlab_mission'), ('disposal_chamber_start', 'dormant', '04b_floodlab_mission'), ('silo_ally_comment', 'command_script', '04b_floodlab_mission'), ('silo_commander_whine', 'command_script', '04b_floodlab_mission'), ('silo_commander_reminder', 'dormant', '04b_floodlab_mission'), ('silo_killer', 'dormant', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('silo_covers_invincible', 'dormant', '04b_floodlab_mission'), ('silo_sentinel_spawner', 'dormant', '04b_floodlab_mission'), ('silo_saving', 'dormant', '04b_floodlab_mission'), ('silo_flood_spawner', 'dormant', '04b_floodlab_mission'), ('elev_go', 'dormant', '04b_floodlab_mission'), ('silo_hall_flood_spawner', 'dormant', '04b_floodlab_mission'), ('silo_start', 'dormant', '04b_floodlab_mission'), ('halls2lab_ally_comment', 'command_script', '04b_floodlab_mission'), ('to_flood_lab', 'dormant', '04b_floodlab_mission'), ('famine_flavor', 'dormant', '04b_floodlab_mission'), ('airlock_commander', 'command_script', '04b_floodlab_mission'), ('airlock_commander_talk', 'dormant', '04b_floodlab_mission'), ('research_arm_bsp_swap', 'dormant', '04b_floodlab_mission'), ('lab_barricades', 'dormant', '04b_floodlab_mission'), ('lab_heretics_ally', 'command_script', '04b_floodlab_mission'), ('lab_heretics_commander', 'command_script', '04b_floodlab_mission'), ('lab_juggernaut_ally', 'command_script', '04b_floodlab_mission'), ('lab_juggernaut_commander', 'command_script', '04b_floodlab_mission'), ('lab_jugg_hint1_ally', 'command_script', '04b_floodlab_mission'), ('lab_jugg_hint1_commander', 'command_script', '04b_floodlab_mission'), ('lab_jugg_hint2_ally', 'command_script', '04b_floodlab_mission'), ('lab_jugg_hint2_commander', 'command_script', '04b_floodlab_mission'), ('stay_shootin', 'command_script', '04b_floodlab_mission'), ('lab_turret_man_R', 'command_script', '04b_floodlab_mission'), ('lab_turret_man_L', 'command_script', '04b_floodlab_mission'), ('fuck_this_turret_shit', 'dormant', '04b_floodlab_mission'), ('lab_wave_new_01', 'dormant', '04b_floodlab_mission'), ('lab_wave_new_02', 'dormant', '04b_floodlab_mission'), ('flood_lab_start', 'dormant', '04b_floodlab_mission'), ('wind', 'dormant', '04b_floodlab_mission'), ('bridge_phantom_arrives', 'command_script', '04b_floodlab_mission'), ('bridge_phantom_go', 'dormant', '04b_floodlab_mission'), ('bridge_commander_comment', 'command_script', '04b_floodlab_mission'), ('bridge_commander_reminder', 'command_script', '04b_floodlab_mission'), ('bridge_reminder', 'dormant', '04b_floodlab_mission'), ('wraparound_right', 'dormant', '04b_floodlab_mission'), ('wraparound_left', 'dormant', '04b_floodlab_mission'), ('bridge_start', 'dormant', '04b_floodlab_mission'), ('hl_killer', 'dormant', '04b_floodlab_mission'), ('hologram_toggle', 'dormant', '04b_floodlab_mission'), ('control_commander_reminder', 'dormant', '04b_floodlab_mission'), ('control_grunt_comment', 'command_script', '04b_floodlab_mission'), ('control_elite_comment', 'command_script', '04b_floodlab_mission'), ('heretic_leader_holes_up', 'command_script', '04b_floodlab_mission'), ('sog_bug_out_01', 'command_script', '04b_floodlab_mission'), ('sog_bug_out_02', 'command_script', '04b_floodlab_mission'), ('sog_bug_out_03', 'command_script', '04b_floodlab_mission'), ('sog_bug_out_04', 'command_script', '04b_floodlab_mission'), ('commander_farewell', 'command_script', '04b_floodlab_mission'), ('spec_op_farewell', 'command_script', '04b_floodlab_mission'), ('soe_bug_out_01', 'command_script', '04b_floodlab_mission'), ('soe_bug_out_02', 'command_script', '04b_floodlab_mission'), ('control_bug_out_flight', 'command_script', '04b_floodlab_mission'), ('bug_out_pussy', 'command_script', '04b_floodlab_mission'), ('control_bug_out', 'dormant', '04b_floodlab_mission'), ('control_flood_spawn', 'dormant', '04b_floodlab_mission'), ('control_room_start', 'dormant', '04b_floodlab_mission'), ('strain', 'dormant', '04b_floodlab_mission'), ('rip', 'dormant', '04b_floodlab_mission'), ('try_to_fix', 'command_script', '04b_floodlab_mission'), ('grav_test', 'dormant', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('cam_shake_cont', 'dormant', '04b_floodlab_mission'), ('cable_invulnerable', 'dormant', '04b_floodlab_mission'), ('cableroom_suck_killer', 'dormant', '04b_floodlab_mission'), ('cableroom_junk_spawn', 'dormant', '04b_floodlab_mission'), ('cable_nav_a', 'dormant', '04b_floodlab_mission'), ('cable_nav_b', 'dormant', '04b_floodlab_mission'), ('cable_nav_c', 'dormant', '04b_floodlab_mission'), ('cableroom_commander_reminder', 'dormant', '04b_floodlab_mission'), ('cable_look', 'command_script', '04b_floodlab_mission'), ('cable_a_health', 'dormant', '04b_floodlab_mission'), ('cable_b_health', 'dormant', '04b_floodlab_mission'), ('cable_c_health', 'dormant', '04b_floodlab_mission'), ('cable_flood_spawner', 'dormant', '04b_floodlab_mission'), ('cable_sentinel_spawner', 'dormant', '04b_floodlab_mission'), ('croom_exit', 'dormant', '04b_floodlab_mission'), ('cable_room_start', 'dormant', '04b_floodlab_mission'), ('plummeting_control_commander', 'dormant', '04b_floodlab_mission'), ('control_return_flood_spawn', 'dormant', '04b_floodlab_mission'), ('control_return_heretic', 'command_script', '04b_floodlab_mission'), ('control_room_return', 'dormant', '04b_floodlab_mission'), ('power_core_heretic', 'command_script', '04b_floodlab_mission'), ('power_core_commander', 'dormant', '04b_floodlab_mission'), ('hl_retreat_x', 'command_script', '04b_floodlab_mission'), ('power_core_start', 'dormant', '04b_floodlab_mission'), ('plummet_killer', 'dormant', '04b_floodlab_mission'), ('plummet_fl', 'dormant', '04b_floodlab_mission'), ('plummet_fr', 'dormant', '04b_floodlab_mission'), ('plummet_nr', 'dormant', '04b_floodlab_mission'), ('plummet_nl', 'dormant', '04b_floodlab_mission'), ('banshee_killer_00', 'dormant', '04b_floodlab_mission'), ('banshee_killer_01', 'dormant', '04b_floodlab_mission'), ('dervish_chase_01', 'command_script', '04b_floodlab_mission'), ('hl_retreat_04', 'command_script', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('dogfight2_commander', 'dormant', '04b_floodlab_mission'), ('boost_test', 'command_script', '04b_floodlab_mission'), ('dogfight_secondtime_start', 'dormant', '04b_floodlab_mission'), ('dervish_chase_02', 'command_script', '04b_floodlab_mission'), ('dervish_recovery', 'command_script', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('bottling_return_s_respawner', 'dormant', '04b_floodlab_mission'), ('bottling_return_cf_respawner', 'dormant', '04b_floodlab_mission'), ('bottling_return_ca_respawner', 'dormant', '04b_floodlab_mission'), ('bottling_return_commander', 'dormant', '04b_floodlab_mission'), ('bottling_fx_01', 'dormant', '04b_floodlab_mission'), ('bottling_fx_02', 'dormant', '04b_floodlab_mission'), ('bottling_fx_03', 'dormant', '04b_floodlab_mission'), ('bottling_fx_04', 'dormant', '04b_floodlab_mission'), ('bottling_fx_05', 'dormant', '04b_floodlab_mission'), ('panic_bottling', 'command_script', '04b_floodlab_mission'), ('bottling_secondtime_start', 'dormant', '04b_floodlab_mission'), ('halls_up_01', 'dormant', '04b_floodlab_mission'), ('halls_up_02', 'dormant', '04b_floodlab_mission'), ('halls_up_03', 'dormant', '04b_floodlab_mission'), ('halls_up_04', 'dormant', '04b_floodlab_mission'), ('halls_up_05', 'dormant', '04b_floodlab_mission'), ('halls_up_06', 'dormant', '04b_floodlab_mission'), ('halls_up_07', 'dormant', '04b_floodlab_mission'), ('panic_halls', 'command_script', '04b_floodlab_mission'), ('to_underhangar_secondtime', 'dormant', '04b_floodlab_mission'), ('underhangar_fx_01', 'dormant', '04b_floodlab_mission'), ('underhangar_fx_02', 'dormant', '04b_floodlab_mission'), ('underhangar_return_commander', 'dormant', '04b_floodlab_mission'), ('underhangar_secondtime_start', 'dormant', '04b_floodlab_mission'), ('other_hall_fx', 'dormant', '04b_floodlab_mission'), ('to_hangar_secondtime', 'dormant', '04b_floodlab_mission'), ('hangar_fx', 'dormant', '04b_floodlab_mission'), ('hack', 'command_script', '04b_floodlab_mission'), ('hl_boss_chat_01', 'command_script', '04b_floodlab_mission'), ('hl_boss_chat_02', 'command_script', '04b_floodlab_mission'), ('hl_boss_chat_03', 'command_script', '04b_floodlab_mission'), ('monitor_chat_01', 'command_script', '04b_floodlab_mission'), ('monitor_chat_02', 'command_script', '04b_floodlab_mission'), ('monitor_chat_03', 'command_script', '04b_floodlab_mission'), ('monitor_chatting', 'dormant', '04b_floodlab_mission'), ('monitor_flit_01', 'command_script', '04b_floodlab_mission'), ('monitor_flit_02', 'command_script', '04b_floodlab_mission'), ('monitor_flit_03', 'command_script', '04b_floodlab_mission'), ('monitor_flit_04', 'command_script', '04b_floodlab_mission'), ('monitor_flit_05', 'command_script', '04b_floodlab_mission'), ('monitor_flit_06', 'command_script', '04b_floodlab_mission'), ('monitor_flit_07', 'command_script', '04b_floodlab_mission'), ('monitor_flit_08', 'command_script', '04b_floodlab_mission'), ('monitor_flit_09', 'command_script', '04b_floodlab_mission'), ('monitor_flit_10', 'command_script', '04b_floodlab_mission'), ('monitor_flit_11', 'command_script', '04b_floodlab_mission'), ('monitor_flit_12', 'command_script', '04b_floodlab_mission'), ('monitor_flit_13', 'command_script', '04b_floodlab_mission'), ('monitor_flit_14', 'command_script', '04b_floodlab_mission'), ('monitor_flit_15', 'command_script', '04b_floodlab_mission'), ('monitor_flit_16', 'command_script', '04b_floodlab_mission'), ('monitor_flit_17', 'command_script', '04b_floodlab_mission'), ('monitor_flit_18', 'command_script', '04b_floodlab_mission'), ('monitor_flit_19', 'command_script', '04b_floodlab_mission'), ('monitor_flit_20', 'command_script', '04b_floodlab_mission'), ('monitor_flitting', 'dormant', '04b_floodlab_mission'), ('boss_fight_cf_spawner_01', 'dormant', '04b_floodlab_mission'), ('boss_fight_s_spawner_01', 'dormant', '04b_floodlab_mission'), ('boss_fight_cf_spawner_02', 'dormant', '04b_floodlab_mission'), ('boss_fight_s_spawner_02', 'dormant', '04b_floodlab_mission'), ('boss_fight_cf_spawner_03', 'dormant', '04b_floodlab_mission'), ('boss_fight_s_spawner_03', 'dormant', '04b_floodlab_mission'), ('boss_fight_cf_hobbled', 'dormant', '04b_floodlab_mission'), ('boss_fight_s_hobbled', 'dormant', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('holo1_deleteme', 'dormant', '04b_floodlab_mission'), ('holo2_deleteme', 'dormant', '04b_floodlab_mission'), ('holo3_deleteme', 'dormant', '04b_floodlab_mission'), ('holo4_deleteme', 'dormant', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('toys', 'dormant', '04b_floodlab_mission'), ('hangar_secondtime_start', 'dormant', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('void', 'static', '04b_floodlab_mission'), ('mission', 'startup', '04b_floodlab_mission'), ('04_intra0_predict', 'dormant', '04b_floodlab_prediction'), ('04_intra1_01_predict', 'dormant', '04b_floodlab_prediction'), ('04_intra1_02_predict', 'dormant', '04b_floodlab_prediction'), ('04_outro1_01_predict', 'dormant', '04b_floodlab_prediction'), ('04_outro1_02_predict', 'dormant', '04b_floodlab_prediction'), ('04_outro1_03_predict', 'dormant', '04b_floodlab_prediction'), ('04_outro2_01_predict', 'dormant', '04b_floodlab_prediction'), ('04_outro2_02_predict', 'dormant', '04b_floodlab_prediction'), ('void', 'static', '04b_floodlab_prediction'), ('void', 'static', '04b_floodlab_prediction'), ('void', 'static', '04b_floodlab_prediction'), ('void', 'static', '04b_floodlab_prediction'), ('void', 'static', '04b_floodlab_prediction'), ('void', 'static', '04b_floodlab_prediction'), ('void', 'static', '04b_floodlab_prediction'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('void', 'static', '04b_floodlab_teleport'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/05a_deltaapproach/05a_deltaapproach': {
        "objects": {
            'LZ_allies': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_elites_bunkered': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_elites_ledge': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_elites_phantom_01': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_elites_phantom_02': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_elites_ridge': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_elites_structure': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_elites_yard': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_enemies_all': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_enemies_structure': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_enemies_turrets': {'category': 'device', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_enemies_yard': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_grunts_bunkered': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_grunts_ledge': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_grunts_phantom_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_grunts_phantom_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_grunts_ridge': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_grunts_structure': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_grunts_yard': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_jackals_phantom_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_jackals_phantom_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_jackals_ridge': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_jackals_structure': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_jackals_yard': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_pelican_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_pelican_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_phantom_01': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_phantom_02': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_turrets_01': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_turrets_02': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_turrets_03': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_turrets_04': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'LZ_warthog_01': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission', '05a_deltaapproach_teleport']},
            'all_allies': {'category': 'object', 'funcs': ['ai_living_count', 'ai_set_orders', 'ai_vehicle_exit'], 'sources': ['05a_deltaapproach_mission', '05a_deltaapproach_teleport']},
            'allies_bridge_pelican': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'allies_lz_ledge': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'allies_lz_pelican': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'allies_lz_ridge': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'allies_old_temple_pelican': {'category': 'object', 'funcs': ['ai_migrate', 'ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'ally_infantry': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'approach_buggers': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'approach_buggers_too': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'approach_elite_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'approach_elite_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'approach_elite_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'approach_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'approach_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'approach_jackal_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'approach_jackal_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'approach_jackal_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_allies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_backdoor_elites_01': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_backdoor_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_backdoor_jackals_01': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_banshees': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_bunker_elites': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_bunker_elites_01': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_bunker_ghosts': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_bunker_grunts': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_bunker_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_bunker_jackals': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_bunker_jackals_01': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_bunker_turrets': {'category': 'device', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_control_elites_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_control_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_control_jackals_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_crack_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_crack_jackals': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_enemies_bunker': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_farside_ghosts': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_farside_wraiths': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_free_ghost/1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_free_ghost/2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_free_ghost/3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_free_ghost/4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_ghost_elites': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_pelican': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_pelican_chasers': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_phantom_01': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_phantom_02': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_phantom_ghosts_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_phantom_ghosts_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_tank': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission', '05a_deltaapproach_teleport']},
            'bridge_turret_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_turret_grunts_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bridge_vehicles_all': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'bunker_turret_remen': {'category': 'device', 'funcs': ['ai_living_count', 'ai_vehicle_enter'], 'sources': ['05a_deltaapproach_mission']},
            'bunker_turret_remen/1': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bunker_turret_remen/2': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'bunker_turret_remen/3': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'carrier': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'chief': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'chief_intro': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'chief_toy': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'cigar': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'corona_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'courtyard_grunts_end': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'covenant': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['05a_deltaapproach_mission']},
            'da_bridge': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['05a_deltaapproach_mission', '05a_deltaapproach_teleport']},
            'delta_halo': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'envy_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grenade_toy_01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'grenade_toy_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'grotto_buggers': {'category': 'object', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_buggers_01': {'category': 'object', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_buggers_02': {'category': 'object', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_buggers_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_buggers_new_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_cave_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_cave_jackals_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_cave_jackals_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_cave_jackals_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_crack_grunts': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_end_elites_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_end_elites_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_end_jackals_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_end_jackals_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_end_jackals_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_grunts_end': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_init_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_init_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_init_05': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_init_06': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_init_07': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_init_09': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_init_11': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_initial': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_phantom': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_phantom_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_phantom_jackals_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_phantom_jackals_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_phantom_jackals_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_pool_grunts': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grotto_sleepers': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'grunt_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'grunt_toy': {'category': 'covenant', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_03': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_04': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_05': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_06': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_07': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_08': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_09': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_10': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_11': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_12': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_13': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_14': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_15': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_16': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_17': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_bay': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_chute': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_close_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_close_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_close_03': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_close_04': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_close_05': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_close_06': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_close_07': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'hev_close_08': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'iac': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'iac_bridge': {'category': 'device', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'intro_crate_01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'intro_crate_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'intro_fire': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'intro_turret': {'category': 'device', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'intro_turret_02': {'category': 'device', 'funcs': ['object_cinematic_lod'], 'sources': ['05a_deltaapproach_cinematics']},
            'jackal_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'johnson': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'lz_enemies_all': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'lz_pelican_01': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'lz_pelican_02': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['05a_deltaapproach_mission']},
            'lz_phantom_01': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'lz_phantom_02': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'lz_stealth_phantom_03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'lz_warthog_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission', '05a_deltaapproach_teleport']},
            'miranda': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'nav_officer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'old_temp_center_fodder': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'old_temp_center_tough': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'old_temp_court_phantom': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_center_all': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_center_elites_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_center_elites_05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_center_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_center_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_center_grunts_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_center_jackals_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_center_jackals_05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_all': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_elites_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_elites_05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_grunts_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_grunts_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_grunts_03': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_grunts_06': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_jackals_03': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_jackals_04': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_jackals_05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_court_jackals_06': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_courtyard_lure': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_elites_near_right': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_ghosts_air': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_ghosts_far': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_grunts_center': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_grunts_center/1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_grunts_far_left': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_grunts_far_left/1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_grunts_far_right': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_grunts_far_right/1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_grunts_near_left': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_grunts_near_left/1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_init_jackals_nl': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_jackals_below_far': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_jackals_below_near': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_jackals_near_right': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_pelican': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_peri_grunts': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_peri_jackals': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_phantom': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_playfight_e': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_playfight_g': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_turrets/center': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_turrets/far_l': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_turrets/far_r': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_turrets/near_l': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'old_temple_vehicles': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'overlook_jackals': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'overlook_jackals_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'overlook_jackals_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['05a_deltaapproach_mission']},
            'prophet': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['05a_deltaapproach_mission']},
            'real_bridge': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['05a_deltaapproach_mission']},
            'regret01': {'category': 'object', 'funcs': ['ai_disregard'], 'sources': ['05a_deltaapproach_mission']},
            'regret02': {'category': 'object', 'funcs': ['ai_disregard'], 'sources': ['05a_deltaapproach_mission']},
            'regret03': {'category': 'object', 'funcs': ['ai_disregard'], 'sources': ['05a_deltaapproach_mission']},
            'rocket_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'smg_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'temple_ent_banshees': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_elites_01l': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_elites_01r': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_elites_02l': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_elites_02r': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_enemies_all': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_ghosts': {'category': 'object', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_ghosts_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_ghosts_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_grunts_01l': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_grunts_01r': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_jackals_01l': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_jackals_01r': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_jackals_02c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_turrets_01/1': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_turrets_01/2': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_turrets_02/1': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_turrets_02/2': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_turrets_03/1': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_turrets_03/2': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_turrets_04/1': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_turrets_04/2': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'temple_ent_turrets_near': {'category': 'device', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'texture_camera': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'tower1_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'tower1_grunts_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'tower1_grunts_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'tower1_hg_01a': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'tower1_hg_01b': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['05a_deltaapproach_mission']},
            'tower1_hg_02a': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'tower1_hg_02b': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'tree_toy': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'tunnel_enemies_all': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'tunnel_ghosts': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'tunnel_ghosts_01': {'category': 'object', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'tunnel_ghosts_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'tunnel_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'tunnel_heavies_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'tunnel_heavies_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'tunnel_infantry': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'tunnel_jackals': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'turret_handheld': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['05a_deltaapproach_cinematics']},
            'turret_handheld_02': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['05a_deltaapproach_cinematics']},
            'vol_approach': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission', '05a_deltaapproach_teleport']},
            'vol_approach_music': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_approach_ramp': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_arbiter_envy': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bridge_all': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bridge_engage': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bridge_farside_all': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bridge_ghost_spawn': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bridge_inside_bunker': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bridge_middle': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bridge_near_bunker': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bridge_pause': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bridge_tank': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bunker_backdoor': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bunker_front': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bunker_lower_level': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bunker_parking': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bunker_roof': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bunker_spawnstop_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bunker_spawnstop_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bunker_spawnstop_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_bunker_upper_level': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_entry_ledge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_grotto': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission', '05a_deltaapproach_teleport']},
            'vol_grotto_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_grotto_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_grotto_far_top': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_grotto_first_pool_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_grotto_first_pool_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_grotto_follow_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_grotto_mid_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_grotto_mid_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lights_on_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lights_on_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lights_on_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lights_on_04': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lights_on_05': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lights_on_06': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lz_all': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lz_in_yard_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lz_in_yard_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lz_leaving_ridge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_lz_warthog': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_no_see_approach': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['05a_deltaapproach_mission']},
            'vol_no_see_ramp': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_airspace_high': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_airspace_low': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_below': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_center_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_center_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_center_05': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_close_nuff': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_court_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_court_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_court_04': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_court_05': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_court_06': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_debris': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_far_left': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_far_right': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_farwall_all': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_in_court': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_int_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_int_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_near_left': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_near_right': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_seawall_all': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_see_nook': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_old_temple_start': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_overlook': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_overlook_pause': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_starting_locations': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_temple_ent_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_temple_ent_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_temple_ent_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_temple_ent_start': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_temple_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_through_debris': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_tower1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_tower1_all': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_tower1_see_hg': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_tower1_upper': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_tunnel_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission', '05a_deltaapproach_teleport']},
            'vol_tunnel_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_tunnel_03': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_waterfall_off': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_waterfall_on': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_winding_path': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission', '05a_deltaapproach_teleport']},
            'vol_winding_path_mid_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'vol_winding_path_mid_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05a_deltaapproach_mission']},
            'w_path_free_ghost': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'w_path_heavies/0': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'w_path_heavies/1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'w_path_heavies/2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'waterfall_close': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_mission']},
            'waterfall_far': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_mission']},
            'weap_officer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'winding_path_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'winding_path_ghosts': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05a_deltaapproach_mission']},
            'winding_path_ghosts_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'winding_path_ghosts_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'winding_path_grunts': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'winding_path_jackals': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'winding_path_ledge_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05a_deltaapproach_mission']},
            'x05_debris': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
            'x05_slipspace': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05a_deltaapproach_cinematics']},
        },
        "scripts": [('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_cinematics'), ('x05_score_01', 'dormant', '05a_deltaapproach_cinematics'), ('x05_foley_01', 'dormant', '05a_deltaapproach_cinematics'), ('x05_slipspace_open', 'dormant', '05a_deltaapproach_cinematics'), ('x05_cinematic_lighting_scene_01', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('x05_foley_02', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0010_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0020_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0030_no1', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0040_wo1', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0050_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0060_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0070_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0080_jon', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0090_cor', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0100_no1', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0110_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_fov_02', 'dormant', '05a_deltaapproach_cinematics'), ('x05_05_dof_scene_02', 'dormant', '05a_deltaapproach_cinematics'), ('x05_light_scene_02_bridge_1', 'dormant', '05a_deltaapproach_cinematics'), ('x05_light_scene_02_hev_1', 'dormant', '05a_deltaapproach_cinematics'), ('x05_light_scene_02_bridge_2', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('x05_score_03', 'dormant', '05a_deltaapproach_cinematics'), ('x05_foley_03', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0120_cor', 'dormant', '05a_deltaapproach_cinematics'), ('x05_cinematic_lighting_scene_03', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('x05_foley_04', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0130_jon', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0140_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0150_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0160_cor', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0170_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0180_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0181_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0190_cor', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0200_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0210_wo1', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0220_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_texture_camera_scene_04', 'dormant', '05a_deltaapproach_cinematics'), ('x05_fov_04', 'dormant', '05a_deltaapproach_cinematics'), ('x05_05_dof_scene_04', 'dormant', '05a_deltaapproach_cinematics'), ('x05_cinematic_lighting_scene_04', 'dormant', '05a_deltaapproach_cinematics'), ('x05_light_scene_04_bridge_1', 'dormant', '05a_deltaapproach_cinematics'), ('x05_light_scene_04_hev_1', 'dormant', '05a_deltaapproach_cinematics'), ('x05_light_scene_04_bridge_2', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('x05_foley_05', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0230_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_cinematic_lighting_scene_05', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('x05_score_06a', 'dormant', '05a_deltaapproach_cinematics'), ('x05_foley_06a', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0240_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_cinematic_light_scene_06a', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('x05_foley_06b', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0250_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0260_jon', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0270_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0280_mir', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0290_mas', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0300_wo1', 'dormant', '05a_deltaapproach_cinematics'), ('x05_fov_06b', 'dormant', '05a_deltaapproach_cinematics'), ('x05_light_scene_06b_bridge_1', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('x05_cinematic_lighting_scene_07', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('x05_foley_08', 'dormant', '05a_deltaapproach_cinematics'), ('x05_0310_cor', 'dormant', '05a_deltaapproach_cinematics'), ('effect_hev_release', 'dormant', '05a_deltaapproach_cinematics'), ('effect_corona', 'dormant', '05a_deltaapproach_cinematics'), ('x05_effect_shake_01', 'dormant', '05a_deltaapproach_cinematics'), ('x05_cinematic_lighting_scene_08', 'dormant', '05a_deltaapproach_cinematics'), ('x05_light_scene_08_space', 'dormant', '05a_deltaapproach_cinematics'), ('destroy_chief', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('c05_intro_foley_01', 'dormant', '05a_deltaapproach_cinematics'), ('c05_1010_cor', 'dormant', '05a_deltaapproach_cinematics'), ('effect_burn_contrails', 'dormant', '05a_deltaapproach_cinematics'), ('effect_chute_pins', 'dormant', '05a_deltaapproach_cinematics'), ('effect_retros_01', 'dormant', '05a_deltaapproach_cinematics'), ('c05_intro_dof_01', 'dormant', '05a_deltaapproach_cinematics'), ('c05_intro_cinematic_light_01', 'dormant', '05a_deltaapproach_cinematics'), ('hev_unhide', 'dormant', '05a_deltaapproach_cinematics'), ('destroy_corona_02', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('little_alien', 'dormant', '05a_deltaapproach_cinematics'), ('c05_intro_foley_02', 'dormant', '05a_deltaapproach_cinematics'), ('effect_retros_02', 'dormant', '05a_deltaapproach_cinematics'), ('effect_retros_03', 'dormant', '05a_deltaapproach_cinematics'), ('c05_intro_dof_02', 'dormant', '05a_deltaapproach_cinematics'), ('c05_intro_cinematic_light_02', 'dormant', '05a_deltaapproach_cinematics'), ('jackal_shield_activate', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('c05_intro_foley_03', 'dormant', '05a_deltaapproach_cinematics'), ('c05_1020_cor', 'dormant', '05a_deltaapproach_cinematics'), ('c05_1030_cor', 'dormant', '05a_deltaapproach_cinematics'), ('effect_dust', 'dormant', '05a_deltaapproach_cinematics'), ('effect_hev_door_release', 'dormant', '05a_deltaapproach_cinematics'), ('intro_turret_fire', 'dormant', '05a_deltaapproach_cinematics'), ('intro_turret_fire_02', 'dormant', '05a_deltaapproach_cinematics'), ('05_intro_fov_03_1', 'dormant', '05a_deltaapproach_cinematics'), ('05_intro_fov_03_2', 'dormant', '05a_deltaapproach_cinematics'), ('c05_intro_cinematic_light_03', 'dormant', '05a_deltaapproach_cinematics'), ('late_pods', 'dormant', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'static', '05a_deltaapproach_cinematics'), ('void', 'stub', '05a_deltaapproach_mission'), ('void', 'stub', '05a_deltaapproach_mission'), ('long_pause', 'command_script', '05a_deltaapproach_mission'), ('forever_pause', 'command_script', '05a_deltaapproach_mission'), ('abort', 'command_script', '05a_deltaapproach_mission'), ('05a_title0', 'dormant', '05a_deltaapproach_mission'), ('05a_title1', 'dormant', '05a_deltaapproach_mission'), ('05a_title2', 'dormant', '05a_deltaapproach_mission'), ('objective_lz_set', 'dormant', '05a_deltaapproach_mission'), ('objective_lz_clear', 'dormant', '05a_deltaapproach_mission'), ('objective_bridge_set', 'dormant', '05a_deltaapproach_mission'), ('objective_bridge_clear', 'dormant', '05a_deltaapproach_mission'), ('objective_ruins_set', 'dormant', '05a_deltaapproach_mission'), ('objective_ruins_clear', 'dormant', '05a_deltaapproach_mission'), ('objective_tower1_set', 'dormant', '05a_deltaapproach_mission'), ('objective_tower1_clear', 'dormant', '05a_deltaapproach_mission'), ('music_05a_01_start', 'dormant', '05a_deltaapproach_mission'), ('music_05a_01_stop', 'dormant', '05a_deltaapproach_mission'), ('music_05a_02_start', 'dormant', '05a_deltaapproach_mission'), ('music_05a_02_stop', 'dormant', '05a_deltaapproach_mission'), ('music_05a_03_start', 'dormant', '05a_deltaapproach_mission'), ('music_05a_03_stop', 'dormant', '05a_deltaapproach_mission'), ('music_05a_04_start', 'dormant', '05a_deltaapproach_mission'), ('music_05a_04_start_alt', 'dormant', '05a_deltaapproach_mission'), ('music_05a_04_stop', 'dormant', '05a_deltaapproach_mission'), ('music_05a_05_start', 'dormant', '05a_deltaapproach_mission'), ('music_05a_05_stop', 'dormant', '05a_deltaapproach_mission'), ('music_05a_06_start', 'dormant', '05a_deltaapproach_mission'), ('kill_volumes', 'dormant', '05a_deltaapproach_mission'), ('kill_stragglers', 'dormant', '05a_deltaapproach_mission'), ('lights', 'dormant', '05a_deltaapproach_mission'), ('lz_phantom_01_crash', 'command_script', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('stay_shooting', 'command_script', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('lz_pelican_wait', 'dormant', '05a_deltaapproach_mission'), ('drive_to_overlook_01', 'command_script', '05a_deltaapproach_mission'), ('drive_to_overlook_02', 'command_script', '05a_deltaapproach_mission'), ('lz_pelican_sighted', 'command_script', '05a_deltaapproach_mission'), ('lz_saddle_up', 'command_script', '05a_deltaapproach_mission'), ('lz_pelican_timer', 'dormant', '05a_deltaapproach_mission'), ('LZ_pelican_arrives', 'command_script', '05a_deltaapproach_mission'), ('other_lz_pelican', 'command_script', '05a_deltaapproach_mission'), ('LZ_pelican', 'dormant', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('lz_turret_reminder', 'dormant', '05a_deltaapproach_mission'), ('ODST_warning', 'command_script', '05a_deltaapproach_mission'), ('ODST_turrets_down', 'command_script', '05a_deltaapproach_mission'), ('LZ_turret_track', 'dormant', '05a_deltaapproach_mission'), ('lz_phantom_01_drop', 'dormant', '05a_deltaapproach_mission'), ('LZ_phantom_arrives_01', 'command_script', '05a_deltaapproach_mission'), ('lz_phantom_02_drop', 'dormant', '05a_deltaapproach_mission'), ('LZ_phantom_arrives_02', 'command_script', '05a_deltaapproach_mission'), ('LZ_phantom_arrives_03', 'command_script', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('LZ_start', 'dormant', '05a_deltaapproach_mission'), ('overlook_reminder', 'dormant', '05a_deltaapproach_mission'), ('overlook_remark', 'command_script', '05a_deltaapproach_mission'), ('overlook_wander1', 'command_script', '05a_deltaapproach_mission'), ('overlook_wander2', 'command_script', '05a_deltaapproach_mission'), ('overlook_start', 'dormant', '05a_deltaapproach_mission'), ('bridge_cortana_comment', 'dormant', '05a_deltaapproach_mission'), ('bridge_wraith_warn', 'command_script', '05a_deltaapproach_mission'), ('bridge_wraith_warning', 'dormant', '05a_deltaapproach_mission'), ('bridge_phantom_01a', 'command_script', '05a_deltaapproach_mission'), ('bridge_phantom_01b', 'command_script', '05a_deltaapproach_mission'), ('bridge_phantom_02a', 'command_script', '05a_deltaapproach_mission'), ('bridge_phantom_02b', 'command_script', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('bridge_ghostman_r', 'command_script', '05a_deltaapproach_mission'), ('bridge_ghostman_l', 'command_script', '05a_deltaapproach_mission'), ('bridge_ghosts_by_phantom', 'dormant', '05a_deltaapproach_mission'), ('bridge_activate_reminder', 'dormant', '05a_deltaapproach_mission'), ('bridge_cortana_response', 'dormant', '05a_deltaapproach_mission'), ('bridge_holo_comment', 'command_script', '05a_deltaapproach_mission'), ('bunker_holo_looper', 'dormant', '05a_deltaapproach_mission'), ('bridge_holo_translate', 'dormant', '05a_deltaapproach_mission'), ('bridge_ally_comment', 'command_script', '05a_deltaapproach_mission'), ('crack_spawn', 'dormant', '05a_deltaapproach_mission'), ('bunker_turret_remanning', 'dormant', '05a_deltaapproach_mission'), ('bunker_upper_spawn_01', 'dormant', '05a_deltaapproach_mission'), ('bunker_upper_spawn_03', 'dormant', '05a_deltaapproach_mission'), ('bunker_lower_spawn_01', 'dormant', '05a_deltaapproach_mission'), ('bunker_spawn_checker', 'dormant', '05a_deltaapproach_mission'), ('bridge_pelican_wait', 'dormant', '05a_deltaapproach_mission'), ('bridge_cross_reminder', 'dormant', '05a_deltaapproach_mission'), ('banshee_boost', 'command_script', '05a_deltaapproach_mission'), ('bridge_pelican_timer', 'dormant', '05a_deltaapproach_mission'), ('gimme_tank', 'command_script', '05a_deltaapproach_mission'), ('bridge_pelican_run', 'dormant', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('bridge_banshee_spawn', 'dormant', '05a_deltaapproach_mission'), ('farside_ghosts_spawn', 'dormant', '05a_deltaapproach_mission'), ('bridge_spare_ghost_spawn', 'dormant', '05a_deltaapproach_mission'), ('bridge_wraith_engage', 'command_script', '05a_deltaapproach_mission'), ('bridges_start', 'dormant', '05a_deltaapproach_mission'), ('waterfall_toggle', 'dormant', '05a_deltaapproach_mission'), ('w_path_turret_0', 'command_script', '05a_deltaapproach_mission'), ('w_path_turret_1', 'command_script', '05a_deltaapproach_mission'), ('w_path_turret_2', 'command_script', '05a_deltaapproach_mission'), ('w_path_turret_deploy', 'dormant', '05a_deltaapproach_mission'), ('throw_grenade', 'command_script', '05a_deltaapproach_mission'), ('winding_path_start', 'dormant', '05a_deltaapproach_mission'), ('temple_ent_turret_spawn', 'dormant', '05a_deltaapproach_mission'), ('temple_ent_ghostman_r', 'command_script', '05a_deltaapproach_mission'), ('temple_ent_ghostman_l', 'command_script', '05a_deltaapproach_mission'), ('temple_ent_ghost_alert', 'dormant', '05a_deltaapproach_mission'), ('temple_ent_veh_spawn', 'dormant', '05a_deltaapproach_mission'), ('back_home_comment', 'command_script', '05a_deltaapproach_mission'), ('temple_ent_reminder', 'dormant', '05a_deltaapproach_mission'), ('old_temple_entrance_start', 'dormant', '05a_deltaapproach_mission'), ('temple_ent_arch', 'dormant', '05a_deltaapproach_mission'), ('old_temple_structure_comment', 'command_script', '05a_deltaapproach_mission'), ('tunnel_turret_0', 'command_script', '05a_deltaapproach_mission'), ('tunnel_turret_1', 'command_script', '05a_deltaapproach_mission'), ('tunnel_turret_2', 'command_script', '05a_deltaapproach_mission'), ('tunnel_turret_3', 'command_script', '05a_deltaapproach_mission'), ('tunnel_start', 'dormant', '05a_deltaapproach_mission'), ('arbiter_envy', 'dormant', '05a_deltaapproach_mission'), ('old_temple_pelican_comment', 'command_script', '05a_deltaapproach_mission'), ('old_temple_pelican_timer', 'dormant', '05a_deltaapproach_mission'), ('old_temple_pelican_arrives', 'command_script', '05a_deltaapproach_mission'), ('old_temple_pelican', 'dormant', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('old_temple_ph_01_arrives', 'command_script', '05a_deltaapproach_mission'), ('old_temple_ph_02_arrives', 'command_script', '05a_deltaapproach_mission'), ('old_temple_ph_04_arrives', 'command_script', '05a_deltaapproach_mission'), ('old_temple_abort', 'command_script', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('old_temple_phantom_04', 'dormant', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('old_temple_vehicle_spawn', 'dormant', '05a_deltaapproach_mission'), ('old_temple_near_right', 'dormant', '05a_deltaapproach_mission'), ('old_temple_far_left', 'dormant', '05a_deltaapproach_mission'), ('old_temple_far_right', 'dormant', '05a_deltaapproach_mission'), ('old_temple_below', 'dormant', '05a_deltaapproach_mission'), ('old_temp_reman_fr', 'command_script', '05a_deltaapproach_mission'), ('old_temp_reman_fl', 'command_script', '05a_deltaapproach_mission'), ('old_temp_reman_nl', 'command_script', '05a_deltaapproach_mission'), ('old_temp_reman_cen', 'command_script', '05a_deltaapproach_mission'), ('old_temple_turret_reman', 'dormant', '05a_deltaapproach_mission'), ('old_temple_perimeter_nuke', 'dormant', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('old_temple_middle_comment', 'command_script', '05a_deltaapproach_mission'), ('old_temple_middle_ally', 'dormant', '05a_deltaapproach_mission'), ('old_temple_center', 'dormant', '05a_deltaapproach_mission'), ('old_temple_playfight', 'dormant', '05a_deltaapproach_mission'), ('old_temple_debris_comment', 'dormant', '05a_deltaapproach_mission'), ('old_temple_middle_reminder', 'dormant', '05a_deltaapproach_mission'), ('old_temple_start', 'dormant', '05a_deltaapproach_mission'), ('old_temple_debris_reminder', 'dormant', '05a_deltaapproach_mission'), ('old_temple_holo_translate', 'dormant', '05a_deltaapproach_mission'), ('courtyard_holo_looper', 'dormant', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('old_temple_archaeologist', 'dormant', '05a_deltaapproach_mission'), ('old_temple_courtyard', 'dormant', '05a_deltaapproach_mission'), ('grotto_cortana_warn', 'dormant', '05a_deltaapproach_mission'), ('grotto_ally_warn', 'command_script', '05a_deltaapproach_mission'), ('grotto_phantom_arrives', 'command_script', '05a_deltaapproach_mission'), ('grotto_phantom_start', 'dormant', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('grotto_cortana_comment', 'dormant', '05a_deltaapproach_mission'), ('grotto_ally_cheese', 'command_script', '05a_deltaapproach_mission'), ('grotto_ally_comments', 'dormant', '05a_deltaapproach_mission'), ('grotto_reminder', 'dormant', '05a_deltaapproach_mission'), ('grotto_pool', 'dormant', '05a_deltaapproach_mission'), ('grotto_buggers_reinforce', 'dormant', '05a_deltaapproach_mission'), ('grotto_extra_checkpoint', 'dormant', '05a_deltaapproach_mission'), ('grotto_entry_patrol', 'command_script', '05a_deltaapproach_mission'), ('grotto_start', 'dormant', '05a_deltaapproach_mission'), ('approach_cortana_comment', 'dormant', '05a_deltaapproach_mission'), ('approach_reminder', 'dormant', '05a_deltaapproach_mission'), ('temple_approach_start', 'dormant', '05a_deltaapproach_mission'), ('tower1_holo_looper', 'dormant', '05a_deltaapproach_mission'), ('tower1_hg_warn', 'dormant', '05a_deltaapproach_mission'), ('long_pause_point', 'command_script', '05a_deltaapproach_mission'), ('tower1_start', 'dormant', '05a_deltaapproach_mission'), ('temple_ent_go', 'command_script', '05a_deltaapproach_mission'), ('bridge_bunker_backup', 'dormant', '05a_deltaapproach_mission'), ('ally_order_monitor', 'dormant', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('mission', 'startup', '05a_deltaapproach_mission'), ('void', 'static', '05a_deltaapproach_mission'), ('x05_01_predict', 'dormant', '05a_deltaapproach_prediction'), ('x05_02_predict', 'dormant', '05a_deltaapproach_prediction'), ('x05_03_predict', 'dormant', '05a_deltaapproach_prediction'), ('x05_04_predict', 'dormant', '05a_deltaapproach_prediction'), ('x05_05_predict', 'dormant', '05a_deltaapproach_prediction'), ('x05_06a_predict', 'dormant', '05a_deltaapproach_prediction'), ('x05_06b_predict', 'dormant', '05a_deltaapproach_prediction'), ('x05_07_predict', 'dormant', '05a_deltaapproach_prediction'), ('x05_08_predict', 'dormant', '05a_deltaapproach_prediction'), ('05_intro_01_predict', 'dormant', '05a_deltaapproach_prediction'), ('05_intro_02_predict', 'dormant', '05a_deltaapproach_prediction'), ('05_intro_03_predict', 'dormant', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_prediction'), ('void', 'static', '05a_deltaapproach_teleport'), ('void', 'static', '05a_deltaapproach_teleport'), ('void', 'static', '05a_deltaapproach_teleport'), ('void', 'static', '05a_deltaapproach_teleport'), ('void', 'static', '05a_deltaapproach_teleport'), ('void', 'static', '05a_deltaapproach_teleport'), ('void', 'static', '05a_deltaapproach_teleport'), ('void', 'static', '05a_deltaapproach_teleport'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/05b_deltatowers/05b_deltatowers': {
        "objects": {
            'all_allies': {'category': 'object', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'all_enemies': {'category': 'object', 'funcs': ['ai_erase', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'allies_infantry': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'assassin_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_elites_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_elites_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_elites_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_elites_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'bridge_grunts_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_grunts_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_grunts_03': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_grunts_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_jackals_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_jackals_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_jackals_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_jackals_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_jackals_05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_jackals_06': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'bridge_jackals_07': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'carrier': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'central_plat_pelican': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'central_plat_pelican_allies': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'central_platform_elites_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'central_platform_elites_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'central_platform_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'central_platform_hunters': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'central_platform_jackals_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'central_platform_jackals_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'central_platform_phantom': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'chief': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'cortana': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'cortana_base': {'category': 'human', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'covenant': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['05b_deltatowers_mission']},
            'elev_under': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'elev_under_switch': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['05b_deltatowers_mission']},
            'elev_under_switch_01': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['05b_deltatowers_mission']},
            'elev_up': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'elev_up_switch': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['05b_deltatowers_mission']},
            'elev_up_switch_01': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['05b_deltatowers_mission']},
            'fake_corpse': {'category': 'object', 'funcs': ['object_cannot_take_damage', 'object_hide'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_a': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_b': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_b_buggers': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_b_elites': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_buggers/1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_buggers/2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_buggers/3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_buggers/4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_bugs_new': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_elite_boarders': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_elite_riders': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_grunt_boarders_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_grunt_boarders_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_grunt_riders': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_jackal_riders': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_launch_a': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_launch_b': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_phantom': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_switch': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['05b_deltatowers_mission']},
            'gondola_01_switch_back': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_a': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_b': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_banshees': {'category': 'object', 'funcs': ['ai_erase', 'ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_grunts': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_jetpacks': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_launch_a': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_launch_b': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_switch': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_switch_back': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['05b_deltatowers_mission']},
            'gondola_02_switch_front': {'category': 'object', 'funcs': ['device_set_power'], 'sources': ['05b_deltatowers_mission']},
            'holo_index': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'holo_library': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'honor_grunts_init_L': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_init_R': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_L/01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_L/02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_L/03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_L/04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_L/05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_R/01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_R/02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_R/03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_R/04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'honor_grunts_new_R/05': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'iac_bridge': {'category': 'device', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'initial_allies': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission', '05b_deltatowers_teleport']},
            'intra2_fleet': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'island_all_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'island_ext_elites_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_ext_elites_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_ext_grunts_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_ext_grunts_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_ext_js_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_ext_js_02': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_ext_js_03': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_ext_js_04': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_gully_buggers_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_gully_elites_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_gully_elites_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_gully_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'island_gully_jackals_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_int_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'island_int_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_int_hg': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_main_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'island_pelican': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_pelican_allies': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_phantom': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'island_phantom_elites': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'island_phantom_grunts': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'island_phantom_jackals': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'johnson': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['05b_deltatowers_cinematics']},
            'matte_horizon': {'category': 'object', 'funcs': ['object_destroy', 'object_hide'], 'sources': ['05b_deltatowers_cinematics']},
            'miranda': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'near_gondola_02_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'near_gondola_02_jackals': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'outro_beam': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'pelican_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['05b_deltatowers_cinematics']},
            'pilot': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['05b_deltatowers_cinematics']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['05b_deltatowers_mission']},
            'regret': {'category': 'object', 'funcs': ['ai_kill', 'ai_place', 'ai_set_orders', 'object_cinematic_lod', 'object_destroy'], 'sources': ['05b_deltatowers_cinematics', '05b_deltatowers_mission']},
            'regret/1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'regret01': {'category': 'object', 'funcs': ['ai_disregard'], 'sources': ['05b_deltatowers_mission']},
            'regret02': {'category': 'object', 'funcs': ['ai_disregard'], 'sources': ['05b_deltatowers_mission']},
            'regret03': {'category': 'object', 'funcs': ['ai_disregard'], 'sources': ['05b_deltatowers_mission']},
            'regret_corpse': {'category': 'object', 'funcs': ['object_destroy', 'object_hide'], 'sources': ['05b_deltatowers_mission']},
            'regret_throne': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_mission']},
            'rubble': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'sunk_chamber_bugs_L_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_bugs_L_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_bugs_R_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_bugs_R_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_exit_e_L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_exit_e_R': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_exit_j01_L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_exit_j01_R': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_exit_j02_L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_exit_j02_R': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_hg_L_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_hg_L_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_hg_R_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_hg_R_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_hunters': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_hg_La': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_hg_Lb': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_hg_Ra': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_hg_Rb': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_js_L01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_js_L02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_js_L03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_js_L04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_js_R01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_js_R02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_js_R03': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_init_js_R04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_jack_L_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_jack_L_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_jack_R_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_jack_R_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_js_L_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_js_L_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_js_R_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chamber_js_R_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chmbr_spwn_L1a': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chmbr_spwn_L1b': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chmbr_spwn_L2a': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chmbr_spwn_L2b': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chmbr_spwn_R1a': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chmbr_spwn_R1b': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chmbr_spwn_R2a': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'sunk_chmbr_spwn_R2b': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'sunken_bugs': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'sunken_chamber_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'sunken_hg_left': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'sunken_hg_right': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'sunken_jacks_left': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'sunken_jacks_right': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'sunken_leftside_nonsnipers': {'category': 'object', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'sunken_leftside_snipers': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'sunken_rightside_nonsnipers': {'category': 'object', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'sunken_rightside_snipers': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'temp_bsp2_allies': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_teleport']},
            'temp_bsp3_allies': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_teleport']},
            'temple_ent_grunts': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'temple_ent_jackals': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'temple_ent_turrets': {'category': 'device', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['05b_deltatowers_mission']},
            'temple_entry_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'temple_escape_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'temple_exit_elites_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_exit_elites_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_exit_elites_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_exit_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_exit_hg_04': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_exit_jackals_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_exit_jackals_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_halls_elites_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_halls_elites_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_halls_jackals_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_halls_jackals_02L': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_halls_jackals_02R': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_heavies': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_hg': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'temple_hg_01L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_hg_01R': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_hg_02L': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_hg_02R': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_hg_init': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'temple_honor_grunts': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'temple_spawndoor_01L': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'temple_spawndoor_01R': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'temple_spawndoor_02L': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'temple_spawndoor_02R': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['05b_deltatowers_mission']},
            'texture_camera': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'throne_regret': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['05b_deltatowers_cinematics']},
            'tower1_buggers_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower1_buggers_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower1_elites_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower1_elites_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower1_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'tower2_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'tower2_grunts_01': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower2_grunts_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower2_jackals_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower2_jackals_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_buggers_01': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_buggers_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_dock_grunts': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_dock_jackals': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_dock_snipers': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_jackals_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_jackals_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_jackals_elev': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['05b_deltatowers_mission']},
            'tower3_main': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'tower3_pelican': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_pelican_allies': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_sleeper': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tower3_turrets': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_01_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_01_grunts_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_01_grunts_02': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_01_grunts_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_01_grunts_patrol': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_02_buggers_01': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_02_buggers_02': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_02_elites_01': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_02_elites_02': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_02_elites_03': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_02_elites_04': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_02_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['05b_deltatowers_mission']},
            'tunnel_02_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['05b_deltatowers_mission']},
            'vol_banshee_retreat': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_bridge': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_bridge_far_half': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_central_platform': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission', '05b_deltatowers_teleport']},
            'vol_elev_shaft_under': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['05b_deltatowers_mission']},
            'vol_elev_shaft_up': {'category': 'object', 'funcs': ['volume_test_object'], 'sources': ['05b_deltatowers_mission']},
            'vol_elev_up_dock': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_gondola_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_gondola_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_in_tower2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_island_ext_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_island_ext_start': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_island_gully_ridge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_island_int_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_island_int_entry': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission', '05b_deltatowers_teleport']},
            'vol_island_int_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_leaving_sunken_chamber': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_near_gondola_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_near_gondola_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_starting_locations': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chamber_far_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chamber_far_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chamber_left': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chamber_near_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chamber_near_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chamber_right': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chamber_safe_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chamber_safe_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chmbr_spwn_L1a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chmbr_spwn_L1b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chmbr_spwn_L2a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chmbr_spwn_L2b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chmbr_spwn_R1a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chmbr_spwn_R1b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chmbr_spwn_R2a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunk_chmbr_spwn_R2b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_sunken_chamber_entry': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_ent_cutscene': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_entry': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_ext': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission', '05b_deltatowers_teleport']},
            'vol_temple_foyer': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_left': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_retreat_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_retreat_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_right': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_spawnroom_01L': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_spawnroom_01R': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_spawnroom_02L': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_temple_spawnroom_02R': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower1_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower1_exit_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower1_exit_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower1_roof': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower1_upper': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower1_upper_right': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower2_by_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower2_entry': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower2_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission', '05b_deltatowers_teleport']},
            'vol_tower2_exit_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower2_ext_entry': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower2_ext_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower3_entry': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission', '05b_deltatowers_teleport']},
            'vol_tower3_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tower3_upstairs': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tunnel_01_entry': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_teleport']},
            'vol_tunnel_01_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tunnel_02_entry': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tunnel_02_mid_01': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'vol_tunnel_02_mid_02': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['05b_deltatowers_mission']},
            'water_1to2a': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_mission']},
            'water_1to2b': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_mission']},
            'water_2to3a': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_mission']},
            'water_2to3b': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['05b_deltatowers_mission']},
        },
        "scripts": [('void', 'stub', '05b_deltatowers_cinematics'), ('void', 'stub', '05b_deltatowers_cinematics'), ('void', 'stub', '05b_deltatowers_cinematics'), ('void', 'stub', '05b_deltatowers_cinematics'), ('void', 'stub', '05b_deltatowers_cinematics'), ('void', 'stub', '05b_deltatowers_cinematics'), ('void', 'stub', '05b_deltatowers_cinematics'), ('void', 'stub', '05b_deltatowers_cinematics'), ('void', 'stub', '05b_deltatowers_cinematics'), ('c05_intra1_score_01', 'dormant', '05b_deltatowers_cinematics'), ('c05_intra1_foley_01', 'dormant', '05b_deltatowers_cinematics'), ('c05_2010_cor', 'dormant', '05b_deltatowers_cinematics'), ('c05_2020_cor', 'dormant', '05b_deltatowers_cinematics'), ('c05_2030_cor', 'dormant', '05b_deltatowers_cinematics'), ('c05_2040_mas', 'dormant', '05b_deltatowers_cinematics'), ('c05_2050_por', 'dormant', '05b_deltatowers_cinematics'), ('c05_2060_cor', 'dormant', '05b_deltatowers_cinematics'), ('c05_2070_mas', 'dormant', '05b_deltatowers_cinematics'), ('c05_2080_mir', 'dormant', '05b_deltatowers_cinematics'), ('cortana_appear', 'dormant', '05b_deltatowers_cinematics'), ('c05_intra1_cinematic_light_01', 'dormant', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('c05_intra1_foley_02', 'dormant', '05b_deltatowers_cinematics'), ('c05_2090_mir', 'dormant', '05b_deltatowers_cinematics'), ('c05_2100_mir', 'dormant', '05b_deltatowers_cinematics'), ('c05_2110_jon', 'dormant', '05b_deltatowers_cinematics'), ('c05_2120_mir', 'dormant', '05b_deltatowers_cinematics'), ('c05_2130_mir', 'dormant', '05b_deltatowers_cinematics'), ('c05_2140_jon', 'dormant', '05b_deltatowers_cinematics'), ('intra1_texture_camera_on', 'dormant', '05b_deltatowers_cinematics'), ('c05_intra1_cinematic_light_02', 'dormant', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('c05_intra1_foley_03', 'dormant', '05b_deltatowers_cinematics'), ('c05_2150_mir', 'dormant', '05b_deltatowers_cinematics'), ('c05_2160_mir', 'dormant', '05b_deltatowers_cinematics'), ('cortana_disappear', 'dormant', '05b_deltatowers_cinematics'), ('c05_intra1_cinematic_light_03', 'dormant', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('c05_intra2_foley', 'dormant', '05b_deltatowers_cinematics'), ('c05_3010_cor', 'dormant', '05b_deltatowers_cinematics'), ('c05_3020_cor', 'dormant', '05b_deltatowers_cinematics'), ('c05_3030_cor', 'dormant', '05b_deltatowers_cinematics'), ('c05_intra2_dof', 'dormant', '05b_deltatowers_cinematics'), ('c05_intra2_cinematic_light', 'dormant', '05b_deltatowers_cinematics'), ('fleet_arrival', 'dormant', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('c05_outro_score_01', 'dormant', '05b_deltatowers_cinematics'), ('c05_outro_foley_01', 'dormant', '05b_deltatowers_cinematics'), ('effect_dust_scrape', 'dormant', '05b_deltatowers_cinematics'), ('c05_outro_01_dof', 'dormant', '05b_deltatowers_cinematics'), ('c05_outro_cinematic_light_01', 'dormant', '05b_deltatowers_cinematics'), ('c05_outro_problem_actors', 'dormant', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('c05_outro_foley_02', 'dormant', '05b_deltatowers_cinematics'), ('effect_dust_land', 'dormant', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('c05_outro_foley_03', 'dormant', '05b_deltatowers_cinematics'), ('c05_outro_fov_01', 'dormant', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('c05_outro_foley_04', 'dormant', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('x07_0220_grv', 'dormant', '05b_deltatowers_cinematics'), ('x07_0230_grv', 'dormant', '05b_deltatowers_cinematics'), ('c05_outro_bubbles', 'dormant', '05b_deltatowers_cinematics'), ('c05_outro_caustic', 'dormant', '05b_deltatowers_cinematics'), ('c05_outro_cinematic_light_05', 'dormant', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'static', '05b_deltatowers_cinematics'), ('void', 'stub', '05b_deltatowers_mission'), ('void', 'stub', '05b_deltatowers_mission'), ('void', 'stub', '05b_deltatowers_mission'), ('long_pause', 'command_script', '05b_deltatowers_mission'), ('forever_pause', 'command_script', '05b_deltatowers_mission'), ('abort', 'command_script', '05b_deltatowers_mission'), ('05b_title0', 'dormant', '05b_deltatowers_mission'), ('05b_title1', 'dormant', '05b_deltatowers_mission'), ('05b_title1_alt', 'dormant', '05b_deltatowers_mission'), ('05b_title2', 'dormant', '05b_deltatowers_mission'), ('objective_towers_set', 'dormant', '05b_deltatowers_mission'), ('objective_towers_clear', 'dormant', '05b_deltatowers_mission'), ('objective_gondola1_set', 'dormant', '05b_deltatowers_mission'), ('objective_gondola1_clear', 'dormant', '05b_deltatowers_mission'), ('objective_sunken_set', 'dormant', '05b_deltatowers_mission'), ('objective_sunken_clear', 'dormant', '05b_deltatowers_mission'), ('objective_temple_set', 'dormant', '05b_deltatowers_mission'), ('objective_temple_clear', 'dormant', '05b_deltatowers_mission'), ('objective_regret_set', 'dormant', '05b_deltatowers_mission'), ('objective_regret_clear', 'dormant', '05b_deltatowers_mission'), ('music_05b_01_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_01_stop', 'dormant', '05b_deltatowers_mission'), ('music_05b_02_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_02_stop', 'dormant', '05b_deltatowers_mission'), ('music_05b_03_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_03_stop', 'dormant', '05b_deltatowers_mission'), ('music_05b_04_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_04_stop', 'dormant', '05b_deltatowers_mission'), ('music_05b_05_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_06_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_06_stop', 'dormant', '05b_deltatowers_mission'), ('music_05b_07_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_08_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_09_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_09_start_alt', 'dormant', '05b_deltatowers_mission'), ('music_05b_09_stop', 'dormant', '05b_deltatowers_mission'), ('music_05b_10_start', 'dormant', '05b_deltatowers_mission'), ('music_05b_10_stop', 'dormant', '05b_deltatowers_mission'), ('kill_volumes', 'dormant', '05b_deltatowers_mission'), ('tower1_holo_looper', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('tower1_cortana_comment', 'dormant', '05b_deltatowers_mission'), ('tower1_start', 'dormant', '05b_deltatowers_mission'), ('tower1_escape', 'command_script', '05b_deltatowers_mission'), ('cortana_bridge_reminder', 'dormant', '05b_deltatowers_mission'), ('bridges_start', 'dormant', '05b_deltatowers_mission'), ('tower2_cortana_comment', 'dormant', '05b_deltatowers_mission'), ('tower2_start', 'dormant', '05b_deltatowers_mission'), ('miranda_pelican_comment', 'dormant', '05b_deltatowers_mission'), ('gondola_01_cortana_warn', 'dormant', '05b_deltatowers_mission'), ('gondola_01_cortana_comment', 'dormant', '05b_deltatowers_mission'), ('gondola_01_cortana_reminder', 'dormant', '05b_deltatowers_mission'), ('gondola_01_ally_comment', 'command_script', '05b_deltatowers_mission'), ('hunter_drop', 'dormant', '05b_deltatowers_mission'), ('central_platform_dropship', 'command_script', '05b_deltatowers_mission'), ('central_platform_pelican_path', 'command_script', '05b_deltatowers_mission'), ('central_platform_pelican', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('central_plat_ph_go', 'dormant', '05b_deltatowers_mission'), ('gondola_01_wake', 'dormant', '05b_deltatowers_mission'), ('central_platform_start', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('assassin_ice_cream', 'dormant', '05b_deltatowers_mission'), ('gondola_01_jumper_01', 'command_script', '05b_deltatowers_mission'), ('gondola_01_jumper_02', 'command_script', '05b_deltatowers_mission'), ('gondola_01_jumper_03', 'command_script', '05b_deltatowers_mission'), ('gondola_01_jumper_04', 'command_script', '05b_deltatowers_mission'), ('gondola_01_buggers_board', 'dormant', '05b_deltatowers_mission'), ('gondola_01_go_reminder', 'dormant', '05b_deltatowers_mission'), ('gondola_01_boarders_warn', 'command_script', '05b_deltatowers_mission'), ('gondola_01_cortana_arch', 'dormant', '05b_deltatowers_mission'), ('gondola_01_retreat', 'command_script', '05b_deltatowers_mission'), ('gondola_01_unload', 'dormant', '05b_deltatowers_mission'), ('gondola_01_flight', 'command_script', '05b_deltatowers_mission'), ('gondola_01_phantom_arrives', 'dormant', '05b_deltatowers_mission'), ('tower3_turret_mount_01', 'command_script', '05b_deltatowers_mission'), ('tower3_turret_mount_02', 'command_script', '05b_deltatowers_mission'), ('tower3_turret_reman', 'dormant', '05b_deltatowers_mission'), ('tower3_dock_above', 'dormant', '05b_deltatowers_mission'), ('gondola_01_nuke', 'dormant', '05b_deltatowers_mission'), ('gondola_01_restarter', 'dormant', '05b_deltatowers_mission'), ('gondola_01_reverser', 'dormant', '05b_deltatowers_mission'), ('tower_cluster_delete', 'dormant', '05b_deltatowers_mission'), ('gondola_01_start', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('tower3_pelican_path', 'command_script', '05b_deltatowers_mission'), ('tower3_pelican_arrives', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('tower3_cortana_comment', 'dormant', '05b_deltatowers_mission'), ('tower3_ally_warn', 'command_script', '05b_deltatowers_mission'), ('tower3_cortana_reminder_02', 'dormant', '05b_deltatowers_mission'), ('elev_under_cortana_comment', 'dormant', '05b_deltatowers_mission'), ('elev_under_ally_01', 'command_script', '05b_deltatowers_mission'), ('elev_under_ally_02', 'command_script', '05b_deltatowers_mission'), ('elev_under_ally_03', 'command_script', '05b_deltatowers_mission'), ('tower3_sleeper_spawn', 'dormant', '05b_deltatowers_mission'), ('elev_under_monitor', 'dormant', '05b_deltatowers_mission'), ('tower3_start', 'dormant', '05b_deltatowers_mission'), ('tunnel_01_cortana_comment', 'dormant', '05b_deltatowers_mission'), ('sunken_tunnel1_start', 'dormant', '05b_deltatowers_mission'), ('sunken_holo_cortana_comment', 'dormant', '05b_deltatowers_mission'), ('sunken_holo_ally_react', 'command_script', '05b_deltatowers_mission'), ('sunken_holo_looper', 'dormant', '05b_deltatowers_mission'), ('sunken_holo_translate', 'dormant', '05b_deltatowers_mission'), ('sunken_chamber_reminder', 'dormant', '05b_deltatowers_mission'), ('hide_rightside_guys', 'dormant', '05b_deltatowers_mission'), ('hide_leftside_guys', 'dormant', '05b_deltatowers_mission'), ('sunken_hologram_focus', 'command_script', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('sunk_chamber_hunters_enter', 'dormant', '05b_deltatowers_mission'), ('sunken_chamber_saves', 'dormant', '05b_deltatowers_mission'), ('sunken_chamber_start', 'dormant', '05b_deltatowers_mission'), ('elev_up_cortana_comment', 'dormant', '05b_deltatowers_mission'), ('elev_up_monitor', 'dormant', '05b_deltatowers_mission'), ('sunken_tunnel2_start', 'dormant', '05b_deltatowers_mission'), ('island_holo_looper', 'dormant', '05b_deltatowers_mission'), ('island_int_translate', 'dormant', '05b_deltatowers_mission'), ('island_interior_start', 'dormant', '05b_deltatowers_mission'), ('island_pelican_comment', 'dormant', '05b_deltatowers_mission'), ('island_pelican_path', 'command_script', '05b_deltatowers_mission'), ('island_pelican_arrives', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('island_gully_start', 'dormant', '05b_deltatowers_mission'), ('gondola_02_cortana_reminder', 'dormant', '05b_deltatowers_mission'), ('island_drop', 'dormant', '05b_deltatowers_mission'), ('island_phantom_path', 'command_script', '05b_deltatowers_mission'), ('island_phantom_arrives', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('island_exterior_start', 'dormant', '05b_deltatowers_mission'), ('island_miranda_conversation', 'dormant', '05b_deltatowers_mission'), ('gondola_02_ally_comment', 'command_script', '05b_deltatowers_mission'), ('temple_ent_turret_01', 'command_script', '05b_deltatowers_mission'), ('temple_ent_turret_02', 'command_script', '05b_deltatowers_mission'), ('banshee_retreat', 'command_script', '05b_deltatowers_mission'), ('gondola_02_nuke', 'dormant', '05b_deltatowers_mission'), ('gondola_02_wake', 'dormant', '05b_deltatowers_mission'), ('gondola_02_restarter', 'dormant', '05b_deltatowers_mission'), ('gondola_02_reverser', 'dormant', '05b_deltatowers_mission'), ('boost_test', 'command_script', '05b_deltatowers_mission'), ('boost_to_temple_01', 'command_script', '05b_deltatowers_mission'), ('boost_to_temple_02', 'command_script', '05b_deltatowers_mission'), ('panic', 'command_script', '05b_deltatowers_mission'), ('gondola_02_start', 'dormant', '05b_deltatowers_mission'), ('temple_hunker', 'command_script', '05b_deltatowers_mission'), ('high_charity_ally_comment', 'command_script', '05b_deltatowers_mission'), ('temple_ent_cortana_reminder', 'dormant', '05b_deltatowers_mission'), ('temple_deploy_l', 'command_script', '05b_deltatowers_mission'), ('temple_deploy_r', 'command_script', '05b_deltatowers_mission'), ('temple_entry_start', 'dormant', '05b_deltatowers_mission'), ('temple_cortana_warn_02', 'dormant', '05b_deltatowers_mission'), ('temple_foyer_start', 'dormant', '05b_deltatowers_mission'), ('temple_cortana_warn_01', 'dormant', '05b_deltatowers_mission'), ('temple_cortana_warn_03', 'dormant', '05b_deltatowers_mission'), ('temple_cortana_reminder', 'dormant', '05b_deltatowers_mission'), ('regret_hint_01', 'dormant', '05b_deltatowers_mission'), ('regret_hint_02', 'dormant', '05b_deltatowers_mission'), ('regret_hint_03', 'dormant', '05b_deltatowers_mission'), ('regret_teleport_comment', 'dormant', '05b_deltatowers_mission'), ('regret_beam_comment', 'dormant', '05b_deltatowers_mission'), ('regret_hg_comment', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('regret_taunts', 'dormant', '05b_deltatowers_mission'), ('temple_grunt_spawner', 'dormant', '05b_deltatowers_mission'), ('temple_hg_respawner', 'dormant', '05b_deltatowers_mission'), ('regret_respawner', 'dormant', '05b_deltatowers_mission'), ('reserve_throne', 'command_script', '05b_deltatowers_mission'), ('regret_pause', 'command_script', '05b_deltatowers_mission'), ('regret_retreat', 'dormant', '05b_deltatowers_mission'), ('regret_death', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('regret_dead_retreat', 'command_script', '05b_deltatowers_mission'), ('temple_center_start', 'dormant', '05b_deltatowers_mission'), ('temple_foyer_retreat', 'dormant', '05b_deltatowers_mission'), ('temple_entry_retreat', 'dormant', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('void', 'static', '05b_deltatowers_mission'), ('mission', 'startup', '05b_deltatowers_mission'), ('05_intra1_01_predict', 'dormant', '05b_deltatowers_prediction'), ('05_intra1_02_predict', 'dormant', '05b_deltatowers_prediction'), ('05_intra1_03_predict', 'dormant', '05b_deltatowers_prediction'), ('05_intra2_01_predict', 'dormant', '05b_deltatowers_prediction'), ('05_outro_01_predict', 'dormant', '05b_deltatowers_prediction'), ('05_outro_02_predict', 'dormant', '05b_deltatowers_prediction'), ('05_outro_03_predict', 'dormant', '05b_deltatowers_prediction'), ('05_outro_04_predict', 'dormant', '05b_deltatowers_prediction'), ('05_outro_05_predict', 'dormant', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_prediction'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('void', 'static', '05b_deltatowers_teleport'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/06a_sentinelwalls/06a_sentinelwalls': {
        "objects": {
            'absorber_a': {'category': 'object', 'funcs': ['object_destroy', 'object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_b': {'category': 'object', 'funcs': ['object_destroy', 'object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_c': {'category': 'object', 'funcs': ['object_destroy', 'object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_d': {'category': 'object', 'funcs': ['object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_e': {'category': 'object', 'funcs': ['object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_f': {'category': 'object', 'funcs': ['object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_g': {'category': 'object', 'funcs': ['object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_h': {'category': 'object', 'funcs': ['object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_i': {'category': 'object', 'funcs': ['object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_ins': {'category': 'object', 'funcs': ['object_destroy', 'object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_ledge_b': {'category': 'object', 'funcs': ['object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_ledge_c': {'category': 'object', 'funcs': ['object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'absorber_plug_landing': {'category': 'object', 'funcs': ['object_get_shield'], 'sources': ['sentinelwalls_mission']},
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['sentinelwalls_mission']},
            'ai_current_squad': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['sentinelwalls_mission']},
            'brute_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'brute_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'brute_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'brute_04': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'brute_hg_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'brute_hg_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'brute_hg_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'brutes_01': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['sentinelwalls_cinematics']},
            'brutes_02': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['sentinelwalls_cinematics']},
            'carbine': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'commander': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'cond_a_cov': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_a': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_c': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_e': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_f': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_g': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_h': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_i': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_j': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_k': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_l': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_m': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_n': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_em_o': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_a/a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_a/c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_a/e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_a/f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_a/g': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_a/h': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_b/i': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_b/j': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_b/k': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_b/l': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_b/m': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_b/n': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_b/o': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sen_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_a_sentinels': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'cond_b_carrier_a': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_enforcer': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_set_orders'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_a_ini_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_a_ini_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_a_ini_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_b_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_c_ini_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_c_ini_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_flood_tube_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_humans': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_humans/a': {'category': 'human', 'funcs': ['ai_kill'], 'sources': ['sentinelwalls_mission']},
            'cond_b_humans/b': {'category': 'human', 'funcs': ['ai_kill'], 'sources': ['sentinelwalls_mission']},
            'cond_b_humans/c': {'category': 'human', 'funcs': ['ai_kill'], 'sources': ['sentinelwalls_mission']},
            'cond_b_infection_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_b': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_b/1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_b/2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_b/3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_b/4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_b/a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_b/b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_tube_b/a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_tube_b/b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_tube_b/c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'cond_b_sen_tube_b/d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'constructors': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['sentinelwalls_mission']},
            'containment_field': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'covenant': {'category': 'object', 'funcs': ['ai_allegiance', 'ai_living_count', 'ai_magically_see', 'ai_set_orders'], 'sources': ['sentinelwalls_cinematics', 'sentinelwalls_mission']},
            'delta_halo': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'dervish': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['sentinelwalls_cinematics']},
            'elite_hg_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'elite_hg_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'elites_01': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['sentinelwalls_cinematics']},
            'elites_02': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['sentinelwalls_cinematics']},
            'elites_03': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['sentinelwalls_cinematics']},
            'factory': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'gap_phantom': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'group_a': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_b': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_c': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_d': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_e': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_f': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_g': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_h': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_i': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_ins': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_ledge_b': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_ledge_c': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_plug_a': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_plug_b': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_plug_c': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_plug_d': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'group_plug_landing': {'category': 'object', 'funcs': ['device_group_get'], 'sources': ['sentinelwalls_mission']},
            'hall_a_con_bk': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_a_con_ini': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_a_cons': {'category': 'object', 'funcs': ['ai_strength'], 'sources': ['sentinelwalls_mission']},
            'hall_a_em_c': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'hall_a_em_d': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'hall_a_em_g': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'hall_a_em_h': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'hall_a_sen': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_a_sen/c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_a_sen/d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_a_sen/g': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_a_sen/h': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_a_sentinels': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'hall_b_cov': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_b_em_b': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'hall_b_em_d': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'hall_b_em_e': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'hall_b_em_f': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'hall_b_em_g': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'hall_b_sen': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_b_sen/b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_b_sen/d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_b_sen/e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_b_sen/f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_b_sen/g': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_b_sentinels': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'hall_c_carrier_c': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_carrier_d': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_carrier_e': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_flood': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['sentinelwalls_mission']},
            'hall_c_flood_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_flood_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_flood_e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_flood_f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_flood_far': {'category': 'covenant', 'funcs': ['ai_magically_see', 'ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_flood_mid': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_flood_near': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_infec': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_marines': {'category': 'human', 'funcs': ['ai_magically_see', 'ai_place'], 'sources': ['sentinelwalls_mission']},
            'hall_c_marines/a': {'category': 'human', 'funcs': ['ai_kill'], 'sources': ['sentinelwalls_mission']},
            'hall_c_marines/b': {'category': 'human', 'funcs': ['ai_kill'], 'sources': ['sentinelwalls_mission']},
            'hall_c_marines/c': {'category': 'human', 'funcs': ['ai_kill'], 'sources': ['sentinelwalls_mission']},
            'hall_c_marines/d': {'category': 'human', 'funcs': ['ai_kill'], 'sources': ['sentinelwalls_mission']},
            'hall_c_sen_tube': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'index_holo': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'ins_con_bk': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['sentinelwalls_mission']},
            'ins_con_mid': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['sentinelwalls_mission']},
            'ins_con_slide': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ins_cons': {'category': 'object', 'funcs': ['ai_strength'], 'sources': ['sentinelwalls_mission']},
            'ins_em_a': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ins_em_b': {'category': 'object', 'funcs': ['object_destroy', 'object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ins_em_c': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'insertion_sen': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'insertion_sentinels': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'intro_sen_maj': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'intro_turret': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'intro_turret_base': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'ledge_a_door_a': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_door_b': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_door_c': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_door_d': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_door_e': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_door_f': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_em_a': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_em_b': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_em_c': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_em_d': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_em_e': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_em_f': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_em_g': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_em_h': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_em_i': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_enforcer': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_bot_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_bot_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_d1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_d2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_dead': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_flood_ini': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen/a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen/b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen/c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen/d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen/e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen/f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen/g': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen/h': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen/i': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sen_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_a_sentinels': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'ledge_b_flood': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_b_sen': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_c_flood': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_magically_see'], 'sources': ['sentinelwalls_mission']},
            'ledge_c_flood_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_c_flood_dead': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_c_flood_fr': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_c_infec_fr': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'ledge_c_phantom': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'matte_mount_doom': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'matte_stardust': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'matte_substance': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'mercy': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'monitor': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'phantom_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'phantom_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'phantom_int': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'piston_a': {'category': 'object', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'piston_b': {'category': 'object', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'piston_c': {'category': 'object', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'piston_d': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'piston_e': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'piston_f': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'piston_g': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'piston_h': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'piston_i': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'piston_ins': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'piston_ledge_b': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'piston_ledge_c': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'piston_plug_landing': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['sentinelwalls_mission']},
            'plug': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['sentinelwalls_mission']},
            'plug_door_a': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_door_b': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_em_a': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_em_b': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_em_c': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_em_d': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_em_e': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_em_f': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_sen': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_sen/a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_sen/b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_sen/c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_sen/d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_sen/e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_bk_sen/f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_em_a': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_em_b': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_em_d': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_em_f': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_em_h': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_em_i': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_enforcer': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_flood': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_flood_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_flood_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_flood_bk': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_flood_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_flood_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sen': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sen/a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sen/b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sen/d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sen/f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sen/h': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sen/i': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sen_elim': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sentinels': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['sentinelwalls_mission']},
            'plug_holder_sentinels_bk': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'plug_intro': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'plug_keylock_a': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_keylock_b': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_keylock_c': {'category': 'object', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'plug_keylock_d': {'category': 'object', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_em_a': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_em_b': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_em_c': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_em_d': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_em_e': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_em_f': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_em_g': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_enforcer': {'category': 'covenant', 'funcs': ['ai_kill', 'ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sen': {'category': 'covenant', 'funcs': ['ai_kill', 'ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sen/a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sen/b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sen/c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sen/d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sen/e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sen/f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sen/g': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sen/h': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plug_launch_sentinels': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['sentinelwalls_mission']},
            'plug_lock_a': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_lock_b': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_lock_c': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_lock_d': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_lock_e': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_lock_f': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_switch': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'device_set_power', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'plug_switch_housing': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_thick_bl': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_thick_br': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_thick_fl': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_thick_fr': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_thin_bl': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_thin_br': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_thin_fl': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plug_thin_fr': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plugabsorber01': {'category': 'object', 'funcs': ['object_destroy', 'object_get_shield', 'object_set_shield'], 'sources': ['sentinelwalls_mission']},
            'plugabsorber02': {'category': 'object', 'funcs': ['object_destroy', 'object_get_shield', 'object_set_shield'], 'sources': ['sentinelwalls_mission']},
            'plugabsorber03': {'category': 'object', 'funcs': ['object_destroy', 'object_get_shield', 'object_set_shield'], 'sources': ['sentinelwalls_mission']},
            'plugabsorber04': {'category': 'object', 'funcs': ['object_destroy', 'object_get_shield', 'object_set_shield'], 'sources': ['sentinelwalls_mission']},
            'plugabsorber05': {'category': 'object', 'funcs': ['object_get_shield', 'object_set_shield'], 'sources': ['sentinelwalls_mission']},
            'plugabsorber06': {'category': 'object', 'funcs': ['object_get_shield', 'object_set_shield'], 'sources': ['sentinelwalls_mission']},
            'plugabsorber07': {'category': 'object', 'funcs': ['object_get_shield', 'object_set_shield'], 'sources': ['sentinelwalls_mission']},
            'plugabsorber08': {'category': 'object', 'funcs': ['object_get_shield', 'object_set_shield'], 'sources': ['sentinelwalls_mission']},
            'plugholder_bk_flood_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plugholder_bk_flood_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plugholder_bk_infec_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plugholder_bk_infec_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plugholder_door': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_mission']},
            'plugholder_lower_hall_flood': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plugholder_lower_hall_infec': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'plugholder_sen_bk_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'prophet': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['sentinelwalls_mission']},
            'pussy_grunt': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders', 'ai_strength'], 'sources': ['sentinelwalls_mission']},
            'qz_camp_turrets': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_carrier': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_cov': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders', 'ai_vehicle_exit'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_flood': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_flood_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_flood_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_flood_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_flood_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_flood_e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_flood_f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_flood_g': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_flood_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_cov_def_soc': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['sentinelwalls_mission']},
            'qz_door': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['sentinelwalls_mission']},
            'qz_ent_pod_a': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'qz_ent_pod_b': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'qz_ent_pod_c': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'qz_ent_pod_d': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'qz_ent_pod_e': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['sentinelwalls_mission']},
            'qz_ini_flood': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders', 'ai_vehicle_enter'], 'sources': ['sentinelwalls_mission']},
            'qz_ini_ins_pods': {'category': 'object', 'funcs': ['ai_migrate', 'ai_vehicle_exit'], 'sources': ['sentinelwalls_mission']},
            'qz_ini_ins_pods/a': {'category': 'object', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['sentinelwalls_mission']},
            'qz_ini_ins_pods/b': {'category': 'object', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['sentinelwalls_mission']},
            'qz_ini_ins_pods/c': {'category': 'object', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['sentinelwalls_mission']},
            'qz_ini_ins_pods/d': {'category': 'object', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['sentinelwalls_mission']},
            'qz_ini_ins_pods/e': {'category': 'object', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['sentinelwalls_mission']},
            'qz_ini_turrets': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_ini_turrets/a': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_initial_flood_bridge': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_initial_flood_camp': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_initial_flood_carrier_camp': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_initial_flood_carrier_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_initial_flood_cave': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_initial_flood_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'qz_phantom': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['sentinelwalls_mission']},
            'sanctum_door': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['sentinelwalls_cinematics']},
            'scene_trigger_4': {'category': 'volume', 'funcs': ['ai_trigger_test'], 'sources': ['sentinelwalls_mission']},
            'so_elite_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'so_elite_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'tartarus': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'texture_halo': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'throne_mercy': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'throne_truth': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'truth': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'tv_cond_a_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_cond_a_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_cond_b_a1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_cond_b_a2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_cond_b_b1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_cond_b_b2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_cond_b_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_cond_b_hum_dead': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_conduit_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_conduit_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_cov_defense': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_game_won': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_a_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_b_fr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_c_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_c_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_c_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_c_d': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_c_e': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_hall_c_f': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ins_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ins_slide_bottom': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_insertion_tube': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a_bot_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a_bot_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a_top_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a_top_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a_top_d1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a_top_d2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a_top_e': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a_top_f': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_a_top_g': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_c_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_ledge_c_fr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_music_06a_10': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_plug_land': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_plug_launch': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_plugholder_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_plugholder_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_plugholder_d': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_plugholder_e': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_plugholder_f': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_pussy_grunt': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_qz_bridge': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_qz_camp': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_qz_cave': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_qz_cov_def_hill': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_qz_initial': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_slide_a': {'category': 'object', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'tv_slide_b': {'category': 'object', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['sentinelwalls_mission']},
            'x06_helmet': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['sentinelwalls_cinematics']},
            'x06_pike_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'x06_pike_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
            'x06_pike_03': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['sentinelwalls_cinematics']},
        },
        "scripts": [('void', 'stub', 'sentinelwalls_cinematics'), ('void', 'stub', 'sentinelwalls_cinematics'), ('void', 'stub', 'sentinelwalls_cinematics'), ('void', 'stub', 'sentinelwalls_cinematics'), ('void', 'stub', 'sentinelwalls_cinematics'), ('void', 'stub', 'sentinelwalls_cinematics'), ('void', 'stub', 'sentinelwalls_cinematics'), ('void', 'stub', 'sentinelwalls_cinematics'), ('cs_brute_walk_01', 'command_script', 'sentinelwalls_cinematics'), ('cs_brute_walk_02', 'command_script', 'sentinelwalls_cinematics'), ('cs_elite_walk_01', 'command_script', 'sentinelwalls_cinematics'), ('cs_elite_walk_02', 'command_script', 'sentinelwalls_cinematics'), ('exchange_of_hats', 'dormant', 'sentinelwalls_cinematics'), ('x06_score_01a', 'dormant', 'sentinelwalls_cinematics'), ('x06_foley_01a', 'dormant', 'sentinelwalls_cinematics'), ('x06_supratitle_01', 'dormant', 'sentinelwalls_cinematics'), ('cinematic_lighting_scene_01a', 'dormant', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('cs_elite_walk_03', 'command_script', 'sentinelwalls_cinematics'), ('final_hg_walk', 'dormant', 'sentinelwalls_cinematics'), ('x06_foley_01b', 'dormant', 'sentinelwalls_cinematics'), ('x06_01b_dof_1', 'dormant', 'sentinelwalls_cinematics'), ('cinematic_lighting_scene_01b', 'dormant', 'sentinelwalls_cinematics'), ('x06_texture_camera_01b_01', 'dormant', 'sentinelwalls_cinematics'), ('open_sanctum_door', 'dormant', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('x06_foley_02', 'dormant', 'sentinelwalls_cinematics'), ('x06_0010_soc', 'dormant', 'sentinelwalls_cinematics'), ('x06_0020_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0030_soc', 'dormant', 'sentinelwalls_cinematics'), ('x06_0040_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0050_soc', 'dormant', 'sentinelwalls_cinematics'), ('x06_0060_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0070_soc', 'dormant', 'sentinelwalls_cinematics'), ('cinematic_lighting_scene_02', 'dormant', 'sentinelwalls_cinematics'), ('x06_texture_camera_02_01', 'dormant', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('x06_foley_03', 'dormant', 'sentinelwalls_cinematics'), ('x06_0080_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0090_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0100_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0110_der', 'dormant', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('x06_score_04', 'dormant', 'sentinelwalls_cinematics'), ('x06_foley_04', 'dormant', 'sentinelwalls_cinematics'), ('x06_0120_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0130_pom', 'dormant', 'sentinelwalls_cinematics'), ('x06_0140_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0150_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0160_pom', 'dormant', 'sentinelwalls_cinematics'), ('x06_fov_01', 'dormant', 'sentinelwalls_cinematics'), ('x06_04_dof_1', 'dormant', 'sentinelwalls_cinematics'), ('x06_04_dof_2', 'dormant', 'sentinelwalls_cinematics'), ('unhide_dervish', 'dormant', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('x06_foley_05', 'dormant', 'sentinelwalls_cinematics'), ('x06_0170_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0180_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0190_pom', 'dormant', 'sentinelwalls_cinematics'), ('x06_0200_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0210_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_0220_pom', 'dormant', 'sentinelwalls_cinematics'), ('x06_0230_pot', 'dormant', 'sentinelwalls_cinematics'), ('x06_05_dof_1', 'dormant', 'sentinelwalls_cinematics'), ('x06_05_dof_2', 'dormant', 'sentinelwalls_cinematics'), ('x06_texture_camera_05_01', 'dormant', 'sentinelwalls_cinematics'), ('monitor_sound', 'dormant', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('c06_intro_sound_scene1_01', 'dormant', 'sentinelwalls_cinematics'), ('c06_intro_foley_01', 'dormant', 'sentinelwalls_cinematics'), ('c06_1010_tar', 'dormant', 'sentinelwalls_cinematics'), ('c06_1020_tar', 'dormant', 'sentinelwalls_cinematics'), ('c06_1030_tar', 'dormant', 'sentinelwalls_cinematics'), ('c06_1040_der', 'dormant', 'sentinelwalls_cinematics'), ('c06_1050_tar', 'dormant', 'sentinelwalls_cinematics'), ('c06_1060_der', 'dormant', 'sentinelwalls_cinematics'), ('c06_1070_tar', 'dormant', 'sentinelwalls_cinematics'), ('c06_1080_tar', 'dormant', 'sentinelwalls_cinematics'), ('c06_1090_tar', 'dormant', 'sentinelwalls_cinematics'), ('c06_1100_der', 'dormant', 'sentinelwalls_cinematics'), ('c06_1110_tar', 'dormant', 'sentinelwalls_cinematics'), ('camera_shake_01', 'dormant', 'sentinelwalls_cinematics'), ('cinematic_light_intro_scene_01', 'dormant', 'sentinelwalls_cinematics'), ('cinematic_light_phantom_int', 'dormant', 'sentinelwalls_cinematics'), ('c06_problem_actors_01', 'dormant', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('c06_intro_sound_scene2_01', 'dormant', 'sentinelwalls_cinematics'), ('c06_intro_sound_scene2_02', 'dormant', 'sentinelwalls_cinematics'), ('c06_intro_sound_scene2_03', 'dormant', 'sentinelwalls_cinematics'), ('c06_intro_foley_02', 'dormant', 'sentinelwalls_cinematics'), ('c06_1120_tar', 'dormant', 'sentinelwalls_cinematics'), ('c06_1130_tar', 'dormant', 'sentinelwalls_cinematics'), ('x06_01_dof_1', 'dormant', 'sentinelwalls_cinematics'), ('arbiter_fires', 'dormant', 'sentinelwalls_cinematics'), ('phantom_fires', 'dormant', 'sentinelwalls_cinematics'), ('c06_intro_predict_ledge_01', 'dormant', 'sentinelwalls_cinematics'), ('c06_intro_predict_ledge_02', 'dormant', 'sentinelwalls_cinematics'), ('create_dervish_again', 'dormant', 'sentinelwalls_cinematics'), ('dervish_unhide', 'dormant', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'static', 'sentinelwalls_cinematics'), ('void', 'stub', 'sentinelwalls_mission'), ('void', 'stub', 'sentinelwalls_mission'), ('difficulty_settings', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('die', 'command_script', 'sentinelwalls_mission'), ('ice_cream_mythic', 'dormant', 'sentinelwalls_mission'), ('chapter_silence', 'dormant', 'sentinelwalls_mission'), ('chapter_remorse', 'dormant', 'sentinelwalls_mission'), ('chapter_war', 'dormant', 'sentinelwalls_mission'), ('objective_lower_set', 'dormant', 'sentinelwalls_mission'), ('objective_lower_clear', 'dormant', 'sentinelwalls_mission'), ('objective_lower_specific_set', 'dormant', 'sentinelwalls_mission'), ('objective_lower_specific_clear', 'dormant', 'sentinelwalls_mission'), ('objective_floodwall_set', 'dormant', 'sentinelwalls_mission'), ('objective_floodwall_clear', 'dormant', 'sentinelwalls_mission'), ('objective_rendezvous_set', 'dormant', 'sentinelwalls_mission'), ('objective_rendezvous_clear', 'dormant', 'sentinelwalls_mission'), ('training_absorber', 'dormant', 'sentinelwalls_mission'), ('music_06a_01', 'dormant', 'sentinelwalls_mission'), ('music_06a_03', 'dormant', 'sentinelwalls_mission'), ('music_06a_04', 'dormant', 'sentinelwalls_mission'), ('music_06a_05', 'dormant', 'sentinelwalls_mission'), ('music_06a_06', 'dormant', 'sentinelwalls_mission'), ('music_06a_07', 'dormant', 'sentinelwalls_mission'), ('music_06a_08', 'dormant', 'sentinelwalls_mission'), ('music_06a_09', 'dormant', 'sentinelwalls_mission'), ('music_06a_10', 'dormant', 'sentinelwalls_mission'), ('sc_cond_cov', 'command_script', 'sentinelwalls_mission'), ('ai_sc_cond_a_cov', 'dormant', 'sentinelwalls_mission'), ('sc_tartarus_reminder', 'dormant', 'sentinelwalls_mission'), ('sc_fleeing_grunts', 'command_script', 'sentinelwalls_mission'), ('ai_sc_hall_b_grunts', 'dormant', 'sentinelwalls_mission'), ('sc_enforcer', 'dormant', 'sentinelwalls_mission'), ('sc_plug_launch', 'dormant', 'sentinelwalls_mission'), ('sc_plug_ride', 'dormant', 'sentinelwalls_mission'), ('sc_marines_a', 'dormant', 'sentinelwalls_mission'), ('sc_marines_b', 'dormant', 'sentinelwalls_mission'), ('cs_sc_qz_ini', 'command_script', 'sentinelwalls_mission'), ('sc_qz_initial', 'dormant', 'sentinelwalls_mission'), ('cs_cov_camp_elite1', 'command_script', 'sentinelwalls_mission'), ('cs_cov_camp_elite2', 'command_script', 'sentinelwalls_mission'), ('cs_cov_camp_elite3', 'command_script', 'sentinelwalls_mission'), ('cs_cov_camp_elite4', 'command_script', 'sentinelwalls_mission'), ('cs_cov_camp_elite5', 'command_script', 'sentinelwalls_mission'), ('cs_cov_camp_elite6', 'command_script', 'sentinelwalls_mission'), ('cs_cov_camp_comm', 'command_script', 'sentinelwalls_mission'), ('cs_cov_camp_elites', 'command_script', 'sentinelwalls_mission'), ('cs_cov_camp_soc', 'command_script', 'sentinelwalls_mission'), ('sc_qz_cov_camp', 'dormant', 'sentinelwalls_mission'), ('attach_absorbers_1', 'dormant', 'sentinelwalls_mission'), ('attach_absorbers_1b', 'dormant', 'sentinelwalls_mission'), ('attach_controls_1', 'dormant', 'sentinelwalls_mission'), ('attach_controls_1b', 'dormant', 'sentinelwalls_mission'), ('open_piston_ins', 'dormant', 'sentinelwalls_mission'), ('open_piston_a', 'dormant', 'sentinelwalls_mission'), ('open_piston_b', 'dormant', 'sentinelwalls_mission'), ('open_piston_c', 'dormant', 'sentinelwalls_mission'), ('open_piston_d', 'dormant', 'sentinelwalls_mission'), ('open_piston_plug_landing', 'dormant', 'sentinelwalls_mission'), ('open_piston_e', 'dormant', 'sentinelwalls_mission'), ('open_piston_f', 'dormant', 'sentinelwalls_mission'), ('open_piston_g', 'dormant', 'sentinelwalls_mission'), ('open_piston_h', 'dormant', 'sentinelwalls_mission'), ('open_piston_i', 'dormant', 'sentinelwalls_mission'), ('open_piston_ledge_b', 'dormant', 'sentinelwalls_mission'), ('open_piston_ledge_c', 'dormant', 'sentinelwalls_mission'), ('piston_control', 'dormant', 'sentinelwalls_mission'), ('cs_pussy_grunt_abort', 'command_script', 'sentinelwalls_mission'), ('pussy_grunt_abort', 'dormant', 'sentinelwalls_mission'), ('pussy_grunt_down', 'command_script', 'sentinelwalls_mission'), ('pussy_grunt_shoot', 'command_script', 'sentinelwalls_mission'), ('pussy_grunt', 'dormant', 'sentinelwalls_mission'), ('cs_pussy_grunt', 'command_script', 'sentinelwalls_mission'), ('pussy_grunt_reminder', 'dormant', 'sentinelwalls_mission'), ('cs_miniaturize', 'command_script', 'sentinelwalls_mission'), ('cs_big', 'command_script', 'sentinelwalls_mission'), ('cs_ins_weld_a', 'command_script', 'sentinelwalls_mission'), ('cs_ins_weld_b', 'command_script', 'sentinelwalls_mission'), ('cs_ins_weld_c', 'command_script', 'sentinelwalls_mission'), ('cs_ins_shoot_absorber_slide', 'command_script', 'sentinelwalls_mission'), ('ins_open_door_slide', 'dormant', 'sentinelwalls_mission'), ('cs_ins_runaway', 'command_script', 'sentinelwalls_mission'), ('cs_ins_shoot_absorber', 'command_script', 'sentinelwalls_mission'), ('ins_open_door', 'dormant', 'sentinelwalls_mission'), ('ai_insertion_emitters', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_hall_a_emitters', 'dormant', 'sentinelwalls_mission'), ('ai_hall_a_const', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_cond_a_emitters_fr', 'dormant', 'sentinelwalls_mission'), ('ai_cond_a_emitters_bk', 'dormant', 'sentinelwalls_mission'), ('ai_cond_a_back_ini', 'dormant', 'sentinelwalls_mission'), ('cs_cond_a_sen_e', 'command_script', 'sentinelwalls_mission'), ('cond_a_delay', 'dormant', 'sentinelwalls_mission'), ('cond_a_initial_delay', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_hall_b_emitters', 'dormant', 'sentinelwalls_mission'), ('cs_plug_launch_enforcer', 'command_script', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_plug_launch_em', 'dormant', 'sentinelwalls_mission'), ('short', 'static', 'sentinelwalls_mission'), ('short', 'static', 'sentinelwalls_mission'), ('short', 'static', 'sentinelwalls_mission'), ('short', 'static', 'sentinelwalls_mission'), ('short', 'static', 'sentinelwalls_mission'), ('short', 'static', 'sentinelwalls_mission'), ('short', 'static', 'sentinelwalls_mission'), ('short', 'static', 'sentinelwalls_mission'), ('short', 'static', 'sentinelwalls_mission'), ('plug_rods08', 'dormant', 'sentinelwalls_mission'), ('plug_rods07', 'dormant', 'sentinelwalls_mission'), ('plug_rods06', 'dormant', 'sentinelwalls_mission'), ('plug_rods05', 'dormant', 'sentinelwalls_mission'), ('plug_rods04', 'dormant', 'sentinelwalls_mission'), ('plug_rods03', 'dormant', 'sentinelwalls_mission'), ('plug_rods02', 'dormant', 'sentinelwalls_mission'), ('plug_rods01', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('plug_absorbers', 'dormant', 'sentinelwalls_mission'), ('cs_gap_phantom', 'command_script', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('lower_shield', 'dormant', 'sentinelwalls_mission'), ('bsp0_cleanup', 'dormant', 'sentinelwalls_mission'), ('cs_move_plug', 'dormant', 'sentinelwalls_mission'), ('cs_gap_flood_jump', 'command_script', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('invulnerable', 'command_script', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('close_plugholder_door', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_plug_holder_em', 'dormant', 'sentinelwalls_mission'), ('ai_plug_holder_em_elim', 'dormant', 'sentinelwalls_mission'), ('ai_plug_holder_flood', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_plug_holder_bk_em', 'dormant', 'sentinelwalls_mission'), ('ai_plugholder_flood_bk', 'dormant', 'sentinelwalls_mission'), ('ai_plugholder_infec_bk_a', 'dormant', 'sentinelwalls_mission'), ('ai_plugholder_infec_bk_b', 'dormant', 'sentinelwalls_mission'), ('kill_hall_c_marines', 'dormant', 'sentinelwalls_mission'), ('ai_hall_c_ini', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_hall_c_flood_spawn', 'dormant', 'sentinelwalls_mission'), ('ai_ledge_a_initial', 'dormant', 'sentinelwalls_mission'), ('ai_ledge_a_location', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_ledge_a_flood_spawn', 'dormant', 'sentinelwalls_mission'), ('ai_ledge_a_flood_bot_a', 'dormant', 'sentinelwalls_mission'), ('ai_ledge_a_flood_bot_b', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_ledge_a_emitters', 'dormant', 'sentinelwalls_mission'), ('kill_cond_b_marines', 'dormant', 'sentinelwalls_mission'), ('conduit_b_locator', 'dormant', 'sentinelwalls_mission'), ('ai_cond_b_carrier_a', 'dormant', 'sentinelwalls_mission'), ('cs_cond_b_damage_enf', 'command_script', 'sentinelwalls_mission'), ('ai_cond_b_b_em', 'dormant', 'sentinelwalls_mission'), ('ai_cond_b_flood_spawn', 'dormant', 'sentinelwalls_mission'), ('cs_cond_b_sen_tube_a', 'command_script', 'sentinelwalls_mission'), ('cs_cond_b_sen_tube_b', 'command_script', 'sentinelwalls_mission'), ('ai_cond_b_sen_tube_b', 'dormant', 'sentinelwalls_mission'), ('slide_a_player0', 'dormant', 'sentinelwalls_mission'), ('slide_a_player1', 'dormant', 'sentinelwalls_mission'), ('slide_b_player0', 'dormant', 'sentinelwalls_mission'), ('slide_b_player1', 'dormant', 'sentinelwalls_mission'), ('ai_ledge_c_flood_ini', 'dormant', 'sentinelwalls_mission'), ('ai_ledge_c_infection_spawn', 'dormant', 'sentinelwalls_mission'), ('cs_ledge_c_phantom', 'command_script', 'sentinelwalls_mission'), ('cs_mortar_a', 'dormant', 'sentinelwalls_mission'), ('cs_mortar_b', 'dormant', 'sentinelwalls_mission'), ('cs_go_to_bridge', 'command_script', 'sentinelwalls_mission'), ('ai_cov_ins_pod_a', 'dormant', 'sentinelwalls_mission'), ('ai_cov_ins_pod_b', 'dormant', 'sentinelwalls_mission'), ('ai_cov_ins_pod_c', 'dormant', 'sentinelwalls_mission'), ('ai_cov_ins_pod_d', 'dormant', 'sentinelwalls_mission'), ('ai_cov_ins_pod_e', 'dormant', 'sentinelwalls_mission'), ('ai_qz_ini_turrets', 'dormant', 'sentinelwalls_mission'), ('ai_cov_ins_pods', 'dormant', 'sentinelwalls_mission'), ('ai_qz_ini_exit_turrets', 'dormant', 'sentinelwalls_mission'), ('cs_crash_factory', 'dormant', 'sentinelwalls_mission'), ('ai_qz_ini_flood', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('ai_qz_cov_def_flood_spawn', 'dormant', 'sentinelwalls_mission'), ('ai_qz_cov_def_carrier', 'dormant', 'sentinelwalls_mission'), ('you_win', 'dormant', 'sentinelwalls_mission'), ('cs_qz_phantom', 'command_script', 'sentinelwalls_mission'), ('enc_insertion', 'dormant', 'sentinelwalls_mission'), ('enc_hall_a', 'dormant', 'sentinelwalls_mission'), ('enc_conduit_a', 'dormant', 'sentinelwalls_mission'), ('enc_hall_b', 'dormant', 'sentinelwalls_mission'), ('enc_plug_launch', 'dormant', 'sentinelwalls_mission'), ('enc_plug_landing', 'dormant', 'sentinelwalls_mission'), ('enc_hall_c', 'dormant', 'sentinelwalls_mission'), ('enc_ledge_a', 'dormant', 'sentinelwalls_mission'), ('enc_conduit_b', 'dormant', 'sentinelwalls_mission'), ('enc_ledge_b', 'dormant', 'sentinelwalls_mission'), ('enc_ledge_c', 'dormant', 'sentinelwalls_mission'), ('enc_qz_initial', 'dormant', 'sentinelwalls_mission'), ('enc_cov_defense', 'dormant', 'sentinelwalls_mission'), ('mission_sentinelwalls', 'dormant', 'sentinelwalls_mission'), ('void', 'static', 'sentinelwalls_mission'), ('mission_main', 'startup', 'sentinelwalls_mission'), ('x06_01a_predict', 'dormant', 'sentinelwalls_prediction'), ('x06_01b_predict', 'dormant', 'sentinelwalls_prediction'), ('x06_02_predict', 'dormant', 'sentinelwalls_prediction'), ('x06_03_predict', 'dormant', 'sentinelwalls_prediction'), ('x06_04_predict', 'dormant', 'sentinelwalls_prediction'), ('x06_05_predict', 'dormant', 'sentinelwalls_prediction'), ('06_intro_01_predict', 'dormant', 'sentinelwalls_prediction'), ('06_intro_02_predict', 'dormant', 'sentinelwalls_prediction'), ('void', 'static', 'sentinelwalls_prediction'), ('void', 'static', 'sentinelwalls_prediction'), ('void', 'static', 'sentinelwalls_prediction'), ('void', 'static', 'sentinelwalls_prediction'), ('void', 'static', 'sentinelwalls_prediction'), ('void', 'static', 'sentinelwalls_prediction'), ('void', 'static', 'sentinelwalls_prediction'), ('void', 'static', 'sentinelwalls_prediction'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('void', 'static', 'sentinelwalls_teleport'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/07a_highcharity/07a_highcharity': {
        "objects": {
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['highcharity_mission']},
            'all_enemies': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'brute_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'brute_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'brute_03': {'category': 'covenant', 'funcs': ['object_cannot_take_damage', 'object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'brute_04': {'category': 'covenant', 'funcs': ['object_cannot_take_damage', 'object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'brute_05': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'brute_06': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'brute_intro_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'brute_intro_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'brute_intro_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'brute_intro_04': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'c07_infection': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['highcharity_cinematics', 'highcharity_mission']},
            'cell_a_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'cell_b_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'chief': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'chief_intro': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'chief_needler': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'corridor_b_covenant': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'corridor_b_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'cortana_0/a': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_0/b': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_0/f': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_0/i': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_3a/tram_a': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_corridor_a/o': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_grand_b/b': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_jail/a': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_jail/b': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_jail/h': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_jail/n': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_jail/p': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_jail/q': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_maus/a': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_maus/f': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_maus/j': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'cortana_room_a/m': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_brute_ini': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'council_brute_ped/a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_brute_ped/b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_brute_ped/c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_brute_ped/chief': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_door_left_a': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'council_door_left_b': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'council_door_left_c': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'council_door_right_a': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'council_door_right_b': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'council_door_right_c': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'council_exit': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['highcharity_mission']},
            'council_grunt_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_lt_brute_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_lt_brute_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_lt_brute_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_lt_grunt_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_lt_grunt_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_lt_grunt_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_lt_upper_brute_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_lt_upper_brute_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_lt_upper_brute_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_ped': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['highcharity_mission']},
            'council_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'council_prophets_floor': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'council_prophets_upper': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_strength'], 'sources': ['highcharity_mission']},
            'council_rt_brute_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_rt_brute_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_rt_brute_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_rt_grunt_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_rt_grunt_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_rt_grunt_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_rt_upper_brute_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_rt_upper_brute_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'council_rt_upper_brute_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'delta_halo': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_cinematics']},
            'dervish': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'dervish_ledge_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'dervish_lift_up': {'category': 'device', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['highcharity_mission']},
            'ext_a_brute_bk_door': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_brute_door': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ext_a_brute_ini': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ext_a_brutes_bk': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_buggers': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ext_a_buggers_bk': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_covenant': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ext_a_elite_ini': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_hunters': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_jackal_snipers_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_jackal_snipers_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_jackal_snipers_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_jackal_snipers_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'ext_a_rangers': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_a_watch_brutes': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ext_a_watch_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_brute_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_brute_ramp': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_brutes_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_brutes_low': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_brutes_low_door': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_covenant': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['highcharity_mission']},
            'ext_b_elite_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_elites_bk_door': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_elites_stealth': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_grunt_bk_door': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_grunts_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_grunts_low': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_grunts_lt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_jackal_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ext_b_prophets': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['highcharity_mission']},
            'garden_a_brute_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_brute_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_brute_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_brute_lt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_brute_rt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_brutes_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_covenant': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'garden_a_elite_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_elite_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_elite_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_elites_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_grunts_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_jackal_snipers': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_jackals_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_a_prophet': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'garden_a_rangers': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_b_brute_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_b_grunt_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_b_grunt_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_b_grunt_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'garden_b_prophet': {'category': 'covenant', 'funcs': ['ai_magically_see'], 'sources': ['highcharity_mission']},
            'garden_tram_a_bk': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['highcharity_mission']},
            'garden_tram_b_bk': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['highcharity_mission']},
            'grand_a_brutes': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'grand_a_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'grand_a_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'grand_a_turret': {'category': 'device', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'grand_b_exit': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['highcharity_mission']},
            'grand_b_hunter_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'grand_b_hunter_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'grand_b_hunters': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'gravemind': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'grunt_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'grunt_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'grunt_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'grunt_04': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'grunt_05': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'grunt_card': {'category': 'covenant', 'funcs': ['object_destroy'], 'sources': ['highcharity_cinematics']},
            'hall_a_brute_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_a_brute_rein': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_a_brute_rein_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_a_grunt_rein': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_a_grunt_rein_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_a_jackal_door': {'category': 'covenant', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'hall_a_jackal_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_a_jackal_patrol_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_a_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'hall_b_brutes': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_b_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_b_grunts_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_b_jackal_door': {'category': 'covenant', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'hall_b_jackals': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_b_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'hall_c_brute_reins': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_c_bugger_reins': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_c_buggers': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_c_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_d_brutes': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_d_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_d_jackals_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hall_d_jackals_fr': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'hammer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'holo_cam': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'holo_generator': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['highcharity_mission']},
            'human': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['highcharity_mission']},
            'ice_cream_effect': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['highcharity_mission']},
            'ice_cream_grunt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'index': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'index_intro': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'infection_form_01': {'category': 'object', 'funcs': ['object_cannot_take_damage', 'object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'infection_form_02': {'category': 'object', 'funcs': ['object_cannot_take_damage', 'object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'intra_pike_01': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['highcharity_cinematics']},
            'intra_pike_02': {'category': 'object', 'funcs': ['object_hide'], 'sources': ['highcharity_cinematics']},
            'ioc': {'category': 'object', 'funcs': ['device_get_position', 'object_destroy'], 'sources': ['highcharity_mission']},
            'ioc_effect': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_mission']},
            'jackal_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'jackal_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'jail_a_brute': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_a_door_a': {'category': 'device', 'funcs': ['device_group_set'], 'sources': ['highcharity_mission']},
            'jail_a_door_b': {'category': 'device', 'funcs': ['device_group_set'], 'sources': ['highcharity_mission']},
            'jail_a_door_c': {'category': 'device', 'funcs': ['device_group_set'], 'sources': ['highcharity_mission']},
            'jail_a_jackals': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_a_marines': {'category': 'human', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'jail_a_needler': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_mission']},
            'jail_a_plasma_rifle': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_mission']},
            'jail_b_brutes': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_b_carbine': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_mission']},
            'jail_b_door_a': {'category': 'device', 'funcs': ['device_group_set'], 'sources': ['highcharity_mission']},
            'jail_b_door_b': {'category': 'device', 'funcs': ['device_group_set'], 'sources': ['highcharity_mission']},
            'jail_b_door_c': {'category': 'device', 'funcs': ['device_group_set'], 'sources': ['highcharity_mission']},
            'jail_b_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_b_marines': {'category': 'human', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'jail_b_plasma_pistol': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_mission']},
            'jail_b_plasma_rifle': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_mission']},
            'jail_brute_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brute_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brute_e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brute_f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brute_g': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brute_i': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brute_j': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brute_k': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brute_l': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brute_m': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brutes_down': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_brutes_ini': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['highcharity_mission']},
            'jail_cell_outer_guards_a': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['highcharity_mission']},
            'jail_cell_outer_guards_b': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['highcharity_mission']},
            'jail_door_c': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_door_d': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_door_e': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_door_f': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_door_g': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_door_i': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_door_j': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_door_k': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_door_l': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_door_m': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'jail_down': {'category': 'object', 'funcs': ['device_set_position', 'object_destroy'], 'sources': ['highcharity_mission']},
            'jail_grunt_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunt_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunt_e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunt_f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunt_g': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunt_i': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunt_j': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunt_k': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunt_l': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunt_m': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunts_down': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_grunts_ini': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'jail_guard_brute_cell_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_guard_brute_cell_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_guard_jackal_cell_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_guard_jackal_cell_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_g': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_i': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_j': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_k': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_l': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackal_m': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackals_down': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'jail_jackals_ini': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'jail_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'jail_up_effect': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['highcharity_mission']},
            'johnson': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'ledge_bot_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ledge_bot_jackals': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ledge_brutes_honor_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ledge_brutes_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'ledge_jackal_left': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ledge_jackal_right': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ledge_lift_brute_lt': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ledge_lift_brute_rt': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ledge_lift_chieftan': {'category': 'human', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ledge_lift_grunt_lt': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'ledge_lift_grunt_rt': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'marines': {'category': 'human', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'matte_high_charity': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_cinematics']},
            'matte_substance': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_cinematics']},
            'maus_bridge_brutes_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_bridge_buggers_ini': {'category': 'device', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_bridge_covenant': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_bridge_elite_rein': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_bridge_elite_turret': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_bridge_elites_ini': {'category': 'covenant', 'funcs': ['ai_place', 'ai_trigger_test'], 'sources': ['highcharity_mission']},
            'maus_bridge_grunt_rein': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_bridge_grunt_rein_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_bridge_hunters': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_bridge_jackals_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_bridge_prophets': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_door_end': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_ent_door_a': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_ent_door_b': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_hall_covenant': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_hall_elites_stealth': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_hall_grunts': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_brutes_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_brutes_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_brutes_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_brutes_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_brutes_e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_brutes_f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_brutes_ini': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_brutes_rein': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_buggers': {'category': 'object', 'funcs': ['ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_inner_buggers_lt': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_buggers_rt': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_covenant': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'maus_inner_door_a': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_inner_door_b': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_inner_door_c': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_inner_door_d': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_inner_door_e': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_inner_door_f': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_inner_elite_zealot': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_elites_ini': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_inner_elites_spec': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_elites_ultra': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_inner_ent': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'maus_inner_hunters_ini': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_inner_prophets': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_inner_turrets': {'category': 'device', 'funcs': ['ai_place', 'ai_set_orders', 'ai_vehicle_exit'], 'sources': ['highcharity_mission']},
            'maus_room_brute_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_covenant': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_room_elite_lt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_elite_rt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_grunt_lt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_grunt_rt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_jackal_bk_lt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_jackal_bk_rt': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_lt_elite_reins': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_lt_grunt_reins': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_prophet': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['highcharity_mission']},
            'maus_room_rt_elite_reins': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'maus_room_rt_grunt_reins': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'mercy': {'category': 'object', 'funcs': ['object_cannot_take_damage', 'object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'mercy_intro': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['highcharity_cinematics']},
            'mercy_no_crown': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'midtower_brutes': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'midtower_bugger_rein': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'midtower_buggers_hall': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'midtower_buggers_ini': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'midtower_covenant': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'midtower_elite_reins': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'midtower_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'midtower_ent_door': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'midtower_exit': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['highcharity_mission']},
            'midtower_jackals': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'midtower_prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'miranda': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'monitor': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'phantom_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'phantom_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'phantom_03': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['highcharity_mission']},
            'prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['highcharity_mission']},
            'regret': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'room_a_brutes_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_a_brutes_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_a_brutes_bk': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_a_brutes_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_a_brutes_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_a_door': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'room_a_grunts_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_a_grunts_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_a_grunts_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_a_jackals_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_a_lift': {'category': 'device', 'funcs': ['device_set_power'], 'sources': ['highcharity_mission']},
            'room_a_lift_effect': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['highcharity_mission']},
            'room_a_prophets': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['highcharity_mission']},
            'room_a_tube_fodder': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['highcharity_mission']},
            'room_b_brutes_ini': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_b_buggers': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['highcharity_mission']},
            'room_b_elites': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'room_b_exit': {'category': 'object', 'funcs': ['device_get_position'], 'sources': ['highcharity_mission']},
            'room_b_lift_effect': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['highcharity_mission']},
            'room_b_marines': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['highcharity_mission']},
            'tartarus': {'category': 'covenant', 'funcs': ['object_cannot_take_damage', 'object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'teleport': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['highcharity_cinematics']},
            'tentacle_arbiter': {'category': 'covenant', 'funcs': ['object_destroy'], 'sources': ['highcharity_cinematics']},
            'tentacle_capture_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['highcharity_cinematics']},
            'tentacle_capture_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['highcharity_cinematics']},
            'tentacle_capture_03': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['highcharity_cinematics']},
            'tentacle_capture_04': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['highcharity_cinematics']},
            'tentacle_capture_05': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'tentacle_chief': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'throne_mercy': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['highcharity_cinematics']},
            'throne_mercy_intro': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['highcharity_cinematics']},
            'throne_truth': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['highcharity_cinematics']},
            'throne_truth_intro': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['highcharity_cinematics']},
            'tram_a_bk_effect': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['highcharity_mission']},
            'tram_a_effect': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['highcharity_mission']},
            'truth': {'category': 'object', 'funcs': ['object_cannot_take_damage', 'object_cinematic_lod', 'object_destroy'], 'sources': ['highcharity_cinematics']},
            'truth_intro': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['highcharity_cinematics']},
            'tv_corridors_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_door_left_a': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_door_left_b': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_door_left_c': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_door_right_a': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_door_right_b': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_door_right_c': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_ext': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_fr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_hall': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_lt_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_lt_fr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_rt_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_council_rt_fr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_dervish_grand_hall': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_dervish_ledge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_dervish_ledge_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_dervish_ledge_fr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_dervish_ledge_lift': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_dervish_ledge_lower': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_ext_a_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_ext_a_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_ext_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_ext_b_low': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_ext_b_lt': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_game_won': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_garden_a_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_garden_a_fr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_garden_a_fr_suck': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_garden_a_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_garden_a_tram': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_garden_a_tram_b': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_garden_b_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_garden_b_fr': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_garden_b_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_gardens_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission', 'highcharity_teleport']},
            'tv_gardens_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission', 'highcharity_teleport']},
            'tv_grand_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_hall_a_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_hall_a_jackal_patrol': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_hall_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_hall_b_jackal': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_hall_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_hall_c_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_hall_d': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_ice_cream': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_a_ent': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_b_ent': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_bot': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_c': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_d': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_e': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_f': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_g': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_i': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_j': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_k': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_l': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_door_m': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jail_top': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_jails': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission', 'highcharity_teleport']},
            'tv_maus_bridge': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_bridge_bk': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_bridge_fr': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_bridge_mid': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_ent': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_ent_door_a': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_ent_door_b': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_inner_door_a': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_inner_door_b': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_inner_door_c': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_inner_door_d': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_inner_door_e': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_inner_door_f': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_inner_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_room': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_maus_room_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_mausoleum': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission', 'highcharity_teleport']},
            'tv_mausoleum_ext': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission', 'highcharity_teleport']},
            'tv_mid_tower': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission', 'highcharity_teleport']},
            'tv_mid_tower_room': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_midtower_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_midtower_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_room_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_room_a_bk': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_room_a_bot': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_room_a_mid': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_room_a_tube': {'category': 'object', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_room_b_start': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_sc_gardens_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_tower_a_ext': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission', 'highcharity_teleport']},
            'tv_tower_a_ramp': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_tower_b_ext': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission', 'highcharity_teleport']},
            'tv_tram_a_no_save': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_tram_b_no_save': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_tram_c_no_save': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
            'tv_tram_d_no_save': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['highcharity_mission']},
        },
        "scripts": [('cs_c07_infection', 'command_script', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_cinematics'), ('x08_score_01', 'dormant', 'highcharity_cinematics'), ('x08_foley_01', 'dormant', 'highcharity_cinematics'), ('blurry_vision', 'dormant', 'highcharity_cinematics'), ('x08_cinematic_light_01', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_02', 'dormant', 'highcharity_cinematics'), ('x08_0020_cor', 'dormant', 'highcharity_cinematics'), ('x08_0030_grv', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_03', 'dormant', 'highcharity_cinematics'), ('x08_0060_mas', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_04', 'dormant', 'highcharity_cinematics'), ('x08_0070_der', 'dormant', 'highcharity_cinematics'), ('x08_0080_grv', 'dormant', 'highcharity_cinematics'), ('x08_0090_grv', 'dormant', 'highcharity_cinematics'), ('x08_0100_der', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_05', 'dormant', 'highcharity_cinematics'), ('x08_0110_grv', 'dormant', 'highcharity_cinematics'), ('x08_0120_grv', 'dormant', 'highcharity_cinematics'), ('x08_0130_grv', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_06a', 'dormant', 'highcharity_cinematics'), ('x08_0140_pnt', 'dormant', 'highcharity_cinematics'), ('x08_0150_por', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_06b', 'dormant', 'highcharity_cinematics'), ('x08_0180_pnt', 'dormant', 'highcharity_cinematics'), ('x08_0190_pnt', 'dormant', 'highcharity_cinematics'), ('x08_0200_por', 'dormant', 'highcharity_cinematics'), ('x08_0210_por', 'dormant', 'highcharity_cinematics'), ('x08_0220_pnt', 'dormant', 'highcharity_cinematics'), ('x08_0230_por', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_06c', 'dormant', 'highcharity_cinematics'), ('x08_0240_pnt', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_07', 'dormant', 'highcharity_cinematics'), ('x08_0250_grv', 'dormant', 'highcharity_cinematics'), ('x08_0260_grv', 'dormant', 'highcharity_cinematics'), ('x08_0251_por', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_08', 'dormant', 'highcharity_cinematics'), ('x08_0270_grv', 'dormant', 'highcharity_cinematics'), ('x08_0280_grv', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_09', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_10', 'dormant', 'highcharity_cinematics'), ('x08_0340_mas', 'dormant', 'highcharity_cinematics'), ('x08_0350_der', 'dormant', 'highcharity_cinematics'), ('x08_0360_grv', 'dormant', 'highcharity_cinematics'), ('x08_0370_grv', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_foley_11', 'dormant', 'highcharity_cinematics'), ('x08_score_11', 'dormant', 'highcharity_cinematics'), ('x08_0380_grv', 'dormant', 'highcharity_cinematics'), ('x08_0390_grv', 'dormant', 'highcharity_cinematics'), ('x08_teleport_build', 'dormant', 'highcharity_cinematics'), ('x08_teleport_characters', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('x08_11_cleanup', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('c07_intro_cinematic_light_01', 'dormant', 'highcharity_cinematics'), ('c07_intro_01_problem_actors', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('c07_intro_foley_02', 'dormant', 'highcharity_cinematics'), ('c07_1010_pot', 'dormant', 'highcharity_cinematics'), ('c07_intro_dof_02', 'dormant', 'highcharity_cinematics'), ('lightmap_shadows_on', 'dormant', 'highcharity_cinematics'), ('c07_intro_cinematic_light_02', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('c07_intro_foley_03', 'dormant', 'highcharity_cinematics'), ('c07_1020_pot', 'dormant', 'highcharity_cinematics'), ('c07_1030_pot', 'dormant', 'highcharity_cinematics'), ('c07_1040_pot', 'dormant', 'highcharity_cinematics'), ('c07_intro_03_fov', 'dormant', 'highcharity_cinematics'), ('c07_intro_cinematic_light_03', 'dormant', 'highcharity_cinematics'), ('texture_camera_start', 'dormant', 'highcharity_cinematics'), ('texture_camera_stop', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('c07_intro_foley_04', 'dormant', 'highcharity_cinematics'), ('c07_1050_pot', 'dormant', 'highcharity_cinematics'), ('c07_1060_mas', 'dormant', 'highcharity_cinematics'), ('c07_1070_crz', 'dormant', 'highcharity_cinematics'), ('c07_1080_pot', 'dormant', 'highcharity_cinematics'), ('effect_chief_teleport', 'dormant', 'highcharity_cinematics'), ('intro_chief_arrival', 'dormant', 'highcharity_cinematics'), ('needler_attach', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('c07_intra1_score_01', 'dormant', 'highcharity_cinematics'), ('c07_intra1_foley_01', 'dormant', 'highcharity_cinematics'), ('c07_2010_tar', 'dormant', 'highcharity_cinematics'), ('c07_intra1_cinematic_light_01', 'dormant', 'highcharity_cinematics'), ('hide_pikes', 'dormant', 'highcharity_cinematics'), ('show_pikes', 'dormant', 'highcharity_cinematics'), ('johnson_emotion', 'dormant', 'highcharity_cinematics'), ('miranda_emotion', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('c07_intra1_foley_02', 'dormant', 'highcharity_cinematics'), ('c07_2020_pot', 'dormant', 'highcharity_cinematics'), ('c07_2030_tar', 'dormant', 'highcharity_cinematics'), ('c07_intra1_02_fov_01', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('c07_intra1_foley_03', 'dormant', 'highcharity_cinematics'), ('c07_2040_pom', 'dormant', 'highcharity_cinematics'), ('effect_infection_burrow', 'dormant', 'highcharity_cinematics'), ('infection_pop_01', 'dormant', 'highcharity_cinematics'), ('infection_pop_02', 'dormant', 'highcharity_cinematics'), ('infection_pop_03', 'dormant', 'highcharity_cinematics'), ('infection_pop_04', 'dormant', 'highcharity_cinematics'), ('infection_pop_05', 'dormant', 'highcharity_cinematics'), ('hide_seek_if_02', 'dormant', 'highcharity_cinematics'), ('kill_infection_forms', 'dormant', 'highcharity_cinematics'), ('delete_mercy_throne', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('c07_intra1_foley_04', 'dormant', 'highcharity_cinematics'), ('c07_2050_pot', 'dormant', 'highcharity_cinematics'), ('c07_2060_pot', 'dormant', 'highcharity_cinematics'), ('c07_2070_pot', 'dormant', 'highcharity_cinematics'), ('c07_intra1_dof_04', 'dormant', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'static', 'highcharity_cinematics'), ('void', 'stub', 'highcharity_mission'), ('void', 'stub', 'highcharity_mission'), ('void', 'stub', 'highcharity_mission'), ('cs_jump', 'command_script', 'highcharity_mission'), ('cs_abort', 'command_script', 'highcharity_mission'), ('cs_alert', 'command_script', 'highcharity_mission'), ('cs_alert_combat', 'command_script', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('cs_c07_infection', 'command_script', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('bullshit', 'dormant', 'highcharity_mission'), ('cs_expand_cortana', 'command_script', 'highcharity_mission'), ('cs_shrink_cortana', 'command_script', 'highcharity_mission'), ('ice_cream_angry', 'dormant', 'highcharity_mission'), ('music_07a_01', 'dormant', 'highcharity_mission'), ('music_07a_02', 'dormant', 'highcharity_mission'), ('music_07a_03', 'dormant', 'highcharity_mission'), ('music_07a_04', 'dormant', 'highcharity_mission'), ('music_07a_05', 'dormant', 'highcharity_mission'), ('music_07a_06', 'dormant', 'highcharity_mission'), ('music_07a_07', 'dormant', 'highcharity_mission'), ('music_07a_08', 'dormant', 'highcharity_mission'), ('chapter_job', 'dormant', 'highcharity_mission'), ('chapter_thanks', 'dormant', 'highcharity_mission'), ('chapter_grudge', 'dormant', 'highcharity_mission'), ('chapter_graves', 'dormant', 'highcharity_mission'), ('objective_locate_set', 'dormant', 'highcharity_mission'), ('objective_locate_clear', 'dormant', 'highcharity_mission'), ('objective_rescue_set', 'dormant', 'highcharity_mission'), ('objective_rescue_clear', 'dormant', 'highcharity_mission'), ('objective_truth_set', 'dormant', 'highcharity_mission'), ('objective_truth_clear', 'dormant', 'highcharity_mission'), ('objective_phantom_set', 'dormant', 'highcharity_mission'), ('objective_phantom_clear', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('sc_council_ini', 'dormant', 'highcharity_mission'), ('sc_brutes_berserk', 'dormant', 'highcharity_mission'), ('sc_council_exit_reminder', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('sc_council_exit_leave', 'dormant', 'highcharity_mission'), ('sc_council_exit', 'dormant', 'highcharity_mission'), ('sc_grand_a_exit', 'dormant', 'highcharity_mission'), ('sc_ledge_chieftan', 'dormant', 'highcharity_mission'), ('sc_ledge_down_reminder', 'dormant', 'highcharity_mission'), ('sc_ledge_down', 'dormant', 'highcharity_mission'), ('sc_corridor_a_amb', 'dormant', 'highcharity_mission'), ('sc_jail_info', 'dormant', 'highcharity_mission'), ('sc_room_a_lift', 'dormant', 'highcharity_mission'), ('sc_room_a_down', 'dormant', 'highcharity_mission'), ('sc_jail_down', 'dormant', 'highcharity_mission'), ('sc_cell_a_ent', 'dormant', 'highcharity_mission'), ('sc_cell_b_ent', 'dormant', 'highcharity_mission'), ('sc_first_cell', 'dormant', 'highcharity_mission'), ('sc_second_cell', 'dormant', 'highcharity_mission'), ('sc_jail_exit', 'dormant', 'highcharity_mission'), ('sc_lift_reins', 'dormant', 'highcharity_mission'), ('sc_jail_clear_reminder', 'dormant', 'highcharity_mission'), ('cs_marines_exit', 'command_script', 'highcharity_mission'), ('sc_jail_clear', 'dormant', 'highcharity_mission'), ('sc_room_b', 'dormant', 'highcharity_mission'), ('sc_corridor_b_exit', 'dormant', 'highcharity_mission'), ('sc_network', 'dormant', 'highcharity_mission'), ('in_amber_clad', 'dormant', 'highcharity_mission'), ('sc_ioc_reminder', 'dormant', 'highcharity_mission'), ('sc_truth_a', 'dormant', 'highcharity_mission'), ('sc_in_amber_clad', 'dormant', 'highcharity_mission'), ('sc_garden_a_tram_reminder', 'dormant', 'highcharity_mission'), ('sc_drive_elites', 'dormant', 'highcharity_mission'), ('sc_gardens_b', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('sc_catch_truth', 'dormant', 'highcharity_mission'), ('sc_maus_interior', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('sc_maus_exit', 'dormant', 'highcharity_mission'), ('marine_migration', 'dormant', 'highcharity_mission'), ('grand_b_door', 'dormant', 'highcharity_mission'), ('cs_council_grunt_a', 'command_script', 'highcharity_mission'), ('cs_council_grunt_b', 'command_script', 'highcharity_mission'), ('cs_council_grunt_c', 'command_script', 'highcharity_mission'), ('cs_council_grunt_d', 'command_script', 'highcharity_mission'), ('ai_council_brutes_berserk', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('ai_council_orders', 'dormant', 'highcharity_mission'), ('ai_council_upper_migrate', 'dormant', 'highcharity_mission'), ('ai_council_upper', 'dormant', 'highcharity_mission'), ('ai_council_floor_spawn', 'dormant', 'highcharity_mission'), ('cs_grand_a_grunt_a', 'command_script', 'highcharity_mission'), ('cs_grand_a_grunt_b', 'command_script', 'highcharity_mission'), ('create_ledge_columns', 'dormant', 'highcharity_mission'), ('cs_ledge_jackals_lt', 'command_script', 'highcharity_mission'), ('cs_ledge_jackals_rt', 'command_script', 'highcharity_mission'), ('cs_ledge_brute_a', 'command_script', 'highcharity_mission'), ('cs_ledge_brute_b', 'command_script', 'highcharity_mission'), ('cs_lift_jump', 'command_script', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('ai_dervish_ledge_orders', 'dormant', 'highcharity_mission'), ('cs_ledge_turrets_left', 'command_script', 'highcharity_mission'), ('cs_ledge_turrets_right', 'command_script', 'highcharity_mission'), ('ai_ledge_lift', 'dormant', 'highcharity_mission'), ('ai_ledge_lower', 'dormant', 'highcharity_mission'), ('cs_hall_a_jackal_ini_a', 'command_script', 'highcharity_mission'), ('cs_hall_a_jackal_ini_b', 'command_script', 'highcharity_mission'), ('cs_hall_a_jackal_ini_c', 'command_script', 'highcharity_mission'), ('cs_hall_a_brute_ini', 'command_script', 'highcharity_mission'), ('cs_hall_a_jackal_ini', 'command_script', 'highcharity_mission'), ('cs_hall_b_jackal_a', 'command_script', 'highcharity_mission'), ('cs_hall_b_jackal_b', 'command_script', 'highcharity_mission'), ('cs_hall_b_brutes', 'command_script', 'highcharity_mission'), ('cs_hall_b_wake_grunts', 'command_script', 'highcharity_mission'), ('cs_room_a_brute_ini', 'command_script', 'highcharity_mission'), ('cs_room_a_jackal_ini', 'command_script', 'highcharity_mission'), ('cs_room_a_brutes_bk', 'command_script', 'highcharity_mission'), ('cs_room_a_to_jail', 'command_script', 'highcharity_mission'), ('room_a_door', 'dormant', 'highcharity_mission'), ('corridor_a_activate', 'dormant', 'highcharity_mission'), ('ai_hall_a_prophets', 'dormant', 'highcharity_mission'), ('ai_room_a', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('cs_ignore_jail_a_marines', 'command_script', 'highcharity_mission'), ('cs_ignore_jail_b_marines', 'command_script', 'highcharity_mission'), ('cs_jail_jackal_ini_a', 'command_script', 'highcharity_mission'), ('cs_jail_jackal_ini_b', 'command_script', 'highcharity_mission'), ('cs_jail_jackal_ini_c', 'command_script', 'highcharity_mission'), ('cs_jail_jackal_ini_d', 'command_script', 'highcharity_mission'), ('cs_jail_jackal_ini_e', 'command_script', 'highcharity_mission'), ('cs_jail_jackal_ini_f', 'command_script', 'highcharity_mission'), ('cs_cell_a_jackal_a', 'command_script', 'highcharity_mission'), ('cs_cell_a_jackal_b', 'command_script', 'highcharity_mission'), ('cs_cell_a_brute', 'command_script', 'highcharity_mission'), ('cs_cell_b_brute', 'command_script', 'highcharity_mission'), ('cs_jail_a_marine_a', 'command_script', 'highcharity_mission'), ('cs_jail_a_marine_b', 'command_script', 'highcharity_mission'), ('cs_jail_b_marine_a', 'command_script', 'highcharity_mission'), ('cs_jail_b_marine_b', 'command_script', 'highcharity_mission'), ('cs_jail_b_marine_c', 'command_script', 'highcharity_mission'), ('ai_cell_a_guards', 'dormant', 'highcharity_mission'), ('ai_cell_b_guards', 'dormant', 'highcharity_mission'), ('cs_lift_grunt_a', 'command_script', 'highcharity_mission'), ('cs_lift_grunt_b', 'command_script', 'highcharity_mission'), ('jail_a_doors', 'dormant', 'highcharity_mission'), ('jail_b_doors', 'dormant', 'highcharity_mission'), ('cor_open_a', 'dormant', 'highcharity_mission'), ('cor_open_b', 'dormant', 'highcharity_mission'), ('ai_jail_a', 'dormant', 'highcharity_mission'), ('ai_jail_b', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('ai_jail_down_lift', 'dormant', 'highcharity_mission'), ('ai_prophets_ini_active', 'dormant', 'highcharity_mission'), ('cs_room_b_brute_ini_a', 'command_script', 'highcharity_mission'), ('cs_room_b_brute_ini_b', 'command_script', 'highcharity_mission'), ('cs_room_b_brute_ini_c', 'command_script', 'highcharity_mission'), ('ai_room_b_buggers', 'dormant', 'highcharity_mission'), ('ai_corridor_b', 'dormant', 'highcharity_mission'), ('cs_elites_up_tower', 'command_script', 'highcharity_mission'), ('ai_ext_a_elite_ini', 'dormant', 'highcharity_mission'), ('ai_ext_a_brute_ini', 'dormant', 'highcharity_mission'), ('ai_ext_a_hunters', 'dormant', 'highcharity_mission'), ('ai_ext_a_prophet_migrate', 'dormant', 'highcharity_mission'), ('ai_ext_a_snipers', 'dormant', 'highcharity_mission'), ('ai_ext_a_fliers', 'dormant', 'highcharity_mission'), ('tram_a_no_save', 'dormant', 'highcharity_mission'), ('tram_b_no_save', 'dormant', 'highcharity_mission'), ('tram_c_no_save', 'dormant', 'highcharity_mission'), ('tram_d_no_save', 'dormant', 'highcharity_mission'), ('ai_garden_a_ini', 'dormant', 'highcharity_mission'), ('ai_garden_a_rangers', 'dormant', 'highcharity_mission'), ('cs_garden_a_turret_bk_a', 'command_script', 'highcharity_mission'), ('cs_garden_a_turret_bk_b', 'command_script', 'highcharity_mission'), ('garden_a_tram_b_on', 'dormant', 'highcharity_mission'), ('cs_midtower_buggers_hall', 'command_script', 'highcharity_mission'), ('ai_midtower_buggers_rein', 'dormant', 'highcharity_mission'), ('ai_midtower_cov_rein', 'dormant', 'highcharity_mission'), ('ai_midtower_prophets', 'dormant', 'highcharity_mission'), ('cs_garden_b_grunts', 'command_script', 'highcharity_mission'), ('garden_b_brute_berserk', 'command_script', 'highcharity_mission'), ('ai_ext_b_dump', 'dormant', 'highcharity_mission'), ('ai_ext_b_reins', 'dormant', 'highcharity_mission'), ('cs_ext_b_grunts_low', 'command_script', 'highcharity_mission'), ('cs_maus_hall_grunts', 'command_script', 'highcharity_mission'), ('maus_door', 'dormant', 'highcharity_mission'), ('cs_maus_room_elite_lt', 'command_script', 'highcharity_mission'), ('cs_maus_room_elite_rt', 'command_script', 'highcharity_mission'), ('ai_maus_room_ini', 'dormant', 'highcharity_mission'), ('ai_maus_bridge_ini', 'dormant', 'highcharity_mission'), ('ai_maus_inner_order_transitions', 'dormant', 'highcharity_mission'), ('ai_maus_inner_brute_reins', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('ai_maus_inner_spawn', 'dormant', 'highcharity_mission'), ('ai_maus_inner_elites_final', 'dormant', 'highcharity_mission'), ('enc_council_chamber', 'dormant', 'highcharity_mission'), ('enc_dervish_ledge', 'dormant', 'highcharity_mission'), ('enc_corridors_a', 'dormant', 'highcharity_mission'), ('enc_jails', 'dormant', 'highcharity_mission'), ('enc_corridors_b', 'dormant', 'highcharity_mission'), ('enc_tower_a_ext', 'dormant', 'highcharity_mission'), ('enc_gardens_a', 'dormant', 'highcharity_mission'), ('ai_midtower_ini', 'dormant', 'highcharity_mission'), ('enc_mid_tower', 'dormant', 'highcharity_mission'), ('enc_gardens_b', 'dormant', 'highcharity_mission'), ('enc_tower_b_ext', 'dormant', 'highcharity_mission'), ('enc_mausoleum_ext', 'dormant', 'highcharity_mission'), ('enc_mausoleum', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('mission_highcharity', 'dormant', 'highcharity_mission'), ('void', 'static', 'highcharity_mission'), ('mission_main', 'startup', 'highcharity_mission'), ('x08_01_predict', 'dormant', 'highcharity_prediction'), ('x08_02_predict', 'dormant', 'highcharity_prediction'), ('x08_03_predict', 'dormant', 'highcharity_prediction'), ('x08_04_predict', 'dormant', 'highcharity_prediction'), ('x08_05_predict', 'dormant', 'highcharity_prediction'), ('x08_06a_predict', 'dormant', 'highcharity_prediction'), ('x08_06b_predict', 'dormant', 'highcharity_prediction'), ('x08_06c_predict', 'dormant', 'highcharity_prediction'), ('x08_07_predict', 'dormant', 'highcharity_prediction'), ('x08_08_predict', 'dormant', 'highcharity_prediction'), ('x08_09_predict', 'dormant', 'highcharity_prediction'), ('x08_10_predict', 'dormant', 'highcharity_prediction'), ('x08_11_predict', 'dormant', 'highcharity_prediction'), ('07_intro_01_predict', 'dormant', 'highcharity_prediction'), ('07_intro_02_predict', 'dormant', 'highcharity_prediction'), ('07_intro_03_predict', 'dormant', 'highcharity_prediction'), ('07_intro_04_predict', 'dormant', 'highcharity_prediction'), ('07_intra1_01_predict', 'dormant', 'highcharity_prediction'), ('07_intra1_02_predict', 'dormant', 'highcharity_prediction'), ('07_intra1_03_predict', 'dormant', 'highcharity_prediction'), ('07_intra1_04_predict', 'dormant', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_prediction'), ('void', 'static', 'highcharity_teleport'), ('void', 'static', 'highcharity_teleport'), ('void', 'static', 'highcharity_teleport'), ('void', 'static', 'highcharity_teleport'), ('void', 'static', 'highcharity_teleport'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/07b_forerunnership/07b_forerunnership': {
        "objects": {
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['forerunnership_mission']},
            'alcove': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['forerunnership_cinematic']},
            'bloom_quad': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['forerunnership_cinematic']},
            'cap': {'category': 'object', 'funcs': ['object_cinematic_visibility', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'chief': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'chief_outro': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['forerunnership_cinematic']},
            'cinematic_fld_inf0/form0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'cinematic_fld_inf0/form1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'cinematic_fld_inf1/form0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'conduit': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'cortana': {'category': 'human', 'funcs': ['ai_place', 'object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic', 'forerunnership_mission']},
            'cortana_base': {'category': 'human', 'funcs': ['object_destroy'], 'sources': ['forerunnership_cinematic']},
            'cortana_outro': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['forerunnership_cinematic']},
            'cortana_trig1': {'category': 'human', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'covenant': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['forerunnership_mission']},
            'dervish_lift': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['forerunnership_mission']},
            'e10_CS_ghost1/pilot1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_CS_ghost1/pilot2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_CS_ghost1/pilot3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_CS_ghost1/pilot4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_cov_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy10': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy11': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy12': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy6': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy7': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy8': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_inf1/guy9': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_swarm1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_fld_swarm2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_flood_master': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['forerunnership_mission']},
            'e10_flood_storm': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['forerunnership_mission']},
            'e10_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_pro_inf1_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e10_pro_inner_sanctum': {'category': 'object', 'funcs': ['ai_strength'], 'sources': ['forerunnership_mission']},
            'e10_stuck_door': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['forerunnership_mission']},
            'e10_tube_door': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['forerunnership_mission']},
            'e11_fld_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e11_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_CS_banshee1': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['forerunnership_mission']},
            'e12_CS_banshee2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_CS_banshee3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_CS_pelican1': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf1_left': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf1_right': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf2_left': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf2_right': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf3_left': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf3_right': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4/ghost1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4/ghost2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4/ghost3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4/guy4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4/guya': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf4/guyz': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_fld_inf5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_flood_rush': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders', 'ai_strength'], 'sources': ['forerunnership_mission']},
            'e12_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_pro_inf2_left': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_pro_inf2_right': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_pro_inf3_end': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_pro_inf4_left': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e12_pro_inf4_right': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e13_fld_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e13_fld_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e13_fld_inf2_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e13_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e13_pro_inf3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e14_pro_ghost1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e14_pro_shadow1': {'category': 'object', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e14_pro_shadow2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_CS_pelican1': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['forerunnership_mission']},
            'e1_CS_pelican1/pilot': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_CS_pelican2': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['forerunnership_mission']},
            'e1_CS_pelican2/pilot': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_gitem1/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_gitem1/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_gitem2/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_gitem2/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf1/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf1/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf1/guy4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf1/guy5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf3/carrier0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf3/carrier1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf3/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf3/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf3/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf3/guy4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf4/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf4/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf4/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf4/guy4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf4/guy5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf4/guy6': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf4_z': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_fld_inf5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_flood_group_1': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['forerunnership_mission']},
            'e1_flood_master': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['forerunnership_mission']},
            'e1_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e1_pro_inf3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e2_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e3_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e3_pro_inf1_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e3_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_buggers': {'category': 'object', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e5_fld_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e5_fld_inf2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['forerunnership_mission']},
            'e5_fld_inf2_z': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug1': {'category': 'object', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_b/guy1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_b/guy2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_b/guy3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_b/guy4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_c': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_c/guy1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_c/guy2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_c/guy3': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_c/guy4': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_bug2_c/guy5': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e5_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf1_a/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf1_a/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf1_a/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf1_a/guy4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf2_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf2_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf2_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf2_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf2_z': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf2_z/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf2_z/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf2_z/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf2_z/guy4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy10': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy6': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy7': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy8': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf4/guy9': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_inf5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_swarm1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_fld_swarm2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_flood_group_1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['forerunnership_mission']},
            'e6_flood_group_2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['forerunnership_mission']},
            'e6_flood_group_3': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e6_flood_group_master': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['forerunnership_mission']},
            'e6_flood_storm': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['forerunnership_mission']},
            'e6_pro_cave1': {'category': 'object', 'funcs': ['ai_strength'], 'sources': ['forerunnership_mission']},
            'e6_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_pro_inf2_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_pro_inf3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e6_pro_inf3_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders', 'ai_strength'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy10': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy11': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy12': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy5': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy6': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy7': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy8': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_inf1/guy9': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_fld_swarm1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e8_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf1': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf1/guy1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf1/guy2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf1/guy3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf3_a': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf3_b': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf3_c': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf3_d': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf3_e': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_inf3_f': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_fld_swarm1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'e9_flood_master': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['forerunnership_mission']},
            'forerunner_ship': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'gravity_bridge_a1': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position', 'device_set_power'], 'sources': ['forerunnership_mission']},
            'gravity_bridge_a2': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position', 'device_set_power'], 'sources': ['forerunnership_mission']},
            'gravity_bridge_b1': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position', 'device_set_power'], 'sources': ['forerunnership_mission']},
            'gravity_bridge_c1': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position', 'device_set_power'], 'sources': ['forerunnership_mission']},
            'infection_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['forerunnership_cinematic']},
            'infection_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'ledge_1': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['forerunnership_cinematic', 'forerunnership_mission']},
            'ledge_97': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['forerunnership_mission']},
            'ledge_98': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['forerunnership_mission']},
            'ledge_99': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['forerunnership_mission']},
            'lift_effect_a': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['forerunnership_mission']},
            'lift_effect_b': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['forerunnership_mission']},
            'matte_high_charity': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['forerunnership_cinematic']},
            'matte_substance': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['forerunnership_cinematic']},
            'maus_platform_a': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['forerunnership_mission']},
            'maus_platform_b': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['forerunnership_mission']},
            'maus_platform_c': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['forerunnership_mission']},
            'maus_platform_d': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['forerunnership_mission']},
            'mercy': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['forerunnership_cinematic']},
            'pelican_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'phantom_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['forerunnership_cinematic']},
            'phantom_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['forerunnership_cinematic']},
            'phantom_03': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['forerunnership_cinematic']},
            'phantom_ledge_flood': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['forerunnership_mission']},
            'ring_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'ring_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'ring_03': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'ring_04': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'ring_05': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'ring_06': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'ring_07': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'ring_08': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['forerunnership_cinematic']},
            'room_a_lift': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['forerunnership_mission']},
            'sanctum_lift': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['forerunnership_mission']},
            'takeoff_dust': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['forerunnership_cinematic']},
            'throne_mercy': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['forerunnership_cinematic']},
            'tomb_overlook_brutes': {'category': 'covenant', 'funcs': ['ai_place', 'ai_strength'], 'sources': ['forerunnership_mission']},
            'tomb_overlook_elite': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'tomb_overlook_elite2': {'category': 'covenant', 'funcs': ['ai_place', 'ai_strength'], 'sources': ['forerunnership_mission']},
            'tomb_overlook_flood2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_strength'], 'sources': ['forerunnership_mission']},
            'tomb_overlook_flood3': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['forerunnership_mission']},
            'tomb_overlook_infection1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'tomb_overlook_infection2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['forerunnership_mission']},
            'tv_conduit_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_conduit_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_cov_defense': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_dervish_ledge_lift': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e10_door_jam': {'category': 'device', 'funcs': ['volume_test_object', 'volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e10_hall_check': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e10_screen': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e10_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e10_trigger2': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e10_trigger5': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e10_trigger6': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e10_trigger7': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e10_trigger9': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e11_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_bottom_blocker': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_final_dialogue': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_left_blocker': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_right_blocker': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_tickle': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_trigger2': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_trigger4': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e12_trigger8': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e13_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e13_trigger6_manhunt': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e14_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e1_gitem1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e1_gitem2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e1_trigger2': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e1_trigger4': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e1_trigger5': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e2_save': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e2_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e2_trigger2': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e3_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e3_trigger2': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_plat_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_plat_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_platform_a1': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_platform_a2': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_platform_b1': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_platform_c1': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_platform_start': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_trigger2': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_trigger3': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e5_trigger_chase': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_ambusher': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_cave_check': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_final_start': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_infinite1': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_infinite2': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_special_1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_special_2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_talkbox': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_trigger3': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_trigger8': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e6_trigger9': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e7_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e7_trigger2': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e8_cave_check': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e8_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e8_trigger2_a': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e9_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e9_hall_check': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e9_surprise': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e9_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_e9_trigger2': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_endroom': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_hall_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_hall_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_hall_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_ledge_a': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_ledge_b': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_ledge_c': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_midroom': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_phantom_ledge': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_plug_land': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_plug_launch': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_qz_initial': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_room_a_lift_bot': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_room_a_lift_top': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_sanctum_lift': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
            'tv_startme': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['forerunnership_mission']},
        },
        "scripts": [('void', 'stub', 'forerunnership_cinematic'), ('void', 'stub', 'forerunnership_cinematic'), ('void', 'stub', 'forerunnership_cinematic'), ('void', 'stub', 'forerunnership_cinematic'), ('void', 'stub', 'forerunnership_cinematic'), ('void', 'stub', 'forerunnership_cinematic'), ('void', 'stub', 'forerunnership_cinematic'), ('void', 'stub', 'forerunnership_cinematic'), ('void', 'stub', 'forerunnership_cinematic'), ('c07_intra1_score_05', 'dormant', 'forerunnership_cinematic'), ('c07_intra1_foley_05', 'dormant', 'forerunnership_cinematic'), ('c07_intra1_05_dof_01', 'dormant', 'forerunnership_cinematic'), ('c07_intra1_cinematic_light_01', 'dormant', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('c07_intra1_foley_06', 'dormant', 'forerunnership_cinematic'), ('c07_2080_mas', 'dormant', 'forerunnership_cinematic'), ('c07_2090_pom', 'dormant', 'forerunnership_cinematic'), ('c07_2100_pom', 'dormant', 'forerunnership_cinematic'), ('c07_2101_pom', 'dormant', 'forerunnership_cinematic'), ('c07_2110_cor', 'dormant', 'forerunnership_cinematic'), ('c07_2120_cor', 'dormant', 'forerunnership_cinematic'), ('c07_intra1_06_dof_01', 'dormant', 'forerunnership_cinematic'), ('c07_intra1_06_fov_01', 'dormant', 'forerunnership_cinematic'), ('infection_pop', 'dormant', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('c07_2130_cor', 'dormant', 'forerunnership_cinematic'), ('c07_2140_cor', 'dormant', 'forerunnership_cinematic'), ('c07_2150_mas', 'dormant', 'forerunnership_cinematic'), ('c07_2160_cor', 'dormant', 'forerunnership_cinematic'), ('c07_2170_cor', 'dormant', 'forerunnership_cinematic'), ('c07_2180_cor', 'dormant', 'forerunnership_cinematic'), ('c07_2190_cor', 'dormant', 'forerunnership_cinematic'), ('c07_intra1_07_fov_01', 'dormant', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('c07_intra1_foley_08', 'dormant', 'forerunnership_cinematic'), ('pelican_crash_01', 'dormant', 'forerunnership_cinematic'), ('pelican_crash_02', 'dormant', 'forerunnership_cinematic'), ('pelican_crash_03', 'dormant', 'forerunnership_cinematic'), ('c07_intra1_08_fov_01', 'dormant', 'forerunnership_cinematic'), ('flood_pelican_unload', 'dormant', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('c07_outro_score_01', 'dormant', 'forerunnership_cinematic'), ('c07_outro_foley_01', 'dormant', 'forerunnership_cinematic'), ('c07_outro_shake', 'dormant', 'forerunnership_cinematic'), ('c07_outro_shake2', 'dormant', 'forerunnership_cinematic'), ('c07_outro_dof_01', 'dormant', 'forerunnership_cinematic'), ('c07_outro_dof_02', 'dormant', 'forerunnership_cinematic'), ('c07_outro_fov_01', 'dormant', 'forerunnership_cinematic'), ('c07_outro_cinematic_lighting_01', 'dormant', 'forerunnership_cinematic'), ('ship_initial_blast', 'dormant', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('c07_outro_foley_02', 'dormant', 'forerunnership_cinematic'), ('c07_9010_cor', 'dormant', 'forerunnership_cinematic'), ('c07_9020_mas', 'dormant', 'forerunnership_cinematic'), ('c07_9030_cor', 'dormant', 'forerunnership_cinematic'), ('c07_9040_cor', 'dormant', 'forerunnership_cinematic'), ('chief_sparks', 'dormant', 'forerunnership_cinematic'), ('c07_outro_fov_02', 'dormant', 'forerunnership_cinematic'), ('c07_outro_cinematic_lighting_02', 'dormant', 'forerunnership_cinematic'), ('ship_take_off_01', 'dormant', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('c07_outro_foley_03', 'dormant', 'forerunnership_cinematic'), ('c07_outro_cinematic_lighting_03', 'dormant', 'forerunnership_cinematic'), ('ship_take_off_02', 'dormant', 'forerunnership_cinematic'), ('ship_take_off_03', 'dormant', 'forerunnership_cinematic'), ('effect_slipspace', 'dormant', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'static', 'forerunnership_cinematic'), ('void', 'stub', 'forerunnership_mission'), ('void', 'stub', 'forerunnership_mission'), ('void', 'stub', 'forerunnership_mission'), ('cs_expand_cortana', 'command_script', 'forerunnership_mission'), ('music_07b_01_start', 'dormant', 'forerunnership_mission'), ('music_07b_01_stop', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('music_07b_02_start', 'dormant', 'forerunnership_mission'), ('music_07b_03_start', 'dormant', 'forerunnership_mission'), ('music_07b_03_stop', 'dormant', 'forerunnership_mission'), ('music_07b_04_start', 'dormant', 'forerunnership_mission'), ('music_07b_04_stop', 'dormant', 'forerunnership_mission'), ('music_07b_05_start', 'dormant', 'forerunnership_mission'), ('music_07b_05_stop', 'dormant', 'forerunnership_mission'), ('music_07b_06_start', 'dormant', 'forerunnership_mission'), ('music_07b_06_stop', 'dormant', 'forerunnership_mission'), ('chapter_purposes', 'dormant', 'forerunnership_mission'), ('chapter_please', 'dormant', 'forerunnership_mission'), ('chapter_sanctified', 'dormant', 'forerunnership_mission'), ('chapter_feeling', 'dormant', 'forerunnership_mission'), ('objective_enter_set', 'dormant', 'forerunnership_mission'), ('objective_enter_clear', 'dormant', 'forerunnership_mission'), ('objective_riptide_set', 'dormant', 'forerunnership_mission'), ('objective_riptide_clear', 'dormant', 'forerunnership_mission'), ('objective_exit_set', 'dormant', 'forerunnership_mission'), ('objective_exit_clear', 'dormant', 'forerunnership_mission'), ('gen_DIA_civil_war_a', 'dormant', 'forerunnership_mission'), ('gen_DIA_civil_war_b', 'dormant', 'forerunnership_mission'), ('gen_DIA_civil_war_c', 'dormant', 'forerunnership_mission'), ('gen_DIA_locking_doors_behind', 'dormant', 'forerunnership_mission'), ('e1_DIA_truth_holycity', 'dormant', 'forerunnership_mission'), ('e5_DIA_get_to_conduit', 'dormant', 'forerunnership_mission'), ('e8_DIA_security_lock', 'dormant', 'forerunnership_mission'), ('e8_DIA_unlock_a', 'dormant', 'forerunnership_mission'), ('e8_DIA_unlock_b', 'dormant', 'forerunnership_mission'), ('e8_DIA_unlock_c', 'dormant', 'forerunnership_mission'), ('e8_DIA_unlock_d', 'dormant', 'forerunnership_mission'), ('e8_DIA_unlock_e', 'dormant', 'forerunnership_mission'), ('e8_DIA_unlock_f', 'dormant', 'forerunnership_mission'), ('e7_DIA_filtration_systems', 'dormant', 'forerunnership_mission'), ('e10_DIA_truth_theparasite', 'dormant', 'forerunnership_mission'), ('e10_DIA_truth_grippedbyfear', 'dormant', 'forerunnership_mission'), ('e10_DIA_truth_noblemercy', 'dormant', 'forerunnership_mission'), ('e10_DIA_civilwar_a', 'dormant', 'forerunnership_mission'), ('e10_DIA_civilwar_b', 'dormant', 'forerunnership_mission'), ('e10_DIA_civilwar_c', 'dormant', 'forerunnership_mission'), ('e12_DIA_tickle_a', 'dormant', 'forerunnership_mission'), ('e12_DIA_truth_becomegods', 'dormant', 'forerunnership_mission'), ('e12_DIA_truth_final', 'dormant', 'forerunnership_mission'), ('e12_DIA_go_conduit_a', 'dormant', 'forerunnership_mission'), ('e12_DIA_go_conduit_b', 'dormant', 'forerunnership_mission'), ('e12_DIA_end_b', 'dormant', 'forerunnership_mission'), ('e12_DIA_tickle_flood', 'dormant', 'forerunnership_mission'), ('e12_DIA_tickle_brutes', 'dormant', 'forerunnership_mission'), ('e12_DIA_tickle_d', 'dormant', 'forerunnership_mission'), ('e12_DIA_end_a', 'dormant', 'forerunnership_mission'), ('e12_DIA_end_c', 'dormant', 'forerunnership_mission'), ('e12_DIA_tickle_c', 'dormant', 'forerunnership_mission'), ('e12_DIA_tickle_b', 'dormant', 'forerunnership_mission'), ('e12_pelican_flyby', 'dormant', 'forerunnership_mission'), ('e12_cs_pelican1', 'command_script', 'forerunnership_mission'), ('e12_tickle', 'dormant', 'forerunnership_mission'), ('e12_stopper', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('e12_final_battle', 'dormant', 'forerunnership_mission'), ('e12_start', 'dormant', 'forerunnership_mission'), ('e12_main', 'dormant', 'forerunnership_mission'), ('e10_sanctum2', 'dormant', 'forerunnership_mission'), ('e10_tickle', 'dormant', 'forerunnership_mission'), ('e10_end_open', 'dormant', 'forerunnership_mission'), ('e10_superflood', 'command_script', 'forerunnership_mission'), ('e10_storm', 'dormant', 'forerunnership_mission'), ('e10_infinite_save', 'dormant', 'forerunnership_mission'), ('e10_sanctum_lift_recall', 'dormant', 'forerunnership_mission'), ('e10_sanctum_lift_crusher', 'dormant', 'forerunnership_mission'), ('e10_battle', 'dormant', 'forerunnership_mission'), ('e10_talking_points', 'dormant', 'forerunnership_mission'), ('e10_start', 'dormant', 'forerunnership_mission'), ('e10_music_aux', 'dormant', 'forerunnership_mission'), ('e10_load', 'dormant', 'forerunnership_mission'), ('e10_key', 'dormant', 'forerunnership_mission'), ('e10_main', 'dormant', 'forerunnership_mission'), ('e9_start', 'dormant', 'forerunnership_mission'), ('e9_main', 'dormant', 'forerunnership_mission'), ('e8_end_open', 'dormant', 'forerunnership_mission'), ('e8_infinite_save', 'dormant', 'forerunnership_mission'), ('e8_sneaky_spawner_dialogue', 'dormant', 'forerunnership_mission'), ('e8_sneaky_spawner', 'dormant', 'forerunnership_mission'), ('e8_load', 'dormant', 'forerunnership_mission'), ('e8_main', 'dormant', 'forerunnership_mission'), ('e7_start', 'dormant', 'forerunnership_mission'), ('e7_main', 'dormant', 'forerunnership_mission'), ('e6_talking', 'dormant', 'forerunnership_mission'), ('e6_go_go_go', 'dormant', 'forerunnership_mission'), ('e6_final', 'dormant', 'forerunnership_mission'), ('e6_ambush', 'dormant', 'forerunnership_mission'), ('e6_cs_attack_the_prophetsCD', 'command_script', 'forerunnership_mission'), ('e6_cs_attack_the_prophetsAB', 'command_script', 'forerunnership_mission'), ('e6_flood_attack_2', 'dormant', 'forerunnership_mission'), ('e6_infinite_save', 'dormant', 'forerunnership_mission'), ('e6_flood_attack_1', 'dormant', 'forerunnership_mission'), ('e6_start', 'dormant', 'forerunnership_mission'), ('e6_main', 'dormant', 'forerunnership_mission'), ('e5_platform_c', 'dormant', 'forerunnership_mission'), ('e5_platform_b', 'dormant', 'forerunnership_mission'), ('e5_platform_a2', 'dormant', 'forerunnership_mission'), ('e5_platform_a1', 'dormant', 'forerunnership_mission'), ('e5_platform_begin', 'dormant', 'forerunnership_mission'), ('e5_cs_leave', 'command_script', 'forerunnership_mission'), ('e5_infinite_save', 'dormant', 'forerunnership_mission'), ('e5_fld_inf2_main', 'dormant', 'forerunnership_mission'), ('e5_start_the_other_fight', 'dormant', 'forerunnership_mission'), ('e5_bugger_spawner', 'dormant', 'forerunnership_mission'), ('e5_start_the_fight', 'dormant', 'forerunnership_mission'), ('e5_talking_points', 'dormant', 'forerunnership_mission'), ('e5_start', 'dormant', 'forerunnership_mission'), ('e5_main', 'dormant', 'forerunnership_mission'), ('e2_cortana_intro', 'dormant', 'forerunnership_mission'), ('e1_cs_gitem1', 'command_script', 'forerunnership_mission'), ('e1_cs_gitem2', 'command_script', 'forerunnership_mission'), ('e1_cs_freakout', 'command_script', 'forerunnership_mission'), ('e1_cs_teleport1', 'command_script', 'forerunnership_mission'), ('e1_cs_teleport2', 'command_script', 'forerunnership_mission'), ('e1_cs_pelican2', 'command_script', 'forerunnership_mission'), ('e1_carrier_drop', 'dormant', 'forerunnership_mission'), ('e1_cs_pelican1', 'command_script', 'forerunnership_mission'), ('e1_infinite_save', 'dormant', 'forerunnership_mission'), ('e1_pro_inf3_place', 'dormant', 'forerunnership_mission'), ('run_grunt_run', 'command_script', 'forerunnership_mission'), ('e1_exterior_checkpoint', 'dormant', 'forerunnership_mission'), ('e1_pro_inf2_place', 'dormant', 'forerunnership_mission'), ('e1_gitem_2', 'dormant', 'forerunnership_mission'), ('e1_gitem_1', 'dormant', 'forerunnership_mission'), ('e1_talking_points', 'dormant', 'forerunnership_mission'), ('e1_flashlight_training', 'dormant', 'forerunnership_mission'), ('e1_mercy', 'dormant', 'forerunnership_mission'), ('e1_main', 'dormant', 'forerunnership_mission'), ('mission_start', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('mission_main', 'startup', 'forerunnership_mission'), ('cinematic_fld_inf0_0', 'command_script', 'forerunnership_mission'), ('cinematic_fld_inf0_1', 'command_script', 'forerunnership_mission'), ('cinematic_fld_inf1_0', 'command_script', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('cs_e5_cov_inf0_elite', 'command_script', 'forerunnership_mission'), ('e10_stuck_door', 'dormant', 'forerunnership_mission'), ('e10_cs_floorit1', 'command_script', 'forerunnership_mission'), ('e10_ender', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('phantom_ledge', 'dormant', 'forerunnership_mission'), ('forerunnership', 'dormant', 'forerunnership_mission'), ('example3', 'dormant', 'forerunnership_mission'), ('cortana_tomb4', 'dormant', 'forerunnership_mission'), ('cortana_tomb3', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('cortana_tomb1', 'dormant', 'forerunnership_mission'), ('example5', 'dormant', 'forerunnership_mission'), ('example4', 'dormant', 'forerunnership_mission'), ('example3', 'dormant', 'forerunnership_mission'), ('example2', 'dormant', 'forerunnership_mission'), ('example', 'dormant', 'forerunnership_mission'), ('dervish_ledge_lift', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('room_a_lift', 'dormant', 'forerunnership_mission'), ('e12_cs_floorit', 'command_script', 'forerunnership_mission'), ('e12_interceptor_boost', 'dormant', 'forerunnership_mission'), ('e12_interceptors', 'dormant', 'forerunnership_mission'), ('e6_end_locked', 'dormant', 'forerunnership_mission'), ('e6_end_open', 'dormant', 'forerunnership_mission'), ('e6_flood_final_rush', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('e5_bugger_reinf_2', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('e5_bugger_reinf_1', 'dormant', 'forerunnership_mission'), ('e14_station_one', 'dormant', 'forerunnership_mission'), ('e14_station_one_complete', 'dormant', 'forerunnership_mission'), ('e14_start', 'dormant', 'forerunnership_mission'), ('e13_tank_rush', 'dormant', 'forerunnership_mission'), ('e13_manhunter', 'dormant', 'forerunnership_mission'), ('e13_start', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('e12_chase_squad', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('e12_start', 'dormant', 'forerunnership_mission'), ('e11_start', 'dormant', 'forerunnership_mission'), ('swarm_chase', 'command_script', 'forerunnership_mission'), ('run_grunt_run', 'command_script', 'forerunnership_mission'), ('e10_grunt_run', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('e8_end_locked', 'dormant', 'forerunnership_mission'), ('e8_end_open', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('e6_unlock_the_door', 'dormant', 'forerunnership_mission'), ('e6_swarm_spawner2', 'dormant', 'forerunnership_mission'), ('e6_swarm_spawner1', 'dormant', 'forerunnership_mission'), ('e9_storm', 'dormant', 'forerunnership_mission'), ('e9_room2', 'dormant', 'forerunnership_mission'), ('e9_surprise', 'dormant', 'forerunnership_mission'), ('e10_crazy_rush', 'dormant', 'forerunnership_mission'), ('void', 'static', 'forerunnership_mission'), ('e5_load', 'dormant', 'forerunnership_mission'), ('e3_pro_inf1_start', 'dormant', 'forerunnership_mission'), ('start_e3', 'dormant', 'forerunnership_mission'), ('e2_cs_hall_patrol', 'command_script', 'forerunnership_mission'), ('e2_pro_inf1_hall_patrol', 'dormant', 'forerunnership_mission'), ('e2_save_trigger', 'dormant', 'forerunnership_mission'), ('e12_you_win', 'dormant', 'forerunnership_mission'), ('07_intra1_05_predict', 'dormant', 'forerunnership_prediction'), ('07_intra1_06_predict', 'dormant', 'forerunnership_prediction'), ('07_intra1_07_predict', 'dormant', 'forerunnership_prediction'), ('07_intra1_08_predict', 'dormant', 'forerunnership_prediction'), ('07_outro_01_predict', 'dormant', 'forerunnership_prediction'), ('07_outro_02_predict', 'dormant', 'forerunnership_prediction'), ('07_outro_03_predict', 'dormant', 'forerunnership_prediction'), ('void', 'static', 'forerunnership_prediction'), ('void', 'static', 'forerunnership_prediction'), ('void', 'static', 'forerunnership_prediction'), ('void', 'static', 'forerunnership_prediction'), ('void', 'static', 'forerunnership_prediction'), ('void', 'static', 'forerunnership_prediction'), ('void', 'static', 'forerunnership_prediction'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/08a_deltacliffs/08a_deltacliffs': {
        "objects": {
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_disregard', 'ai_migrate', 'ai_strength', 'ai_vehicle_enter', 'ai_vehicle_exit'], 'sources': ['08a_deltacliffs_mission']},
            'ai_current_squad': {'category': 'object', 'funcs': ['ai_erase', 'ai_strength'], 'sources': ['08a_deltacliffs_mission']},
            'brute_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['08a_deltacliffs_cinematics']},
            'brute_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['08a_deltacliffs_cinematics']},
            'brute_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['08a_deltacliffs_cinematics']},
            'brute_04': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_hide'], 'sources': ['08a_deltacliffs_cinematics']},
            'commander': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08a_deltacliffs_cinematics']},
            'covenant': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'dervish': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08a_deltacliffs_cinematics']},
            'dervish_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08a_deltacliffs_cinematics']},
            'e10_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_cov_inf0/elite0': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['08a_deltacliffs_mission']},
            'e10_cov_inf0/elite1': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['08a_deltacliffs_mission']},
            'e10_cov_inf0/elite2': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['08a_deltacliffs_mission']},
            'e10_cov_inf0/elite3': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['08a_deltacliffs_mission']},
            'e10_exit_door': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pod0_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pod1_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pod2_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pod3_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_ghosts0_0': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_inf1': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_inf1_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_inf1_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_inf1_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_inf2_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_inf2_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_inf3': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_set_orders'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_phantom0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_wraith0': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_wraith0_0': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e10_pro_wraith0_1': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e1_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e1_cov_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e1_cov_inf2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['08a_deltacliffs_mission']},
            'e1_cov_inf2/elite1': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['08a_deltacliffs_mission']},
            'e1_cov_inf2/elite2': {'category': 'covenant', 'funcs': ['ai_place', 'ai_vehicle_exit'], 'sources': ['08a_deltacliffs_mission']},
            'e1_cov_inf2/gold_elite': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place', 'ai_vehicle_exit'], 'sources': ['08a_deltacliffs_mission']},
            'e1_gun0': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e1_gun1': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e1_gun2': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e1_gun3': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e1_gun4': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pod0_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pod1_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pod2_inserter': {'category': 'object', 'funcs': ['device_get_position', 'device_set_position', 'object_destroy'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pro': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pro_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pro_inf0_1_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pro_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pro_inf0_3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e1_pro_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e2_antennae': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['08a_deltacliffs_mission']},
            'e2_cov': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e2_cov_gold_elite': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e2_cov_grunts0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e2_cov_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e2_cov_inf1': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e2_pro': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e2_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e2_pro_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e2_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e2_pro_inf3': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e3_cov_gold_elite': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e3_cov_grunts0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e3_cov_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e3_exit_door': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['08a_deltacliffs_mission']},
            'e3_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e3_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e3_pro_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e3_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e4_cov_gold_elite': {'category': 'covenant', 'funcs': ['ai_migrate'], 'sources': ['08a_deltacliffs_mission']},
            'e4_cov_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place', 'ai_set_orders'], 'sources': ['08a_deltacliffs_mission']},
            'e4_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e4_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e4_pro_inf2_0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e5_cov_gold_elite': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place', 'ai_set_orders', 'ai_strength'], 'sources': ['08a_deltacliffs_mission']},
            'e5_cov_grunts0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place', 'ai_strength'], 'sources': ['08a_deltacliffs_mission']},
            'e5_cov_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e5_pro': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e5_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place', 'ai_strength'], 'sources': ['08a_deltacliffs_mission']},
            'e5_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e6_cov': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['08a_deltacliffs_mission']},
            'e6_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e6_cov_gold_elite': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e6_cov_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e6_cov_inf1': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e6_ghost_ledge_door': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['08a_deltacliffs_mission']},
            'e6_player_exited_onto_ledge': {'category': 'object', 'funcs': ['ai_trigger_test'], 'sources': ['08a_deltacliffs_mission']},
            'e6_pro': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e6_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e6_pro_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e6_pro_phantom0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e7_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['08a_deltacliffs_mission']},
            'e7_cov_ghosts1': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e7_pro_inf': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e7_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate'], 'sources': ['08a_deltacliffs_mission']},
            'e7_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e7_pro_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e7_pro_inf1_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e7_pro_inf1_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e7_pro_inf1_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e7_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e8_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_migrate'], 'sources': ['08a_deltacliffs_mission']},
            'e8_cov_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e8_pro': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e8_pro_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e8_pro_inf1': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e8_pro_inf1_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e8_pro_inf1_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e8_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e8_pro_spectre0': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e9_cov_ghosts0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e9_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'e9_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e9_pro_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e9_pro_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e9_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place', 'ai_strength'], 'sources': ['08a_deltacliffs_mission']},
            'e9_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e9_pro_inf3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e9_pro_phantom0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08a_deltacliffs_mission']},
            'e9_trap_target0': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['08a_deltacliffs_mission']},
            'e9_trap_target1': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['08a_deltacliffs_mission']},
            'generic_player_sighted': {'category': 'object', 'funcs': ['ai_trigger_test'], 'sources': ['08a_deltacliffs_mission']},
            'generic_player_within_2wu': {'category': 'object', 'funcs': ['ai_trigger_test'], 'sources': ['08a_deltacliffs_mission']},
            'intra1_door': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['08a_deltacliffs_cinematics']},
            'intro_plasma_rifle': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08a_deltacliffs_cinematics']},
            'miranda': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08a_deltacliffs_cinematics']},
            'monitor': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08a_deltacliffs_cinematics']},
            'phantom_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08a_deltacliffs_cinematics']},
            'phantom_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08a_deltacliffs_cinematics']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['08a_deltacliffs_mission']},
            'prophets': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08a_deltacliffs_mission']},
            'tartarus': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08a_deltacliffs_cinematics']},
            'tv_e10_armory': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_armory_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_bridge': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_exit_door': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_inf1_1_init': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_inf1_2_init': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_near_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_pro_inf1_do_or_die': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_pro_inf2_retreat0': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_pro_inf2_retreat2': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e10_second_half': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e1_area_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e1_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e1_ledge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e1_pro_inf0_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e1_second_wall': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e1_third_wall': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e2_cov_inf1_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e2_main_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e2_pro_inf1_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e2_pro_inf3_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e3_lower_level': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e3_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e3_near_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e4_first_step': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e4_ground_floor_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e4_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e4_pre_main': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e4_second_step': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e5_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e5_lower_level': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e5_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e6_ledge0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e6_ledge1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e6_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e6_on_ledge0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e6_pro_inf1_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e7_end_section': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e7_grunts_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e7_main_begin0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e7_main_begin1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e7_middle_section': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e7_pro_inf1_0_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e7_pro_inf1_2_unsafe': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e8_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e8_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e8_spectre_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e9_first_drop': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e9_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e9_pro_inf3_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e9_trap_trigger0': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_e9_trap_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'tv_mission_end': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08a_deltacliffs_mission']},
            'wraith_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['08a_deltacliffs_cinematics']},
        },
        "scripts": [('void', 'stub', '08a_deltacliffs_cinematics'), ('void', 'stub', '08a_deltacliffs_cinematics'), ('void', 'stub', '08a_deltacliffs_cinematics'), ('void', 'stub', '08a_deltacliffs_cinematics'), ('c08_intro_foley_01', 'dormant', '08a_deltacliffs_cinematics'), ('intro_fov', 'dormant', '08a_deltacliffs_cinematics'), ('intro_dof', 'dormant', '08a_deltacliffs_cinematics'), ('effect_teleport', 'dormant', '08a_deltacliffs_cinematics'), ('cinematic_lighting_intro', 'dormant', '08a_deltacliffs_cinematics'), ('plasma_rifle_attach', 'dormant', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('c08_intra1_foley_01', 'dormant', '08a_deltacliffs_cinematics'), ('c08_2010_soc', 'dormant', '08a_deltacliffs_cinematics'), ('c04_intra1_dof_01', 'dormant', '08a_deltacliffs_cinematics'), ('cinematic_lighting_intra1_01', 'dormant', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('c08_intra1_sound_scene2_01', 'dormant', '08a_deltacliffs_cinematics'), ('c08_intra1_score_02', 'dormant', '08a_deltacliffs_cinematics'), ('c08_intra1_foley_02', 'dormant', '08a_deltacliffs_cinematics'), ('c08_2020_der', 'dormant', '08a_deltacliffs_cinematics'), ('c08_2030_soc', 'dormant', '08a_deltacliffs_cinematics'), ('c04_intra1_dof_02', 'dormant', '08a_deltacliffs_cinematics'), ('cinematic_lighting_intra1_02', 'dormant', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('c08_intra1_sound_scene3_01', 'dormant', '08a_deltacliffs_cinematics'), ('c08_intra1_foley_03', 'dormant', '08a_deltacliffs_cinematics'), ('c08_2040_tar', 'dormant', '08a_deltacliffs_cinematics'), ('cinematic_lighting_intra1_03', 'dormant', '08a_deltacliffs_cinematics'), ('show_brutes', 'dormant', '08a_deltacliffs_cinematics'), ('door_close', 'dormant', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('void', 'static', '08a_deltacliffs_cinematics'), ('void', 'stub', '08a_deltacliffs_mission'), ('void', 'stub', '08a_deltacliffs_mission'), ('boolean', 'static', '08a_deltacliffs_mission'), ('boolean', 'static', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('objective0_set', 'dormant', '08a_deltacliffs_mission'), ('objective0_clear', 'dormant', '08a_deltacliffs_mission'), ('objective1_set', 'dormant', '08a_deltacliffs_mission'), ('objective1_clear', 'dormant', '08a_deltacliffs_mission'), ('objective2_set', 'dormant', '08a_deltacliffs_mission'), ('objective2_clear', 'dormant', '08a_deltacliffs_mission'), ('objective3_set', 'dormant', '08a_deltacliffs_mission'), ('music_08a_01_stop', 'dormant', '08a_deltacliffs_mission'), ('music_08a_01_start_alt', 'dormant', '08a_deltacliffs_mission'), ('music_08a_01_start', 'dormant', '08a_deltacliffs_mission'), ('music_08a_02_stop', 'dormant', '08a_deltacliffs_mission'), ('music_08a_02_start', 'dormant', '08a_deltacliffs_mission'), ('music_08a_03_stop', 'dormant', '08a_deltacliffs_mission'), ('music_08a_03_start_alt', 'dormant', '08a_deltacliffs_mission'), ('music_08a_03_start', 'dormant', '08a_deltacliffs_mission'), ('music_08a_04_start', 'dormant', '08a_deltacliffs_mission'), ('music_08a_05_start', 'dormant', '08a_deltacliffs_mission'), ('chapter_title0', 'dormant', '08a_deltacliffs_mission'), ('chapter_title1', 'dormant', '08a_deltacliffs_mission'), ('chapter_title2', 'dormant', '08a_deltacliffs_mission'), ('boolean', 'static', '08a_deltacliffs_mission'), ('boolean', 'static', '08a_deltacliffs_mission'), ('boolean', 'static', '08a_deltacliffs_mission'), ('boolean', 'static', '08a_deltacliffs_mission'), ('cs_e10_pro_phantom0_entry', 'command_script', '08a_deltacliffs_mission'), ('cs_e10_weapon_scene0', 'command_script', '08a_deltacliffs_mission'), ('cs_e10_weapon_scene1', 'command_script', '08a_deltacliffs_mission'), ('cs_e10_pro_inf1_0_patrol0', 'command_script', '08a_deltacliffs_mission'), ('cs_e10_pro_inf1_0_patrol1', 'command_script', '08a_deltacliffs_mission'), ('cs_e10_pro_ghosts0_entry', 'command_script', '08a_deltacliffs_mission'), ('e10_pod0_insertion', 'dormant', '08a_deltacliffs_mission'), ('e10_pod1_insertion', 'dormant', '08a_deltacliffs_mission'), ('e10_pod2_insertion', 'dormant', '08a_deltacliffs_mission'), ('e10_pod3_insertion', 'dormant', '08a_deltacliffs_mission'), ('e10_weapon_scene', 'dormant', '08a_deltacliffs_mission'), ('e10_fallback_checkpoint0', 'dormant', '08a_deltacliffs_mission'), ('e10_pro_phantom0_main', 'dormant', '08a_deltacliffs_mission'), ('e10_pro_ghosts0_main', 'dormant', '08a_deltacliffs_mission'), ('e10_pro_wraith0_main', 'dormant', '08a_deltacliffs_mission'), ('e10_pro_inf3_main', 'dormant', '08a_deltacliffs_mission'), ('e10_pro_inf2_main', 'dormant', '08a_deltacliffs_mission'), ('e10_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e10_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e10_cov_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e10_cov_ghosts0_main', 'dormant', '08a_deltacliffs_mission'), ('e10_key', 'dormant', '08a_deltacliffs_mission'), ('e10_main', 'dormant', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('cs_e9_pro_inf1_trap', 'command_script', '08a_deltacliffs_mission'), ('cs_e9_pro_inf1_abort', 'command_script', '08a_deltacliffs_mission'), ('cs_e9_pro_phantom0_overflight', 'command_script', '08a_deltacliffs_mission'), ('e9_weather_control', 'dormant', '08a_deltacliffs_mission'), ('e9_pro_phantom0_main', 'dormant', '08a_deltacliffs_mission'), ('e9_pro_inf3_main', 'dormant', '08a_deltacliffs_mission'), ('e9_pro_inf2_main', 'dormant', '08a_deltacliffs_mission'), ('e9_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e9_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e9_cov_ghosts0_main', 'dormant', '08a_deltacliffs_mission'), ('e9_main', 'dormant', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('cs_e8_cov_inf0_init', 'command_script', '08a_deltacliffs_mission'), ('e8_pro_spectre0_main', 'dormant', '08a_deltacliffs_mission'), ('e8_pro_inf2_main', 'dormant', '08a_deltacliffs_mission'), ('e8_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e8_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e8_cov_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e8_cov_ghosts0_main', 'dormant', '08a_deltacliffs_mission'), ('e8_main', 'dormant', '08a_deltacliffs_mission'), ('cs_e7_cov_grunt0', 'command_script', '08a_deltacliffs_mission'), ('cs_e7_cov_grunt1', 'command_script', '08a_deltacliffs_mission'), ('e7_pro_inf2_main', 'dormant', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('e7_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e7_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e7_cov_ghosts1_main', 'dormant', '08a_deltacliffs_mission'), ('e7_cov_ghosts0_main', 'dormant', '08a_deltacliffs_mission'), ('e7_main', 'dormant', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('cs_e6_weapon_scene', 'command_script', '08a_deltacliffs_mission'), ('e6_weapon_scene', 'dormant', '08a_deltacliffs_mission'), ('cs_e6_pro_phantom0_entry', 'command_script', '08a_deltacliffs_mission'), ('cs_e6_pro_phantom0_exit', 'command_script', '08a_deltacliffs_mission'), ('cs_e6_pro_inf0_1_firing', 'command_script', '08a_deltacliffs_mission'), ('cs_e6_pro_inf0_0_firing', 'command_script', '08a_deltacliffs_mission'), ('cs_e6_pro_inf1_entry', 'command_script', '08a_deltacliffs_mission'), ('boolean', 'static', '08a_deltacliffs_mission'), ('e6_objectives', 'dormant', '08a_deltacliffs_mission'), ('e6_pro_phantom0_main', 'dormant', '08a_deltacliffs_mission'), ('e6_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e6_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e6_cov_ghosts0_main', 'dormant', '08a_deltacliffs_mission'), ('e6_cov_gold_elite_main', 'dormant', '08a_deltacliffs_mission'), ('e6_cov_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e6_cov_grunts0_main', 'dormant', '08a_deltacliffs_mission'), ('e6_cov_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e6_main', 'dormant', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('cs_e5_cov_gold_elite_creep', 'command_script', '08a_deltacliffs_mission'), ('cs_e5_cov_gold_elite_attack', 'command_script', '08a_deltacliffs_mission'), ('cs_e5_cov_grunts0_cower', 'command_script', '08a_deltacliffs_mission'), ('e5_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e5_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e5_cov_grunts0_main', 'dormant', '08a_deltacliffs_mission'), ('e5_cov_gold_elite_main', 'dormant', '08a_deltacliffs_mission'), ('e5_cov_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e5_main', 'dormant', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('cs_e4_alarm_scene', 'command_script', '08a_deltacliffs_mission'), ('e4_pro_inf2_main', 'dormant', '08a_deltacliffs_mission'), ('e4_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e4_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e4_cov_gold_elite_main', 'dormant', '08a_deltacliffs_mission'), ('e4_cov_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e4_main', 'dormant', '08a_deltacliffs_mission'), ('cs_e3_alarm_scene', 'command_script', '08a_deltacliffs_mission'), ('cs_e3_cov_grunts0_cower', 'command_script', '08a_deltacliffs_mission'), ('cs_e3_cov_gold_elite_charge', 'command_script', '08a_deltacliffs_mission'), ('cs_e3_cov_stealth_major_charge', 'command_script', '08a_deltacliffs_mission'), ('e3_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e3_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e3_cov_grunts0_main', 'dormant', '08a_deltacliffs_mission'), ('e3_cov_gold_elite_main', 'dormant', '08a_deltacliffs_mission'), ('e3_cov_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e3_main', 'dormant', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('cs_e2_alarm_scene', 'command_script', '08a_deltacliffs_mission'), ('cs_e2_cov_grunts0_flee', 'command_script', '08a_deltacliffs_mission'), ('cs_e2_cov_grunts0_abort', 'command_script', '08a_deltacliffs_mission'), ('cs_e2_cov_gold_elite_charge0', 'command_script', '08a_deltacliffs_mission'), ('cs_e2_cov_stealth_elite_charge0', 'command_script', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('e2_alarm_scene', 'dormant', '08a_deltacliffs_mission'), ('e2_pro_inf3_main', 'dormant', '08a_deltacliffs_mission'), ('e2_pro_inf2_main', 'dormant', '08a_deltacliffs_mission'), ('e2_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e2_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e2_cov_grunts0_main', 'dormant', '08a_deltacliffs_mission'), ('e2_cov_gold_elite_main', 'dormant', '08a_deltacliffs_mission'), ('e2_cov_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e2_cov_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e2_main', 'dormant', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('cs_e1_pro_inf0_0_patrol0', 'command_script', '08a_deltacliffs_mission'), ('cs_e1_pro_inf0_1_patrol0', 'command_script', '08a_deltacliffs_mission'), ('cs_e1_pro_inf0_1_patrol1', 'command_script', '08a_deltacliffs_mission'), ('cs_e1_cov_inf0_scene', 'command_script', '08a_deltacliffs_mission'), ('cs_e1_stealth_major_scene', 'command_script', '08a_deltacliffs_mission'), ('cs_e1_watch_pods', 'command_script', '08a_deltacliffs_mission'), ('cs_e1_zealot_intro', 'command_script', '08a_deltacliffs_mission'), ('e1_pod0_insertion', 'dormant', '08a_deltacliffs_mission'), ('e1_pod1_insertion', 'dormant', '08a_deltacliffs_mission'), ('e1_pod2_insertion', 'dormant', '08a_deltacliffs_mission'), ('e1_objectives', 'dormant', '08a_deltacliffs_mission'), ('e1_guns_aux', 'dormant', '08a_deltacliffs_mission'), ('e1_guns', 'dormant', '08a_deltacliffs_mission'), ('e1_music_aux', 'dormant', '08a_deltacliffs_mission'), ('e1_pro_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e1_pro_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e1_cov_inf2_main', 'dormant', '08a_deltacliffs_mission'), ('e1_cov_inf1_main', 'dormant', '08a_deltacliffs_mission'), ('e1_cov_inf0_main', 'dormant', '08a_deltacliffs_mission'), ('e1_main', 'dormant', '08a_deltacliffs_mission'), ('mission_start', 'dormant', '08a_deltacliffs_mission'), ('void', 'static', '08a_deltacliffs_mission'), ('mission_main', 'startup', '08a_deltacliffs_mission'), ('08_intro_01_predict', 'dormant', '08a_deltacliffs_prediction'), ('08_intra1_01_predict', 'dormant', '08a_deltacliffs_prediction'), ('08_intra1_02_predict', 'dormant', '08a_deltacliffs_prediction'), ('08_intra1_03_predict', 'dormant', '08a_deltacliffs_prediction'), ('void', 'static', '08a_deltacliffs_prediction'), ('void', 'static', '08a_deltacliffs_prediction'), ('void', 'static', '08a_deltacliffs_prediction'), ('void', 'static', '08a_deltacliffs_prediction'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
    'scenarios/solo/08b_deltacontrol/08b_deltacontrol': {
        "objects": {
            'ai_current_actor': {'category': 'object', 'funcs': ['ai_erase', 'ai_kill', 'ai_vehicle_exit'], 'sources': ['08b_deltacontrol_mission']},
            'ai_current_squad': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['08b_deltacontrol_mission']},
            'beacon_01': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'beacon_02': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'beacon_03': {'category': 'object', 'funcs': ['device_set_position'], 'sources': ['08b_deltacontrol_cinematics']},
            'bloom_quad': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'boss_brute_reenforcements': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'boss_brute_reenforcements_many': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'boss_brute_start': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'boss_elite_reenforcements': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'boss_elite_reenforcements_many': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'boss_elite_start': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'boss_johnson': {'category': 'human', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'boss_miranda': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'boss_monitor': {'category': 'object', 'funcs': ['ai_erase', 'ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'boss_tartarus': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_kill', 'ai_place'], 'sources': ['08b_deltacontrol_boss']},
            'brute_01': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'brute_02': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'brute_03': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'brute_04': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'c08_intra3_lift': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'cairo_bridge': {'category': 'device', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'chief': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'commander': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'cortana': {'category': 'human', 'funcs': ['object_cinematic_lod'], 'sources': ['08b_deltacontrol_cinematics']},
            'cov_sniper': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'covenant': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['08b_deltacontrol_boss', '08b_deltacontrol_mission']},
            'dervish': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy', 'object_hide'], 'sources': ['08b_deltacontrol_cinematics']},
            'dervish_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'e11_cov': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['08b_deltacontrol_mission']},
            'e11_cov_banshees0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_door0': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['08b_deltacontrol_mission']},
            'e11_exit_door': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_banshees0': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_banshees0_0': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_banshees0_1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_ghosts0': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_phantom0_0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_spectres0': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_wraith0_0': {'category': 'object', 'funcs': ['ai_braindead', 'ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_wraith0_1': {'category': 'object', 'funcs': ['ai_braindead'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_wraith1': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_wraith1_0': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_wraith1_0/driver': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_wraith1_1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_wraith1_1/driver': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_wraith1_2/driver': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e11_pro_wraith1_3/driver': {'category': 'object', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e12_cov': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['08b_deltacontrol_mission']},
            'e12_cov_banshees0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e12_cov_inf0': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['08b_deltacontrol_mission']},
            'e12_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['08b_deltacontrol_mission']},
            'e12_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_set_orders'], 'sources': ['08b_deltacontrol_mission']},
            'e12_cov_inf0_1/elite0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e12_cov_inf0_1/elite1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e12_cov_inf0_1/elite2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e12_cov_phantom0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e12_door0': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['08b_deltacontrol_mission']},
            'e12_door1': {'category': 'device', 'funcs': ['device_get_position', 'device_set_position'], 'sources': ['08b_deltacontrol_mission']},
            'e12_pro': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['08b_deltacontrol_mission']},
            'e12_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e12_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e12_pro_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e12_pro_inf0_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e12_pro_inf0_sighted_player': {'category': 'covenant', 'funcs': ['ai_trigger_test'], 'sources': ['08b_deltacontrol_mission']},
            'e13_boss_platform': {'category': 'device', 'funcs': ['device_set_position'], 'sources': ['08b_deltacontrol_cinematics']},
            'e13_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['08b_deltacontrol_mission']},
            'e13_cov_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e13_cov_inf0_1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e13_mars_johnson': {'category': 'human', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e13_mars_miranda': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e13_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_set_orders'], 'sources': ['08b_deltacontrol_mission']},
            'e13_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e13_pro_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e13_pro_tartarus': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e13_rotors': {'category': 'object', 'funcs': ['device_get_position', 'object_destroy'], 'sources': ['08b_deltacontrol_boss', '08b_deltacontrol_cinematics', '08b_deltacontrol_mission']},
            'e13_sen_monitor': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e1_cov_spectre0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e1_cov_wraiths0': {'category': 'covenant', 'funcs': ['ai_migrate'], 'sources': ['08b_deltacontrol_mission']},
            'e1_cov_wraiths0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e1_pro_ghosts0': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e1_pro_ghosts0_0': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e1_pro_ghosts0_1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e1_pro_ghosts0_2': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e1_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e1_pro_phantom0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e1_pro_wraith0': {'category': 'object', 'funcs': ['ai_braindead', 'ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e2_cov_spectre0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e2_cov_wraith0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e2_exit_door': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['08b_deltacontrol_mission']},
            'e2_pro_ghosts0': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e2_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e2_pro_phantom0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e2_pro_phantom0_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e2_pro_wraith0': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e3_cov': {'category': 'covenant', 'funcs': ['ai_erase'], 'sources': ['08b_deltacontrol_mission']},
            'e3_cov_hunters0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e3_cov_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e3_pro': {'category': 'object', 'funcs': ['ai_erase'], 'sources': ['08b_deltacontrol_mission']},
            'e3_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e3_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e3_pro_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e3_pro_inf1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e3_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e4_cov_hunters0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e4_cov_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e4_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e4_pro_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e4_pro_inf2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e4_pro_inf3': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e5_cov_hunters0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e5_cov_inf0': {'category': 'covenant', 'funcs': ['ai_migrate', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e5_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e5_pro_inf1': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e5_pro_inf2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e5_pro_inf3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e5_pro_phantom0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e6_cov': {'category': 'covenant', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e6_cov_hunters0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place', 'ai_set_orders'], 'sources': ['08b_deltacontrol_mission']},
            'e6_cov_inf0': {'category': 'covenant', 'funcs': ['ai_place', 'ai_set_orders'], 'sources': ['08b_deltacontrol_mission']},
            'e6_cov_inf1': {'category': 'covenant', 'funcs': ['ai_migrate'], 'sources': ['08b_deltacontrol_mission']},
            'e6_cov_inf1_0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e6_cov_inf1_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e6_cov_inf1_2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e6_cov_inf1_3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e6_jail_shield0': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['08b_deltacontrol_mission']},
            'e6_jail_shield1': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['08b_deltacontrol_mission']},
            'e6_jail_shield2': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['08b_deltacontrol_mission']},
            'e6_jail_shield3': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['08b_deltacontrol_mission']},
            'e6_jail_shield4': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['08b_deltacontrol_mission']},
            'e6_jail_shield5': {'category': 'object', 'funcs': ['object_get_health'], 'sources': ['08b_deltacontrol_mission']},
            'e6_pro': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e6_pro_inf0_0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e6_pro_inf0_1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e6_pro_inf0_2': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e7_cov_hunters0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e7_cov_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e7_door0': {'category': 'device', 'funcs': ['device_get_position'], 'sources': ['08b_deltacontrol_mission']},
            'e7_mars': {'category': 'human', 'funcs': ['ai_erase'], 'sources': ['08b_deltacontrol_mission']},
            'e7_mars_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e7_pro_inf0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e8_cov_banshees0/banshee0': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e8_cov_banshees0/banshee1': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e8_cov_banshees0/banshee2': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e8_cov_banshees0/banshee3': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e8_cov_banshees0/banshee4': {'category': 'covenant', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e8_mars_inf0': {'category': 'covenant', 'funcs': ['ai_erase', 'ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e8_pro_wraiths0': {'category': 'object', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e8_pro_wraiths0_0': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e8_pro_wraiths0_1': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e8_pro_wraiths0_2': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e9_pro_banshees0': {'category': 'object', 'funcs': ['ai_living_count', 'ai_migrate', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e9_pro_inf0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e9_pro_phantom0': {'category': 'covenant', 'funcs': ['ai_living_count', 'ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e9_pro_spectres0': {'category': 'object', 'funcs': ['ai_living_count'], 'sources': ['08b_deltacontrol_mission']},
            'e9_pro_spectres0_0': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'e9_pro_spectres0_1': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'forerunner_ship': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'generic_player_sighted': {'category': 'object', 'funcs': ['ai_trigger_test'], 'sources': ['08b_deltacontrol_mission']},
            'halo': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'hammer': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'hood': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'human': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['08b_deltacontrol_boss']},
            'index': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'index_x09': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'johnson': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'johnson_02': {'category': 'human', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'kill_e13_0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_boss']},
            'matte_earth': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['08b_deltacontrol_cinematics']},
            'matte_halo': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['08b_deltacontrol_cinematics']},
            'matte_high_charity': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['08b_deltacontrol_cinematics']},
            'matte_moon': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['08b_deltacontrol_cinematics']},
            'matte_substance': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['08b_deltacontrol_cinematics']},
            'miranda': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'monitor': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'player': {'category': 'object', 'funcs': ['ai_allegiance'], 'sources': ['08b_deltacontrol_boss', '08b_deltacontrol_mission']},
            'prophet': {'category': 'covenant', 'funcs': ['ai_allegiance'], 'sources': ['08b_deltacontrol_boss']},
            'repository': {'category': 'object', 'funcs': ['device_set_position', 'object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'rotors_x09': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'scarab': {'category': 'object', 'funcs': ['device_get_position', 'object_destroy', 'object_teleport'], 'sources': ['08b_deltacontrol_cinematics', '08b_deltacontrol_mission']},
            'scarab_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'scarab_gunners/main_gunner': {'category': 'object', 'funcs': ['ai_place'], 'sources': ['08b_deltacontrol_mission']},
            'scarab_screen': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'slipspace': {'category': 'object', 'funcs': ['object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'spore_01': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['08b_deltacontrol_cinematics']},
            'spore_02': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['08b_deltacontrol_cinematics']},
            'spore_03': {'category': 'object', 'funcs': ['object_cinematic_lod'], 'sources': ['08b_deltacontrol_cinematics']},
            'tartarus': {'category': 'covenant', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'tentacle_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility'], 'sources': ['08b_deltacontrol_cinematics']},
            'tentacle_02': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility'], 'sources': ['08b_deltacontrol_cinematics']},
            'tentacle_03': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility'], 'sources': ['08b_deltacontrol_cinematics']},
            'tentacle_04': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_cinematic_visibility'], 'sources': ['08b_deltacontrol_cinematics']},
            'tv_boss_ledge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_boss']},
            'tv_boss_platform': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_boss']},
            'tv_e11_exit_vicinity': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e11_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e11_outer_cove': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e11_pro_wraiths1_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e12_chamber_entered': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e12_cov_banshee0_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e12_ledge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e12_ledge_entrance': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e12_pro_inf0_end': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e12_swap_room_halfway': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e13_cutscene_trigger0': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e13_cutscene_trigger1': {'category': 'volume', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e1_advance0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e1_advance1': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e1_advance2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e1_advance3': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e1_advance4': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e1_canyon_entry': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e2_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e2_near_perimeter': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e2_pro_wraiths0_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e3_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e3_player_advance0': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e3_player_advance2': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e3_pro_inf0_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e3_pro_inf1_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e4_corner': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e4_halfway': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e4_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e4_main_shutdown': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e5_bridge_exit': {'category': 'device', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e5_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e5_pro_inf3_init': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e5_pro_phantom0_begin': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e6_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e6_main_room': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e7_brute_area': {'category': 'covenant', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e7_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e7_on_ledge': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e8_exit': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e8_scarab_fire_unsafe': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e9_main_begin': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e9_pro_banshees0_stop': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_e9_second_bend': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'tv_scarab': {'category': 'object', 'funcs': ['volume_test_objects'], 'sources': ['08b_deltacontrol_mission']},
            'wraith_01': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'x09_alcove': {'category': 'object', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'x09_chamber_door': {'category': 'device', 'funcs': ['object_cinematic_lod', 'object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
            'x09_lift': {'category': 'device', 'funcs': ['object_destroy'], 'sources': ['08b_deltacontrol_cinematics']},
        },
        "scripts": [('cs_boss_brutes_stunned', 'command_script', '08b_deltacontrol_boss'), ('cs_boss_tartarus_stunned', 'command_script', '08b_deltacontrol_boss'), ('cs_boss_tartarus_jump', 'command_script', '08b_deltacontrol_boss'), ('cs_boss_tartarus_cheer', 'command_script', '08b_deltacontrol_boss'), ('cs_boss_tartarus_taunt', 'command_script', '08b_deltacontrol_boss'), ('cs_boss_tartarus_shakefist', 'command_script', '08b_deltacontrol_boss'), ('cs_boss_johnson_idle', 'command_script', '08b_deltacontrol_boss'), ('cs_boss_johnson_idle2', 'command_script', '08b_deltacontrol_boss'), ('cs_boss_johnson_shoot', 'command_script', '08b_deltacontrol_boss'), ('cs_boss_miranda_nocrouch', 'command_script', '08b_deltacontrol_boss'), ('void', 'static', '08b_deltacontrol_boss'), ('void', 'static', '08b_deltacontrol_boss'), ('boss_flavor', 'dormant', '08b_deltacontrol_boss'), ('boss_music', 'dormant', '08b_deltacontrol_boss'), ('short', 'static', '08b_deltacontrol_boss'), ('short', 'static', '08b_deltacontrol_boss'), ('short', 'static', '08b_deltacontrol_boss'), ('void', 'static', '08b_deltacontrol_boss'), ('void', 'static', '08b_deltacontrol_boss'), ('void', 'static', '08b_deltacontrol_boss'), ('void', 'static', '08b_deltacontrol_boss'), ('void', 'static', '08b_deltacontrol_boss'), ('void', 'static', '08b_deltacontrol_boss'), ('void', 'static', '08b_deltacontrol_boss'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_cinematics'), ('c08_intra1_score_04', 'dormant', '08b_deltacontrol_cinematics'), ('c08_intra1_foley_04', 'dormant', '08b_deltacontrol_cinematics'), ('c08_2050_der', 'dormant', '08b_deltacontrol_cinematics'), ('c08_2060_soc', 'dormant', '08b_deltacontrol_cinematics'), ('c08_2070_grv', 'dormant', '08b_deltacontrol_cinematics'), ('c08_2080_der', 'dormant', '08b_deltacontrol_cinematics'), ('c08_2090_soc', 'dormant', '08b_deltacontrol_cinematics'), ('c08_2100_soc', 'dormant', '08b_deltacontrol_cinematics'), ('c04_intra1_fov_04', 'dormant', '08b_deltacontrol_cinematics'), ('c04_intra1_dof_04', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_intra1_04', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('c08_intra2_foley_01', 'dormant', '08b_deltacontrol_cinematics'), ('c08_3010_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_3020_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_3030_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_3040_der', 'dormant', '08b_deltacontrol_cinematics'), ('intra2_texture_cam_01', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_intra2', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('scarab_shake', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('c08_intra2_foley_02', 'dormant', '08b_deltacontrol_cinematics'), ('c08_3050_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_3061_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_3070_jon', 'dormant', '08b_deltacontrol_cinematics'), ('intra2_dof', 'dormant', '08b_deltacontrol_cinematics'), ('scarab_shake2', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('c08_intra3_foley_01', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4010_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4020_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4030_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4040_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4050_mir', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4060_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_intra3_fov_01', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_intra3_01', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('c08_intra2_miranda_emotion_01', 'dormant', '08b_deltacontrol_cinematics'), ('c08_intra2_miranda_emotion_02', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('c08_intra3_score_02', 'dormant', '08b_deltacontrol_cinematics'), ('c08_intra3_foley_02', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4070_der', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4080_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4100_der', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4110_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4120_der', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4140_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4150_der', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4160_der', 'dormant', '08b_deltacontrol_cinematics'), ('unhide_dervish', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('c08_intra3_foley_03', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4170_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4180_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4190_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4200_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4201_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4220_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4230_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4240_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4250_der', 'dormant', '08b_deltacontrol_cinematics'), ('c08_intra3_fov_03', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_intra3_03', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('c08_intra3_foley_04', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4260_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4270_der', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4280_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4290_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4300_der', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('c08_intra3_foley_05', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4310_jon', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4320_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4330_tar', 'dormant', '08b_deltacontrol_cinematics'), ('c08_4340_tar', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_intra3_05', 'dormant', '08b_deltacontrol_cinematics'), ('index_insertion', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('c08_intra3_05_cleanup', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('create_lift', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x09_foley_1', 'dormant', '08b_deltacontrol_cinematics'), ('x09_01_stop_sounds', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_x09_01', 'dormant', '08b_deltacontrol_cinematics'), ('x09_fov_01', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x09_miranda_emotion_01', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x09_score_2', 'dormant', '08b_deltacontrol_cinematics'), ('x09_foley_2', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_x09_02', 'dormant', '08b_deltacontrol_cinematics'), ('x09_dof_01', 'dormant', '08b_deltacontrol_cinematics'), ('lift_deactivate', 'dormant', '08b_deltacontrol_cinematics'), ('x09_miranda_emotion_02', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x09_foley_3', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x09_foley_4', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_x09_04', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x09_foley_5', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0010_mir', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0020_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0030_mir', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0040_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0050_mir', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0060_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0070_mir', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_x09_05', 'dormant', '08b_deltacontrol_cinematics'), ('beacon_shuffle', 'dormant', '08b_deltacontrol_cinematics'), ('x09_miranda_emotion_05', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x09_foley_6', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0080_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0090_mir', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0100_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0110_jon', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0120_mir', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0130_gsp', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0140_der', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_x09_06', 'dormant', '08b_deltacontrol_cinematics'), ('x09_miranda_emotion_06a', 'dormant', '08b_deltacontrol_cinematics'), ('x09_miranda_emotion_06b', 'dormant', '08b_deltacontrol_cinematics'), ('x09_miranda_emotion_06c', 'dormant', '08b_deltacontrol_cinematics'), ('x09_johnson_emotion_06a', 'dormant', '08b_deltacontrol_cinematics'), ('x09_johnson_emotion_06b', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x09_foley_7', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0150_to1', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_x09_07', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x09_score_8', 'dormant', '08b_deltacontrol_cinematics'), ('x09_foley_8', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0160_lhd', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0180_mas', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0190_mas', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0200_lhd', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0210_lhd', 'dormant', '08b_deltacontrol_cinematics'), ('x09_0220_mas', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_light_x09_chief_01', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_light_x09_hood_01', 'dormant', '08b_deltacontrol_cinematics'), ('final_explosion', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_light_x09_chief_02', 'dormant', '08b_deltacontrol_cinematics'), ('x09_hood_emotion_08', 'dormant', '08b_deltacontrol_cinematics'), ('shake_chief', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x10_score_1', 'dormant', '08b_deltacontrol_cinematics'), ('x10_foley_1', 'dormant', '08b_deltacontrol_cinematics'), ('x10_0010_grv', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_x10_01', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('x10_score_2', 'dormant', '08b_deltacontrol_cinematics'), ('x10_0020_grv', 'dormant', '08b_deltacontrol_cinematics'), ('x10_0030_grv', 'dormant', '08b_deltacontrol_cinematics'), ('x10_0040_cor', 'dormant', '08b_deltacontrol_cinematics'), ('x10_0041_cor', 'dormant', '08b_deltacontrol_cinematics'), ('cinematic_lighting_x10_02', 'dormant', '08b_deltacontrol_cinematics'), ('effect_cortana_appear', 'dormant', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'static', '08b_deltacontrol_cinematics'), ('void', 'stub', '08b_deltacontrol_mission'), ('void', 'stub', '08b_deltacontrol_mission'), ('void', 'stub', '08b_deltacontrol_mission'), ('void', 'stub', '08b_deltacontrol_mission'), ('void', 'stub', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('chapter_title0', 'dormant', '08b_deltacontrol_mission'), ('chapter_title1', 'dormant', '08b_deltacontrol_mission'), ('chapter_title2', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('objective0_set', 'dormant', '08b_deltacontrol_mission'), ('objective0_clear', 'dormant', '08b_deltacontrol_mission'), ('objective1_set', 'dormant', '08b_deltacontrol_mission'), ('objective1_clear', 'dormant', '08b_deltacontrol_mission'), ('objective2_set', 'dormant', '08b_deltacontrol_mission'), ('objective2_clear', 'dormant', '08b_deltacontrol_mission'), ('objective3_set', 'dormant', '08b_deltacontrol_mission'), ('objective3_clear', 'dormant', '08b_deltacontrol_mission'), ('objective4_set', 'dormant', '08b_deltacontrol_mission'), ('objective4_clear', 'dormant', '08b_deltacontrol_mission'), ('music_08b_01_stop', 'dormant', '08b_deltacontrol_mission'), ('music_08b_01_start_alt', 'dormant', '08b_deltacontrol_mission'), ('music_08b_01_start', 'dormant', '08b_deltacontrol_mission'), ('music_08b_02_stop', 'dormant', '08b_deltacontrol_mission'), ('music_08b_02_start', 'dormant', '08b_deltacontrol_mission'), ('music_08b_03_stop', 'dormant', '08b_deltacontrol_mission'), ('music_08b_03_start', 'dormant', '08b_deltacontrol_mission'), ('music_08b_04_stop', 'dormant', '08b_deltacontrol_mission'), ('music_08b_04_start', 'dormant', '08b_deltacontrol_mission'), ('music_08b_05_stop', 'dormant', '08b_deltacontrol_mission'), ('music_08b_05_start_alt', 'dormant', '08b_deltacontrol_mission'), ('music_08b_05_start', 'dormant', '08b_deltacontrol_mission'), ('music_08b_06_start', 'dormant', '08b_deltacontrol_mission'), ('music_08b_07_start', 'dormant', '08b_deltacontrol_mission'), ('music_08b_08_start', 'dormant', '08b_deltacontrol_mission'), ('music_08b_09_stop', 'dormant', '08b_deltacontrol_mission'), ('music_08b_09_start_alt', 'dormant', '08b_deltacontrol_mission'), ('music_08b_09_start', 'dormant', '08b_deltacontrol_mission'), ('music_08b_10_stop', 'dormant', '08b_deltacontrol_mission'), ('music_08b_10_start', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('e13_order_cycle', 'dormant', '08b_deltacontrol_mission'), ('e13_sen_monitor_main', 'dormant', '08b_deltacontrol_mission'), ('e13_pro_tartarus_main', 'dormant', '08b_deltacontrol_mission'), ('e13_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e13_mars_miranda_main', 'dormant', '08b_deltacontrol_mission'), ('e13_mars_johnson_main', 'dormant', '08b_deltacontrol_mission'), ('e13_cov_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e13_main', 'dormant', '08b_deltacontrol_mission'), ('e13_cinematic_main', 'dormant', '08b_deltacontrol_mission'), ('cs_e12_cov_phantom0_entry', 'command_script', '08b_deltacontrol_mission'), ('cs_e12_pro_inf0_1_wait', 'command_script', '08b_deltacontrol_mission'), ('cs_e12_pro_inf0_wait0', 'command_script', '08b_deltacontrol_mission'), ('cs_e12_pro_inf0_wait1', 'command_script', '08b_deltacontrol_mission'), ('cs_e12_cov_inf0_look', 'command_script', '08b_deltacontrol_mission'), ('cs_e12_cov_inf0_follow', 'command_script', '08b_deltacontrol_mission'), ('cs_e12_pro_inf0_captain', 'command_script', '08b_deltacontrol_mission'), ('cs_e12_pro_inf0_berserker', 'command_script', '08b_deltacontrol_mission'), ('cs_e12_cov_banshee0_entry', 'command_script', '08b_deltacontrol_mission'), ('e12_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e12_pro_inf0_ender', 'dormant', '08b_deltacontrol_mission'), ('e12_cov_phantom0_main', 'dormant', '08b_deltacontrol_mission'), ('e12_cov_banshees0_main', 'dormant', '08b_deltacontrol_mission'), ('e12_cov_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e12_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('cs_e11_pro_phantom0_0_main', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_pro_phantom0_1_main', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_attack_scarab', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_attack_scarab_behavior', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_pro_wraiths1_shoot', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_pro_wraiths1_bombard', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_ghost_door0_entry', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_spectre_door0_entry', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_pro_banshees0_0_entry', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_pro_banshees0_1_entry', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_scarab_main_gun_shoot', 'command_script', '08b_deltacontrol_mission'), ('cs_e11_cov_banshees0_die', 'command_script', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('short', 'static', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('e11_pro_phantom1_main', 'dormant', '08b_deltacontrol_mission'), ('e11_pro_phantom0_main', 'dormant', '08b_deltacontrol_mission'), ('e11_pro_banshees0_main', 'dormant', '08b_deltacontrol_mission'), ('e11_pro_spectres0_main', 'dormant', '08b_deltacontrol_mission'), ('e11_pro_ghosts0_main', 'dormant', '08b_deltacontrol_mission'), ('e11_pro_wraith_checkpoints', 'dormant', '08b_deltacontrol_mission'), ('e11_pro_wraith1_main', 'dormant', '08b_deltacontrol_mission'), ('e11_cov_banshees0_main', 'dormant', '08b_deltacontrol_mission'), ('e11_navpoint', 'dormant', '08b_deltacontrol_mission'), ('e11_navpoint_kill', 'dormant', '08b_deltacontrol_mission'), ('e11_door_opening', 'dormant', '08b_deltacontrol_mission'), ('e11_scarab_main', 'dormant', '08b_deltacontrol_mission'), ('e11_key', 'dormant', '08b_deltacontrol_mission'), ('e11_main', 'dormant', '08b_deltacontrol_mission'), ('cs_e9_pro_phantom0_exit', 'command_script', '08b_deltacontrol_mission'), ('cs_e9_pro_phantom0_entry', 'command_script', '08b_deltacontrol_mission'), ('cs_e9_pro_banshees0_entry', 'command_script', '08b_deltacontrol_mission'), ('e9_pro_spectres0_main', 'dormant', '08b_deltacontrol_mission'), ('e9_pro_phantom0_main', 'dormant', '08b_deltacontrol_mission'), ('e9_pro_banshees0_main', 'dormant', '08b_deltacontrol_mission'), ('e9_pro_inf3_main', 'dormant', '08b_deltacontrol_mission'), ('e9_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e9_scarab_navpoint', 'dormant', '08b_deltacontrol_mission'), ('e9_scarab_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('e9_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('cs_e8_pro_phantom0_exit', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_cov_banshee0_entry0', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_cov_banshee0_entry1', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_cov_banshee0_entry2', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_cov_banshee0_flyby', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_pro_wraith0_0_bombard', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_pro_wraith0_1_bombard', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_pro_wraith0_2_bombard', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_scarab_main_gun_idle', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_scarab_main_gun_shoot0', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_scarab_main_gun_shoot1', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_scarab_main_gun_shoot2', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_mars_johnson_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_mars_inf0_emerge', 'command_script', '08b_deltacontrol_mission'), ('cs_e8_mars_inf0_retreat', 'command_script', '08b_deltacontrol_mission'), ('e8_scarab_main', 'dormant', '08b_deltacontrol_mission'), ('e8_wraith_dialogue', 'dormant', '08b_deltacontrol_mission'), ('e8_pro_wraiths0_main', 'dormant', '08b_deltacontrol_mission'), ('e8_cov_banshees0_main', 'dormant', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('e8_mars_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e8_cov_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e8_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('scarab_test_loop', 'dormant', '08b_deltacontrol_mission'), ('cs_e7_mars_inf0_wait', 'command_script', '08b_deltacontrol_mission'), ('cs_e7_mars_inf0_johnson', 'command_script', '08b_deltacontrol_mission'), ('cs_e7_pro_inf0_wait', 'command_script', '08b_deltacontrol_mission'), ('cs_e7_pro_inf0_captain_alert', 'command_script', '08b_deltacontrol_mission'), ('cs_e7_pro_inf0_captain', 'command_script', '08b_deltacontrol_mission'), ('cs_e7_pro_inf0_sentry0_alerted', 'command_script', '08b_deltacontrol_mission'), ('cs_e7_pro_inf0_sentry0', 'command_script', '08b_deltacontrol_mission'), ('e7_mars_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e7_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e7_cov_hunters0_main', 'dormant', '08b_deltacontrol_mission'), ('e7_cov_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e7_scarab_main', 'startup', '08b_deltacontrol_mission'), ('e7_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('cs_e6_destroy_door0', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_destroy_door1', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_destroy_door2', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_destroy_door3', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_destroy_door4', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_destroy_door5', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_release_captives', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_jailbreak_behavior', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_cov_inf1_0_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_cov_inf1_1_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_cov_inf1_2_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_cov_inf1_3_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_cov_hunters0_0_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_cov_hunters0_1_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e6_jailbreak_scene', 'command_script', '08b_deltacontrol_mission'), ('e6_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e6_cov_hunters0_main', 'dormant', '08b_deltacontrol_mission'), ('e6_cov_inf1_main', 'dormant', '08b_deltacontrol_mission'), ('e6_cov_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e6_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('cs_e5_pro_phantom0_entry', 'command_script', '08b_deltacontrol_mission'), ('cs_e5_pro_phantom0_exit', 'command_script', '08b_deltacontrol_mission'), ('e5_pro_phantom0_main', 'dormant', '08b_deltacontrol_mission'), ('e5_pro_inf3_main', 'dormant', '08b_deltacontrol_mission'), ('e5_pro_inf2_main', 'dormant', '08b_deltacontrol_mission'), ('e5_pro_inf1_main', 'dormant', '08b_deltacontrol_mission'), ('e5_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e5_cov_hunters0_main', 'dormant', '08b_deltacontrol_mission'), ('e5_cov_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e5_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('e4_music', 'dormant', '08b_deltacontrol_mission'), ('e4_pro_inf3_main', 'dormant', '08b_deltacontrol_mission'), ('e4_pro_inf2_main', 'dormant', '08b_deltacontrol_mission'), ('e4_pro_inf1_main', 'dormant', '08b_deltacontrol_mission'), ('e4_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e4_cov_hunters0_main', 'dormant', '08b_deltacontrol_mission'), ('e4_cov_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e4_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('cs_e3_cov_hunters0_0', 'command_script', '08b_deltacontrol_mission'), ('cs_e3_cov_hunters0_1', 'command_script', '08b_deltacontrol_mission'), ('cs_e3_cov_inf0_0', 'command_script', '08b_deltacontrol_mission'), ('cs_e3_cov_inf0_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e3_pro_inf2_idle', 'command_script', '08b_deltacontrol_mission'), ('cs_e3_weapon_scene', 'command_script', '08b_deltacontrol_mission'), ('e3_weapon_scene', 'dormant', '08b_deltacontrol_mission'), ('e3_objective_failsafe', 'dormant', '08b_deltacontrol_mission'), ('e3_pro_inf2_main', 'dormant', '08b_deltacontrol_mission'), ('e3_pro_inf1_main', 'dormant', '08b_deltacontrol_mission'), ('e3_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e3_cov_hunters0_main', 'dormant', '08b_deltacontrol_mission'), ('e3_cov_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e3_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('e2_dialogue', 'dormant', '08b_deltacontrol_mission'), ('e2_door_unlocker', 'dormant', '08b_deltacontrol_mission'), ('cs_e2_pro_phantom0_0_entry', 'command_script', '08b_deltacontrol_mission'), ('cs_e2_pro_phantom0_0_exit', 'command_script', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('e2_pro_phantoms0_main', 'dormant', '08b_deltacontrol_mission'), ('e2_pro_wraiths0_main', 'dormant', '08b_deltacontrol_mission'), ('e2_pro_ghosts0_main', 'dormant', '08b_deltacontrol_mission'), ('e2_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e2_cov_wraith0_main', 'dormant', '08b_deltacontrol_mission'), ('e2_cov_spectre0_main', 'dormant', '08b_deltacontrol_mission'), ('e2_main', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('cs_e1_pro_phantom0_exit', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_pro_phantom0_entry', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_cov_spectre0_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_cov_spectre0_passenger', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_cov_commander0_legendary', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_cov_commander0_init', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_pro_ghosts0_2_entry0', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_pro_ghosts0_2_entry1', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_pro_ghosts0_1_entry0', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_pro_ghosts0_1_entry1', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_pro_ghosts0_0_entry0', 'command_script', '08b_deltacontrol_mission'), ('cs_e1_pro_ghosts0_0_entry1', 'command_script', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('boolean', 'static', '08b_deltacontrol_mission'), ('e1_weather', 'dormant', '08b_deltacontrol_mission'), ('e1_pro_phantom0_main', 'dormant', '08b_deltacontrol_mission'), ('e1_pro_ghosts0_main', 'dormant', '08b_deltacontrol_mission'), ('e1_pro_inf0_main', 'dormant', '08b_deltacontrol_mission'), ('e1_cov_spectre0_main', 'dormant', '08b_deltacontrol_mission'), ('e1_cov_wraiths0_main', 'dormant', '08b_deltacontrol_mission'), ('e1_main', 'dormant', '08b_deltacontrol_mission'), ('mission_start', 'dormant', '08b_deltacontrol_mission'), ('void', 'static', '08b_deltacontrol_mission'), ('mission_main', 'startup', '08b_deltacontrol_mission'), ('08_intra1_04_predict', 'dormant', '08b_deltacontrol_prediction'), ('08_intra2_01_predict', 'dormant', '08b_deltacontrol_prediction'), ('08_intra2_02_predict', 'dormant', '08b_deltacontrol_prediction'), ('08_intra3_01_predict', 'dormant', '08b_deltacontrol_prediction'), ('08_intra3_02_predict', 'dormant', '08b_deltacontrol_prediction'), ('08_intra3_03_predict', 'dormant', '08b_deltacontrol_prediction'), ('08_intra3_04_predict', 'dormant', '08b_deltacontrol_prediction'), ('08_intra3_05_predict', 'dormant', '08b_deltacontrol_prediction'), ('08_intra3_06_predict', 'dormant', '08b_deltacontrol_prediction'), ('x09_01_predict', 'dormant', '08b_deltacontrol_prediction'), ('x09_02_predict', 'dormant', '08b_deltacontrol_prediction'), ('x09_03_predict', 'dormant', '08b_deltacontrol_prediction'), ('x09_04_predict', 'dormant', '08b_deltacontrol_prediction'), ('x09_05_predict', 'dormant', '08b_deltacontrol_prediction'), ('x09_06_predict', 'dormant', '08b_deltacontrol_prediction'), ('x09_07_predict', 'dormant', '08b_deltacontrol_prediction'), ('x09_08_predict', 'dormant', '08b_deltacontrol_prediction'), ('x10_01_predict', 'dormant', '08b_deltacontrol_prediction'), ('x10_02_predict', 'dormant', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('void', 'static', '08b_deltacontrol_prediction'), ('unit', 'static', 'global_scripts'), ('unit', 'static', 'global_scripts'), ('short', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('boolean', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('_stealth_toggle_monitor', 'dormant', 'global_scripts'), ('_stealth_timer_monitor', 'dormant', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts'), ('void', 'static', 'global_scripts')],
    },
}


CATEGORY_COLORS = {
    'covenant': '#D85A30',
    'human':    '#378ADD',
    'device':   '#1D9E75',
    'volume':   '#EF9F27',
    'object':   '#9898b8',
}

CATEGORY_LABELS = {
    'covenant': 'Covenant AI',
    'human':    'Human AI',
    'device':   'Device',
    'volume':   'Volume',
    'object':   'Object',
}

SCRIPT_TYPE_COLORS = {
    'dormant':    '#7F77DD',
    'continuous': '#3dcc96',
    'startup':    '#f0b040',
    'static':     '#9898b8',
    'stub':       '#555577',
}


def get_script_db(map_path: str) -> dict:
    norm = map_path.replace("\\\\", "/").replace("\\", "/").strip()
    return SCRIPT_DATABASE.get(norm, {"objects": {}, "scripts": []})



def _script_section(name: str) -> str:
    """Extract the section prefix from a script name.
    e.g. 'bay1_cov_floor_elt' -> 'bay1', 'e11_cov_inf1_0/elite0' -> 'e11'
    Returns '' if no clear prefix found."""
    import re as _re
    m = _re.match(r'^([a-zA-Z]+[0-9]*)', name)
    return m.group(1) if m else ""



class ScriptsMixin:
    """Scripts tab: named script entities cross-referenced with live objects."""

    def _build_scripts_panel(self, parent):
        self._scripts_db         = {}
        self._scripts_seen       = set()   # names ever placed (for DEAD state)
        self._scripts_filter_cat = tk.StringVar(value="all")
        self._scripts_filter_sect= tk.StringVar(value="all")
        self._scripts_filter_state = tk.StringVar(value="all")
        self._scripts_filter_alive = tk.BooleanVar(value=False)
        self._scripts_show_orphans = tk.BooleanVar(value=False)
        self._scripts_search     = tk.StringVar()
        # Timer watch state: name -> {state, state_time, placed_time, history}
        self._timer_watches: dict  = {}   # pinned script names -> watch data
        self._timer_states:  dict  = {}   # name -> last known state str
        # Kill trigger progress tracking: group name -> initial placed count
        self._kg_initial:    dict  = {}   # name -> int (first non-zero count seen)
        # Change log entries: list of dicts
        self._change_log:    list  = []
        self._change_log_max = 60
        # Flow diagram canvas reference
        self._flow_canvas    = None
        self._flow_node_pos  = {}   # section -> (x,y)

        # ── Notebook: Named Objects + Orphans ─────────────────────────────
        nb = ttk.Notebook(parent)
        nb.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        self._scripts_nb = nb

        # ── Tab 1: Named objects ──────────────────────────────────────────
        tab_named = ttk.Frame(nb)
        nb.add(tab_named, text="Named Objects")

        # Filter bar
        fbar = ttk.Frame(tab_named)
        fbar.pack(fill=tk.X, pady=(4, 2))

        ttk.Label(fbar, text="Category:").pack(side=tk.LEFT, padx=(0, 2))
        cats = ["all"] + list(CATEGORY_LABELS.values())
        cat_combo = ttk.Combobox(fbar, textvariable=self._scripts_filter_cat,
                                  values=cats, width=12, state="readonly")
        cat_combo.pack(side=tk.LEFT, padx=(0, 6))
        cat_combo.bind("<<ComboboxSelected>>", lambda _: self._scripts_refresh())

        ttk.Label(fbar, text="Section:").pack(side=tk.LEFT, padx=(0, 2))
        self._scripts_sect_combo = ttk.Combobox(
            fbar, textvariable=self._scripts_filter_sect,
            values=["all"], width=12, state="readonly")
        self._scripts_sect_combo.pack(side=tk.LEFT, padx=(0, 6))
        self._scripts_sect_combo.bind(
            "<<ComboboxSelected>>", lambda _: self._scripts_refresh())

        ttk.Label(fbar, text="State:").pack(side=tk.LEFT, padx=(0, 2))
        state_combo = ttk.Combobox(
            fbar, textvariable=self._scripts_filter_state,
            values=["all", "NOT YET", "PLACED", "DEAD"], width=9, state="readonly")
        state_combo.pack(side=tk.LEFT, padx=(0, 6))
        state_combo.bind("<<ComboboxSelected>>", lambda _: self._scripts_refresh())

        ttk.Label(fbar, text="Search:").pack(side=tk.LEFT, padx=(0, 2))
        ttk.Entry(fbar, textvariable=self._scripts_search,
                  width=18).pack(side=tk.LEFT)
        self._scripts_search.trace_add("write", lambda *_: self._scripts_refresh())

        self._scripts_count_lbl = ttk.Label(
            fbar, text="", foreground="#9898b8", font=("Consolas", 9))
        self._scripts_count_lbl.pack(side=tk.RIGHT)

        # Main pane
        pane = ttk.PanedWindow(tab_named, orient=tk.HORIZONTAL)
        pane.pack(fill=tk.BOTH, expand=True)

        # Left: object table
        left = ttk.Frame(pane)
        pane.add(left, weight=3)
        obj_cols = ("name", "section", "category", "state",
                    "living", "obj_type", "health", "cluster")
        self._scripts_tree = ttk.Treeview(left, columns=obj_cols,
                                           show="headings", selectmode="browse")
        obj_col_cfg = [
            ("name",     "Script Name", 190, tk.W),
            ("section",  "Section",      80, tk.W),
            ("category", "Category",     82, tk.W),
            ("state",    "State",        70, tk.CENTER),
            ("living",   "Enemies",      64, tk.CENTER),
            ("obj_type", "Obj Type",     80, tk.W),
            ("health",   "HP",           44, tk.CENTER),
            ("cluster",  "Cluster",      50, tk.E),
        ]
        for col, hd, w, anc in obj_col_cfg:
            self._scripts_tree.heading(col, text=hd,
                command=lambda c=col: self._scripts_sort(c))
            self._scripts_tree.column(col, width=w, anchor=anc, minwidth=20)
        for cat, color in CATEGORY_COLORS.items():
            self._scripts_tree.tag_configure(cat, foreground=color)
        self._scripts_tree.tag_configure("placed",  foreground="#3dcc96",
                                                    background="#0e2218")
        self._scripts_tree.tag_configure("dead",    foreground="#3a3a5a")
        self._scripts_tree.tag_configure("notyet",  foreground="#9898b8")
        self._scripts_tree.tag_configure("kill_enc",foreground="#f0b040")

        vsb = ttk.Scrollbar(left, orient=tk.VERTICAL,
                             command=self._scripts_tree.yview)
        self._scripts_tree.configure(yscrollcommand=vsb.set)
        self._scripts_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._scripts_tree.bind("<<TreeviewSelect>>", self._on_script_obj_select)
        self._scripts_tree.bind("<Up>",
            lambda e: self.after(0, self._on_script_obj_select))
        self._scripts_tree.bind("<Down>",
            lambda e: self.after(0, self._on_script_obj_select))

        # Right: detail + scripts list
        right = ttk.Frame(pane)
        pane.add(right, weight=2)

        obj_det = ttk.LabelFrame(right, text="Script object detail")
        obj_det.pack(fill=tk.X, padx=4, pady=(0, 4))
        self._scripts_detail_text = tk.Text(
            obj_det, height=9, bg="#14141c", fg="#e8e8f0",
            font=("Consolas", 10), relief=tk.FLAT,
            state=tk.DISABLED, cursor="arrow", padx=6, pady=4)
        self._scripts_detail_text.pack(fill=tk.X)
        for tag, fg in [("key","#7ab4e0"),("val","#e8e8f0"),("live","#3dcc96"),
                        ("dead","#3a3a5a"),("addr","#60a8f0"),("warn","#f0b040")]:
            self._scripts_detail_text.tag_configure(tag, foreground=fg)

        scr_frame = ttk.LabelFrame(right, text="Map scripts")
        scr_frame.pack(fill=tk.BOTH, expand=True, padx=4)
        scr_cols = ("name", "type", "source")
        self._scripts_list_tree = ttk.Treeview(
            scr_frame, columns=scr_cols, show="headings", height=7)
        for col, hd, w, anc in [("name","Script Name",175,tk.W),
                                  ("type","Type",75,tk.W),
                                  ("source","Source",135,tk.W)]:
            self._scripts_list_tree.heading(col, text=hd)
            self._scripts_list_tree.column(col, width=w, anchor=anc, minwidth=20)
        for stype, color in SCRIPT_TYPE_COLORS.items():
            self._scripts_list_tree.tag_configure(stype, foreground=color)
        scr_vsb = ttk.Scrollbar(scr_frame, orient=tk.VERTICAL,
                                  command=self._scripts_list_tree.yview)
        self._scripts_list_tree.configure(yscrollcommand=scr_vsb.set)
        self._scripts_list_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scr_vsb.pack(side=tk.RIGHT, fill=tk.Y)

        scr_sfr = ttk.Frame(right)
        scr_sfr.pack(fill=tk.X, padx=4, pady=(2, 0))
        ttk.Label(scr_sfr, text="Filter scripts:",
                  foreground="#9898b8", font=("Consolas", 9)).pack(side=tk.LEFT)
        self._scripts_list_search = tk.StringVar()
        ttk.Entry(scr_sfr, textvariable=self._scripts_list_search,
                  width=18).pack(side=tk.LEFT, padx=4)
        self._scripts_list_search.trace_add(
            "write", lambda *_: self._scripts_refresh_list())

        # ── Tab 2: Enemy Groups ───────────────────────────────────────────
        tab_enemies = ttk.Frame(nb)
        nb.add(tab_enemies, text="⚔ Enemy Groups")

        eg_info = ttk.Label(tab_enemies,
            text="Script groups using ai_living_count — shows live enemy counts per group.",
            foreground="#9898b8", font=("Consolas", 9))
        eg_info.pack(fill=tk.X, padx=8, pady=(6, 2))

        # Filter bar
        eg_fbar = ttk.Frame(tab_enemies)
        eg_fbar.pack(fill=tk.X, padx=8, pady=(0, 4))
        ttk.Label(eg_fbar, text="Section:").pack(side=tk.LEFT, padx=(0, 2))
        self._eg_filter_sect = tk.StringVar(value="all")
        self._eg_sect_combo = ttk.Combobox(
            eg_fbar, textvariable=self._eg_filter_sect,
            values=["all"], width=12, state="readonly")
        self._eg_sect_combo.pack(side=tk.LEFT, padx=(0, 6))
        self._eg_sect_combo.bind("<<ComboboxSelected>>", lambda _: self._eg_refresh())
        ttk.Label(eg_fbar, text="Search:").pack(side=tk.LEFT, padx=(0, 2))
        self._eg_search = tk.StringVar()
        ttk.Entry(eg_fbar, textvariable=self._eg_search, width=18).pack(side=tk.LEFT)
        self._eg_search.trace_add("write", lambda *_: self._eg_refresh())
        self._eg_count_lbl = ttk.Label(
            eg_fbar, text="", foreground="#9898b8", font=("Consolas", 9))
        self._eg_count_lbl.pack(side=tk.RIGHT)

        # Enemy group table
        eg_cols = ("name", "section", "enemies", "total", "types", "avg_hp", "min_hp", "state")
        self._eg_tree = ttk.Treeview(tab_enemies, columns=eg_cols, show="headings")
        eg_col_cfg = [
            ("name",    "Group Name",  200, tk.W),
            ("section", "Section",      70, tk.W),
            ("enemies", "Enemies",      60, tk.CENTER),
            ("total",   "Total",        50, tk.CENTER),
            ("types",   "Types",       180, tk.W),
            ("avg_hp",  "Avg HP",       55, tk.CENTER),
            ("min_hp",  "Min HP",       55, tk.CENTER),
            ("state",   "State",        65, tk.CENTER),
        ]
        for col, hd, w, anc in eg_col_cfg:
            self._eg_tree.heading(col, text=hd,
                command=lambda c=col: self._eg_sort(c))
            self._eg_tree.column(col, width=w, anchor=anc, minwidth=20)
        self._eg_tree.tag_configure("active",   foreground="#f0b040", background="#1a1500")
        self._eg_tree.tag_configure("placed",   foreground="#3dcc96", background="#0e2218")
        self._eg_tree.tag_configure("dead",     foreground="#3a3a5a")
        self._eg_tree.tag_configure("notyet",   foreground="#9898b8")
        self._eg_tree.tag_configure("critical", foreground="#cc3333", background="#200808")
        eg_vsb = ttk.Scrollbar(tab_enemies, orient=tk.VERTICAL,
                                command=self._eg_tree.yview)
        self._eg_tree.configure(yscrollcommand=eg_vsb.set)
        self._eg_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(8, 0), pady=(0, 4))
        eg_vsb.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 4), padx=(0, 8))
        self._eg_tree.bind("<<TreeviewSelect>>", lambda _: self._eg_draw_bars())

        # Kill trigger progress bars
        eg_bar_lbl = ttk.Label(tab_enemies, text="Kill trigger progress  (enemies remaining / initial placed)",
                               foreground="#9898b8", font=("Consolas", 8))
        eg_bar_lbl.pack(fill=tk.X, padx=8)
        self._eg_bar_canvas = tk.Canvas(tab_enemies, bg="#0d0d12",
                                         height=110, highlightthickness=0)
        self._eg_bar_canvas.pack(fill=tk.X, padx=8, pady=(2, 8))

        # ── Tab 3: Encounter Flow ────────────────────────────────────────
        tab_flow = ttk.Frame(nb)
        nb.add(tab_flow, text="🔀 Flow")

        flow_top = ttk.Frame(tab_flow)
        flow_top.pack(fill=tk.X, padx=8, pady=(4, 2))
        ttk.Label(flow_top, text="Encounter section progression — color: grey=not yet, amber=active, green=cleared",
                  foreground="#9898b8", font=("Consolas", 8)).pack(side=tk.LEFT)
        ttk.Button(flow_top, text="Redraw", width=7,
                   command=self._flow_redraw).pack(side=tk.RIGHT)

        flow_outer = tk.Frame(tab_flow, bg="#0d0d12")
        flow_outer.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
        flow_vsb = ttk.Scrollbar(flow_outer, orient=tk.VERTICAL)
        flow_hsb = ttk.Scrollbar(flow_outer, orient=tk.HORIZONTAL)
        flow_vsb.pack(side=tk.RIGHT, fill=tk.Y)
        flow_hsb.pack(side=tk.BOTTOM, fill=tk.X)
        self._flow_canvas = tk.Canvas(
            flow_outer, bg="#0d0d12", highlightthickness=0,
            yscrollcommand=flow_vsb.set, xscrollcommand=flow_hsb.set)
        flow_vsb.config(command=self._flow_canvas.yview)
        flow_hsb.config(command=self._flow_canvas.xview)
        self._flow_canvas.pack(fill=tk.BOTH, expand=True)
        self._flow_canvas.bind("<Button-1>", self._flow_on_click)
        self._flow_canvas.bind(
            "<MouseWheel>",
            lambda e: self._flow_canvas.yview_scroll(-1 if e.delta > 0 else 1, "units"))

        # ── Tab 4: Source Map (dependency) ───────────────────────────────
        tab_srcmap = ttk.Frame(nb)
        nb.add(tab_srcmap, text="📦 Source Map")

        sm_top = ttk.Frame(tab_srcmap)
        sm_top.pack(fill=tk.X, padx=8, pady=(4, 2))
        ttk.Label(sm_top, text="Dormant scripts grouped by source file — shows which scripts share an encounter system.",
                  foreground="#9898b8", font=("Consolas", 8)).pack(side=tk.LEFT)
        sm_search_var = tk.StringVar()
        self._sm_search = sm_search_var
        ttk.Label(sm_top, text="Filter:").pack(side=tk.RIGHT, padx=(8, 2))
        ttk.Entry(sm_top, textvariable=sm_search_var, width=18).pack(side=tk.RIGHT)
        sm_search_var.trace_add("write", lambda *_: self._srcmap_refresh())

        sm_cols = ("name", "type", "state")
        self._sm_tree = ttk.Treeview(tab_srcmap, columns=sm_cols, show="tree headings")
        for col, hd, w, anc in [
                ("name",  "Script / Source",  260, tk.W),
                ("type",  "Type",              80, tk.W),
                ("state", "State",             70, tk.CENTER)]:
            self._sm_tree.heading(col, text=hd)
            self._sm_tree.column(col, width=w, anchor=anc, minwidth=30)
        self._sm_tree.column("#0", width=0, minwidth=0, stretch=False)
        for stype, color in SCRIPT_TYPE_COLORS.items():
            self._sm_tree.tag_configure(f"t_{stype}", foreground=color)
        self._sm_tree.tag_configure("src_header", foreground="#7ab4e0",
                                     font=("Consolas", 9, "bold"))
        self._sm_tree.tag_configure("placed",  foreground="#3dcc96", background="#0e2218")
        self._sm_tree.tag_configure("dead",    foreground="#3a3a5a")
        sm_vsb = ttk.Scrollbar(tab_srcmap, orient=tk.VERTICAL,
                                command=self._sm_tree.yview)
        self._sm_tree.configure(yscrollcommand=sm_vsb.set)
        self._sm_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(8, 0), pady=(0, 8))
        sm_vsb.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 8), padx=(0, 8))

        # ── Tab 5: Change Log ─────────────────────────────────────────────
        tab_changelog = ttk.Frame(nb)
        nb.add(tab_changelog, text="📋 Changes")

        cl_top = ttk.Frame(tab_changelog)
        cl_top.pack(fill=tk.X, padx=8, pady=(4, 2))
        ttk.Label(cl_top, text="Live memory diff — spawns, deaths, HP changes, teleports.",
                  foreground="#9898b8", font=("Consolas", 8)).pack(side=tk.LEFT)
        ttk.Button(cl_top, text="Clear", width=6,
                   command=self._changelog_clear).pack(side=tk.RIGHT)

        cl_filter_fr = ttk.Frame(tab_changelog)
        cl_filter_fr.pack(fill=tk.X, padx=8, pady=(0, 2))
        self._cl_show_spawn  = tk.BooleanVar(value=True)
        self._cl_show_death  = tk.BooleanVar(value=True)
        self._cl_show_hp     = tk.BooleanVar(value=True)
        self._cl_show_tele   = tk.BooleanVar(value=True)
        self._cl_hp_thresh   = tk.DoubleVar(value=0.05)
        for text, var in [("Spawns", self._cl_show_spawn),
                           ("Deaths", self._cl_show_death),
                           ("HP Δ",   self._cl_show_hp),
                           ("Teleports", self._cl_show_tele)]:
            tk.Checkbutton(cl_filter_fr, text=text, variable=var,
                           command=self._changelog_redisplay,
                           bg="#0d0d12", fg="#aaaacc", selectcolor="#0d0d12",
                           activebackground="#0d0d12", activeforeground="#aaaacc",
                           relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 8))
        ttk.Label(cl_filter_fr, text="HP thresh:").pack(side=tk.LEFT)
        ttk.Spinbox(cl_filter_fr, from_=0.01, to=0.5, increment=0.01,
                    textvariable=self._cl_hp_thresh, width=5,
                    command=self._changelog_redisplay).pack(side=tk.LEFT, padx=(2, 0))

        cl_frame = tk.Frame(tab_changelog, bg="#0d0d12")
        cl_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(2, 8))
        cl_vsb = ttk.Scrollbar(cl_frame, orient=tk.VERTICAL)
        cl_vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._cl_text = tk.Text(
            cl_frame, bg="#0d0d12", fg="#c8c8e0",
            font=("Consolas", 9), relief=tk.FLAT,
            state=tk.DISABLED, cursor="arrow",
            yscrollcommand=cl_vsb.set, wrap=tk.NONE)
        cl_vsb.config(command=self._cl_text.yview)
        self._cl_text.pack(fill=tk.BOTH, expand=True)
        # Colour tags for change log
        for tag, fg, bg in [
                ("spawn",   "#3dcc96", "#0a1a10"),
                ("death",   "#cc4444", "#1a0808"),
                ("hp",      "#f0b040", "#1a1300"),
                ("tele",    "#7F77DD", "#0e0e20"),
                ("time",    "#555577", ""),
                ("label",   "#9898b8", ""),
                ("neutral", "#606080", "")]:
            kw = {"foreground": fg}
            if bg:
                kw["background"] = bg
            self._cl_text.tag_configure(tag, **kw)

        # ── Tab 6: Orphaned objects ───────────────────────────────────────
        tab_orphans = ttk.Frame(nb)
        nb.add(tab_orphans, text="Orphaned Objects")

        orp_info = ttk.Label(tab_orphans,
            text="Live objects in the object table with no matching script name for this map.",
            foreground="#9898b8", font=("Consolas", 9))
        orp_info.pack(fill=tk.X, padx=8, pady=(6, 2))

        orp_cols = ("index", "salt", "type", "tag", "health", "cluster", "origin")
        self._scripts_orp_tree = ttk.Treeview(
            tab_orphans, columns=orp_cols, show="headings")
        orp_col_cfg = [
            ("index",   "Idx",   50, tk.E),
            ("salt",    "Salt",  60, tk.E),
            ("type",    "Type",  90, tk.W),
            ("tag",     "Tag",  280, tk.W),
            ("health",  "HP",    50, tk.CENTER),
            ("cluster", "Clus",  45, tk.E),
            ("origin",  "Origin",190, tk.W),
        ]
        for col, hd, w, anc in orp_col_cfg:
            self._scripts_orp_tree.heading(col, text=hd)
            self._scripts_orp_tree.column(col, width=w, anchor=anc, minwidth=20)

        orp_vsb = ttk.Scrollbar(tab_orphans, orient=tk.VERTICAL,
                                  command=self._scripts_orp_tree.yview)
        self._scripts_orp_tree.configure(yscrollcommand=orp_vsb.set)
        self._scripts_orp_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,
                                     padx=(8, 0), pady=(0, 8))
        orp_vsb.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 8), padx=(0, 8))

        self._scripts_orp_count_lbl = ttk.Label(
            tab_orphans, text="", foreground="#9898b8", font=("Consolas", 9))
        self._scripts_orp_count_lbl.pack()

        # ── Tab 3: Timer Watch ────────────────────────────────────────────
        tab_timers = ttk.Frame(nb)
        nb.add(tab_timers, text="⏱ Timers")

        # Top controls
        tw_top = ttk.Frame(tab_timers)
        tw_top.pack(fill=tk.X, padx=8, pady=(6, 2))

        ttk.Label(tw_top, text="Watch dormant scripts as timers.",
                  foreground="#9898b8", font=("Consolas", 9)).pack(side=tk.LEFT)

        tw_btn_clr = ttk.Button(tw_top, text="Clear All",
                                width=9, command=self._timer_clear_all)
        tw_btn_clr.pack(side=tk.RIGHT)

        # Search/add bar
        tw_add_fr = ttk.Frame(tab_timers)
        tw_add_fr.pack(fill=tk.X, padx=8, pady=(0, 4))
        ttk.Label(tw_add_fr, text="Add watch:").pack(side=tk.LEFT, padx=(0, 4))
        self._timer_add_var = tk.StringVar()
        tw_entry = ttk.Entry(tw_add_fr, textvariable=self._timer_add_var, width=30)
        tw_entry.pack(side=tk.LEFT, padx=(0, 4))
        tw_entry.bind("<Return>", lambda _: self._timer_add_watch())
        ttk.Button(tw_add_fr, text="Add", width=5,
                   command=self._timer_add_watch).pack(side=tk.LEFT)

        # Autocomplete listbox (dormant scripts)
        tw_picker_fr = ttk.LabelFrame(tab_timers, text="Dormant scripts (double-click to watch)")
        tw_picker_fr.pack(fill=tk.X, padx=8, pady=(0, 4))
        tw_picker_cols = ("name", "source")
        self._timer_picker_tree = ttk.Treeview(
            tw_picker_fr, columns=tw_picker_cols, show="headings", height=5)
        for col, hd, w in [("name","Script Name",220),("source","Source",200)]:
            self._timer_picker_tree.heading(col, text=hd)
            self._timer_picker_tree.column(col, width=w, anchor=tk.W, minwidth=60)
        self._timer_picker_tree.tag_configure("dormant", foreground="#7F77DD")
        self._timer_picker_tree.tag_configure("continuous", foreground="#3dcc96")
        tw_pk_vsb = ttk.Scrollbar(tw_picker_fr, orient=tk.VERTICAL,
                                   command=self._timer_picker_tree.yview)
        self._timer_picker_tree.configure(yscrollcommand=tw_pk_vsb.set)
        self._timer_picker_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tw_pk_vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._timer_picker_tree.bind("<Double-1>", self._timer_picker_dblclick)

        tw_pick_search_fr = ttk.Frame(tab_timers)
        tw_pick_search_fr.pack(fill=tk.X, padx=8, pady=(0, 2))
        ttk.Label(tw_pick_search_fr, text="Filter:",
                  foreground="#9898b8", font=("Consolas", 9)).pack(side=tk.LEFT)
        self._timer_pick_search = tk.StringVar()
        ttk.Entry(tw_pick_search_fr, textvariable=self._timer_pick_search,
                  width=22).pack(side=tk.LEFT, padx=4)
        self._timer_pick_search.trace_add("write", lambda *_: self._timer_refresh_picker())

        # Active timer watch table
        tw_frame = ttk.LabelFrame(tab_timers, text="Active Timer Watches")
        tw_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 6))
        tw_cols = ("name", "state", "elapsed", "dur", "transitions")
        self._timer_tree = ttk.Treeview(
            tw_frame, columns=tw_cols, show="headings")
        tw_col_cfg = [
            ("name",        "Script Name",   220, tk.W),
            ("state",       "State",           70, tk.CENTER),
            ("elapsed",     "In State",        80, tk.CENTER),
            ("dur",         "Last Active",     80, tk.CENTER),
            ("transitions", "History",        280, tk.W),
        ]
        for col, hd, w, anc in tw_col_cfg:
            self._timer_tree.heading(col, text=hd)
            self._timer_tree.column(col, width=w, anchor=anc, minwidth=30)
        self._timer_tree.tag_configure("placed",  foreground="#3dcc96", background="#0e2218")
        self._timer_tree.tag_configure("notyet",  foreground="#9898b8")
        self._timer_tree.tag_configure("dead",    foreground="#555577")
        tw_vsb = ttk.Scrollbar(tw_frame, orient=tk.VERTICAL,
                                command=self._timer_tree.yview)
        self._timer_tree.configure(yscrollcommand=tw_vsb.set)
        self._timer_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tw_vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._timer_tree.bind("<Delete>", self._timer_remove_selected)
        ttk.Label(tab_timers,
                  text="Delete key removes selected watch",
                  foreground="#555577", font=("Consolas", 8)).pack()

    def _scripts_on_map_change(self, map_path: str):
        self._scripts_db   = get_script_db(map_path)
        self._scripts_seen = set()   # reset encounter state on map change
        # Rebuild section list for filter combo
        sections = set()
        for name in self._scripts_db.get("objects", {}):
            s = _script_section(name)
            if s:
                sections.add(s)
        sect_vals = ["all"] + sorted(sections)
        self._scripts_sect_combo.configure(values=sect_vals)
        self._scripts_filter_sect.set("all")
        self._scripts_refresh()
        self._scripts_refresh_list()
        self._eg_refresh()
        self._srcmap_refresh()
        self._flow_redraw()
        self._timer_refresh_picker()
        # Rebuild section filter for enemy groups tab
        sections = set()
        for name, info in self._scripts_db.get("objects", {}).items():
            if "ai_living_count" in info.get("funcs", []):
                s = _script_section(name)
                if s:
                    sections.add(s)
        self._eg_sect_combo.configure(values=["all"] + sorted(sections))
        self._eg_filter_sect.set("all")
        # Reset kill trigger initial counts and change log on map change
        self._kg_initial.clear()
        self._change_log.clear()
        self._changelog_redisplay()
        # Reset timer watch states on map change
        import time as _time
        for name, watch in self._timer_watches.items():
            watch["state"]      = "NOT YET"
            watch["state_time"] = _time.time()
            watch["placed_time"] = None
            watch["active_dur"]  = None
            watch["history"]     = []
        self._timer_states.clear()

    def _scripts_refresh(self):
        tree   = self._scripts_tree
        db     = self._scripts_db
        objs   = getattr(self, "_objects", [])
        fcat   = self._scripts_filter_cat.get()
        fsect  = self._scripts_filter_sect.get()
        fstate = self._scripts_filter_state.get()
        falive = False   # removed: state filter replaces this
        query  = self._scripts_search.get().lower().strip()

        # Build tag short-name → object lookup from live table
        live_lookup: dict[str, list] = {}
        for o in objs:
            if not o.get("active"):
                continue
            tag = o.get("definition_tag", "") or ""
            short = tag.split("]")[-1].strip().lower() if "]" in tag else tag.lower()
            if short:
                live_lookup.setdefault(short, []).append(o)

        # Build script-name → matching live objects (substring match)
        def find_live(name: str):
            nl = name.lower()
            result = []
            for lk, los in live_lookup.items():
                if nl in lk or lk in nl:
                    result.extend(los)
            return result

        # Update seen set: any name that currently has a live match is PLACED
        for name in db.get("objects", {}):
            if find_live(name):
                self._scripts_seen.add(name)

        wanted = {}
        for name, info in db.get("objects", {}).items():
            cat_key  = info["category"]
            cat_disp = CATEGORY_LABELS.get(cat_key, cat_key)
            section  = _script_section(name)

            if fcat  != "all" and cat_disp != fcat:
                continue
            if fsect != "all" and section  != fsect:
                continue
            if query and query not in name.lower():
                continue

            live_objs = find_live(name)
            is_live   = bool(live_objs)
            was_seen  = name in self._scripts_seen

            if is_live:
                state = "PLACED"
            elif was_seen:
                state = "DEAD"
            else:
                state = "NOT YET"

            if fstate != "all" and state != fstate:
                continue

            # Kill trigger counter: count live enemy-type objects
            ENEMY_TYPES = {"biped", "vehicle", "creature"}
            is_kill_enc = "ai_living_count" in info.get("funcs", [])
            live_enemies = [o for o in live_objs if o.get("type") in ENEMY_TYPES]
            if is_kill_enc and live_objs:
                living_str = f"{len(live_enemies)}/{len(live_objs)}"
            elif is_kill_enc:
                living_str = "0"
            else:
                living_str = ""

            # Row display values
            best = live_objs[0] if live_objs else None
            obj_type = best.get("type", "")    if best else ""
            hp       = best.get("health")      if best else None
            clus     = best.get("cluster")     if best else None
            hp_s     = f"{hp:.2f}" if hp is not None else "—"
            clus_s   = str(clus)   if clus is not None else "—"

            if state == "PLACED":
                row_tag = ("placed",)
            elif state == "DEAD":
                row_tag = ("dead",)
            else:
                row_tag = (cat_key,)

            if is_kill_enc and state == "PLACED":
                row_tag = ("kill_enc",)

            wanted[name] = {
                "vals": (name, section, cat_disp, state,
                         living_str, obj_type, hp_s, clus_s),
                "tag":  row_tag,
            }

        existing = set(tree.get_children(""))
        for iid in existing - wanted.keys():
            tree.delete(iid)
        for name, d in wanted.items():
            if tree.exists(name):
                tree.item(name, values=d["vals"], tags=d["tag"])
            else:
                tree.insert("", tk.END, iid=name, values=d["vals"], tags=d["tag"])

        n_placed = sum(1 for d in wanted.values()
                       if d["vals"][3] == "PLACED")
        n_dead   = sum(1 for d in wanted.values()
                       if d["vals"][3] == "DEAD")
        self._scripts_count_lbl.config(
            text=f"{len(wanted)} entries  "
                 f"{n_placed} placed  {n_dead} dead")

        # Also refresh orphans
        self._scripts_refresh_orphans()

    def _scripts_refresh_list(self):
        tree  = self._scripts_list_tree
        db    = self._scripts_db
        query = self._scripts_list_search.get().lower().strip()
        wanted = {}
        for sname, stype, src in db.get("scripts", []):
            if query and query not in sname.lower() and query not in src.lower():
                continue
            iid = f"{sname}|{src}"
            wanted[iid] = (sname, stype, src)
        existing = set(tree.get_children(""))
        for iid in existing - wanted.keys():
            tree.delete(iid)
        for iid, (sname, stype, src) in wanted.items():
            tag = (stype,) if stype in SCRIPT_TYPE_COLORS else ()
            if tree.exists(iid):
                tree.item(iid, values=(sname, stype, src), tags=tag)
            else:
                tree.insert("", tk.END, iid=iid, values=(sname, stype, src), tags=tag)

    def _scripts_refresh_orphans(self):
        """Populate the Orphaned Objects tab with live objects not in script DB."""
        tree = self._scripts_orp_tree
        db   = self._scripts_db
        objs = getattr(self, "_objects", [])

        # All script names for quick lookup
        script_names = set(n.lower() for n in db.get("objects", {}))

        orphans = []
        for o in objs:
            if not o.get("active"):
                continue
            tag = o.get("definition_tag", "") or ""
            short = tag.split("]")[-1].strip().lower() if "]" in tag else tag.lower()
            if not short:
                continue
            # Check if any script name substring-matches this tag
            matched = any(sn in short or short in sn for sn in script_names)
            if not matched:
                orphans.append(o)

        wanted = {}
        for o in orphans:
            idx  = o.get("index", 0)
            salt = o.get("salt",  0)
            iid  = f"{idx}:{salt}"
            typ  = o.get("type", "")
            tag  = o.get("definition_tag", "")
            hp   = o.get("health")
            clus = o.get("cluster")
            orig = o.get("origin") or (None, None, None)
            hp_s   = f"{hp:.2f}" if hp is not None else "—"
            clus_s = str(clus) if clus is not None else "—"
            orig_s = (f"({orig[0]:.1f},{orig[1]:.1f},{orig[2]:.1f})"
                      if orig[0] is not None else "—")
            wanted[iid] = (str(idx), f"{salt:04X}", typ, tag, hp_s, clus_s, orig_s)

        existing = set(tree.get_children(""))
        for iid in existing - wanted.keys():
            tree.delete(iid)
        for iid, vals in wanted.items():
            if tree.exists(iid):
                tree.item(iid, values=vals)
            else:
                tree.insert("", tk.END, iid=iid, values=vals)

        self._scripts_orp_count_lbl.config(
            text=f"{len(orphans)} orphaned objects")

    def _on_script_obj_select(self, _event=None):
        sel = self._scripts_tree.selection()
        if not sel:
            return
        name = sel[0]
        info = self._scripts_db.get("objects", {}).get(name)
        if info:
            self._scripts_show_detail(name, info)

    def _scripts_show_detail(self, name: str, info: dict):
        txt = self._scripts_detail_text
        txt.config(state=tk.NORMAL)
        txt.delete("1.0", tk.END)
        def row(label, value, tag="val"):
            txt.insert(tk.END, f"  {label:<22}", "key")
            txt.insert(tk.END, f"{value}\n", tag)
        row("Script name", name)
        row("Category",    CATEGORY_LABELS.get(info["category"], info["category"]))
        row("Sources",     ", ".join(info["sources"]))
        row("Functions",   ", ".join(info["funcs"]))
        objs = getattr(self, "_objects", [])
        matches = []
        nl = name.lower()
        for o in objs:
            tag = o.get("definition_tag", "") or ""
            short = tag.split("]")[-1].strip().lower() if "]" in tag else tag.lower()
            if short and (nl in short or short in nl):
                matches.append(o)
        txt.insert(tk.END, "\n")
        ENEMY_TYPES = {"biped", "vehicle", "creature"}
        if matches:
            enemies = [o for o in matches if o.get("type") in ENEMY_TYPES]
            txt.insert(tk.END, f"  Live matches ({len(matches)}):\n", "live")
            # Type breakdown for kill-trigger groups
            if "ai_living_count" in info.get("funcs", []):
                from collections import Counter
                type_counts = Counter(o.get("type", "?") for o in matches)
                enemy_counts = Counter(o.get("type", "?") for o in enemies)
                txt.insert(tk.END, f"  Enemy count:          ", "key")
                txt.insert(tk.END, f"{len(enemies)} enemies  ({len(matches)} total)\n", "live")
                txt.insert(tk.END, f"  By type:              ", "key")
                breakdown = "  ".join(f"{t}={n}" for t, n in sorted(type_counts.items()))
                txt.insert(tk.END, f"{breakdown}\n", "val")
                # Average HP of enemies
                hps = [o.get("health") for o in enemies if o.get("health") is not None]
                if hps:
                    avg_hp = sum(hps) / len(hps)
                    min_hp = min(hps)
                    txt.insert(tk.END, f"  Avg HP / Min HP:      ", "key")
                    txt.insert(tk.END, f"{avg_hp:.2f} / {min_hp:.2f}\n", "val")
                txt.insert(tk.END, "\n")
            for o in matches[:6]:
                idx  = o.get("index", "?")
                salt = o.get("salt", 0)
                hp   = o.get("health")
                orig = o.get("origin") or (None,None,None)
                hp_s = f"{hp:.2f}" if hp is not None else "—"
                orig_s = (f"({orig[0]:.2f},{orig[1]:.2f},{orig[2]:.2f})"
                          if orig[0] is not None else "—")
                is_enemy = o.get("type") in ENEMY_TYPES
                tag = "live" if is_enemy else "warn"
                row(f"  [{idx:04d}:{salt:04X}]",
                    f"{o.get('type','?')}  hp={hp_s}  {orig_s}", tag)
            if len(matches) > 6:
                txt.insert(tk.END, f"  ... and {len(matches)-6} more\n", "dead")
        else:
            txt.insert(tk.END, "  Not found in object table\n", "dead")
        txt.config(state=tk.DISABLED)

    def _scripts_sort(self, col):
        data = [(self._scripts_tree.set(iid, col), iid)
                for iid in self._scripts_tree.get_children("")]
        data.sort()
        for i, (_, iid) in enumerate(data):
            self._scripts_tree.move(iid, "", i)

    # ── Enemy Groups helpers ──────────────────────────────────────────────

    def _eg_refresh(self):
        """Refresh the Enemy Groups tab."""
        from collections import Counter
        ENEMY_TYPES = {"biped", "vehicle", "creature"}
        tree  = self._eg_tree
        db    = self._scripts_db
        objs  = getattr(self, "_objects", [])
        fsect = self._eg_filter_sect.get()
        query = self._eg_search.get().lower().strip()

        # Build live object lookup by tag short name
        live_lookup: dict = {}
        for o in objs:
            if not o.get("active"):
                continue
            tag   = o.get("definition_tag", "") or ""
            short = tag.split("]")[-1].strip().lower() if "]" in tag else tag.lower()
            if short:
                live_lookup.setdefault(short, []).append(o)

        def find_live(name: str):
            nl = name.lower()
            result = []
            for lk, los in live_lookup.items():
                if nl in lk or lk in nl:
                    result.extend(los)
            return result

        wanted = {}
        for name, info in db.get("objects", {}).items():
            if "ai_living_count" not in info.get("funcs", []):
                continue
            section = _script_section(name)
            if fsect != "all" and section != fsect:
                continue
            if query and query not in name.lower():
                continue

            live_objs  = find_live(name)
            enemies    = [o for o in live_objs if o.get("type") in ENEMY_TYPES]
            non_combat = [o for o in live_objs if o.get("type") not in ENEMY_TYPES]

            # State
            is_live  = bool(live_objs)
            was_seen = name in self._scripts_seen
            if is_live:
                state = "PLACED"
            elif was_seen:
                state = "DEAD"
            else:
                state = "NOT YET"

            # Type breakdown string
            if live_objs:
                type_counts = Counter(o.get("type", "?") for o in live_objs)
                types_str = "  ".join(f"{t}×{n}" for t, n in sorted(type_counts.items()))
            else:
                types_str = "—"

            # HP stats
            hps = [o.get("health") for o in enemies if o.get("health") is not None]
            avg_hp_s = f"{sum(hps)/len(hps):.2f}" if hps else "—"
            min_hp_s = f"{min(hps):.2f}"           if hps else "—"

            n_enemies = len(enemies)
            n_total   = len(live_objs)

            # Tag
            if state == "DEAD":
                tag = ("dead",)
            elif state == "NOT YET":
                tag = ("notyet",)
            elif n_enemies == 0 and n_total > 0:
                tag = ("placed",)   # placed but no combatants (vehicles/equipment only)
            elif hps and min(hps) < 0.25:
                tag = ("critical",) # someone is critically low
            elif n_enemies > 0:
                tag = ("active",)   # enemies alive
            else:
                tag = ("notyet",)

            wanted[name] = {
                "vals": (name, section,
                         str(n_enemies) if is_live else "—",
                         str(n_total)   if is_live else "—",
                         types_str,
                         avg_hp_s, min_hp_s, state),
                "tag": tag,
            }

        existing = set(tree.get_children(""))
        for iid in existing - wanted.keys():
            tree.delete(iid)
        for name, d in wanted.items():
            if tree.exists(name):
                tree.item(name, values=d["vals"], tags=d["tag"])
            else:
                tree.insert("", tk.END, iid=name, values=d["vals"], tags=d["tag"])

        n_active = sum(1 for d in wanted.values() if d["tag"][0] in ("active","critical"))
        n_dead   = sum(1 for d in wanted.values() if d["tag"][0] == "dead")
        self._eg_count_lbl.config(
            text=f"{len(wanted)} groups  {n_active} active  {n_dead} cleared")

    def _eg_sort(self, col):
        data = [(self._eg_tree.set(iid, col), iid)
                for iid in self._eg_tree.get_children("")]
        try:
            data.sort(key=lambda x: float(x[0].replace("—", "-1").replace("×","")) if x[0] else -1)
        except ValueError:
            data.sort()
        for i, (_, iid) in enumerate(data):
            self._eg_tree.move(iid, "", i)

        # ── Timer Watch helpers ───────────────────────────────────────────────

    def _timer_refresh_picker(self):
        """Populate the dormant-script picker from the current map DB."""
        tree  = self._timer_picker_tree
        db    = self._scripts_db
        query = self._timer_pick_search.get().lower().strip()
        wanted = {}
        for sname, stype, src in db.get("scripts", []):
            if stype not in ("dormant", "continuous"):
                continue
            if query and query not in sname.lower() and query not in src.lower():
                continue
            iid = f"{sname}|{src}"
            wanted[iid] = (sname, src, stype)
        existing = set(tree.get_children(""))
        for iid in existing - wanted.keys():
            tree.delete(iid)
        for iid, (sname, src, stype) in wanted.items():
            tag = (stype,)
            if tree.exists(iid):
                tree.item(iid, values=(sname, src), tags=tag)
            else:
                tree.insert("", tk.END, iid=iid, values=(sname, src), tags=tag)

    def _timer_picker_dblclick(self, _event=None):
        sel = self._timer_picker_tree.selection()
        if not sel:
            return
        iid = sel[0]
        vals = self._timer_picker_tree.item(iid, "values")
        if vals:
            self._timer_add_watch(vals[0])

    def _timer_add_watch(self, name: str = None):
        import time as _time
        if name is None:
            name = self._timer_add_var.get().strip()
        if not name:
            return
        if name not in self._timer_watches:
            self._timer_watches[name] = {
                "state": "NOT YET",
                "state_time": _time.time(),
                "placed_time": None,
                "active_dur": None,
                "history": [],
            }
            self._timer_states[name] = "NOT YET"
        self._timer_add_var.set("")
        self._timer_update_watches()

    def _timer_remove_selected(self, _event=None):
        sel = self._timer_tree.selection()
        for iid in sel:
            self._timer_watches.pop(iid, None)
            self._timer_states.pop(iid, None)
            if self._timer_tree.exists(iid):
                self._timer_tree.delete(iid)

    def _timer_clear_all(self):
        self._timer_watches.clear()
        self._timer_states.clear()
        for iid in self._timer_tree.get_children(""):
            self._timer_tree.delete(iid)

    def _timer_compute_state(self, name: str) -> str:
        """Return PLACED / DEAD / NOT YET for a watched script name."""
        objs = getattr(self, "_objects", [])
        nl   = name.lower()
        live_lookup = {}
        for o in objs:
            if not o.get("active"):
                continue
            tag   = o.get("definition_tag", "") or ""
            short = tag.split("]")[-1].strip().lower() if "]" in tag else tag.lower()
            if short:
                live_lookup.setdefault(short, []).append(o)
        is_live = any(nl in lk or lk in nl for lk in live_lookup)
        if is_live:
            return "PLACED"
        if name in self._scripts_seen:
            return "DEAD"
        return "NOT YET"

    def _timer_update_watches(self):
        import time as _time
        now  = _time.time()
        tree = self._timer_tree

        def fmt_dur(secs):
            if secs is None:
                return "—"
            if secs < 60:
                return f"{secs:.1f}s"
            m, s = divmod(int(secs), 60)
            return f"{m}m{s:02d}s"

        for name, watch in self._timer_watches.items():
            new_state = self._timer_compute_state(name)
            prev      = watch["state"]

            if new_state != prev:
                # State transition — record history
                elapsed_in_prev = now - watch["state_time"]
                watch["history"].append(
                    f"{prev}({fmt_dur(elapsed_in_prev)})")
                if len(watch["history"]) > 6:
                    watch["history"] = watch["history"][-6:]

                if new_state == "PLACED":
                    watch["placed_time"] = now
                elif prev == "PLACED" and new_state == "DEAD":
                    if watch["placed_time"] is not None:
                        watch["active_dur"] = now - watch["placed_time"]

                watch["state"]      = new_state
                watch["state_time"] = now
                self._scripts_seen.add(name)

            elapsed = now - watch["state_time"]
            state   = watch["state"]
            history_str = " → ".join(watch["history"][-4:])

            tag = {"PLACED": "placed", "DEAD": "dead"}.get(state, "notyet")

            vals = (
                name,
                state,
                fmt_dur(elapsed),
                fmt_dur(watch["active_dur"]),
                history_str,
            )

            if tree.exists(name):
                tree.item(name, values=vals, tags=(tag,))
            else:
                tree.insert("", tk.END, iid=name, values=vals, tags=(tag,))


    # ══════════════════════════════════════════════════════════════════════
    # ENCOUNTER FLOW DIAGRAM
    # ══════════════════════════════════════════════════════════════════════

    def _flow_compute_states(self):
        """Return dict of section -> (state, enemy_count) from current objects."""
        import re as _re
        ENEMY_TYPES = {"biped", "vehicle", "creature"}
        db   = self._scripts_db
        objs = getattr(self, "_objects", [])

        # Build live lookup
        live_lookup = {}
        for o in objs:
            if not o.get("active"):
                continue
            tag   = o.get("definition_tag", "") or ""
            short = tag.split("]")[-1].strip().lower() if "]" in tag else tag.lower()
            if short:
                live_lookup.setdefault(short, []).append(o)

        def find_live(name):
            nl = name.lower()
            result = []
            for lk, los in live_lookup.items():
                if nl in lk or lk in nl:
                    result.extend(los)
            return result

        # Aggregate per section
        section_states = {}   # section -> {"placed": bool, "dead": bool, "enemies": int}
        for name, info in db.get("objects", {}).items():
            m = _re.match(r'^([a-zA-Z]+[0-9]+)', name)
            if not m:
                continue
            sec = m.group(1)
            live = find_live(name)
            enemies = sum(1 for o in live if o.get("type") in ENEMY_TYPES)
            was_seen = name in self._scripts_seen

            st = section_states.setdefault(sec, {"placed": False, "dead": False, "enemies": 0})
            if live:
                st["placed"] = True
                st["enemies"] += enemies
            elif was_seen:
                st["dead"] = True

        return section_states

    def _flow_redraw(self):
        c = self._flow_canvas
        if c is None:
            return
        c.delete("all")

        import re as _re
        section_states = self._flow_compute_states()
        if not section_states:
            c.create_text(20, 20, anchor="nw", fill="#3a3a5a",
                          font=("Consolas", 10), text="No map loaded or no script sections found.")
            return

        # Sort sections naturally (e1, e2, ... e10, e11, etc.)
        def sec_key(s):
            m = _re.match(r'^([a-zA-Z]+)([0-9]+)', s)
            return (m.group(1), int(m.group(2))) if m else (s, 0)

        sections = sorted(section_states.keys(), key=sec_key)

        # Layout: wrap into rows of ~8 nodes
        NODE_W, NODE_H = 90, 44
        PAD_X, PAD_Y   = 18, 18
        COLS = 8
        rows = [sections[i:i+COLS] for i in range(0, len(sections), COLS)]

        total_w = COLS * (NODE_W + PAD_X) + PAD_X
        total_h = len(rows) * (NODE_H + PAD_Y * 2) + PAD_Y * 2
        c.configure(scrollregion=(0, 0, max(total_w, 600), max(total_h, 300)))

        node_centers = {}
        for row_i, row in enumerate(rows):
            for col_i, sec in enumerate(row):
                x = PAD_X + col_i * (NODE_W + PAD_X) + NODE_W // 2
                y = PAD_Y * 2 + row_i * (NODE_H + PAD_Y * 2) + NODE_H // 2
                node_centers[sec] = (x, y)

        # Draw edges first (so nodes paint over them)
        for i, sec in enumerate(sections[:-1]):
            next_sec = sections[i + 1]
            if sec in node_centers and next_sec in node_centers:
                x1, y1 = node_centers[sec]
                x2, y2 = node_centers[next_sec]
                # Only draw edge if same row
                if abs(y1 - y2) < 5:
                    c.create_line(x1 + NODE_W // 2, y1,
                                  x2 - NODE_W // 2, y2,
                                  fill="#2a2a40", width=1, arrow=tk.LAST,
                                  arrowshape=(8, 10, 4))

        # Draw nodes
        for sec, (x, y) in node_centers.items():
            st = section_states.get(sec, {})
            is_placed = st.get("placed", False)
            is_dead   = st.get("dead",   False)
            n_enemies = st.get("enemies", 0)

            if is_placed and n_enemies > 0:
                fill, outline, fg = "#2a1a00", "#f0b040", "#f0b040"   # active - amber
                label2 = f"{n_enemies} ▲"
            elif is_placed:
                fill, outline, fg = "#0e2218", "#3dcc96", "#3dcc96"   # placed, no enemies
                label2 = "✓"
            elif is_dead:
                fill, outline, fg = "#141420", "#3a3a5a", "#555577"   # cleared
                label2 = "✓"
            else:
                fill, outline, fg = "#0d0d12", "#2a2a48", "#9898b8"   # not yet
                label2 = "?"

            x0, y0 = x - NODE_W // 2, y - NODE_H // 2
            x1, y1 = x + NODE_W // 2, y + NODE_H // 2
            c.create_rectangle(x0, y0, x1, y1, fill=fill, outline=outline, width=1)
            c.create_text(x, y - 8, fill=fg, font=("Consolas", 9, "bold"), text=sec)
            c.create_text(x, y + 9, fill=fg, font=("Consolas", 8), text=label2)
            # tag for click
            c.addtag_overlapping(f"node_{sec}", x0, y0, x1, y1)

    def _flow_on_click(self, event):
        c = self._flow_canvas
        if c is None:
            return
        cx, cy = c.canvasx(event.x), c.canvasy(event.y)
        tags = c.gettags(c.find_closest(cx, cy))
        for t in tags:
            if t.startswith("node_"):
                sec = t[5:]
                # Switch Named Objects tab to filter by this section
                self._scripts_filter_sect.set(sec)
                self._scripts_refresh()
                try:
                    self._scripts_nb.select(0)   # jump to Named Objects tab
                except Exception:
                    pass
                break

    # ══════════════════════════════════════════════════════════════════════
    # KILL TRIGGER PROGRESS BARS
    # ══════════════════════════════════════════════════════════════════════

    def _eg_draw_bars(self):
        """Draw kill-trigger progress bars for the selected (or all active) groups."""
        from collections import Counter
        ENEMY_TYPES = {"biped", "vehicle", "creature"}
        c = self._eg_bar_canvas
        if c is None:
            return
        c.delete("all")

        db   = self._scripts_db
        objs = getattr(self, "_objects", [])

        # Live lookup
        live_lookup = {}
        for o in objs:
            if not o.get("active"):
                continue
            tag   = o.get("definition_tag", "") or ""
            short = tag.split("]")[-1].strip().lower() if "]" in tag else tag.lower()
            if short:
                live_lookup.setdefault(short, []).append(o)

        def find_live(name):
            nl = name.lower()
            result = []
            for lk, los in live_lookup.items():
                if nl in lk or lk in nl:
                    result.extend(los)
            return result

        # Determine which groups to show:
        # prefer selected rows, else all active ai_living_count groups
        sel = self._eg_tree.selection()
        if sel:
            groups = [n for n in sel
                      if "ai_living_count" in db.get("objects", {}).get(n, {}).get("funcs", [])]
        else:
            groups = [n for n, info in db.get("objects", {}).items()
                      if "ai_living_count" in info.get("funcs", [])
                      and bool(find_live(n))]
            groups = groups[:12]   # cap at 12 bars

        if not groups:
            c.create_text(10, 10, anchor="nw", fill="#3a3a5a",
                          font=("Consolas", 9),
                          text="No active kill-trigger groups. Select rows above or wait for enemies to spawn.")
            c.configure(height=30)
            return

        BAR_H    = 16
        BAR_PAD  = 6
        LABEL_W  = 160
        BAR_X    = LABEL_W + 8
        needed_h = len(groups) * (BAR_H + BAR_PAD) + BAR_PAD + 4
        c.configure(height=max(60, min(needed_h, 160)))
        c_width  = c.winfo_width() or 500
        BAR_W    = max(80, c_width - BAR_X - 60)

        for i, name in enumerate(groups):
            live  = find_live(name)
            n_now = sum(1 for o in live if o.get("type") in ENEMY_TYPES)

            # Track initial: once we see enemies, record the max
            if n_now > 0:
                prev = self._kg_initial.get(name, 0)
                if n_now > prev:
                    self._kg_initial[name] = n_now
            n_init = self._kg_initial.get(name, n_now) or 1

            frac = n_now / n_init if n_init else 0.0
            y    = BAR_PAD + i * (BAR_H + BAR_PAD)

            # Label (truncated)
            lbl = name if len(name) <= 22 else name[:20] + "…"
            c.create_text(4, y + BAR_H // 2, anchor="w", fill="#9898b8",
                          font=("Consolas", 8), text=lbl)

            # Background track
            c.create_rectangle(BAR_X, y, BAR_X + BAR_W, y + BAR_H,
                               fill="#1a1a28", outline="#2a2a40")

            # Filled portion
            fill_w = int(BAR_W * frac)
            if fill_w > 0:
                # Colour: green→amber→red based on fraction remaining
                if frac > 0.6:
                    bar_col = "#cc3333"   # lots remaining - danger red
                elif frac > 0.25:
                    bar_col = "#f0b040"   # getting low - amber
                else:
                    bar_col = "#3dcc96"   # almost clear - green
                c.create_rectangle(BAR_X, y, BAR_X + fill_w, y + BAR_H,
                                   fill=bar_col, outline="")

            # Count label
            pct = int(frac * 100)
            count_txt = f"{n_now}/{n_init}  {pct}%"
            c.create_text(BAR_X + BAR_W + 6, y + BAR_H // 2, anchor="w",
                          fill="#c8c8e0", font=("Consolas", 8), text=count_txt)

    # ══════════════════════════════════════════════════════════════════════
    # SOURCE MAP (Script dependency / grouping by source file)
    # ══════════════════════════════════════════════════════════════════════

    def _srcmap_refresh(self):
        tree  = self._sm_tree
        db    = self._scripts_db
        query = getattr(self, "_sm_search", None)
        q     = query.get().lower().strip() if query else ""

        # Group dormant/continuous scripts by source file
        from collections import defaultdict
        by_src = defaultdict(list)
        for sname, stype, src in db.get("scripts", []):
            if stype not in ("dormant", "continuous", "startup"):
                continue
            if q and q not in sname.lower() and q not in src.lower():
                continue
            by_src[src].append((sname, stype))

        # Compute state for each script name via seen set
        def script_state(sname):
            nl = sname.lower()
            objs = getattr(self, "_objects", [])
            live_lookup = {}
            for o in objs:
                if not o.get("active"):
                    continue
                tag   = o.get("definition_tag", "") or ""
                short = tag.split("]")[-1].strip().lower() if "]" in tag else tag.lower()
                if short:
                    live_lookup.setdefault(short, []).append(o)
            is_live = any(nl in lk or lk in nl for lk in live_lookup)
            if is_live:
                return "PLACED"
            if sname in self._scripts_seen:
                return "DEAD"
            return "—"

        # Clear and repopulate
        for iid in tree.get_children(""):
            tree.delete(iid)

        for src in sorted(by_src.keys()):
            scripts = by_src[src]
            n_placed = sum(1 for sname, _ in scripts if script_state(sname) == "PLACED")
            src_lbl  = f"{src}  ({len(scripts)} scripts"
            if n_placed:
                src_lbl += f", {n_placed} active"
            src_lbl += ")"
            parent = tree.insert("", tk.END, values=(src_lbl, "", ""),
                                 tags=("src_header",), open=True)
            for sname, stype in sorted(scripts):
                state = script_state(sname)
                if state == "PLACED":
                    row_tag = ("placed",)
                elif state == "DEAD":
                    row_tag = ("dead",)
                else:
                    row_tag = (f"t_{stype}",)
                tree.insert(parent, tk.END, values=(sname, stype, state),
                            tags=row_tag)

    # ══════════════════════════════════════════════════════════════════════
    # MEMORY DIFF / CHANGE LOG
    # ══════════════════════════════════════════════════════════════════════

    def _changelog_ingest(self):
        """Pull new events from app-level logs and HP diffs into _change_log."""
        import time as _time
        objs      = getattr(self, "_objects", [])
        prev_objs = getattr(self, "_prev_objects", {})
        spawn_log = getattr(self, "_spawn_log", [])
        thresh    = self._cl_hp_thresh.get()
        now       = _time.time()

        # Track which spawn_log entries we've already consumed using a watermark
        watermark = getattr(self, "_cl_spawn_watermark", 0)
        new_entries = []

        for entry in spawn_log[watermark:]:
            ts, kind, idx, label = entry
            new_entries.append({"kind": kind, "idx": idx, "label": label, "ts": ts})
        self._cl_spawn_watermark = len(spawn_log)

        # HP changes for currently active objects
        for o in objs:
            if not o.get("active"):
                continue
            idx  = o["index"]
            prev = prev_objs.get(idx)
            if not prev:
                continue
            hp_now  = o.get("health")
            hp_prev = prev.get("health")
            if hp_now is not None and hp_prev is not None:
                delta = hp_now - hp_prev
                if abs(delta) >= thresh:
                    tag   = o.get("definition_tag", "") or ""
                    short = tag.split("]")[-1].strip() if "]" in tag else tag
                    label = f"{o.get('type','?')}:{short}" if short else o.get("type", "?")
                    new_entries.append({
                        "kind": "hp", "idx": idx, "label": label,
                        "delta": delta, "hp": hp_now, "ts": now,
                    })
            # Teleport
            if o.get("teleported"):
                mag  = o.get("pos_delta_mag", 0) or 0
                tag  = o.get("definition_tag", "") or ""
                short = tag.split("]")[-1].strip() if "]" in tag else tag
                label = f"{o.get('type','?')}:{short}" if short else o.get("type", "?")
                new_entries.append({
                    "kind": "tele", "idx": idx, "label": label,
                    "mag": mag, "ts": now,
                })

        if new_entries:
            self._change_log.extend(new_entries)
            if len(self._change_log) > self._change_log_max:
                self._change_log = self._change_log[-self._change_log_max:]
            self._changelog_redisplay()

    def _changelog_redisplay(self):
        """Repaint the change log text widget from _change_log."""
        import time as _time
        txt = self._cl_text
        txt.config(state=tk.NORMAL)
        txt.delete("1.0", tk.END)

        show_spawn = self._cl_show_spawn.get()
        show_death = self._cl_show_death.get()
        show_hp    = self._cl_show_hp.get()
        show_tele  = self._cl_show_tele.get()

        now = _time.time()
        entries = list(reversed(self._change_log))   # newest first

        for e in entries:
            kind = e["kind"]
            if kind == "spawn"  and not show_spawn: continue
            if kind == "death"  and not show_death: continue
            if kind == "hp"     and not show_hp:    continue
            if kind == "tele"   and not show_tele:  continue

            age  = now - e.get("ts", now)
            age_s = f"{age:5.1f}s ago" if age < 3600 else f"{age/60:.1f}m ago"
            idx  = e.get("idx", "?")
            lbl  = e.get("label", "?")

            if kind == "spawn":
                txt.insert(tk.END, f" [{idx:04}] ", "label")
                txt.insert(tk.END, "SPAWN  ", "spawn")
                txt.insert(tk.END, f"{lbl:<38}", "spawn")
                txt.insert(tk.END, f"  {age_s}\n", "time")
            elif kind == "death":
                txt.insert(tk.END, f" [{idx:04}] ", "label")
                txt.insert(tk.END, "DEATH  ", "death")
                txt.insert(tk.END, f"{lbl:<38}", "death")
                txt.insert(tk.END, f"  {age_s}\n", "time")
            elif kind == "hp":
                delta = e.get("delta", 0)
                hp    = e.get("hp", 0)
                sign  = "+" if delta > 0 else ""
                txt.insert(tk.END, f" [{idx:04}] ", "label")
                txt.insert(tk.END, "HP Δ   ", "hp")
                txt.insert(tk.END, f"{lbl:<28}", "hp")
                txt.insert(tk.END, f"  {sign}{delta:+.3f}  hp={hp:.3f}", "hp")
                txt.insert(tk.END, f"  {age_s}\n", "time")
            elif kind == "tele":
                mag = e.get("mag", 0)
                txt.insert(tk.END, f" [{idx:04}] ", "label")
                txt.insert(tk.END, "TELE   ", "tele")
                txt.insert(tk.END, f"{lbl:<28}", "tele")
                txt.insert(tk.END, f"  dist={mag:.2f}wu", "tele")
                txt.insert(tk.END, f"  {age_s}\n", "time")

        if not self._change_log:
            txt.insert(tk.END, "  Waiting for changes…\n", "neutral")
        txt.config(state=tk.DISABLED)

    def _changelog_clear(self):
        self._change_log.clear()
        self._cl_spawn_watermark = len(getattr(self, "_spawn_log", []))
        self._changelog_redisplay()

    def _scripts_tick(self):
        try:
            tab = self._main_nb.index(self._main_nb.select())
            if tab == 4:
                self._changelog_ingest()
                self._scripts_refresh()
                self._eg_refresh()
                self._eg_draw_bars()
                self._flow_redraw()
                self._timer_update_watches()
        except Exception:
            pass


