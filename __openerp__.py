  GNU nano 2.2.6                                 File: __openerp__.py                                                                         

# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014-Today Business Tec Systems SA (<http://www.businesstec.net>).
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
    'name': 'Partner Plain Report',
    'version': '1.0',
    'sequence': 18,
    'summary': 'Printing lists of the customers',
    'description': """
     TBD
    """,
    'author': 'Business Tec Systems S.A.',
    'website': 'http://www.businesstec.net',
    'depends': ['sale', 'report'],
    'category': 'Sale',
    'data': ['view/ppr.xml',
    'ppr_view.xml'],
    'installable': True,
}

