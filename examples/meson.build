examples_deps = [libvpx_dep]

# List of examples to build. UTILS are tools meant for distribution
# while EXAMPLES demonstrate specific portions of the API.

# Unlike the original, I'm putting all the common files in a
# single library to save on up to 16 copies of the same translation unit
# (y4minput.c and tools_common.c, for instance).

vpx_examples_common_headers = []

vpx_examples_common_sources = []

if features.get('decoders', false) or features.get('encoders', false)
	vpx_examples_common_headers += files(
		'../vpx_ports/mem_ops.h',
		'../vpx_ports/mem_ops_aligned.h',
		'../vpx_ports/msvc.h',
		'../args.h',
		'../ivfdec.h',
		'../y4minput.h',
		'../tools_common.h',
		'../ivfenc.h', # encoders or decoders or vp8|9_encoder or (decoders and vp9_encoder)
		'../vpx_ports/vpx_timer.h',
		'../video_common.h',
	)

	vpx_examples_common_sources += files(
		'../args.c',
		'../ivfdec.c',
		'../y4minput.c',
		'../tools_common.c',
		'../ivfenc.c', # encoders or decoders or vp8|9_encoder or (decoders and vp9_encoder)
	)
endif

if features.get('decoders', false)
	vpx_examples_common_headers += files(
		'../vpx_ports/compiler_attributes.h',
		'../md5_utils.h',
		'../video_reader.h',
	)

	vpx_examples_common_sources += files(
		'../md5_utils.c',
		'../video_reader.c',
	)
endif

if features.get('encoders', false) or features.get('vp9_encoder', false)
	vpx_examples_common_headers += files(
		'../vpxstats.h',
	)

	vpx_examples_common_sources += files(
		'../vpxstats.c',
	)
endif

if features.get('encoders', false) or (features.get('decoders', false) and features.get('vp9_encoder', false))
	vpx_examples_common_headers += files(
		'../video_writer.h',
	)

	vpx_examples_common_sources += files(
		'../video_writer.c',
	)
endif

vpx_examples_common = static_library(
	'vpx_examples_common',
	vpx_examples_common_sources,
	extra_files: vpx_examples_common_headers,
	dependencies: examples_deps,
)

examples_deps += declare_dependency(
	link_with: vpx_examples_common,
	include_directories: include_directories('.'),
)

vpxdec_headers = files(
	'../vpx/vpx_integer.h',
	'../y4menc.h',
)

vpxdec_srcs = files(
	'../vpxdec.c',
	'../y4menc.c',
)

vpxenc_headers = files(
	'../vpxenc.h',
	'../rate_hist.h',
	'../warnings.h',
)

vpxenc_srcs = files(
	'../vpxenc.c',
	'../rate_hist.c',
	'../warnings.c',
)

vp9_spatial_svc_encoder_headers = files(
	'svc_context.h',
)

vp9_spatial_svc_encoder_srcs = files(
	'vp9_spatial_svc_encoder.c',
	'svc_encodeframe.c',
)

vpx_temporal_svc_encoder_headers = files(
)

vpx_temporal_svc_encoder_srcs = files(
	'vpx_temporal_svc_encoder.c',
)

simple_decoder_headers = files(
)

simple_decoder_srcs  = files(
	'simple_decoder.c',
)

postproc_headers = files(
)

postproc_srcs  = files(
	'postproc.c',
)

decode_to_md5_srcs = files(
	'decode_to_md5.c'
)

decode_to_md5_headers = files(
)

simple_encoder_headers = files(
)

simple_encoder_srcs = files(
	'simple_encoder.c',
)

simple_encoder_headers = files(
)

vp9_lossless_encoder_srcs = files(
	'vp9_lossless_encoder.c',
)

vp9_lossless_encoder_headers = files(
)

twopass_encoder_srcs = files(
	'twopass_encoder.c',
)

twopass_encoder_headers = files(
)

decode_with_drops_srcs = files(
	'decode_with_drops.c',
)

decode_with_drops_headers = files(
)

set_maps_srcs = files(
	'set_maps.c',
)

set_maps_headers = files(
)

vp8cx_set_ref_srcs = files(
	'vp8cx_set_ref.c',
)

vp8cx_set_ref_headers = files(
)

vp9cx_set_ref_srcs = files(
	'vp9cx_set_ref.c',
)

vp9cx_set_ref_headers = files(
)

vp8_multi_resolution_encoder_srcs = files(
	'vp8_multi_resolution_encoder.c',
)

vp9cx_set_ref_headers = files(
)

# Add compile flags and include path for libwebm sources.
if features.get('webm_io', false)
	examples_deps += libwebm_dep

	vpxdec_headers += files(
		'../webmdec.h',
	)
	vpxdec_srcs += files(
		'../webmdec.cc'
	)

	vpxenc_headers += files(
		'../webmenc.h',
	)
	vpxenc_srcs += files(
		'../webmenc.cc'
	)
endif

if features.get('decoders', false)
	vpxdec_deps = examples_deps

	if features.get('libyuv', false)
		vpxdec_deps += libyuv_dep
	endif

	vpxdec = executable(
		'vpxdec',
		vpxdec_srcs,
		extra_files: vpxdec_headers,
		dependencies: vpxdec_deps,
		install: features.get('install_bins', false),
	)
endif

if features.get('encoders', false)
	vpxenc_deps = examples_deps

	if features.get('libyuv', false)
		vpxenc_deps += libyuv_dep
	endif

	vpxenc = executable(
		'vpxenc',
		vpxenc_srcs,
		extra_files: vpxenc_headers,
		dependencies: vpxenc_deps,
		install: features.get('install_bins', false),
	)
endif

if features.get('vp9_encoder', false)
	vp9_spatial_svc_encoder = executable(
		'vp9_spatial_svc_encoder',
		vp9_spatial_svc_encoder_srcs,
		extra_files: vp9_spatial_svc_encoder_headers,
		dependencies: examples_deps,
	)
endif

if not features.get('shared', false)
	resize_util = executable(
		'resize_util',
		files(
			'resize_util.c'
		),
		dependencies: examples_deps,
	)
endif

if features.get('encoders', false)
	vpx_temporal_svc_encoder = executable(
		'vpx_temporal_svc_encoder',
		vpx_temporal_svc_encoder_srcs,
		extra_files: vpx_temporal_svc_encoder_headers,
		dependencies: examples_deps,
	)

	# Frame by frame MD5 checksum
	decode_to_md5 = executable(
		'decode_to_md5',
		decode_to_md5_srcs,
		extra_files: decode_to_md5_headers,
		dependencies: examples_deps,
	)

	# Simplified encoder loop
	simple_encoder = executable(
		'simple_encoder',
		simple_encoder_srcs,
		extra_files: simple_encoder_headers,
		dependencies: examples_deps,
	)

	# Simplified lossless VP9 encoder
	vp9_lossless_encoder = executable(
		'vp9_lossless_encoder',
		vp9_lossless_encoder_srcs,
		extra_files: vp9_lossless_encoder_headers,
		dependencies: examples_deps,
	)

	# Two-pass encoder loop
	twopass_encoder = executable(
		'twopass_encoder',
		twopass_encoder_srcs,
		extra_files: twopass_encoder_headers,
		dependencies: examples_deps,
	)

	# Set active and ROI maps
	set_maps = executable(
		'set_maps',
		set_maps_srcs,
		extra_files: set_maps_headers,
		dependencies: examples_deps,
	)
endif

if features.get('decoders', false)
	# Simplified decoder loop
	simple_decoder = executable(
		'simple_decoder',
		simple_decoder_srcs,
		extra_files: simple_decoder_headers,
		dependencies: examples_deps,
	)

	postproc = executable(
		'postproc',
		postproc_srcs,
		extra_files: postproc_headers,
		dependencies: examples_deps,
	)

	# Drops frames while decoding
	decode_with_drops = executable(
		'decode_with_drops',
		decode_with_drops_srcs,
		extra_files: postproc_headers,
		dependencies: examples_deps,
	)
endif

if features.get('vp8_encoder', false)
	# VP8 set encoder reference frame
	vp8cx_set_ref = executable(
		'vp8cx_set_ref',
		vp8cx_set_ref_srcs,
		extra_files: vp8cx_set_ref_headers,
		dependencies: examples_deps,
	)
endif

if features.get('vp9_encoder', false) and features.get('decoders', false)
	# VP9 set encoder reference frame
	vp9cx_set_ref = executable(
		'vp9cx_set_ref',
		vp9cx_set_ref_srcs,
		extra_files: vp9cx_set_ref_headers,
		dependencies: examples_deps,
	)
endif

if features.get('multi_res_encoding', false) and features.get('libyuv', false)
	# VP8 Multiple-resolution Encoding
	vp8_multi_resolution_encoder = executable(
		'vp8_multi_resolution_encoder',
		vp8_multi_resolution_encoder_srcs,
		extra_files: vp8_multi_resolution_encoder_headers,
		dependencies: examples_deps + libyuv_dep,
	)
endif

#
# Documentation Rules
#
# %.dox: %.c
# 	@echo "    [DOXY] $@"
# 	@mkdir -p $(dir $@)
# 	@echo "/*!\page example_$(@F:.dox=) $(@F:.dox=)" > $@
# 	@echo "   \includelineno $(<F)" >> $@
# 	@echo "*/" >> $@

# samples.dox: examples.mk
# 	@echo "    [DOXY] $@"
# 	@echo "/*!\page samples Sample Code" > $@
# 	@echo "    This SDK includes a number of sample applications."\
# 				"Each sample documents a feature of the SDK in both prose"\
# 				"and the associated C code."\
# 				"The following samples are included: ">>$@
# 	@$(foreach ex,$(sort $(notdir $(EXAMPLES:.c=))),\
# 		 echo "     - \subpage example_$(ex) $($(ex).DESCRIPTION)" >> $@;)
# 	@echo >> $@
# 	@echo "    In addition, the SDK contains a number of utilities."\
# 							"Since these utilities are built upon the concepts described"\
# 							"in the sample code listed above, they are not documented in"\
# 							"pieces like the samples are. Their source is included here"\
# 							"for reference. The following utilities are included:" >> $@
# 	@$(foreach ex,$(sort $(UTILS:.c=)),\
# 		 echo "     - \subpage example_$(ex) $($(ex).DESCRIPTION)" >> $@;)
# 	@echo "*/" >> $@

# CLEAN-OBJS += examples.doxy samples.dox $(ALL_EXAMPLES:.c=.dox)
# DOCS-yes += examples.doxy samples.dox
# examples.doxy: samples.dox $(ALL_EXAMPLES:.c=.dox)
# 	@echo "INPUT += $^" > $@
# 	@echo "ENABLED_SECTIONS += samples" >> $@
