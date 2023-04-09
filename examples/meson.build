examples_deps = [libvpx_dep]

# List of examples to build. UTILS are tools meant for distribution
# while EXAMPLES demonstrate specific portions of the API.

# Unlike the original, I'm putting all the common files in a
# single library.

vpxdec_headers = files(
	'../md5_utils.h',
	'../vpx_ports/compiler_attributes.h',
	'../vpx_ports/mem_ops.h',
	'../vpx_ports/mem_ops_aligned.h',
	'../vpx_ports/msvc.h',
	'../vpx_ports/vpx_timer.h',
	'../vpx/vpx_integer.h',
	'../args.h',
	'../ivfdec.h',
	'../y4minput.h',
	'../tools_common.h',
	'../y4menc.h',
)

vpxdec_srcs = files(
	'../vpxdec.c',
	'../md5_utils.c',
	'../args.c',
	'../ivfdec.c',
	'../y4minput.c',
	'../tools_common.c',
	'../y4menc.c',
)

vpxenc_headers = files(
	'../args.h',
	'../y4minput.h',
	'../vpxenc.h',
	'../ivfdec.h',
	'../ivfenc.h',
	'../rate_hist.h',
	'../tools_common.h',
	'../warnings.h',
	'../vpx_ports/mem_ops.h',
	'../vpx_ports/mem_ops_aligned.h',
	'../vpx_ports/msvc.h',
	'../vpx_ports/vpx_timer.h',
	'../vpxstats.h',
)

vpxenc_srcs = files(
	'../vpxenc.c',
	'../args.c',
	'../y4minput.c',
	'../ivfdec.c',
	'../ivfenc.c',
	'../rate_hist.c',
	'../tools_common.c',
	'../warnings.c',
	'../md5_utils.c',
	'../vpxstats.c',
)

vp9_spatial_svc_encoder_headers = files(
	'../args.h',
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_writer.h',
	'../vpx_ports/msvc.h',
	'../vpxstats.h',
	'svc_context.h',
)

vp9_spatial_svc_encoder_srcs = files(
	'vp9_spatial_svc_encoder.c',
	'../args.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_writer.c',
	'../vpxstats.c',
	'svc_encodeframe.c',
)

vpx_temporal_svc_encoder_headers = files(
	'../ivfenc.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_writer.h',
	'../vpx_ports/msvc.h',
	'../y4minput.h',
)

vpx_temporal_svc_encoder_srcs = files(
	'vpx_temporal_svc_encoder.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_writer.c',
)

simple_decoder_srcs  = files(
	'simple_decoder.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_reader.c',
)

simple_decoder_headers = files(
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_reader.h',
	'../vpx_ports/mem_ops.h',
	'../vpx_ports/mem_ops_aligned.h',
	'../vpx_ports/msvc.h',
)

simple_decoder_srcs  = files(
	'simple_decoder.c',
	'../ivfdec.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_reader.c',
)

simple_decoder_headers = files(
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_reader.h',
	'../vpx_ports/mem_ops.h',
	'../vpx_ports/mem_ops_aligned.h',
	'../vpx_ports/msvc.h',
)

postproc_srcs  = files(
	'postproc.c',
	'../ivfdec.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_reader.c',
)

postproc_headers = files(
	'../ivfdec.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_reader.h',
	'../vpx_ports/mem_ops.h',
	'../vpx_ports/mem_ops_aligned.h',
	'../vpx_ports/msvc.h',
)

decode_to_md5_srcs = files(
	'decode_to_md5.c',
	'../md5_utils.c',
	'../ivfdec.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_reader.c',
)

decode_to_md5_headers = files(
	'../md5_utils.h',
	'../ivfdec.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_reader.h',
	'../vpx_ports/compiler_attributes.h',
	'../vpx_ports/mem_ops.h',
	'../vpx_ports/mem_ops_aligned.h',
	'../vpx_ports/msvc.h',
)

simple_encoder_srcs = files(
	'simple_encoder.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_writer.c',
)

simple_encoder_headers = files(
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_writer.h',
	'../vpx_ports/msvc.h',
)

vp9_lossless_encoder_srcs = files(
	'vp9_lossless_encoder.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_writer.c',
)

vp9_lossless_encoder_headers = files(
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_writer.h',
	'../vpx_ports/msvc.h',
)

twopass_encoder_srcs = files(
	'twopass_encoder.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_writer.c',
)

twopass_encoder_headers = files(
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_writer.h',
	'../vpx_ports/msvc.h',
)

decode_with_drops_srcs = files(
	'decode_with_drops.c',
	'../ivfdec.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_reader.c',
)

decode_with_drops_headers = files(
	'../ivfdec.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_reader.h',
	'../vpx_ports/mem_ops.h',
	'../vpx_ports/mem_ops_aligned.h',
	'../vpx_ports/msvc.h',
)

set_maps_srcs = files(
	'set_maps.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_writer.c',
)

set_maps_headers = files(
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_writer.h',
	'../vpx_ports/msvc.h',
)

vp8cx_set_ref_srcs = files(
	'vp8cx_set_ref.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_writer.c',
)

vp8cx_set_ref_headers = files(
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_writer.h',
	'../vpx_ports/msvc.h',
)

vp9cx_set_ref_srcs = files(
	'vp9cx_set_ref.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_writer.c',
)

vp9cx_set_ref_headers = files(
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_writer.h',
	'../vpx_ports/msvc.h',
)

vp8_multi_resolution_encoder_srcs = files(
	'vp8_multi_resolution_encoder.c',
	'../ivfenc.c',
	'../y4minput.c',
	'../tools_common.c',
	'../video_writer.c',
)

vp9cx_set_ref_headers = files(
	'../ivfenc.h',
	'../y4minput.h',
	'../tools_common.h',
	'../video_common.h',
	'../video_writer.h',
	'../vpx_ports/msvc.h',
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
