# Software License Agreement (BSD License)
#
# Copyright (c) 2010, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id: __init__.py 10652 2010-08-11 22:01:37Z kwc $

import os
import sys

fedora_map = {
    '19': 'schrodingers'
    '18': 'beefy',
    '17': 'spherical',
    }

fedora_inv_map = dict([[v,k] for k,v in fedora_map.items()])

def fedora_release():
    """
    WARNING: this can only be called on an Fedora system
    """
    if not os.path.isfile('/etc/issue'):
        raise Exception("this is not an fedora system")        
    f = open('/etc/issue')
    for s in f:
        if s.startswith('Fedora'):
            v = s.split()[2]
            v = '.'.join(v.split('.')[:2])
        try:
            return fedora_map[v]
        except KeyError:
            raise Exception("unrecognized fedora version %s" % v)
    raise Exception("could not parse fedora release version")

def fedora_release_version(fedora_rel)
    return fedora_inv_map[fedora_rel]

def redhatify_name(name):
    """
    Convert ROS stack name to rpm conventions (dashes, not underscores)
    """
    return name.replace('_', '-')

def redhatify_version(stack_version, distro_version, fedora_rel=None):
    """
    WARNING: this can only be called on an Fedora system and will lock to the platform it is called on
    """
    if fedora_rel is None:
        fedora_rel = fedora_release()
    fedora_ver = fedora_release_version(fedora_rel)
    return stack_version+'-'+distro_version+'.fc%s'%fedora_ver
