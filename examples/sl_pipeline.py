from desc.pipeline import Pipeline, ProcessingNode, DataProduct

SLPipeline = Pipeline('Strong Lensing Pipeline')

SLFinder = SLPipeline.add_processing_node('SLFinder')
dm_level1_catalog = DataProduct('DM Level 1 catalog')
dm_images = DataProduct('DM image data')
SLFinder.set_input(dm_level1_catalog, dm_images)
sl_candidates = DataProduct('SL candidates')
SLFinder.set_output(sl_candidates)

SpaceWarps = SLPipeline.add_processing_node('SpaceWarps')
SpaceWarps.set_input(sl_candidates)
desc_lenses = DataProduct('DESC Lenses')
SpaceWarps.set_output(desc_lenses)

SLMonitor = SLPipeline.add_processing_node('SLMonitor')
SLMonitor.set_input(dm_images, desc_lenses)
sl_light_curves = DataProduct('SL light curves')
SLMonitor.set_output(sl_light_curves)

SLTimer = SLPipeline.add_processing_node('SLTimer')
SLTimer.set_input(sl_light_curves)
sl_time_delays = DataProduct('SL time delays')
SLTimer.set_output(sl_time_delays)

SLENV = SLPipeline.add_processing_node('SLENV')
wl_shapes = DataProduct('WL shapes')
photo_zs = DataProduct('Photo-zs')
cosmo_sims = DataProduct('Cosmo sims')
SLENV.set_input(wl_shapes, photo_zs, cosmo_sims)
wl_params = DataProduct('WL parameters')
SLENV.set_output(wl_params)

SLModeler = SLPipeline.add_processing_node('SLModeler')
follow_up_data = DataProduct('Follow-up data')
SLModeler.set_input(sl_time_delays, follow_up_data)
lens_models = DataProduct('Lens models')
SLModeler.set_output(lens_models)

SLCosmo = SLPipeline.add_processing_node('SLCosmo')
SLCosmo.set_input(lens_models)
sl_cosmo_params = DataProduct('SL cosmological parameters')
SLCosmo.set_output(sl_cosmo_params)
