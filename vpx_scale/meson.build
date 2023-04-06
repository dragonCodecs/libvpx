# vp8_common.mk

#### --- GENERATED --- ####

scale_sources = files(
	'generic/yv12config.c',
	'generic/yv12extend.c',
	'vpx_scale_rtcd.c',
)

scale_optional_sources = {
	'dspr2' : files(
		'mips/dspr2/yv12extend_dspr2.c'
	),
	'spatial_resampling' : files(
		'generic/vpx_scale.c',
		'generic/gen_scalers.c'
	),
}

scale_headers_sources = files(
	'yv12config.h',
)

scale_headers_optional_sources = {
	'spatial_resampling' : files(
		'vpx_scale.h'
	),
}

#### --- END GENERATED --- ####

optional_sources = get_variable('scale_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		scale_sources += comp_sources
	endif
endforeach

codec_srcs += scale_sources

optional_sources = get_variable('scale_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		scale_headers_sources += comp_sources
	endif
endforeach

codec_headers += scale_headers_sources

vpx_scale_rtcd_defs = files(
	'vpx_scale_rtcd.pl',
)

vpx_scale_rtcd_h = custom_target(
	'vpx_scale_rtcd.h',
	command: rtcd_h_template + ['--sym=@0@'.format('vpx_scale_rtcd'), '@INPUT1@'],
	input: [config_mk, vpx_scale_rtcd_defs[0]],
	output: 'vpx_scale_rtcd.h',
	capture: true,
)

codec_srcs += vpx_scale_rtcd_h
codec_headers += vpx_scale_rtcd_defs
