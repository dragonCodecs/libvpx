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
    ]
)

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

c = meson.get_compiler('c')
cpp = meson.get_compiler('cpp')

configuration = configuration_data()
features = configuration_data()

c_args = []
cpp_args = []
link_args = []

libyuv_cpp_args = []

# process_common_toolchain

gcc_target = ''
tgt_isa = target_machine.cpu_family()
tgt_os = target_machine.system()
float_abi = ''

if tgt_isa == 'arm'
    gcc_target = run_command('gcc', '-dumpmachine', check: false)
    if gcc_target.contains('hardfloat') or gcc_target.contains('gnueabihf')
        float_abi = 'hard'
    else
        float_abi = 'softfp'
    endif
endif

if tgt_os == 'darwin'
    gcc_target = run_command('gcc', '-dumpmachine', check: false)
endif

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
