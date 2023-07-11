import numpy as np
NEW_WOFS_FEATURE_NAMES = ['ws_80__time_max__amp_ens_mean_spatial_perc_90',
 'mid_level_lapse_rate__ens_mean__spatial_mean',
 'wz_0to2_instant__time_max__amp_ens_mean_spatial_perc_90',
 'div_10m__time_min__ens_std__spatial_mean',
 'srh_0to3__ens_mean__spatial_mean',
 'w_down__time_min__ens_mean__spatial_mean',
 'w_up__time_max__ens_std__spatial_mean',
 'low_level_lapse_rate__ens_mean__spatial_mean',
 'ws_80__time_max__ens_mean__spatial_mean',
 'uh_2to5_instant__time_max__ens_std__spatial_mean',
 'comp_dz__time_max__amp_ens_mean_spatial_perc_90',
 'buoyancy__time_min__amp_ens_mean_spatial_perc_10',
 'hailcast__time_max__ens_std__spatial_mean',
 'dbz_1to3__time_max__amp_ens_mean_spatial_perc_90',
 'u_10__ens_std__spatial_mean',
 'u_10__ens_mean__spatial_mean',
 'dbz_1to3__time_max__ens_std__spatial_mean',
 'shear_u_0to1__ens_mean__spatial_mean',
 'cin_sfc__ens_mean__spatial_mean',
 '10-500m_bulkshear__time_max__amp_ens_mean_spatial_perc_90',
 'w_down__time_min__ens_min__spatial_mean',
 'wz_0to2_instant__time_max__ens_mean__spatial_mean',
 'low_level_lapse_rate__ens_std__spatial_mean',
 'w_up__time_max__amp_ens_mean_spatial_perc_90',
 'ctt__time_min__amp_ens_mean_spatial_perc_10',
 'v_10__ens_std__spatial_mean',
 'div_10m__time_min__ens_min__spatial_mean',
 'uh_0to2_instant__time_max__ens_std__spatial_mean',
 'wz_0to2_instant__time_max__ens_std__spatial_mean',
 'uh_2to5_instant__time_max__amp_ens_std_spatial_perc_90',
 'buoyancy__time_min__ens_mean__spatial_mean',
 'dbz_3to5__time_max__ens_mean__spatial_mean',
 'shear_u_0to6__ens_std__spatial_mean',
 'srh_0to1__ens_mean__spatial_mean',
 'w_down__time_min__ens_std__spatial_mean',
 'srh_0to1__ens_std__spatial_mean',
 'uh_0to2_instant__time_max__amp_ens_mean_spatial_perc_90',
 'lcl_sfc__ens_std__spatial_mean',
 'shear_u_0to6__ens_mean__spatial_mean',
 'dbz_3to5__time_max__ens_std__spatial_mean',
 'ctt__time_min__amp_ens_std_spatial_perc_10',
 'comp_dz__time_max__ens_std__spatial_mean',
 'shear_v_0to1__ens_std__spatial_mean',
 'Initialization Time',
 'w_1km__time_max__amp_ens_mean_spatial_perc_90',
 'comp_dz__time_max__amp_ens_std_spatial_perc_90',
 'w_down__time_min__amp_ens_std_spatial_perc_10',
 'shear_v_0to6__ens_mean__spatial_mean',
 'wz_0to2_instant__time_max__amp_ens_std_spatial_perc_90',
 '10-500m_bulkshear__time_max__amp_ens_std_spatial_perc_90',
 'ws_80__time_max__amp_ens_std_spatial_perc_90',
 'buoyancy__time_min__amp_ens_std_spatial_perc_10',
 '10-500m_bulkshear__time_max__ens_std__spatial_mean',
 'w_1km__time_max__ens_std__spatial_mean',
 'mid_level_lapse_rate__ens_std__spatial_mean',
 'comp_dz__time_max__ens_mean__spatial_mean',
 '10-500m_bulkshear__time_max__ens_mean__spatial_mean',
 'buoyancy__time_min__ens_std__spatial_mean',
 'dbz_3to5__time_max__amp_ens_std_spatial_perc_90',
 'cape_sfc__ens_std__spatial_mean',
 'dbz_1to3__time_max__amp_ens_std_spatial_perc_90',
 'dbz_3to5__time_max__amp_ens_mean_spatial_perc_90',
 'uh_2to5_instant__time_max__amp_ens_mean_spatial_perc_90',
 'div_10m__time_min__amp_ens_mean_spatial_perc_10',
 'w_up__time_max__amp_ens_std_spatial_perc_90',
 'w_1km__time_max__amp_ens_std_spatial_perc_90',
 'v_10__ens_mean__spatial_mean',
 'srh_0to3__ens_std__spatial_mean',
 'ws_80__time_max__ens_std__spatial_mean',
 'dbz_1to3__time_max__ens_mean__spatial_mean',
 'uh_0to2_instant__time_max__ens_mean__spatial_mean',
 'div_10m__time_min__ens_mean__spatial_mean',
 'ctt__time_min__ens_mean__spatial_mean',
 'hailcast__time_max__amp_ens_std_spatial_perc_90',
 'div_10m__time_min__amp_ens_std_spatial_perc_10',
 'cape_sfc__ens_mean__spatial_mean',
 'w_1km__time_max__ens_mean__spatial_mean',
 'ctt__time_min__ens_min__spatial_mean',
 'shear_u_0to1__ens_std__spatial_mean',
 'shear_v_0to6__ens_std__spatial_mean',
 'lcl_sfc__ens_mean__spatial_mean',
 'buoyancy__time_min__ens_min__spatial_mean',
 'uh_0to2_instant__time_max__amp_ens_std_spatial_perc_90',
 'hailcast__time_max__amp_ens_mean_spatial_perc_90',
 'w_down__time_min__amp_ens_mean_spatial_perc_10',
 'ctt__time_min__ens_std__spatial_mean',
 'cin_sfc__ens_std__spatial_mean',
 'w_up__time_max__ens_mean__spatial_mean',
 'shear_v_0to1__ens_mean__spatial_mean',
 'uh_2to5_instant__time_max__ens_mean__spatial_mean',
 'hailcast__time_max__ens_mean__spatial_mean']


WOFS_FEATURE_NAMES = ['srh_0to1_ens_mean_spatial_mean',
 'srh_0to3_ens_mean_spatial_mean',
 'cape_ml_ens_mean_spatial_mean',
 'cin_ml_ens_mean_spatial_mean',
 'shear_u_0to6_ens_mean_spatial_mean',
 'shear_v_0to6_ens_mean_spatial_mean',
 'shear_u_0to1_ens_mean_spatial_mean',
 'shear_v_0to1_ens_mean_spatial_mean',
 'lcl_ml_ens_mean_spatial_mean',
 'th_e_ml_ens_mean_spatial_mean',
 'u_10_ens_mean_spatial_mean',
 'v_10_ens_mean_spatial_mean',
 'mid_level_lapse_rate_ens_mean_spatial_mean',
 'low_level_lapse_rate_ens_mean_spatial_mean',
 'temperature_850mb_ens_mean_spatial_mean',
 'temperature_700mb_ens_mean_spatial_mean',
 'temperature_500mb_ens_mean_spatial_mean',
 'geopotential_height_850mb_ens_mean_spatial_mean',
 'geopotential_height_700mb_ens_mean_spatial_mean',
 'geopotential_height_500mb_ens_mean_spatial_mean',
 'dewpoint_850mb_ens_mean_spatial_mean',
 'dewpoint_700mb_ens_mean_spatial_mean',
 'dewpoint_500mb_ens_mean_spatial_mean',
 'uh_0to2_time_max_ens_mean_spatial_mean',
 'uh_2to5_time_max_ens_mean_spatial_mean',
 'wz_0to2_time_max_ens_mean_spatial_mean',
 'comp_dz_time_max_ens_mean_spatial_mean',
 'ws_80_time_max_ens_mean_spatial_mean',
 'w_up_time_max_ens_mean_spatial_mean',
 'hailcast_time_max_ens_mean_spatial_mean',
 'w_1km_time_max_ens_mean_spatial_mean',
 '10-m_bulk_shear_time_max_ens_mean_spatial_mean',
 'dbz_1to3km_max_time_max_ens_mean_spatial_mean',
 'dbz_3to5km_max_time_max_ens_mean_spatial_mean',
 'cloud_top_temp_time_min_ens_mean_spatial_mean',
 'bouyancy_time_min_ens_mean_spatial_mean',
 'divergence_10m_time_min_ens_mean_spatial_mean',
 'w_down_time_min_ens_mean_spatial_mean',
 'srh_0to1_ens_std_spatial_mean',
 'srh_0to3_ens_std_spatial_mean',
 'cape_ml_ens_std_spatial_mean',
 'cin_ml_ens_std_spatial_mean',
 'shear_u_0to6_ens_std_spatial_mean',
 'shear_v_0to6_ens_std_spatial_mean',
 'shear_u_0to1_ens_std_spatial_mean',
 'shear_v_0to1_ens_std_spatial_mean',
 'lcl_ml_ens_std_spatial_mean',
 'th_e_ml_ens_std_spatial_mean',
 'u_10_ens_std_spatial_mean',
 'v_10_ens_std_spatial_mean',
 'mid_level_lapse_rate_ens_std_spatial_mean',
 'low_level_lapse_rate_ens_std_spatial_mean',
 'temperature_850mb_ens_std_spatial_mean',
 'temperature_700mb_ens_std_spatial_mean',
 'temperature_500mb_ens_std_spatial_mean',
 'geopotential_height_850mb_ens_std_spatial_mean',
 'geopotential_height_700mb_ens_std_spatial_mean',
 'geopotential_height_500mb_ens_std_spatial_mean',
 'dewpoint_850mb_ens_std_spatial_mean',
 'dewpoint_700mb_ens_std_spatial_mean',
 'dewpoint_500mb_ens_std_spatial_mean',
 'uh_0to2_time_max_ens_std_spatial_mean',
 'uh_2to5_time_max_ens_std_spatial_mean',
 'wz_0to2_time_max_ens_std_spatial_mean',
 'comp_dz_time_max_ens_std_spatial_mean',
 'ws_80_time_max_ens_std_spatial_mean',
 'w_up_time_max_ens_std_spatial_mean',
 'hailcast_time_max_ens_std_spatial_mean',
 'w_1km_time_max_ens_std_spatial_mean',
 '10-m_bulk_shear_time_max_ens_std_spatial_mean',
 'dbz_1to3km_max_time_max_ens_std_spatial_mean',
 'dbz_3to5km_max_time_max_ens_std_spatial_mean',
 'cloud_top_temp_time_min_ens_std_spatial_mean',
 'bouyancy_time_min_ens_std_spatial_mean',
 'divergence_10m_time_min_ens_std_spatial_mean',
 'w_down_time_min_ens_std_spatial_mean',
 'uh_0to2_time_max_ens_std_of_90th',
 'uh_0to2_time_max_ens_mean_of_90th',
 'uh_2to5_time_max_ens_std_of_90th',
 'uh_2to5_time_max_ens_mean_of_90th',
 'wz_0to2_time_max_ens_std_of_90th',
 'wz_0to2_time_max_ens_mean_of_90th',
 'comp_dz_time_max_ens_std_of_90th',
 'comp_dz_time_max_ens_mean_of_90th',
 'ws_80_time_max_ens_std_of_90th',
 'ws_80_time_max_ens_mean_of_90th',
 'w_up_time_max_ens_std_of_90th',
 'w_up_time_max_ens_mean_of_90th',
 'hailcast_time_max_ens_std_of_90th',
 'hailcast_time_max_ens_mean_of_90th',
 'w_1km_time_max_ens_std_of_90th',
 'w_1km_time_max_ens_mean_of_90th',
 '10-m_bulk_shear_time_max_ens_std_of_90th',
 '10-m_bulk_shear_time_max_ens_mean_of_90th',
 'dbz_1to3km_max_time_max_ens_std_of_90th',
 'dbz_1to3km_max_time_max_ens_mean_of_90th',
 'dbz_3to5km_max_time_max_ens_std_of_90th',
 'dbz_3to5km_max_time_max_ens_mean_of_90th',
 'cloud_top_temp_time_min_ens_std_of_10th',
 'cloud_top_temp_time_min_ens_mean_of_10th',
 'bouyancy_time_min_ens_std_of_10th',
 'bouyancy_time_min_ens_mean_of_10th',
 'divergence_10m_time_min_ens_std_of_10th',
 'divergence_10m_time_min_ens_mean_of_10th',
 'w_down_time_min_ens_std_of_10th',
 'w_down_time_min_ens_mean_of_10th',
 'area',
 'eccentricity',
 'extent',
 'label',
 'major_axis_length',
 'minor_axis_length',                  
 'orientation',
 'Initialization Time',
                ]





obj_props_for_learning = ['area',
                          'eccentricity',
                          'extent',
                          'orientation',
                          'minor_axis_length',
                          'major_axis_length',
                          'matched_to_tornado_warn_ploys_15km',
                          'matched_to_tornado_warn_ploys_30km',
                          'matched_to_severe_wx_warn_polys_15km'
                          'matched_to_severe_wx_warn_polys_30km'
                          'obj_centroid_x',
                          'obj_centroid_y']

morph_vars = ['area',
                    'eccentricity',
                          'extent',
                          'orientation',
                          'minor_axis_length',
                          'major_axis_length',
                          ]


env_vars_smryfiles = [
                       'srh_0to1',
                       'srh_0to3',
                       'cape_ml',
                       'cin_ml',
                       'shear_u_0to6',
                       'shear_v_0to6',
                       'shear_u_0to1',
                       'shear_v_0to1',
                       'lcl_ml',
                       'th_e_ml',
                       'u_10',
                       'v_10']

env_vars_wofsdata  = [
                        'mid_level_lapse_rate',
                        'low_level_lapse_rate',
                        'temperature_850mb',
                        'temperature_700mb',
                        'temperature_500mb',
                        'geopotential_height_850mb',
                        'geopotential_height_700mb',
                        'geopotential_height_500mb',
                        'dewpoint_850mb',
                        'dewpoint_700mb',
                        'dewpoint_500mb',
                        ]

storm_vars_smryfiles = [ 'uh_0to2',
                         'uh_2to5',
                         'wz_0to2',
                         'comp_dz',
                         'ws_80',
                         'w_up',
                         'hailcast' ]

storm_vars_wofsdata = [ 'w_1km',
                        'w_down',
                        '10-m_bulk_shear',
                        'divergence_10m',
                        'bouyancy',
                        'cloud_top_temp',
                        'dbz_1to3km_max',
                        'dbz_3to5km_max']



min_vars = [ 'cloud_top_temp',
             'bouyancy',
             'divergence_10m',
             'w_down'
             ]

WOFS_VARS = ['10-500m_bulkshear', 'Initialization Time', 'buoyancy', 'cape_sfc',
       'cin_sfc', 'comp_dz', 'ctt', 'dbz_1to3', 'dbz_3to5', 'div_10m',
       'hailcast', 'lcl_sfc', 'low_level_lapse_rate', 'mid_level_lapse_rate',
       'shear_u_0to1', 'shear_u_0to6', 'shear_v_0to1', 'shear_v_0to6',
       'srh_0to1', 'srh_0to3', 'u_10', 'uh_0to2_instant', 'uh_2to5_instant',
       'v_10', 'w_1km', 'w_down', 'w_up', 'ws_80', 'wz_0to2_instant']


smryfile_variables = {'ENS': storm_vars_smryfiles, 'ENV': env_vars_smryfiles}
wofsdata_variables = storm_vars_wofsdata + env_vars_wofsdata

storm_variables = storm_vars_smryfiles + storm_vars_wofsdata
#storm_variables = ['10-500m_bulk_shear' if x == '10-m_bulk_shear' else x for x in storm_variables]
environmental_variables = env_vars_wofsdata + env_vars_smryfiles

map_to_readable_names={
                    'Run Date' : 'Run Date',
                    'Bias' : 'Bias',
                    'MRMS Reflectivity @ 0 min':'MRMS Reflectivity @ Initialization',
                    'MRMS Reflectivity @ 15 min':'MRMS Reflectivity 15 min after Initialization',
                    'MRMS Reflectivity @ 30 min':'MRMS Reflectivity 30 min after Initialization',
                    'obj_centroid_x': 'X-comp of Object Centroid',
                    'obj_centroid_y': 'Y-comp of Object Centroid',
                    'area': 'Area',
                    'eccentricity': 'Eccentricity',
                    'extent' : 'Extent',
                    'orientation': 'Orientation',
                    'minor_axis_length': 'Minor Ax. Len.',
                    'major_axis_length': 'Major Ax. Len.',
                    'matched_to_tornado_warn_ploys_15km': 'Matched to Tornado Warning Polygon (15 km)',
                    'matched_to_tornado_warn_ploys_30km': 'Matched to Tornado Warning Polygon (30 km)',
                    'matched_to_severe_wx_warn_polys_15km': 'Matched to Severe Weather Warning Polygon (15 km)',
                    'matched_to_severe_wx_warn_polys_30km': 'Matched to Severe Weather Warning Polygon (30 km)',
                    'label': 'Object Label',
                    'ensemble_member': 'Ensemble Member',
                    'cape_0to3_ml':'0-3 km ML CAPE',
                    'cin_ml': 'ML CIN',
                    'cape_ml': 'ML CAPE',
                    'lcl_ml': 'ML LCL',
                    'u_10': '10-m U',
                    'v_10': '10-m V',
                    'th_e_ml': 'ML  $\\theta_{e}$',
                    'theta_e': 'ML $\\theta_{e}$',
                    'shear_u_0to6': '0-6 km U Shear',
                    'shear_v_0to6': '0-6 km V Shear',
                    'shear_u_0to1' : '0-1 km U Shear',
                    'shear_v_0to1' : '0-1 km V Shear',
                    'srh_0to1': 'SRH$_{0-1}$',
                    'srh_0to3': 'SRH$_{0-3}$',
                    'qv_2': '2-m Water Vapor',
                    't_2': '2-m Temperature',
                    'td_2': '2-m Dewpoint Temperature',
                    'bouyancy': 'Near-Surface Buoyancy',
                    'cp_bouy': 'Near-Surface Buoyancy',
                    'rel_helicity_0to1': '0-1 km Relative Helicity',
                    '10-500m_bulk_shear': '10-500 m Bulk Shear',
                    '10-500m_bulkshear': '10-500 m Bulk Shear',
                    '10-m_bulk_shear' : '10-500 m Bulk Shear',
                    'mid_level_lapse_rate': '500-700 mb Lap. Rate',
                    'low_level_lapse_rate': '0-3 km Lapse Rate',
                    'temperature_850mb': 'T (850 mb)',
                    'temperature_700mb': 'T (700 mb)',
                    'temperature_500mb': 'T (500 mb)',
                    'temperature_850': 'T (850 mb)',
                    'temperature_700': 'T (700 mb)',
                    'temperature_500': 'T (500 mb)',
                    'geopotential_height_850mb': '850 mb Geop. Hgt.',
                    'geopotential_height_500mb': '500 mb Geop. Hgt.',
                    'geopotential_height_700mb': '700 mb Geop. Hgt.',
                    'geo_hgt_850': '$\Phi_{850}$',
                    'geo_hgt_500': '$\Phi_{500}$',
                    'geo_hgt_700': '$\Phi_{700}$',
                    'dewpoint_850mb': 'T$_{d, 850}$',
                    'dewpoint_700mb': 'T$_{d, 700}$',
                    'dewpoint_500mb': 'T$_{d, 500}$',
                    'td_850' :  'T$_{d, 850}$',
                    'td_700' :  'T$_{d, 700}$',
                    'td_500' :  'T$_{d, 500}$',
                    'cloud_top_temp': 'CTT',
                    'ctt' : 'CTT',
                    'dbz_1to3km_max': '1-3 km Max Refl.',
                    'dbz_3to5km_max': '3-5 km Max Refl.',
                    'dbz_3to5': '3-5 km Max Refl.',
                    'uh_0to2': '0-2 km UH',
                    'uh_2to5': '2-5 km UH',
                    'wz_0to2': '0-2 km Vert. Vort.',
                    'comp_dz': 'Comp. Refl.',
                    'ws_80'  : '80-m Wind Speed',
                    'w_1km'  : 'Low-level $W$',
                    'w_down' : 'Downdraft',
                    'w_up': 'Updraft',
                    'hail': 'Hail',
                    'hailcast': 'Hail',
                    'Initialization Time' : 'Initialization Time',
                    'divergence_10m': '10-m Div.',
                    'div_10m': '10-m Div.'
                    }



map_to_units={
               'Bias' : 'unitless',
                'area': 'grid cells',
                'eccentricity': 'unitless',
                'extent' : 'unitless',
                'orientation': 'unitless',
                'minor_axis_length': 'grid length',
                'major_axis_length': 'grid length',
                'cin_ml': 'J kg$^{-1}$',
                'cape_ml': 'J kg$^{-1}$',
                'lcl_ml': 'm',
                'u_10': 'kts',
                'v_10': 'kts',
                'th_e_ml': 'K',
                'theta_e': 'K',
                'shear_u_0to6': 'kts',
                'shear_v_0to6': 'kts',
                'shear_u_0to1' : 'kts',
                'shear_v_0to1' : 'kts',
                'srh_0to1': 'm$^{2}$ s$^{-2}$',
                'srh_0to3': 'm$^{2}$ s$^{-2}$',
                'qv_2': 'g kg$^{-1}$',
                't_2': '$^{\circ}$F',
                'td_2': '$^{\circ}$F',
                'bouyancy': 'm s$^{-2}$',
                'cp_bouy': 'm s$^{-2}$',
                '10-500m_bulk_shear': 'm s$^{-1}$',
                '10-500m_bulkshear': 'm s$^{-1}$',
                '10-m_bulk_shear' : 'm s$^{-1}$',
                'mid_level_lapse_rate': '$^{\circ}$C / Km',
                'low_level_lapse_rate': '$^{\circ}$C / Km',
                    'temperature_850mb': '${^\circ}$C',
                    'temperature_700mb': '$^{\circ}$C',
                    'temperature_500mb': '${^\circ}$C',
                    'temperature_850': '$^{\circ}$C',
                    'temperature_700': '$^{\circ$}$C',
                    'temperature_500': '$^{\circ$}$C',
                    'geopotential_height_850mb': 'm',
                    'geopotential_height_500mb': 'm',
                    'geopotential_height_700mb': 'm',
                    'geo_hgt_850': 'm',
                    'geo_hgt_500': 'm',
                    'geo_hgt_700': 'm',
                    'dewpoint_850mb': '$^{\circ}$C',
                    'dewpoint_700mb': '$^{\circ}$C',
                    'dewpoint_500mb': '$^{\circ}$C',
                    'td_850' :  '$^{\circ}$C',
                    'td_700' :  '$^{\circ}$C',
                    'td_500' :  '$^{\circ}$C',
                    'cloud_top_temp': '$^{\circ}$C',
                    'ctt' : '$^{\circ}$C',
                    'dbz_1to3km_max': 'dBZ',
                    'dbz_3to5km_max': 'dBZ',
                    'dbz_1to3' : 'dBZ',
                    'dbz_3to5' : 'dBZ',
                    'uh_0to2': 'm$^{2}$ s$^{-2}$',
                    'uh_2to5': 'm$^{2}$ s$^{-2}$',
                    'wz_0to2': 's$^{-1}$',
                    'comp_dz': 'dBZ',
                    'ws_80'  : 'kts',
                    'w_1km'  : 'm s$^{-1}$',
                    'w_down' : 'm s$^{-1}$',
                    'w_up': 'm s$^{-1}$',
                    'hail': 'in.',
                    'hailcast': 'in.',
                    'Initialization Time' : 'Initialization Time',
                    'divergence_10m': 'kts',
                    'div_10m': 'kts',
                    'Run Date' : 'Run Date',
                    }


def to_color(f):
    varname = f.split('_ens')[0].split('_time')[0]
    if varname in storm_variables:
        color = 'lightcoral'
    elif varname in environmental_variables:
        color = 'lightblue'
    elif varname in obj_props_for_learning:
        color = 'peachpuff'
    else:
        color = 'lightgreen'
    
    return color

def get_units(feature):
    """ return units of a variable """
    varname = feature.split('_ens')[0].split('_time')[0]
    return map_to_units.get(varname, feature)


def to_readable_names(features):
    if not isinstance(features, list):
        features = [features]
    
    for f in features:
        old_f = f
        varname = f.split('_ens')[0].split('_time')[0]
    
        
        try:
            f = f.replace(varname, map_to_readable_names[varname])
        except:
            f = varname
        f = f.replace('_time_max', ' (time max)')
        f = f.replace('_time_min', ' (time min)')
        f = f.replace('_time_std', ' (time std)')
        f = f.replace('_ens_mean', ' (Ens. mean)')
        f = f.replace('_ens_std', ' (Ens. std)')
        f = f.replace('_spatial_mean', '')

        components = f.split('(')
        varname = components[0]
        ens_stat = components[-1].replace(')','').replace('std', 'stdev')

        if 'Ens.' not in f:
            official_name = f
        else:
            if '90' in ens_stat or '10' in ens_stat:
                p = 90 if '90' in ens_stat else 10
                ens_stat = '%s' % (ens_stat.split("_")[0])
                ens_stat = ens_stat.replace('Ens. mean', '$\mu_{e,A}$')
                ens_stat = ens_stat.replace('Ens. stdev', '$\sigma_{e,A}$')
            else:
                ens_stat = f'{ens_stat.split("_")[0]}'
                ens_stat = ens_stat.replace('Ens. mean', '$\mu_{e,S}$')
                ens_stat = ens_stat.replace('Ens. stdev', '$\sigma_{e,S}$')

            if len(components) == 3:
                time_stat = components[1]
                time_stat = time_stat.replace(') ', '').title().replace(' ', '-')
                time_stat = 'min' if 'Min' in time_stat else 'max'
                official_name = fr'{varname} ({ens_stat})'
            else:
                official_name = fr'{varname} ({ens_stat})'
                
        return official_name

MORPHOLOGICAL_FEATURES = [
                          'area',
                          'eccentricity',
                          'extent',
                          'orientation',
                          'minor_axis_length',
                          'major_axis_length',
                          'intensity_max',
                          'ens_track_prob'
                          ]



ENV_VARS =  [   'freezing_level',
              'theta_e',
              'u_10',
              'v_10',
              'temperature_850',
              'temperature_700',
              'temperature_500',
              'td_850',
              'td_700',
              'td_500',
              'mid_level_lapse_rate',
              'low_level_lapse_rate',
              'geo_hgt_850',
              'geo_hgt_500',
              'geo_hgt_700',
              'td_850',
              'td_700',
              'td_500',
              'QVAPOR_850',
              'QVAPOR_700',
              'QVAPOR_500',
              'qv_2',
             'srh_0to1',
             'srh_0to3',
             'cape_ml',
             'cin_ml',
             'shear_u_0to6',
             'shear_v_0to6',
             'shear_u_0to1',
             'shear_v_0to1',
             'shear_u_3to6',
             'shear_v_3to6',
             'stp', 
             'lcl_ml',
             'srh_0to500',
             'stp_srh0to500',
           ]

STORM_VARS  = [ 'uh_0to2_instant',
              'uh_2to5_instant',
              'wz_0to2_instant',
              'comp_dz',
              'ws_80',
              'w_up',
              'hailcast',
              'w_1km',
              'w_down',
              '10-500m_bulkshear',
              'div_10m',
              'buoyancy',
              'ctt',
              'dbz_3to5', 
              'dbz_1to3', 
              'dbz_1km', 
              'okubo_weiss',
]


map_to_readable_names={
                    'Run Date' : 'Run Date',
                    'Bias' : 'Bias',
                    'obj_centroid_x': 'X-comp of Object Centroid',
                    'obj_centroid_y': 'Y-comp of Object Centroid',
                    'area': 'Area',
                    'eccentricity': 'Eccentricity',
                    'extent' : 'Extent',
                    'orientation': 'Orientation',
                    'minor_axis_length': 'Minor Ax. Len.',
                    'major_axis_length': 'Major Ax. Len.',
                    'label': 'Object Label',
                    'ensemble_member': 'Ensemble Member',
                    'cape_0to3_ml':'0-3 km ML CAPE',
                    'cin_ml': 'ML CIN',
                    'cin_mu': 'MU CIN',
                    'cin_sfc': 'Surface-based CIN',
    
                    'cape_ml': 'ML CAPE',
                    'cape_mu': 'MU CAPE',
                    'cape_sfc': 'Surface-based CAPE',
    
                    'lcl_ml': 'ML LCL',
                    'lcl_mu': 'MU LCL',
                    'lcl_sfc': 'Surface-based LCL',
    
                    'u_10': '10-m U-wind comp.',
                    'v_10': '10-m V-wind comp.',
                    'th_e_ml': 'ML  $\\theta_{e}$',
                    'theta_e': 'ML $\\theta_{e}$',
                    'shear_u_3to6' : '3-6 km U-Shear',
                    'shear_v_3to6' : '3-6 km V-Shear',
                    'shear_u_0to6': '0-6 km U-Shear',
                    'shear_v_0to6': '0-6 km V-Shear',
                    'shear_u_0to1' : '0-1 km U-Shear',
                    'shear_v_0to1' : '0-1 km V-Shear',
                    'srh_0to1': '0-1 km SRH',
                    'srh_0to3': '0-3 km SRH',
                    'srh_0to500' : '0-500 m SRH',
                    'qv_2': '2-m Water Vapor',
                    't_2': '2-m Temp.',
                    'td_2': '2-m Dewpoint Temp.',
                    'bouyancy': 'Near-SFC Buoyant Forcing',
                    'buoyancy' : 'Near-SFC Buoyant Forcing',
                    'cp_bouy': 'SFC Buoyancy',
                    'rel_helicity_0to1': '0-1 km Relative Helicity',
                    '10-500m_bulk_shear': '10-500 m Bulk Shear',
                    '10-500m_bulkshear': '10-500 m Bulk Shear',
                    '10-m_bulk_shear' : '10-500 m Bulk Shear',
                    'mid_level_lapse_rate': '500-700 mb Lapse Rate',
                    'low_level_lapse_rate': '0-3 km Lapse Rate',
                    'temperature_850mb': 'T (850 mb)',
                    'temperature_700mb': 'T (700 mb)',
                    'temperature_500mb': 'T (500 mb)',
                    'temperature_850': 'T (850 mb)',
                    'temperature_700': 'T (700 mb)',
                    'temperature_500': 'T (500 mb)',
                    'geopotential_height_850mb': '850 mb Geop. Hgt.',
                    'geopotential_height_500mb': '500 mb Geop. Hgt.',
                    'geopotential_height_700mb': '700 mb Geop. Hgt.',
                    'geo_hgt_850': '$\Phi_{850}$',
                    'geo_hgt_500': '$\Phi_{500}$',
                    'geo_hgt_700': '$\Phi_{700}$',
                    'dewpoint_850mb': 'T$_{d, 850}$',
                    'dewpoint_700mb': 'T$_{d, 700}$',
                    'dewpoint_500mb': 'T$_{d, 500}$',
                    'td_850' :  'T$_{d, 850}$',
                    'td_700' :  'T$_{d, 700}$',
                    'td_500' :  'T$_{d, 500}$',
                    'cloud_top_temp': 'Cloud Top Temp.',
                    'ctt' : 'Cloud Top Temp.',
                    'dbz_1to3km_max': '1-3 km Max Refl.',
                    'dbz_1to3' : '1-3 km Max Refl.',
                    'dbz_3to5km_max': '3-5 km Max Refl.',
                    'dbz_3to5': '3-5 km Max Refl.',
                    'dbz_1km' : '1 km Refl.', 
                    'uh_0to2': '0-2 km UH',
                    'uh_2to5': '2-5 km UH',
                    'wz_0to2': '0-2 km Vert. Vort.',
                    'uh_0to2_instant': '0-2 km UH',
                    'uh_2to5_instant': '2-5 km UH',
                    'wz_0to2_instant': '0-2 km Vert. Vort.',
                    'comp_dz': 'Comp. Refl.',
                    'ws_80'  : '80-m Wind Speed',
                    'w_1km'  : 'Low-level $W$',
                    'w_down' : 'Downdraft',
                    'w_up': 'Updraft',
                    'hail': 'Hail',
                    'hailcast': 'Hail',
                    'Initialization Time' : 'Initialization Time',
                    'divergence_10m': '10-m Div.',
                    'div_10m': '10-m Div.',
                    'QVAPOR_850' : '850mb Water Vapor', 
                    'QVAPOR_700' : '700mb Water Vapor', 
                    'QVAPOR_500' : '500mb Water Vapor', 
                    'freezing_level' : 'Freezing Level', 
                    'stp' : 'STP', 
                    'stp_srh0to500' : r'STP$_{SRH0TO500}$',
                    'okubo_weiss' : 'Okubo-Weiss Num.',
                    'ens_track_prob' : 'Max Ens. Prob', 
                    'area_ratio' : 'unitless', 
                    'avg_updraft_track_area' : "Ens. Avg. Updraft Track Area", 
                    }



map_to_units={
               'Bias' : 'unitless',
                'area': 'grid cells',
                'eccentricity': 'unitless',
                'extent' : 'unitless',
                'orientation': 'unitless',
                'minor_axis_length': 'grid length',
                'major_axis_length': 'grid length',
                'cin_ml': 'J kg$^{-1}$',
                'cape_ml': 'J kg$^{-1}$',
                'lcl_ml': 'm',
                'cin_sfc': 'J kg$^{-1}$',
                'cape_sfc': 'J kg$^{-1}$',
                'lcl_sfc': 'm',
   
                'cin_mu': 'J kg$^{-1}$',
                'cape_mu': 'J kg$^{-1}$',
                'lcl_mu': 'm',
                'u_10': 'kts',
                'v_10': 'kts',
                'th_e_ml': 'K',
                'theta_e': 'K',
                'shear_u_0to6': 'kts',
                'shear_v_0to6': 'kts',
                'shear_u_3to6': 'kts',
                'shear_v_3to6': 'kts',
                'shear_u_0to1' : 'kts',
                'shear_v_0to1' : 'kts',
                'srh_0to1': 'm$^{2}$ s$^{-2}$',
                'srh_0to3': 'm$^{2}$ s$^{-2}$',
                'srh_0to500': 'm$^{2}$ s$^{-2}$',
                'qv_2': 'g kg$^{-1}$',
                't_2': '$^{\circ}$F',
                'td_2': '$^{\circ}$F',
                'bouyancy': 'm s$^{-2}$',
                'buoyancy' : 'm s$^{-2}$',
                'cp_bouy': 'm s$^{-2}$',
                '10-500m_bulk_shear': 'kts',
                '10-500m_bulkshear': 'kts',
                '10-m_bulk_shear' : 'kts',
                'mid_level_lapse_rate': '$^{\circ}$C / Km',
                'low_level_lapse_rate': '$^{\circ}$C / Km',
                    'temperature_850mb': '${^\circ}$F',
                    'temperature_700mb': '$^{\circ}$F',
                    'temperature_500mb': '${^\circ}$F',
                    'temperature_850': '$^{\circ}$F',
                    'temperature_700': '$^{\circ}$F',
                    'temperature_500': '$^{\circ}$F',
                    'geopotential_height_850mb': 'm',
                    'geopotential_height_500mb': 'm',
                    'geopotential_height_700mb': 'm',
                    'geo_hgt_850': 'm',
                    'geo_hgt_500': 'm',
                    'geo_hgt_700': 'm',
                    'dewpoint_850mb': '$^{\circ}$F',
                    'dewpoint_700mb': '$^{\circ}$F',
                    'dewpoint_500mb': '$^{\circ}$F',
                    'td_850' :  '$^{\circ}$F',
                    'td_700' :  '$^{\circ}$F',
                    'td_500' :  '$^{\circ}$F',
                    'cloud_top_temp': '$^{\circ}$F',
                    'ctt' : '$^{\circ}$F',
                    'dbz_1to3km_max': 'dBZ',
                    'dbz_1to3' : 'dBZ',
                    'dbz_1km' : 'dBZ',
                    'dbz_3to5km_max': 'dBZ',
                    'dbz_1to3' : 'dBZ',
                    'dbz_3to5' : 'dBZ',
                    'uh_0to2': 'm$^{2}$ s$^{-2}$',
                    'uh_2to5': 'm$^{2}$ s$^{-2}$',
                    'wz_0to2': 's$^{-1}$',
                    'uh_0to2_instant': 'm$^{2}$ s$^{-2}$',
                    'uh_2to5_instant': 'm$^{2}$ s$^{-2}$',
                    'wz_0to2_instant': 's$^{-1}$',
    
                    'comp_dz': 'dBZ',
                    'ws_80'  : 'kts',
                    'w_1km'  : 'm s$^{-1}$',
                    'w_down' : 'm s$^{-1}$',
                    'w_up': 'm s$^{-1}$',
                    'hail': 'in.',
                    'hailcast': 'in.',
                    'Initialization Time' : 'Hrs After Mignight',
                    'divergence_10m': 'kts',
                    'div_10m': 'kts',
                    'Run Date' : 'Run Date',
                    'okubo_weiss' : 'unitless', 
                    'forecast_time_index' : 'unitless',
                    'avg_updraft_track_area' : 'unitless',
                    'area_ratio' : 'unitless', 
                    'QVAPOR_850' : 'g/kg', 
                    'QVAPOR_700' : 'g/kg', 
                    'QVAPOR_500' : 'g/kg', 
                    'freezing_level' : 'm', 
                    'stp' : 'unitless', 
                    'stp_srh0to500' : 'unitless',
                    'okubo_weiss' : 'unitless',
                    'ens_track_prob' : 'unitless',
                    'obj_centroid_y' : 'unitless', 
                    'obj_centroid_x' : 'unitless', 
                    'label' : 'unitless', 
                    'avg_updraft_track_area' : "grid cells", 
                    }


def to_new_color(f):
    varname = f.split('__')[0]

    if varname in STORM_VARS:
        color = 'lightcoral'
    elif varname in ENV_VARS:
        color = 'lightblue'
    elif varname in MORPHOLOGICAL_FEATURES:
        color = 'peachpuff'
    else:
        color = 'lightgreen'
    
    return color

def get_units(feature):
    """ return units of a variable """
    varname = feature.split('_ens')[0].split('_time')[0]
    return map_to_units.get(varname, feature)


def to_readable_names(features):
    if not isinstance(features, list):
        features = [features]
    
    for f in features:
        old_f = f
        varname = f.split('_ens')[0].split('_time')[0]
    
        
        try:
            f = f.replace(varname, map_to_readable_names[varname])
        except:
            f = varname
        f = f.replace('_time_max', ' (time max)')
        f = f.replace('_time_min', ' (time min)')
        f = f.replace('_time_std', ' (time std)')
        f = f.replace('_ens_mean', ' (Ens. mean)')
        f = f.replace('_ens_std', ' (Ens. std)')
        f = f.replace('_spatial_mean', '')

        components = f.split('(')
        varname = components[0]
        ens_stat = components[-1].replace(')','').replace('std', 'stdev')

        if 'Ens.' not in f:
            official_name = f
        else:
            if '90' in ens_stat or '10' in ens_stat:
                p = 90 if '90' in ens_stat else 10
                ens_stat = '%s' % (ens_stat.split("_")[0])
                #ens_stat = ens_stat.replace('Ens. mean', '$\mu_{e,A}$')
                #ens_stat = ens_stat.replace('Ens. stdev', '$\sigma_{e,A}$')
            else:
                ens_stat = f'{ens_stat.split("_")[0]}'
                #ens_stat = ens_stat.replace('Ens. mean', '$\mu_{e,S}$')
                #ens_stat = ens_stat.replace('Ens. stdev', '$\sigma_{e,S}$')

            if len(components) == 3:
                time_stat = components[1]
                time_stat = time_stat.replace(') ', '').title().replace(' ', '-')
                time_stat = 'min' if 'Min' in time_stat else 'max'
                official_name = fr'{ens_stat} {varname}'
            else:
                official_name = fr'{ens_stat} {varname}'

    return official_name

def to_units(f):
    comps = f.split('__') 
    var = comps[0]
    return map_to_units[var] #.get(varname, '')

def to_display_name(f):
    stat_mapper = {'amp_ens_mean' : '$\mu_{e,A}$', 
               'amp_ens_std' : '$\sigma_{e,A}$',
               'amp_ens_max' : 'max', 
               'ens_std' : '$\sigma_{e,S}$', 
               'ens_mean' : '$\mu_{e,S}$',
               'ens_max' : 'Ens. Max',
               'ens_min' : 'Ens. Min',
              }

    comps = f.split('__') 
    var = comps[0]
    
    var = map_to_readable_names[var] #.get(var, var) 
    if len(comps)>1:
        if 'time' in comps[1]:
            # Intra-storm 
            ens_stat = stat_mapper[(comps[2]).split('_spatial')[0]]
            if comps[-1] == 'cond':
                ens_stat = f'Cond. {ens_stat}'
        else:
            # Env
            ens_stat = stat_mapper[comps[1]]
    
        display = f'{var} ({ens_stat})'
    else:
        display = var
        
    return display


wofs_vars_display = {f : to_display_name(f) for f in WOFS_VARS }
wofs_display_feature_names = {f : to_readable_names(f) for f in WOFS_FEATURE_NAMES}
wofs_feature_colors = {f : to_color(f) for f in WOFS_FEATURE_NAMES}
wofs_feature_colors1 = {f : to_new_color(f) for f in WOFS_VARS }

new_wofs_display_feature_names = {f : to_display_name(f) for f in NEW_WOFS_FEATURE_NAMES}
new_wofs_feature_colors = {f : to_new_color(f) for f in NEW_WOFS_FEATURE_NAMES}
new_wofs_units = {f : to_units(f) for f in NEW_WOFS_FEATURE_NAMES}


    
pretty_names = [ '$IR_{min}$', '$IR_{1st}$', '$IR_{10th}$', '$IR_{25th}$', '$IR_{med}$',
  '$IR_{75th}$',  '$IR_{90th}$',  '$IR_{99th}$', '$IR_{max}$', '$WV_{min}$', '$WV_{1st}$', '$WV_{10th}$', '$WV_{25th}$', '$WV_{med}$',
  '$WV_{75th}$',  '$WV_{90th}$',  '$WV_{99th}$', '$WV_{max}$', '$VIS_{min}$', '$VIS_{1st}$', '$VIS_{10th}$', '$VIS_{25th}$', '$VIS_{med}$',
  '$VIS_{75th}$',  '$VIS_{90th}$',  '$VIS_{99th}$', '$VIS_{max}$', '$VIL_{min}$', '$VIL_{1st}$', '$VIL_{10th}$', '$VIL_{25th}$', '$VIL_{med}$',
  '$VIL_{75th}$',  '$VIL_{90th}$',  '$VIL_{99th}$', '$VIL_{max}$',]

sat_units = {'ir' : '$\degree$C', 
             'vl' : '$kg \ m^{-2}$',
             'wv' : '$\degree$C',
             'vi' : '%',  
            }


sat_display_feature_names = {'q000_ir': '$IR_{min}$',
 'q001_ir': '$IR_{1st}$',
 'q010_ir': '$IR_{10th}$',
 'q025_ir': '$IR_{25th}$',
 'q050_ir': '$IR_{med}$',
 'q075_ir': '$IR_{75th}$',
 'q090_ir': '$IR_{90th}$',
 'q099_ir': '$IR_{99th}$',
 'q100_ir': '$IR_{max}$',
 'q000_wv': '$WV_{min}$',
 'q001_wv': '$WV_{1st}$',
 'q010_wv': '$WV_{10th}$',
 'q025_wv': '$WV_{25th}$',
 'q050_wv': '$WV_{med}$',
 'q075_wv': '$WV_{75th}$',
 'q090_wv': '$WV_{90th}$',
 'q099_wv': '$WV_{99th}$',
 'q100_wv': '$WV_{max}$',
 'q000_vi': '$VIS_{min}$',
 'q001_vi': '$VIS_{1st}$',
 'q010_vi': '$VIS_{10th}$',
 'q025_vi': '$VIS_{25th}$',
 'q050_vi': '$VIS_{med}$',
 'q075_vi': '$VIS_{75th}$',
 'q090_vi': '$VIS_{90th}$',
 'q099_vi': '$VIS_{99th}$',
 'q100_vi': '$VIS_{max}$',
 'q000_vl': '$VIL_{min}$',
 'q001_vl': '$VIL_{1st}$',
 'q010_vl': '$VIL_{10th}$',
 'q025_vl': '$VIL_{25th}$',
 'q050_vl': '$VIL_{med}$',
 'q075_vl': '$VIL_{75th}$',
 'q090_vl': '$VIL_{90th}$',
 'q099_vl': '$VIL_{99th}$',
 'q100_vl': '$VIL_{max}$'}

cs = ['q000_ir',
 'q001_ir',
 'q010_ir',
 'q025_ir',
 'q050_ir',
 'q075_ir',
 'q090_ir',
 'q099_ir',
 'q100_ir',
 'q000_wv',
 'q001_wv',
 'q010_wv',
 'q025_wv',
 'q050_wv',
 'q075_wv',
 'q090_wv',
 'q099_wv',
 'q100_wv',
 'q000_vi',
 'q001_vi',
 'q010_vi',
 'q025_vi',
 'q050_vi',
 'q075_vi',
 'q090_vi',
 'q099_vi',
 'q100_vi',
 'q000_vl',
 'q001_vl',
 'q010_vl',
 'q025_vl',
 'q050_vl',
 'q075_vl',
 'q090_vl',
 'q099_vl',
 'q100_vl']

r = [255/255,127/255,127/255]
b = [126/255,131/255,248/255]

colors = [r,b,'k','y']
sat_color_dict = {}
cit = -1
for i in np.arange(0,36):
    if np.mod(i,9) == 0:
        cit += 1
        c = colors[cit]
    sat_color_dict[cs[i]] = c
    
sat_color_dict['IR'] = r
sat_color_dict['VIL'] = 'y'
sat_color_dict['VIS'] = 'k'
sat_color_dict['WV'] = b
    
lightning_units = {f : sat_units[f.split('_')[1]] for f in cs}



# Predictor columns. Order matters! Wouldn't touch this.
PREDICTOR_COLUMNS = ['dllwave_flux', 'dwpt2m', 'fric_vel', 'gflux', 'high_cloud',
            'lat_hf', 'low_cloud', 'mid_cloud', 'sat_irbt', 'sens_hf',
            'sfcT_hrs_ab_frez', 'sfcT_hrs_bl_frez', 'sfc_rough', 'sfc_temp',
            'swave_flux', 'temp2m', 'tmp2m_hrs_ab_frez', 'tmp2m_hrs_bl_frez',
            'tot_cloud', 'uplwav_flux', 'vbd_flux', 'vdd_flux', 'wind10m',
            'date_marker', 'urban','rural','d_ground','d_rad_d','d_rad_u',
            'hrrr_dT']

units = ['W m$^{-2}$', '$^{\circ}$C', 'm s$^{-1}$', 'W m$^{-2}$', '%', 'W m$^{-2}$', '%', '%', 
         '$^{\circ}$C', 'W m$^{-2}$', 'hrs', 'hrs', 'unitless','$^{\circ}$C', 'W m$^{-2}$', '$^{\circ}$C', 
         'hrs', 'hrs', '%', 'W m$^{-2}$', 'W m$^{-2}$', 'W m$^{-2}$', 'm s$^{-1}$', 'days', 'unitless', 
         'unitless', 'W m$^{-2}$', 'W m$^{-2}$', 'W m$^{-2}$', '$^{\circ}$C']

# The target variable
TARGET_COLUMN = 'cat_rt'

# Dictionary that maps predictor columns to pretty names
FIGURE_MAPPINGS = {
    'dllwave_flux': '$\lambda_{\downarrow}$',
    'dwpt2m': '$T_{d}$',
    'fric_vel': '$V_{fric}$',
    'gflux': 'G',
    'high_cloud': '$C_{high}$',
    'lat_hf':'$L_{hf}$',
    'low_cloud': '$C_{low}$',
    'mid_cloud': '$C_{mid}$',
    'sat_irbt':'$T_{irbt}$',
    'sens_hf': '$S_{hf}$',
    'sfcT_hrs_ab_frez': 'Hours T$_{sfc}$ > 0$^{\circ}$C',
    'sfcT_hrs_bl_frez': 'Hours T$_{sfc}$ $\leq$ 0$^{\circ}$C',
    'sfc_rough': '$S_{R}$',
    'sfc_temp': '$T_{sfc}$',
    'swave_flux': 'S',
    'temp2m': '$T_{2m}$',
    'tmp2m_hrs_ab_frez':'Hours T$_{2m}$ > 0$^{\circ}$C',
    'tmp2m_hrs_bl_frez':'Hours T$_{2m}$ $\leq$ 0$^{\circ}$C',
    'tot_cloud': '$C_{total}$',
    'uplwav_flux':r'$\lambda_{\uparrow}$',
    'vbd_flux': '$V_{bd}$',
    'vdd_flux': '$V_{dd}$',
    'wind10m': '$U_{10m}$',
    'date_marker': 'Date Marker',
    'urban': '$L_{urban}$',
    'rural': '$L_{rural}$',
    'd_ground': '$G_{diff}$',
    'd_rad_d': '$dR_{down}$',
    'd_rad_u': '$dR_{up}$',
    'hrrr_dT': '$dT_{hrrr}$'
}

COLOR_DICT = { 'dllwave_flux':'xkcd:light light green',
              'dwpt2m': 'xkcd:powder blue',
              'gflux':'xkcd:light light green',
              'high_cloud':'xkcd:light periwinkle',
              'lat_hf':'xkcd:light light green',
              'low_cloud':'xkcd:light periwinkle',
              'mid_cloud':'xkcd:light periwinkle',
              'sat_irbt':'xkcd:light periwinkle',
              'sens_hf':'xkcd:light light green',
            'sfcT_hrs_ab_frez':'xkcd:powder blue',
            'sfcT_hrs_bl_frez':'xkcd:powder blue',
            'sfc_rough':'xkcd:orangish',
            'sfc_temp':'xkcd:powder blue',
            'swave_flux':'xkcd:light light green',
            'temp2m':'xkcd:powder blue',
            'tmp2m_hrs_ab_frez':'xkcd:powder blue',
            'tmp2m_hrs_bl_frez':'xkcd:powder blue',
            'tot_cloud':'xkcd:light periwinkle',
            'uplwav_flux':'xkcd:light light green',
            'vbd_flux':'xkcd:light light green',
            'vdd_flux':'xkcd:light light green',
            'wind10m':'xkcd:orangish',
            'date_marker':'xkcd:orangish',
            'urban':'xkcd:orangish',
            'rural':'xkcd:orangish',
            'd_ground':'xkcd:light light green',
            'd_rad_d':'xkcd:light light green',
            'd_rad_u':'xkcd:light light green',
            'hrrr_dT':'xkcd:powder blue', 
             'fric_vel' : 'xkcd:orangish',
             'Temperature' : 'xkcd:powder blue',
             'Freezing Duration' : 'xkcd:orangish', 
              'Cloud Coverage' : 'xkcd:light periwinkle',
              'Radiation' : 'xkcd:light light green'
             
             }

UNITS = {c : u for c,u in zip(PREDICTOR_COLUMNS , units)}


PIMP_MAPPINGS = {
    'dllwave_flux': 'Downward longwave Rad. flux',
    'dwpt2m': 'Dewpoint Temperature',
    'fric_vel': '$V_{fric}$',
    'gflux': 'G',
    'high_cloud': '$C_{high}$',
    'lat_hf':'Latent Heat Flux',
    'low_cloud': 'Low cloud cover percentage',
    'mid_cloud': '$C_{mid}$',
    'sat_irbt':'Simulated Brightness Temp.',
    'sens_hf': '$S_{hf}$',
    'sfcT_hrs_ab_frez': 'Hours $T_{sfc}$ $> $0$\circ$C',
    'sfcT_hrs_bl_frez': 'Hours $T_{sfc}$ $<= $0$\circ$C',
    'sfc_rough': '$S_{R}$',
    'sfc_temp': 'Surface Temperature',
    'swave_flux': 'S',
    'temp2m': '$T_{2m}$',
    'tmp2m_hrs_ab_frez':'Hours $T_{2m}$ $> $0$\circ$C',
    'tmp2m_hrs_bl_frez':'Hours $T_{2m}$ $<= $0$\circ$C',
    'tot_cloud': '$C_{total}$',
    'uplwav_flux':r'$\lambda_{\uparrow}$',
    'vbd_flux': '$V_{bd}$',
    'vdd_flux': '$V_{dd}$',
    'wind10m': '$U_{10m}$',
    'date_marker': 'Date Marker',
    'urban': '$L_{urban}$',
    'rural': '$L_{rural}$',
    'd_ground': '$G_{diff}$',
    'd_rad_d': '$dR_{down}$',
    'd_rad_u': '$dR_{up}$',
    'hrrr_dT': '$dT_{hrrr}$'
}

feature_colors = {**new_wofs_feature_colors, **wofs_feature_colors, **sat_color_dict, **COLOR_DICT, **wofs_feature_colors1}
display_feature_names = {**new_wofs_display_feature_names, **wofs_vars_display, 
                         **wofs_display_feature_names, **sat_display_feature_names, **FIGURE_MAPPINGS}

display_units = {**new_wofs_units, **UNITS, **lightning_units}