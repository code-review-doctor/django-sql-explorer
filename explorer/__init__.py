__version_info__ = {
    'major': 2,
    'minor': 4,
    'micro': 0,
    'releaselevel': 'final',
    'serial': 0
}


def get_version(short=False):
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append(
            '%s%i' % (
                __version_info__['releaselevel'][0],
                __version_info__['serial'])
        )
    return ''.join(vers)


__version__ = get_version()

default_app_config = 'explorer.apps.ExplorerAppConfig'
