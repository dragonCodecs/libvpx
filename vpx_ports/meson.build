# vpx_ports.mk

#### --- GENERATED --- ####

ports_sources = files(
)

ports_optional_sources = {
	'mmx' : files(
		# 'emms_mmx.c' # MANUAL
	),
}

ports_headers_sources = files(
	'bitops.h',
	'compiler_attributes.h',
	'mem.h',
	'msvc.h',
	'static_assert.h',
	'system_state.h',
	'vpx_timer.h',
	# 'x86.h', # MANUAL
	# 'asmdefs_mmi.h', # MANUAL
)

ports_headers_optional_sources = {
}

ports_asm_sources = files(
	# 'x86_abi_support.asm', # MANUAL
)

ports_asm_optional_sources = {
	'mmx' : files(
		# 'emms_mmx.asm' # MANUAL
	),
	'msvs' : files(
		# 'float_control_word.asm' # MANUAL
	),
}

if features.get('x86', false) # MANUAL
	ports_optional_sources += {
		'mmx' : ports_optional_sources['mmx'] +
		 files(
			'emms_mmx.c'
		),
	}
endif

if features.get('x86_64', false) # MANUAL
	# Visual Studio x64 does not support the _mm_empty() intrinsic.
	ports_asm_optional_sources += {
		'mmx' : ports_asm_optional_sources['mmx'] +
		 files(
			'emms_mmx.asm'
		),
	}

	if features.get('msvs', true)
		ports_asm_optional_sources += {
			'msvs' : ports_asm_optional_sources['msvs'] +files(
				'float_control_word.asm'
			),
		}
	endif
endif

if features.get('x86', false) or features.get('x86_64', false)
	ports_asm_sources += files(
		'x86_abi_support.asm'
	)

	ports_headers_sources += files(
		'x86.h'
	)
endif

if features.get('mips', false)
	ports_headers_optional_sources += files(
		'asmdefs_mmi.h'
	)
endif

#### --- END GENERATED --- ####

optional_sources = get_variable('ports_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		ports_sources += comp_sources
	endif
endforeach

codec_srcs += ports_sources

optional_sources = get_variable('ports_headers_optional_sources', {})
foreach comp_name, comp_sources : optional_sources
	if features.get(comp_name, false)
		ports_headers_sources += comp_sources
	endif
endforeach

codec_headers += ports_headers_sources
