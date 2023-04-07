# vpx_codec.mk

#### --- GENERATED --- ####

api_sources = files(
	'src/vpx_decoder.c',
	'src/vpx_encoder.c',
	'src/vpx_codec.c',
	'src/vpx_image.c',
)

api_optional_sources = {
}

api_headers_sources = files(
	'vpx_decoder.h',
	'vpx_encoder.h',
	'internal/vpx_codec_internal.h',
	'internal/vpx_ratectrl_rtc.h',
	'vpx_codec.h',
	'vpx_frame_buffer.h',
	'vpx_image.h',
	'vpx_integer.h',
	'vpx_ext_ratectrl.h',
)

api_headers_optional_sources = {
	'vp8_decoder' : files(
		'vp8.h',
		'vp8dx.h'
	),
	'vp8_encoder' : files(
		'vp8.h',
		'vp8cx.h'
	),
}

api_doc_headers_sources = files(
	'vpx_codec.h',
	'vpx_decoder.h',
	'vpx_encoder.h',
	'vpx_ext_ratectrl.h',
	'vpx_frame_buffer.h',
	'vpx_image.h',
)

api_doc_headers_optional_sources = {
	'vp8_decoder' : files(
		'vp8.h',
		'vp8dx.h'
	),
	'vp8_encoder' : files(
		'vp8.h',
		'vp8cx.h'
	),
}

#### --- END GENERATED --- ####

codec_srcs += api_sources
optional_sources = get_variable('api_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if not features.get(comp_name, false)
		continue
	endif
	if ARCH_EXT_LIST.contains(comp_name)
		codec_arch_srcs += {
			comp_name: codec_arch_srcs.get(comp_name, []) + comp_sources
		}
	else
		codec_srcs += comp_sources
	endif
endforeach

codec_headers += api_headers_sources
optional_sources = get_variable('api_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if not features.get(comp_name, false)
		continue
	endif
	if ARCH_EXT_LIST.contains(comp_name)
		codec_arch_headers += {
			comp_name: codec_arch_headers.get(comp_name, []) + comp_sources
		}
	else
		api_headers_sources += comp_sources
	endif
endforeach

codec_headers += api_doc_headers_sources
optional_sources = get_variable('api_doc_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if not features.get(comp_name, false)
		continue
	endif
	if ARCH_EXT_LIST.contains(comp_name)
		codec_arch_headers += {
			comp_name: codec_arch_headers.get(comp_name, []) + comp_sources
		}
	else
		codec_headers += comp_sources
	endif
endforeach

codec_exports += files(
	'exports_com'
)

if features.get('encoders', false)
	codec_exports += files(
		'exports_enc',
	)
endif

if features.get('decoders', false)
	codec_exports += files(
		'exports_dec',
	)
endif
