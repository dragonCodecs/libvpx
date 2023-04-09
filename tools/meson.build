tiny_ssim_srcs = files(
	'tiny_ssim.c',
	'../y4minput.c',
	'../vpx/src/vpx_image.c',
	'../vpx_mem/vpx_mem.c',
)

tiny_ssim_headers = files(
	'../vpx/vpx_integer.h',
	'../y4minput.h',
	'../vpx/vpx_codec.h',
	'../vpx_mem/vpx_mem.h',
	'../vpx_dsp/ssim.h',
	'../vpx_scale/yv12config.h',
	'../vpx_ports/mem.h',
	'../vpx_mem/include/vpx_mem_intrnl.h',
)

# Generate SSIM/PSNR from raw .yuv files
tiny_ssim = executable(
	'tiny_ssim',
	tiny_ssim_srcs,
	extra_files: tiny_ssim_headers,
	dependencies: libvpx_dep,
	install: get_option('install_bins'),
)

# #
# # Documentation Rules
# #
# %.dox: %.c
# 	@echo "    [DOXY] $@"
# 	@mkdir -p $(dir $@)
# 	@echo "/*!\page tools_$(@F:.dox=) $(@F:.dox=)" > $@
# 	@echo "   \includelineno $(<F)" >> $@
# 	@echo "*/" >> $@

# tools.dox: tools.mk
# 	@echo "    [DOXY] $@"
# 	@echo "/*!\page tools Tools" > $@
# 	@echo "    This SDK includes a number of tools/utilities."\
# 	      "The following tools are included: ">>$@
# 	@$(foreach ex,$(sort $(notdir $(TOOLS:.c=))),\
# 	   echo "     - \subpage tools_$(ex) $($(ex).DESCRIPTION)" >> $@;)
# 	@echo "*/" >> $@

# CLEAN-OBJS += tools.doxy tools.dox $(TOOLS:.c=.dox)
# DOCS-yes += tools.doxy tools.dox
# tools.doxy: tools.dox $(TOOLS:.c=.dox)
# 	@echo "INPUT += $^" > $@
