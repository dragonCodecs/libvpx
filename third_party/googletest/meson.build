gtest_srcs = files(
	'src/src/gtest-all.cc',
)

gtest_includes = include_directories(
	'src',
	'src/include'
)

gtest_flags = []

if features.get('pthread_h', false)
	gtest_flags += ['-DGTEST_HAS_PTHREAD=0']
endif

libgtest = static_library(
	'gtest',
	gtest_srcs,
	cpp_args: gtest_flags,
	include_directories: gtest_includes,
	dependencies: extra_libs,
)

gtest_dep = declare_dependency(
	link_with: libgtest,
	compile_args: gtest_flags,
	dependencies: extra_libs,
	include_directories: gtest_includes,
)
