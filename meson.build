project(
	'libvpx',
	'c', 'cpp',
	version: '1.3.1',
	default_options: [
		# Enforce c89 for c files. Don't be too strict about it though. Allow
		# gnu extensions like "//" for comments.
		'c_std=gnu89',
		'cpp_std=gnu++11',
		'warning_level=2',
		'b_bitcode=true',
	]
)

configuration = configuration_data()
features = configuration_data()

c_args = []
cpp_args = []
asm_args = []
tune_cflags = ''
rtcd_options = []
link_args = []
extra_libs = []

libyuv_cpp_args = []

#######################
###### configure ######
#######################

# all_targets is a list of all targets that can be configured
# note that these should be in dependency order for now.
all_targets = [
	'libs',
	'examples',
	'tools',
	'docs',
]

# all targets available are enabled, by default.
foreach t : all_targets
	features.set(t, true)
endif

# we don't use diff in Meson.

perl_exe = find_program('perl', required: true)

doxygen_exe = find_program('doxygen', required: true)

if doxygen_exe.found()
	doxygen_version = run_command(
		doxygen_exe,
		'--version',
		check: true,
		capture: true
	)

	if doxygen_version.version_compare('>= 2.0.0') or doxygen_version.version_compare('>= 1.6.0') or doxygen_version.version_compare('>= 1.5.5.3')
		features.set('doxygen', true)
	endif
endif

# We don't disable codecs when their source directory does not exist
# because it's Git and they all exist.

# install everything except the sources, by default. sources will have
# to be enabled when doing dist builds, since that's no longer a common
# case.
if features.get('doxygen', false)
	features.set('install_docs', true)
endif
features.set('install_bins', true)
features.set('install_libs', true)

# This feature is governed by Meson
features.set('static', get_option('default_library') == 'static')
features.set('optimizations', true)
# This feature is governed by Meson
features.set('dependency_tracking', true)
features.set('spatial_resampling', true)
features.set('multithread', true)
features.set('os_support', true)
features.set('temporal_denoising', true)

CODECS = [
	'vp8_encoder',
	'vp8_decoder',
	'vp9_encoder',
	'vp9_decoder',
]

CODEC_FAMILIES = [
	'vp8',
	'vp9',
]

ARCH_LIST = [
	'arm',
	'mips',
	'x86',
	'x86_64',
	'ppc',
	'loongarch',
]

ARCH_EXT_LIST_X86 = [
	'mmx',
	'sse',
	'sse2',
	'sse3',
	'ssse3',
	'sse4_1',
	'avx',
	'avx2',
	'avx512',
]

ARCH_EXT_LIST_LOONGSON = [
	'mmi',
	'lsx',
	'lasx',
]

ARCH_EXT_LIST = [
	'neon',
	'neon_asm',

	'mips32',
	'dspr2',
	'msa',
	'mips64',
] + ARCH_EXT_LIST_X86 + [
	'vsx',
] + ARCH_EXT_LIST_LOONGSON

HAVE_LIST = ARCH_EXT_LIST + [
	'vpx_ports',
	'pthread_h',
	'unistd_h',
]

EXPERIMENT_LIST = [
	'fp_mb_stats',
	'emulate_hardware',
	'non_greedy_mv',
	'rate_ctrl',
	'collect_component_timing',
]

CONFIG_LIST = [
	'dependency_tracking',
	'external_build',
	'install_docs',
	'install_bins',
	'install_libs',
	'install_srcs',
	'debug',
	'gprof',
	'gcov',
	'rvct',
	'gcc',
	'msvs',
	'pic',
	'big_endian',

	'codec_srcs',
	'debug_libs',

	'dequant_tokens',
	'dc_recon',
	'runtime_cpu_detect',
	'postproc',
	'vp9_postproc',
	'multithread',
	'internal_stats',
] + CODECS + CODEC_FAMILIES + [
	'encoders',
	'decoders',
	'static_msvcrt',
	'spatial_resampling',
	'realtime_only',
	'onthefly_bitpacking',
	'error_concealment',
	'shared',
	'static',
	'small',
	'postproc_visualizer',
	'os_support',
	'unit_tests',
	'webm_io',
	'libyuv',
	'decode_perf_tests',,
	'encode_perf_tests',
	'multi_res_encoding',
	'temporal_denoising',
	'vp9_temporal_denoising',
	'coefficient_range_checking',
	'vp9_highbitdepth',
	'better_hw_compatibility',
	'experimental',
	'size_limit',
	'always_adjust_bpm',
	'bitstream_debug',
	'mismatch_debug',
] + EXPERIMENT_LIST

# this is the list of toggleable options in meson_options.txt
# EXCEPT for a couple that I've separated because they're
# derived from the Meson configuration.
CMDLINE_SELECT = [
	# 'dependency_tracking', # Meson enabled by default (see above)
	# 'external_build', # Meson has no idea of toolchains
	# 'extra_warnings', # Meson handled
	# 'werror', # Meson handled
	'install_docs',
	'install_bins',
	'install_libs',
	'install_srcs',
	# 'debug', # Meson handled
	'gprof',
	# 'gcov', # Meson handled
	'pic',
	# 'optimizations', # Meson handled
	# 'ccache', # Meson handled
	'runtime_cpu_detect',
	'thumb',

	'libs',
	'examples',
	'tools',
	'docs',
	# 'libc', # Meson has no idea of libc
	# 'as', # Meson handled
	# 'size_limit', # Meson handled
	'codec_srcs',
	'debug_libs',

	'dequant_tokens',
	'dc_recon',
	'postproc',
	'vp9_postproc',
	'multithread', # Meson handled
	'internal_stats', # Meson handled
] + CODECS + CODECS_FAMILIES + [
	'static_msvcrt',
	'spatial_resampling',
	'realtime_only',
	'onthefly_bitpacking',
	'error_concealment',
	'shared',
	'static',
	'small',
	'postproc_visualizer',
	'unit_tests',
	'webm_io',
	'libyuv',
	'decode_perf_tests',
	'encode_perf_tests',
	'multi_res_encoding',
	'temporal_denoising',
	'vp9_temporal_denoising',
	'consistent_recode',
	'coefficient_range_checking',
	'better_hw_compatibility',
	'vp9_highbitdepth',
	'experimental',
	'always_adjust_bpm',
	'bitstream_debug',
	'mismatch_debug',
]

# process #


# process_cmdline #

features.set('extra_warnings', get_option('warning_level') >= 2)
features.set('werror', get_option('werror'))
features.set('debug', ['debug', 'debugoptimized'].contains(get_option('buildtype')))
features.set('gcov', get_option('b_coverage'))
# Warning: we drop Yasm compatibility because Meson
# provides NASM support by default
features.set('as', add_language('nasm'))
size_limit_value = get_option('size_limit', '').split('x')
if size_limit_value.length() != 2
	error('Invalid size-limit: must be of the form WIDTHxHEIGHT')
else
	w = size_limit_value[0].to_int()
	h = size_limit_value[1].to_int()
	if w <= 0 or h <= 0
		error('Invalid size-limit: too small.')
	elif w >= 65536 or h >= 65536
		error('Invalid size-limit: too big.')
	else
		c_args += [
			'-DDECODE_WIDTH_LIMIT=@0@'.format(w),
			'-DDECODE_HEIGHT_LIMIT=@0@'.format(h),
			language: 'c',
		]
		features.set('size_limit', true)
	endif
endif
tune_cpu = get_option('tune_cpu', '')

enable_features = get_option('enable_features')
disable_features = get_option('disable_features')
force_disable_features = get_option('force_disable_features')
force_enable_features = get_option('force_enable_features')

# Iterates through positional parameters, checks to confirm the parameter has
# not been explicitly (force) disabled, and enables the setting controlled by
# the parameter when the setting is not disabled.
# soft_enable
foreach feature: enable_features
	if not features.has(feature) or feature.get(feature, true)
		if not feature.get(feature, true)
			message('\t enabling @0@'.format(feature))
		endif
		features.set(feature, true)
	endif
endif

# Iterates through positional parameters, checks to confirm the parameter has
# not been explicitly (force) enabled, and disables the setting controlled by
# the parameter when the setting is not enabled.
foreach feature: disable_features
	if not features.has(feature) or not feature.get(feature, false)
		if not feature.get(feature, false)
			message('\t disabling @0@'.format(feature))
		endif
		features.set(feature, false)
	endif
endif

foreach feature: force_disable_features
	message('\t forcibly disabling @0@'.format(feature))
	features.set(feature, false)
endif
foreach feature: force_enable_features
	message('\t forcibly enabling @0@'.format(feature))
	features.set(feature, true)
endif

# TODO: check the rest of cmdlist_set

## post_process_common_cmdline ##

## post_process_cmdline ##

if features.get('coefficient_range_checking', false)
	message('coefficient-range-checking is for decoders only, disabling encoders')
	if not features.has('vp8_encoder') or not feature.get('vp8_encoder', false)
		features.set('vp8_encoder', false)
	endif
	if not features.has('vp9_encoder') or not feature.get('vp9_encoder', false)
		features.set('vp9_encoder', false)
	endif
endif

### process_toolchain ###
#### process_common_toolchain ####

c = meson.get_compiler('c')
cpp = meson.get_compiler('cpp')
asm = disabler()
if add_language('asm')
	asm = meson.get_compiler('as')
endif

tgt_isa = target_machine.cpu_family()
tgt_os = target_machine.system()
if tgt_os == 'windows' or tgt_os == 'cygwin'
	tgt_os == 'windows'
endif

if tgt_isa == 'arm'
	# The __SOFTFP__ macro is unreliable, clang defines it
	# as __SOFT_FP__. The other one matches the configure script better.
	if c.get_define('__ARM_PCS_VFP') != ''
		float_abi = 'hard'
	else
		float_abi = 'softfp'
	endif
endif

# The gcc -dumpmachine bit is used to force -mmacosx-version-min/max
if ['darwin', 'ios', 'tvos'].contains(target_machine.system())
	warning('Apple target detected, please supply the --m(macos|ios)-version-* and -isysroot flags through -Dc_flags or a native file')
endif

# Enable the architecture family
if tgt_isa == 'arm' or tgt_isa == 'aarch64'
	features.set('arm', true)
elif tgt_isa.starts_with('mips')
	features.set('mips', true)
elif tgt_isa.starts_with('ppc')
	features.set('ppc', true)
elif tgt_isa == 'loongarch64'
	features.set('loongarch', true)
	loongson_features = ['lsx', 'lasx']
	foreach feature : loongson_features
		if not features.has(feature) or feature.get(feature, true)
			if not feature.get(feature, true)
				message('\t enabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	endif
endif

# Handle Solaris variants. Solaris 10 needs -lposix4
if tgt_os == 'sunos'
	extra_libs += compiler.find_library('posix4', required: true)
endif

if tgt_isa == 'arm' or tgt_isa == 'aarch64'
	feature = 'neon'
	if not features.has(feature) or feature.get(feature, true)
		if not feature.get(feature, true)
			message('\t enabling @0@'.format(feature))
		endif
		features.set(feature, true)
	endif

	if tgt_isa == 'arm'
		# Only enable neon_asm when neon is also enabled.
		if features.get('neon', false)
			feature = 'neon_asm'
			if not features.has(feature) or feature.get(feature, true)
				if not feature.get(feature, true)
					message('\t enabling @0@'.format(feature))
				endif
				features.set(feature, true)
			endif
		endif
		# If someone tries to force it through, die.
		if not features.get('neon', false) and features.get('neon_asm', false)
			error('Disabling neon while keeping neon-asm is not supported')
		endif
	endif

	if compiler.get_id() == 'gcc' or compiler.get_id() == 'clang'
		tune_cflags = '-mtune=@0@'

		if tgt_isa == 'arm'
			if features.get('neon', false) or features.get('neon_asm', false)
				gcc_flags = ['-mfpu=neon']
				c_args += c.get_supported_arguments(gcc_flags) #-ftree-vectorize
				cpp_args += cpp.get_supported_arguments(gcc_flags)
				asm_args += asm.get_supported_arguments(gcc_flags)
			endif
		endif

		asm_conversion_exe = find_program('build/make/ads2gas.pl', required: true)
		asm_conversion_cmd = [asm_conversion_exe]
		
		if tgt_os == 'windows'
			asm_conversion_cmd += ['-noelf']
			features.set('thumb', true)
		endif

		if features.get('thumb', true)
			asm_conversion_cmd += ['-thumb']
			gcc_flags = ['-mthumb']
			c_args += c.get_supported_arguments(gcc_flags) #-ftree-vectorize
			cpp_args += cpp.get_supported_arguments(gcc_flags)
			gcc_flags = ['-mthumb', '-mimplicit-it=always']
			asm_args += asm.get_supported_arguments(gcc_flags)
		endif
	elif compiler.get_argument_syntax() == 'msvc'
		# A number of ARM-based Windows platforms are constrained by their
		# respective SDKs' limitations. Fortunately, these are all 32-bit ABIs
		# and so can be selected as 'win32'.

		if tgt_isa == 'arm'
			asm_conversion_exe = find_program('build/make/ads2armasm_ms.pl', required: true)
			asm_conversion_cmd = [asm_conversion_exe]
			features.set('multithread', false)
			features.set('unit_tests', false)
			# We drive MSVC through Ninja here, so don't disable examples nor tools.
		else
			# Windows 10 on ARM, on the other hand, has full Windows SDK support
			# for building Win32 ARM64 applications in addition to ARM64
			# Windows Store apps. It is the only 64-bit ARM ABI that
			# Windows supports, so it is the default definition of 'win64'.
			# ARM64 build support officially shipped in Visual Studio 15.9.0.

			# Because the ARM64 Windows SDK's arm_neon.h is ARM32-specific
			# while LLVM's is not, probe its validity.
			if features.get('neon', false)
				if not c.has_header('arm_neon.h')
					features.set('win_arm64_neon_h_workaround', c.has_header('arm64_neon.h'))
				endif
			endif
		endif
	endif

	if tgt_os == 'android'
		message('Assuming standalone build with NDK toolchain.')
		features.set('static', true)
		feature = 'unit_tests'
		if not features.has(feature) or feature.get(feature, true)
			if not feature.get(feature, true)
				message('\t enabling @0@'.format(feature))
			endif
			features.set(feature, true)
		endif
	elif tgt_os == 'darwin'
		# Darwin toolchain and embed-bitcode options are Meson handled.
		asm_conversion_exe = find_program('build/make/ads2gas_apple.pl', required: true)
		asm_conversion_cmd = [asm_conversion_exe]
	elif tgt_os == 'linux'
		features.set('linux', true)
	endif
elif tgt_isa.starts_with('mips')
	tune_cflags = '-mtune=@0@'

	if tune_cpu != ''
		if tune_cpu == 'p5600'
			gcc_flags = ['-mips32r5', '-mload-store-pairs', '-msched-weight', '-mhard-float', '-mfp64']
			c_args += c.get_supported_arguments(gcc_flags)
			cpp_args += cpp.get_supported_arguments(gcc_flags)
			gcc_flags = ['-mips32r5', '-mhard-float', '-mfp64']
			asm_args += asm.get_supported_arguments(gcc_flags)
			gcc_flags = ['-mfp64']
			link_args += c.get_supported_link_arguments(gcc_flags)
		elif ['i6400', 'p6600'].contains(tune_cpu)
			gcc_flags = ['-mips64r6', '-mabi=64', '-msched-weight', '-mload-store-pairs', '-mhard-float', '-mfp64']
			c_args += c.get_supported_arguments(gcc_flags)
			cpp_args += cpp.get_supported_arguments(gcc_flags)
			gcc_flags = ['-mips64r6', '-mabi=64', '-mhard-float', '-mfp64']
			asm_args += asm.get_supported_arguments(gcc_flags)
			gcc_flags = ['-mips64r6', '-mabi=64', '-mfp64']
			link_args += c.get_supported_link_arguments(gcc_flags)
		elif tune_cpu.starts_with('loongson3')
			if c.get_supported_arguments('-march=loongson3a')
				loongson_features = ['mmi', 'msa']
				foreach feature: loongson_features
					if not features.has(feature) or feature.get(feature, true)
						if not feature.get(feature, true)
							message('\t enabling @0@'.format(feature))
						endif
						features.set(feature, true)
					else
						features.set(feature, false)
					endif
				endif
			else
				features.set('mmi', true)
			endif

			if features.get('mmi', false) or features.get('msa', false)
				feature = 'runtime_cpu_detect'
				if not features.has(feature) or feature.get(feature, true)
					if not feature.get(feature, true)
						message('\t enabling @0@'.format(feature))
					endif
					features.set(feature, true)
				endif
			endif

			if enabled msa; then
				# TODO(libyuv:793)
				# The new mips functions in libyuv do not build
				# with the toolchains we currently use for testing.
				feature = 'libyuv'
				if not features.has(feature) or not feature.get(feature, false)
					if not feature.get(feature, false)
						message('\t disabling @0@'.format(feature))
					endif
					features.set(feature, false)
				endif
			endif

			# KPIC is a flag that is valid only for SunCC.
			# As such, we'll use the Meson derived version.
		endif
	endif
elif tgt_isa == 'ppc64' and target_machine.endian() == 'little'
	if features.get('vsx', false)
		rtcd_options += ['--disable-vsx']
	endif

	if tune_cpu.starts_with('power')
		tune_cflags = '-mcpu=@0@'
	endif
elif tgt_isa.starts_with('x86')

elif tgt_isa == 'loongarch64'

elif compiler.get_argument_syntax() != 'msvc'
	features.set('gcc', true)
endif

# Try to enable CPU specific tuning

# process_toolchain

features.set('extra_warnings', get_option('warning_level') >= 2)

if features.get('gcc', false)
	gcc_flags = [
		'-Wdeclaration-after-statement',
		'-Wdisabled-optimization',
		'-Wextra-semi',
		'-Wextra-semi-stmt',
		'-Wfloat-conversion',
		'-Wformat=2',
		'-Wparentheses-equality',
		'-Wpointer-arith',
		'-Wtype-limits',
		'-Wcast-qual',
		'-Wvla',
		'-Wimplicit-function-declaration',
		'-Wmissing-declarations',
		'-Wmissing-prototypes',
		'-Wuninitialized',
		'-Wunreachable-code-loop-increment',
		'-Wunused',
	]

	c_args += c.get_supported_arguments(gcc_flags)
	cpp_args += cpp.get_supported_arguments(gcc_flags)

	# gtest does not do well with
	# these flags so add them explicitly to CFLAGS only.
	c_args += c.get_supported_arguments('-Wundef')
	c_args += c.get_supported_arguments('-Wframe-larger-than=52000')

	if (features.get('mips') or inline != '') and features.get('extra_warnings', false)
		c_args += c.get_supported_arguments('-Wno-unused-function')
		cpp_args += cpp.get_supported_arguments('-Wno-unused-function')
	endif

	# Avoid this warning for third_party C++ sources. Some reorganization
	# would be needed to apply this only to test/*.cc.
	c_args += c.get_supported_arguments('-Wshorten-64-to-32')

	# Quiet gcc 6 vs 7 abi warnings:
	# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=77728
	if features.get('arm', false)
		cpp_args += cpp.get_supported_arguments('-Wno-psabi')
	endif

	# Enforce C++11 compatibility.
	cpp_args += cpp.get_supported_arguments(
		'-Wc++14-extensions',
		'-Wc++17-extensions',
		'-Wc++20-extensions',
	)

	# disable some warnings specific to libyuv.
	libyuv_cpp_args += cpp.get_supported_arguments(
		'-Wno-missing-declarations',
		'-Wno-missing-prototypes',
		'-Wno-unused-parameter',
	)
endif

if features.get('icc', false)
	# Warning levels are governed globally by Meson.
	icc_flags = [
		'-Wpointer-arith',
		# ICC has a number of floating point optimizations that we disable
		# in favor of deterministic output WRT to other compilers
		'-fp-model=precise',
	]

	c_args += c.get_supported_arguments(icc_flags)
	cpp_args += cpp.get_supported_arguments(icc_flags)
endif

# Enable extra, harmless warnings. These might provide additional insight
# to what the compiler is doing and why, but in general, but they shouldn't
# be treated as fatal, even if we're treating warnings as errors.
extra_warnings = [
	'-Wdisabled-optimization',
	'-Winline',
	# RVCT is not yet supported by Meson.
	# '--remarks',
]

if features.get('extra_warnings', false)
	c_args += c.get_supported_arguments(extra_warnings)
	if features.get('gcc', false)
		foreach w: extra_warnings
			c_args += c.get_supported_arguments('-Wno-error=@0@'.format(w))
		endforeach
	endif
endif

if features.get('mips')
	features.set('dequant_tokens', true)
	features.set('dc_recon', true)
endif

if features.get('internal_stats')
	features.set('vp9_postproc', true)
endif

# "Enable" the postbuild target if building for visual studio.
# The only relevant bits for Meson is the __inline definition.
if cpp.get_argument_syntax() == 'msvc'
	configuration.set('INLINE', '__inline')
endif

# Other toolchain specific defaults
if target_machine.cpu_family() == 'x86' or target_machine.cpu_family() == 'x86_64'
	# soft_enable
	if not features.get('postproc', true)
		features.set('postproc', true)
	endif
endif

if features.get('postproc_visualizer', false)
	# TODO: read list of features and make them flags
	if not features.get('postproc', false)
		error('postproc_visualizer requires postproc to be enabled')
	endif
endif

# Enable unit tests by default if we have a working C++ compiler.
if c.get_argument_syntax() == 'msvc'
	# soft_enable
	if not features.get('unit_tests', true)
		features.set('unit_tests', true)
	endif
	# soft_enable
	if not features.get('webm_io', true)
		features.set('webm_io', true)
	endif
	# soft_enable
	if not features.get('libyuv', true)
		features.set('libyuv', true)
	endif
elif target_machine.system() == 'android'
	if c.get_supported_arguments('-std=gnu++11')
		# soft_enable
		if not features.get('webm_io', true)
			features.set('webm_io', true)
		endif
	endif
	# soft_enable
	if not features.get('libyuv', true)
		features.set('libyuv', true)
	endif
	# GTestLog must be modified to use Android logging utilities.
elif target_machine.system() == 'darwin'
	# Meson already handles the cpp_std flag.
	# iOS/ARM builds do not work with gtest. This does not match
	# x86 targets.
# Meson does not support iOS.
# elif target_machine.system() == 'ios'
#     if c.get_supported_arguments('-std=gnu++11')
#         # soft_enable
#         if not features.get('webm_io', true)
#             features.set('webm_io', true)
#         endif
#     endif
#     # soft_enable
#     if not features.get('libyuv', true)
#         features.set('libyuv', true)
#     endif
elif target_machine.system() == 'windows'
	# Some mingw toolchains don't have pthread available by default.
	# Treat these more like visual studio where threading in gtest
	# would be disabled for the same reason.
	if c.get_supported_arguments('-std=gnu++11')
		# soft_enable
		if not features.get('unit_tests', true)
			features.set('unit_tests', true)
		endif
		if not features.get('webm_io', true)
			features.set('webm_io', true)
		endif
	endif
	if cpp.compiles('int z;')
		if not features.get('libyuv', true)
			features.set('libyuv', true)
		endif
	endif
else
	if features.get('pthread_h', false)
		# soft_enable
		if not features.get('unit_tests', true)
			features.set('unit_tests', true)
		endif
	endif
	# soft_enable
	if not features.get('webm_io', true)
		features.set('webm_io', true)
	endif
	if cpp.compiles('int z;')
		if not features.get('libyuv', true)
			features.set('libyuv', true)
		endif
	endif
endif

##
## END APPLICATION SPECIFIC CONFIGURATION
##
# CONFIGURE_ARGS="$@"
# process "$@"
# print_webm_license ${BUILD_PFX}vpx_config.c "/*" " */"
# cat <<EOF >> ${BUILD_PFX}vpx_config.c
# #include "vpx/vpx_codec.h"
# static const char* const cfg = "$CONFIGURE_ARGS";
# const char *vpx_codec_build_config(void) {return cfg;}
# EOF

vpx_config_h = configure_file(
	output: 'vpx_config.h',
	configuration: {}
)
