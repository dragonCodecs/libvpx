# vp9_common.mk

#### --- GENERATED --- ####

dsp_sources = files(
	'prob.c',
	# 'bitwriter.c', # MANUAL
	# 'bitwriter_buffer.c', # MANUAL
	# 'psnr.c', # MANUAL
	# 'bitreader.c', # MANUAL
	# 'bitreader_buffer.c', # MANUAL
	'intrapred.c',
	# 'add_noise.c', # MANUAL
	# 'deblock.c', # MANUAL
	# 'vpx_convolve.c', # MANUAL
	# 'arm/vpx_convolve_copy_neon_asm.asm', # MANUAL
	# 'arm/vpx_convolve8_horiz_filter_type2_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_vert_filter_type2_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_horiz_filter_type1_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_vert_filter_type1_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_avg_horiz_filter_type2_neon.asm' # MANUAL,
	# 'arm/vpx_convolve8_avg_vert_filter_type2_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_avg_horiz_filter_type1_neon.asm', # MANUAL
	# 'arm/vpx_convolve8_avg_vert_filter_type1_neon.asm', # MANUAL
	# 'arm/vpx_convolve_avg_neon_asm.asm', # MANUAL
	# 'arm/vpx_convolve8_neon_asm.c', # MANUAL
	# 'arm/vpx_convolve_copy_neon.c', # MANUAL
	# 'arm/vpx_convolve8_neon.c', # MANUAL
	# 'arm/vpx_convolve_avg_neon.c', # MANUAL
	# 'arm/vpx_convolve_neon.c', # MANUAL
	# 'loopfilter.c', # MANUAL
	# 'arm/loopfilter_16_neon.asm', # MANUAL
	# 'arm/loopfilter_8_neon.asm', # MANUAL
	# 'arm/loopfilter_4_neon.asm', # MANUAL
	'fwd_txfm.c',
	'inv_txfm.c',
	'arm/idct_neon.asm',
	'arm/idct4x4_1_add_neon.asm',
	'arm/idct4x4_add_neon.asm',
	'quantize.c',
	'avg.c',
	'skin_detection.c',
	'sad.c',
	'subtract.c',
	'sum_squares.c',
	'variance.c',
	'vpx_dsp_rtcd.c',
)

dsp_optional_sources = {
	'avx' : files(
		'x86/quantize_avx.c'
	),
	'avx2' : files(
		# 'x86/vpx_subpixel_8t_intrin_avx2.c', # MANUAL
		# 'x86/highbd_convolve_avx2.c', # MANUAL
		# 'x86/loopfilter_avx2.c', # MANUAL
		# 'x86/fwd_txfm_avx2.c', # MANUAL
		'x86/quantize_avx2.c',
		'x86/highbd_quantize_intrin_avx2.c',
		'x86/avg_intrin_avx2.c',
		'x86/sad4d_avx2.c',
		'x86/sad_avx2.c',
		'x86/subtract_avx2.c',
		'x86/highbd_sad4d_avx2.c',
		'x86/highbd_sad_avx2.c',
		'x86/variance_avx2.c'
	),
	'avx512' : files(
		'x86/sad4d_avx512.c'
	),
	'dspr2' : files(
		'mips/intrapred4_dspr2.c',
		'mips/intrapred8_dspr2.c',
		'mips/intrapred16_dspr2.c',
		'mips/common_dspr2.c',
		# 'mips/convolve2_avg_dspr2.c', # MANUAL
		# 'mips/convolve2_avg_horiz_dspr2.c', # MANUAL
		# 'mips/convolve2_dspr2.c', # MANUAL
		# 'mips/convolve2_horiz_dspr2.c', # MANUAL
		# 'mips/convolve2_vert_dspr2.c', # MANUAL
		# 'mips/convolve8_avg_dspr2.c', # MANUAL
		# 'mips/convolve8_avg_horiz_dspr2.c', # MANUAL
		# 'mips/convolve8_dspr2.c', # MANUAL
		# 'mips/convolve8_horiz_dspr2.c', # MANUAL
		# 'mips/convolve8_vert_dspr2.c', # MANUAL
		# 'mips/loopfilter_filters_dspr2.c', # MANUAL
		# 'mips/loopfilter_mb_dspr2.c', # MANUAL
		# 'mips/loopfilter_mb_horiz_dspr2.c', # MANUAL
		# 'mips/loopfilter_mb_vert_dspr2.c', # MANUAL
		'mips/itrans4_dspr2.c',
		'mips/itrans8_dspr2.c',
		'mips/itrans16_dspr2.c',
		'mips/itrans32_dspr2.c',
		'mips/itrans32_cols_dspr2.c'
	),
	'internal_stats' : files(
		# 'ssim.c', # MANUAL
		# 'psnrhvs.c', # MANUAL
		# 'fastssim.c' # MANUAL
	),
	'lsx' : files(
		'loongarch/intrapred_lsx.c',
		# 'loongarch/vpx_convolve8_avg_horiz_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_avg_vert_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_horiz_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_vert_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve8_avg_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve_avg_lsx.c', # MANUAL
		# 'loongarch/vpx_convolve_copy_lsx.c', # MANUAL
		# 'loongarch/loopfilter_16_lsx.c', # MANUAL
		# 'loongarch/loopfilter_8_lsx.c', # MANUAL
		# 'loongarch/loopfilter_4_lsx.c', # MANUAL
		# 'loongarch/fwd_txfm_lsx.c', # MANUAL
		# 'loongarch/fwd_dct32x32_lsx.c', # MANUAL
		'loongarch/idct32x32_lsx.c',
		'loongarch/quantize_lsx.c',
		'loongarch/avg_lsx.c',
		'loongarch/sad_lsx.c',
		'loongarch/subtract_lsx.c',
		'loongarch/variance_lsx.c',
		'loongarch/sub_pixel_variance_lsx.c',
		'loongarch/avg_pred_lsx.c'
	),
	'mmi' : files(
		# 'mips/vpx_convolve8_mmi.c',
		'mips/sad_mmi.c',
		'mips/subtract_mmi.c',
		'mips/variance_mmi.c'
	),
	'msa' : files(
		# 'mips/add_noise_msa.c', # MANUAL
		# 'mips/deblock_msa.c', # MANUAL
		'mips/intrapred_msa.c',
		# 'mips/vpx_convolve8_avg_horiz_msa.c', # MANUAL
		# 'mips/vpx_convolve8_avg_msa.c', # MANUAL
		# 'mips/vpx_convolve8_avg_vert_msa.c', # MANUAL
		# 'mips/vpx_convolve8_horiz_msa.c', # MANUAL
		# 'mips/vpx_convolve8_msa.c', # MANUAL
		# 'mips/vpx_convolve8_vert_msa.c', # MANUAL
		# 'mips/vpx_convolve_avg_msa.c', # MANUAL
		# 'mips/vpx_convolve_copy_msa.c', # MANUAL
		# 'mips/loopfilter_16_msa.c', # MANUAL
		# 'mips/loopfilter_8_msa.c', # MANUAL
		# 'mips/loopfilter_4_msa.c', # MANUAL
		'mips/fwd_txfm_msa.c',
		# 'mips/fwd_dct32x32_msa.c', # MANUAL
		'mips/idct4x4_msa.c',
		'mips/idct8x8_msa.c',
		'mips/idct16x16_msa.c',
		'mips/idct32x32_msa.c',
		'mips/avg_msa.c',
		'mips/sum_squares_msa.c',
		'mips/sad_msa.c',
		'mips/subtract_msa.c',
		'mips/variance_msa.c',
		'mips/sub_pixel_variance_msa.c'
	),
	'neon' : files(
		# 'arm/highbd_intrapred_neon.c', # MANUAL
		# 'arm/deblock_neon.c', # MANUAL
		'arm/intrapred_neon.c',
		# 'arm/highbd_vpx_convolve_copy_neon.c', # MANUAL
		# 'arm/highbd_vpx_convolve_avg_neon.c', # MANUAL
		# 'arm/highbd_vpx_convolve8_neon.c', # MANUAL
		# 'arm/highbd_vpx_convolve_neon.c', # MANUAL
		# 'arm/vpx_scaled_convolve8_neon.c', # MANUAL
		# 'arm/loopfilter_neon.c', # MANUAL
		# 'arm/highbd_loopfilter_neon.c', # MANUAL
		# 'arm/fdct4x4_neon.c', # MANUAL
		# 'arm/fdct8x8_neon.c', # MANUAL
		# 'arm/fdct16x16_neon.c', # MANUAL
		# 'arm/fdct32x32_neon.c', # MANUAL
		# 'arm/fdct_partial_neon.c', # MANUAL
		'arm/highbd_idct4x4_add_neon.c',
		'arm/highbd_idct8x8_add_neon.c',
		'arm/highbd_idct16x16_add_neon.c',
		'arm/highbd_idct32x32_add_neon.c',
		'arm/highbd_idct32x32_34_add_neon.c',
		'arm/highbd_idct32x32_135_add_neon.c',
		'arm/highbd_idct32x32_1024_add_neon.c',
		'arm/idct4x4_1_add_neon.c',
		'arm/idct4x4_add_neon.c',
		'arm/idct8x8_1_add_neon.c',
		'arm/idct8x8_add_neon.c',
		'arm/idct16x16_1_add_neon.c',
		'arm/idct16x16_add_neon.c',
		'arm/idct32x32_1_add_neon.c',
		'arm/idct32x32_34_add_neon.c',
		'arm/idct32x32_135_add_neon.c',
		'arm/idct32x32_add_neon.c',
		'arm/quantize_neon.c',
		'arm/highbd_quantize_neon.c',
		'arm/avg_neon.c',
		'arm/hadamard_neon.c',
		'arm/sum_squares_neon.c',
		'arm/sad4d_neon.c',
		'arm/sad_neon.c',
		'arm/subtract_neon.c',
		'arm/highbd_sad_neon.c',
		'arm/avg_pred_neon.c',
		'arm/subpel_variance_neon.c',
		'arm/variance_neon.c',
		'arm/highbd_variance_neon.c'
	),
	'neon_asm' : files(
		'arm/intrapred_neon_asm.asm',
		'arm/save_reg_neon.asm'
	),
	'sse2' : files(
		# 'x86/highbd_intrapred_intrin_sse2.c', # MANUAL
		# 'x86/post_proc_sse2.c', # MANUAL
		# 'x86/vpx_subpixel_4t_intrin_sse2.c', # MANUAL
		# 'x86/loopfilter_sse2.c', # MANUAL
		# 'x86/highbd_loopfilter_sse2.c', # MANUAL
		# 'x86/fwd_txfm_sse2.c', # MANUAL
		'x86/inv_txfm_sse2.c',
		'x86/highbd_idct4x4_add_sse2.c',
		'x86/highbd_idct8x8_add_sse2.c',
		'x86/highbd_idct16x16_add_sse2.c',
		'x86/highbd_idct32x32_add_sse2.c',
		'x86/quantize_sse2.c',
		'x86/highbd_quantize_intrin_sse2.c',
		'x86/avg_intrin_sse2.c',
		'x86/sum_squares_sse2.c',
		'x86/avg_pred_sse2.c',
		'x86/highbd_variance_sse2.c'
	),
	'sse4_1' : files(
		'x86/highbd_idct4x4_add_sse4.c',
		'x86/highbd_idct8x8_add_sse4.c',
		'x86/highbd_idct16x16_add_sse4.c',
		'x86/highbd_idct32x32_add_sse4.c'
	),
	'ssse3' : files(
		# 'x86/highbd_intrapred_intrin_ssse3.c', # MANUAL
		'x86/vpx_subpixel_8t_intrin_ssse3.c',
		'x86/inv_txfm_ssse3.c',
		'x86/quantize_ssse3.c'
	),
	'vsx' : files(
		'ppc/intrapred_vsx.c',
		# 'ppc/deblock_vsx.c', # MANUAL
		# 'ppc/vpx_convolve_vsx.c', # MANUAL
		# 'ppc/fdct32x32_vsx.c', # MANUAl
		'ppc/inv_txfm_vsx.c',
		'ppc/quantize_vsx.c',
		'ppc/hadamard_vsx.c',
		'ppc/sad_vsx.c',
		'ppc/subtract_vsx.c',
		'ppc/variance_vsx.c'
	),
}

dsp_headers_sources = files(
	'vpx_dsp_common.h',
	'prob.h',
	# 'bitwriter.h', # MANUAL
	# 'bitwriter_buffer.h', # MANUAL
	# 'psnr.h', # MANUAL
	# 'bitreader.h', # MANUAL
	# 'bitreader_buffer.h', # MANUAL
	# 'postproc.h', # MANUAL
	'vpx_filter.h',
	# 'vpx_convolve.h', # MANUAL
	# 'arm/vpx_convolve8_neon_asm.h', # MANUAL
	'txfm_common.h',
	# 'fwd_txfm.h',
	'inv_txfm.h',
	'quantize.h',
	'skin_detection.h',
	'variance.h',
)

dsp_headers_optional_sources = {
	'avx2' : files(
		'x86/bitdepth_conversion_avx2.h',
		# 'x86/convolve_avx2.h', # MANUAL
		# 'x86/fwd_dct32x32_impl_avx2.h' # MANUAL
	),
	'dspr2' : files(
		'mips/common_dspr2.h',
		# 'mips/convolve_common_dspr2.h', # MANUAL
		# 'mips/loopfilter_filters_dspr2.h', # MANUAL
		# 'mips/loopfilter_macros_dspr2.h', # MANUAL
		# 'mips/loopfilter_masks_dspr2.h', # MANUAL
		'mips/inv_txfm_dspr2.h'
	),
	'internal_stats' : files(
		# 'ssim.h' # MANUAL
	),
	'lsx' : files(
		# 'loongarch/vpx_convolve_lsx.h', # MANUAL
		# 'loongarch/loopfilter_lsx.h', # MANUAL
		'loongarch/txfm_macros_lsx.h',
		# 'loongarch/fwd_txfm_lsx.h', # MANUAL
		'loongarch/variance_lsx.h',
		'loongarch/bitdepth_conversion_lsx.h'
	),
	'msa' : files(
		'mips/macros_msa.h',
		# 'mips/vpx_convolve_msa.h', # MANUAL
		# 'mips/loopfilter_msa.h', # MANUAL
		'mips/txfm_macros_msa.h',
		# 'mips/fwd_txfm_msa.h', # MANUAL
		'mips/inv_txfm_msa.h'
	),
	'neon' : files(
		'arm/highbd_idct_neon.h',
		'arm/idct_neon.h',
		'arm/mem_neon.h',
		'arm/sum_neon.h',
		'arm/transpose_neon.h',
		'arm/vpx_convolve8_neon.h'
	),
	'sse2' : files(
		'x86/bitdepth_conversion_sse2.h',
		# 'x86/convolve_sse2.h', # MANUAL
		'x86/txfm_common_sse2.h',
		# 'x86/fwd_txfm_sse2.h', # MANUAL
		# 'x86/fwd_txfm_impl_sse2.h', # MANUAL
		# 'x86/fwd_dct32x32_impl_sse2.h', # MANUAL
		'x86/inv_txfm_sse2.h',
		'x86/highbd_inv_txfm_sse2.h',
		'x86/quantize_sse2.h',
		'x86/mem_sse2.h',
		'x86/transpose_sse2.h'
	),
	'sse4_1' : files(
		'x86/highbd_inv_txfm_sse4.h'
	),
	'ssse3' : files(
		# 'x86/convolve_ssse3.h', # MANUAL
		'x86/inv_txfm_ssse3.h',
		'x86/quantize_ssse3.h'
	),
	'vsx' : files(
		'ppc/types_vsx.h',
		'ppc/txfm_common_vsx.h',
		'ppc/transpose_vsx.h',
		'ppc/bitdepth_conversion_vsx.h'
	),
}

dsp_asm_optional_sources = {
	'sse2' : files(
		'x86/intrapred_sse2.asm',
		# 'x86/highbd_intrapred_sse2.asm', # MANUAL
		# 'x86/add_noise_sse2.asm', # MANUAL
		# 'x86/deblock_sse2.asm', # MANUAL
		# 'x86/vpx_subpixel_8t_sse2.asm', # MANUAL
		# 'x86/vpx_subpixel_bilinear_sse2.asm', # MANUAL
		# 'x86/vpx_high_subpixel_8t_sse2.asm', # MANUAL
		# 'x86/vpx_high_subpixel_bilinear_sse2.asm', # MANUAL
		# 'x86/vpx_convolve_copy_sse2.asm', # MANUAL
		'x86/inv_wht_sse2.asm',
		'x86/sad4d_sse2.asm',
		'x86/sad_sse2.asm',
		'x86/subtract_sse2.asm',
		'x86/highbd_sad4d_sse2.asm',
		'x86/highbd_sad_sse2.asm',
		'x86/ssim_opt_x86_64.asm',
		'x86/highbd_variance_impl_sse2.asm',
		'x86/highbd_subpel_variance_impl_sse2.asm'
	),
	'ssse3' : files(
		'x86/intrapred_ssse3.asm',
		# 'x86/vpx_subpixel_8t_ssse3.asm', # MANUAL
		# 'x86/vpx_subpixel_bilinear_ssse3.asm', # MANUAL
		# 'x86/fwd_txfm_ssse3_x86_64.asm', # MANUAL
		'x86/avg_ssse3_x86_64.asm'
	),
}


if features.get('encoders', false) # MANUAL
	dsp_sources += files(
		'bitwriter.c',
		'bitwriter_buffer.c',
		'psnr.c',
	)

	dsp_headers_sources += files(
		'bitwriter.h',
		'bitwriter_buffer.h',
		'psnr.h',
	)

	dsp_optional_sources += {
		'internal_stats' : dsp_optional_sources['internal_stats'] + files(
			'ssim.c',
			'psnrhvs.c',
			'fastssim.c'
		),
	}

	dsp_headers_optional_sources += {
		'internal_stats' : dsp_headers_optional_sources['internal_stats'] + files(
			'ssim.h'
		),
	}
endif

if features.get('encoders', false) # MANUAL
	dsp_sources += files(
		'bitreader.c',
		'bitreader_buffer.c',
	)

	dsp_headers_sources += files(
		'bitreader.h',
		'bitreader_buffer.h',
	)
endif

# intra predictions
if features.get('vp9_highbitdepth', false) # MANUAL
	dsp_asm_optional_sources += {
		'sse2' : dsp_asm_optional_sources['sse2'] + files(
			'x86/highbd_intrapred_sse2.asm',
		)
	}

	dsp_optional_sources += {
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/highbd_intrapred_intrin_sse2.c',
		),
		'ssse3' : dsp_optional_sources['ssse3'] + files(
			'x86/highbd_intrapred_intrin_ssse3.c',
		),
		'neon' : dsp_optional_sources['ssse3'] + files(
			'arm/highbd_intrapred_neon.c',
		),
	}
endif

# intra predictions
if not features.get('postproc', false) and not features.get('vp9_postproc', false) # MANUAL
	dsp_sources += files(
		'add_noise.c',
		'deblock.c',
	)

	dsp_headers_sources += files(
		'postproc.h',
	)

	dsp_optional_sources += {
		'msa' : dsp_optional_sources['msa'] + files(
			'mips/add_noise_msa.c',
			'mips/deblock_msa.c',
		),
		'neon' : dsp_optional_sources['msa'] + files(
			'arm/deblock_neon.c',
		),
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/post_proc_sse2.c',
		),
		'vsx' : dsp_optional_sources['vsx'] + files(
			'ppc/deblock_vsx.c',
		),
	}

	dsp_asm_optional_sources += {
		'sse2' : dsp_asm_optional_sources['sse2'] + files(
			'x86/add_noise_sse2.asm',
			'x86/deblock_sse2.asm',
		),
		'ssse3': files(
			'x86/vpx_subpixel_8t_ssse3.asm',
			'x86/vpx_subpixel_bilinear_ssse3.asm',
		)
	}
endif

dsp_asm_optional_sources += {
	'neon_asm' : asm_transformer.process(
		files(
			'arm/intrapred_neon_asm.asm',
		)
	)
}

if features.get('vp9', false)
	# interpolation filters

	dsp_sources += files(
		'vpx_convolve.c',
		# loop filters
		'loopfilter.c',
	)

	dsp_headers_sources += files(
		'vpx_convolve.h',
	)

	dsp_headers_optional_sources += {
		'x86' : files(
			'x86/convolve.h',
		),
		'x86_64' : files(
			'x86/convolve.h',
		),
		'sse2' : dsp_headers_optional_sources['sse2'] + files(
			'x86/convolve_sse2.h',
		),
		'ssse3' : dsp_headers_optional_sources['ssse3'] + files(
			'x86/convolve_ssse3.h',
		),
		'avx2' : dsp_headers_optional_sources['avx2'] + files(
			'x86/convolve_avx2.h',
		),
		'msa' : dsp_headers_optional_sources['msa'] + files(
			# common (msa)
			'mips/vpx_convolve_msa.h',
			# loop filters
			'mips/loopfilter_msa.h',
		),
		'dspr2' : dsp_headers_optional_sources['dspr2'] + files(
			# common (dspr2)
			'convolve_common_dspr2.h',
			# loop filters
			'mips/loopfilter_filters_dspr2.h',
			'mips/loopfilter_macros_dspr2.h',
			'mips/loopfilter_masks_dspr2.h',
		),
		'lsx' : dsp_headers_optional_sources['lsx'] + files(
			# common (lsx)
			'loongarch/vpx_convolve_lsx.h',
			# loop filters
			'loongarch/loopfilter_lsx.h',
		)
	}

	dsp_asm_optional_sources += {
		'sse2' : dsp_asm_optional_sources['sse2'] + files(
			'x86/vpx_subpixel_8t_sse2.asm',
			'x86/vpx_subpixel_bilinear_sse2.asm',
			'x86/vpx_convolve_copy_sse2.asm',
		)
	}

	dsp_optional_sources += {
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/vpx_subpixel_4t_intrin_sse2.c',
			# loop filters
			'x86/loopfilter_sse2.c',
		),
		'avx2' : dsp_optional_sources['avx2'] + files(
			'x86/vpx_subpixel_8t_intrin_avx2.c',
			# loop filters
			'x86/loopfilter_avx2.c',
		),
		'ssse3' : dsp_optional_sources['ssse3'] + files(
			'x86/vpx_subpixel_8t_intrin_ssse3.c',
		),
		'neon' : dsp_optional_sources['neon'] + files(
			'arm/vpx_scaled_convolve8_neon.c',
		),
		'msa' : dsp_optional_sources['msa'] + files(
			# common (msa)
			'mips/vpx_convolve8_avg_horiz_msa.c',
			'mips/vpx_convolve8_avg_msa.c',
			'mips/vpx_convolve8_avg_vert_msa.c',
			'mips/vpx_convolve8_horiz_msa.c',
			'mips/vpx_convolve8_msa.c',
			'mips/vpx_convolve8_vert_msa.c',
			'mips/vpx_convolve_avg_msa.c',
			'mips/vpx_convolve_copy_msa.c',
			# loop filters
			'mips/loopfilter_16_msa.c',
			'mips/loopfilter_8_msa.c',
			'mips/loopfilter_4_msa.c',
		),
		'mmi' : dsp_optional_sources['mmi'] + files(
			'mips/vpx_convolve8_mmi.c',
		),
		'dspr2' : dsp_optional_sources['dspr2'] + files(
			# common (dspr2)
			'mips/convolve2_avg_dspr2.c',
			'mips/convolve2_avg_horiz_dspr2.c',
			'mips/convolve2_dspr2.c',
			'mips/convolve2_horiz_dspr2.c',
			'mips/convolve2_vert_dspr2.c',
			'mips/convolve8_avg_dspr2.c',
			'mips/convolve8_avg_horiz_dspr2.c',
			'mips/convolve8_dspr2.c',
			'mips/convolve8_horiz_dspr2.c',
			'mips/convolve8_vert_dspr2.c',
			# loop filters
			'mips/loopfilter_filters_dspr2.c',
			'mips/loopfilter_mb_dspr2.c',
			'mips/loopfilter_mb_horiz_dspr2.c',
			'mips/loopfilter_mb_vert_dspr2.c',
		),
		'vpx' : dsp_optional_sources['vpx'] + files(
			'ppc/vpx_convolve_vsx.c',
		)
		'lsx' : dsp_optional_sources['lsx'] + files(
			# common (lsx)
			'loongarch/vpx_convolve8_avg_horiz_lsx.c',
			'loongarch/vpx_convolve8_avg_vert_lsx.c',
			'loongarch/vpx_convolve8_horiz_lsx.c',
			'loongarch/vpx_convolve8_vert_lsx.c',
			'loongarch/vpx_convolve8_lsx.c',
			'loongarch/vpx_convolve8_avg_lsx.c',
			'loongarch/vpx_convolve_avg_lsx.c',
			'loongarch/vpx_convolve_copy_lsx.c',
			# loop filters
			'loongarch/loopfilter_16_lsx.c',
			'loongarch/loopfilter_8_lsx.c',
			'loongarch/loopfilter_4_lsx.c',
		)
	}

	if features.get('vp9_highbitdepth', false)
		dsp_asm_optional_sources += {
			'sse2' : dsp_asm_optional_sources['sse2'] + files(
				'x86/vpx_high_subpixel_8t_sse2.asm',
				'x86/vpx_high_subpixel_bilinear_sse2.asm',
			)
		}

		dsp_optional_sources += {
			'avx2' : dsp_optional_sources['avx2'] + files(
				'x86/highbd_convolve_avx2.c'
			),
			'sse2' : dsp_optional_sources['sse2'] + files(
				# loop filters
				'x86/highbd_loopfilter_sse2.c'
			)
			'neon' : dsp_optional_sources['neon'] + files(
				'arm/highbd_vpx_convolve_copy_neon.c',
				'arm/highbd_vpx_convolve_avg_neon.c',
				'arm/highbd_vpx_convolve8_neon.c',
				'arm/highbd_vpx_convolve_neon.c',
				# loop filters
				'arm/highbd_loopfilter_neon.c',
			)
		}
	endif

	if features.get('neon_asm', false)
		dsp_sources += transformer.process(
			files(
				'arm/vpx_convolve_copy_neon_asm.asm',
				'arm/vpx_convolve8_horiz_filter_type2_neon.asm',
				'arm/vpx_convolve8_vert_filter_type2_neon.asm',
				'arm/vpx_convolve8_horiz_filter_type1_neon.asm',
				'arm/vpx_convolve8_vert_filter_type1_neon.asm',
				'arm/vpx_convolve8_avg_horiz_filter_type2_neon.asm',
				'arm/vpx_convolve8_avg_vert_filter_type2_neon.asm',
				'arm/vpx_convolve8_avg_horiz_filter_type1_neon.asm',
				'arm/vpx_convolve8_avg_vert_filter_type1_neon.asm',
				'arm/vpx_convolve_avg_neon_asm.asm',
				# loop filters
				'arm/loopfilter_16_neon.asm',
				'arm/loopfilter_8_neon.asm',
				'arm/loopfilter_4_neon.asm',
			)
		)

		dsp_sources += files(
			'arm/vpx_convolve8_neon_asm.c',
			'arm/vpx_convolve_neon.c',
		)

		dsp_headers_sources += files(
			'arm/vpx_convolve8_neon_asm.h',
		)
	elif features.get('neon', false)
		dsp_sources += files(
			'arm/vpx_convolve_copy_neon.c',
			'arm/vpx_convolve8_neon.c',
			'arm/vpx_convolve_avg_neon.c',
			'arm/vpx_convolve_neon.c',
			# loop filters
			'arm/loopfilter_neon.c',
		)
	endif
endif

# forward transform
if features.get('vp9_encoder', false)
	dsp_sources += files(
		'fwd_txfm.c',
	)

	dsp_headers_sources += files(
		'fwd_txfm.h',
	)

	dsp_headers_optional_sources += {
		'sse2' : dsp_headers_optional_sources['sse2'] + files(
			'x86/fwd_txfm_sse2.h',
			'x86/fwd_txfm_impl_sse2.h',
			'x86/fwd_dct32x32_impl_sse2.h',
		),
		'avx2' : dsp_headers_optional_sources['avx2'] + files(
			'x86/fwd_dct32x32_impl_avx2.h'
		),
		'msa' : dsp_headers_optional_sources['msa'] + files(
			'mips/fwd_txfm_msa.h'
		),
		'lsx' : dsp_headers_optional_sources['lsx'] + files(
			'loongarch/fwd_txfm_lsx.h'
		)
	}

	dsp_optional_sources += {
		'sse2' : dsp_optional_sources['sse2'] + files(
			'x86/fwd_txfm_sse2.c',
		),
		'neon': dsp_optional_sources['neon'] + files(
			'arm/fdct4x4_neon.c',
			'arm/fdct8x8_neon.c',
			'arm/fdct16x16_neon.c',
			'arm/fdct32x32_neon.c',
			'arm/fdct_partial_neon.c',
		),
		'msa' : dsp_headers_optional_sources['msa'] + files(
			'mips/fwd_txfm_msa.c',
		),
		'lsx' : dsp_headers_optional_sources['lsx'] + files(
			'loongarch/fwd_txfm_lsx.c',
		),
		'vsx' : dsp_headers_optional_sources['vsx'] + files(
			'ppc/fdct32x32_vsx.c',
		),
	}

	if features.get('x86_64', false)
		dsp_asm_optional_sources += {
			'ssse3' : dsp_asm_optional_sources['ssse3'] + files(
				'x86/fwd_txfm_ssse3_x86_64.asm',
			)
		}
	endif

	if not features.get('vp9_highbitdepth', false)
		dsp_optional_sources += {
			'avx2' : dsp_optional_sources['avx2'] + files(
				'x86/fwd_txfm_avx2.c'
			),
			'msa' : dsp_optional_sources['msa'] + files(
				# loop filters
				'mips/fwd_dct32x32_msa.c'
			)
			'lsx' : dsp_optional_sources['lsx'] + files(
				# loop filters
				'loongarch/fwd_dct32x32_lsx.c',
			)
		}
	endif
endif

#### --- END GENERATED --- ####

optional_sources = get_variable('dsp_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		dsp_sources += comp_sources
	endif
endforeach

codec_srcs += dsp_sources

optional_sources = get_variable('dsp_asm_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		dsp_sources += comp_sources
	endif
endforeach

codec_srcs += dsp_sources

vpx_dsp_rtcd_h = custom_target(
	'vpx_dsp_rtcd.h',
	command: [rtcd_exe, '--arch=@0@'.format(tgt_isa), '--sym=@0@'.format('vpx_dsp_rtcd'), '--config=@INPUT@'] + rtcd_options,
	depend_files: files('vpx_dsp/vpx_dsp_rtcd_defs.pl'),
	input: vpx_config_h,
	output: 'vp9_rtcd.h',
	capture: true,
)

codec_srcs += vpx_dsp_rtcd_h
