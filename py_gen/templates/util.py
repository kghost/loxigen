:: # Copyright 2013, Big Switch Networks, Inc.
:: #
:: # LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
:: # the following special exception:
:: #
:: # LOXI Exception
:: #
:: # As a special exception to the terms of the EPL, you may distribute libraries
:: # generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
:: # that copyright and licensing notices generated by LoxiGen are not altered or removed
:: # from the LoxiGen Libraries and the notice provided below is (i) included in
:: # the LoxiGen Libraries, if distributed in source code form and (ii) included in any
:: # documentation for the LoxiGen Libraries, if distributed in binary form.
:: #
:: # Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
:: #
:: # You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
:: # a copy of the EPL at:
:: #
:: # http://www.eclipse.org/legal/epl-v10.html
:: #
:: # Unless required by applicable law or agreed to in writing, software
:: # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
:: # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
:: # EPL for the specific language governing permissions and limitations
:: # under the EPL.
::
:: include('_copyright.py')

:: include('_autogen.py')

import loxi
import const
import struct

def pretty_mac(mac):
    return ':'.join(["%02x" % x for x in mac])

def pretty_ipv4(v):
    return "%d.%d.%d.%d" % ((v >> 24) & 0xFF, (v >> 16) & 0xFF, (v >> 8) & 0xFF, v & 0xFF)

def pretty_flags(v, flag_names):
    set_flags = []
    for flag_name in flag_names:
        flag_value = getattr(const, flag_name)
        if v & flag_value == flag_value:
            set_flags.append(flag_name)
        elif v & flag_value:
            set_flags.append('%s&%#x' % (flag_name, v & flag_value))
        v &= ~flag_value
    if v:
        set_flags.append("%#x" % v)
    return '|'.join(set_flags) or '0'

:: if version in [1,2]:
def pretty_wildcards(v):
    if v == const.OFPFW_ALL:
        return 'OFPFW_ALL'
    flag_names = ['OFPFW_IN_PORT', 'OFPFW_DL_VLAN', 'OFPFW_DL_SRC', 'OFPFW_DL_DST',
                  'OFPFW_DL_TYPE', 'OFPFW_NW_PROTO', 'OFPFW_TP_SRC', 'OFPFW_TP_DST',
                  'OFPFW_NW_SRC_MASK', 'OFPFW_NW_DST_MASK', 'OFPFW_DL_VLAN_PCP',
                  'OFPFW_NW_TOS']
    return pretty_flags(v, flag_names)
:: #endif

def pretty_port(v):
    named_ports = [(k,v2) for (k,v2) in const.__dict__.iteritems() if k.startswith('OFPP_')]
    for (k, v2) in named_ports:
        if v == v2:
            return k
    return v
