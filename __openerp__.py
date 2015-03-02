# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Jan Vereecken.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Clubit Defaults',
    'version' : '0.1.0',
    'author' : 'Jan Vereecken',
    'category': 'Base',
    'description': 'Defaults the way we like it, aha aha.',
    'complexity': 'normal',
    'website': 'www.clubit.be',
    'data': [
        'data/clubit_defaults_data.xml',
        'data/mail_data.xml'
    ],
    'depends' : [
        'account',
        'mail',
        'web'
    ],
    'js': [
        'static/src/js/*.js',
    ],
    'qweb': [
    ],
    'css': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,                
}
