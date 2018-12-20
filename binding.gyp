{
	'targets': [
		{
			'target_name': 'pcre2',
			'sources': [ 'src/addon.cc', 'src/PCRE2Wrapper.cc' ],
			'actions': [
				{
					'action_name': 'build PCRE2 library',
					'message': 'Building PCRE2 library...',
					'inputs': [''],
					'outputs': [''],
					'action': ['eval', 'sh ./compile'],
				},
			],
			"include_dirs": [
				"<!(node -e \"require('nan')\")",
				"build_pcre2/include/",
				"deps/pcre2/src/"
			],
			"libraries": [ "../build_pcre2/lib/libpcre2-8.a" ],
			'conditions': [
				[ 'OS!="win"', {
					'cflags+': [ '-std=c++11' ],
					'cflags_c+': [ '-std=c++11' ],
					'cflags_cc+': [ '-std=c++11' ],
				}],
			],
			'cflags!': [ '-O2' ],
			'cflags+': [ '-O3' ],
			'cflags_cc!': [ '-O2' ],
			'cflags_cc+': [ '-O3' ],
			'cflags_c!': [ '-O2' ],
			'cflags_c+': [ '-O3' ],
		},
	]
}
