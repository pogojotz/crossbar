###############################################################################
#
# Crossbar.io FX Master
# Copyright (c) Crossbar.io Technologies GmbH. All rights reserved.
#
###############################################################################

from typing import Dict, List  # noqa

from crossbarfx.master.api.remote import RemoteApi

__all__ = ('RemoteNativeProcessApi', )


class RemoteNativeProcessApi(RemoteApi):
    """
    Remote API to CF native node processes:

    * node controller
    * router worker
    * container worker
    * proxy worker
    """

    PREFIX = u'crossbarfabriccenter.remote.nativeprocess.'

    PROCS = {
        # these are node level procedures
        u'node': [
            u'get_cpu_count',
            u'get_cpu_affinity',
            u'set_cpu_affinity',
            u'get_process_info',
            u'get_process_stats',
            u'set_process_stats_monitoring',
            u'get_process_monitor',
            u'trigger_gc',
            u'start_manhole',
            u'stop_manhole',
            u'get_manhole',
        ],
    }

    EVENTS = {
        # these are node level topics
        u'node': []
    }  # type: Dict[str, List]
