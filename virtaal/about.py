# -*- coding: utf-8 -*-
# 
# Copyright 2008 Zuza Software Foundation
# 
# This file is part of virtaal.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with translate; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import gtk
import os
import __version__

_ = lambda x: x

class About(gtk.AboutDialog):
    def __init__(self, parent):
        gtk.AboutDialog.__init__(self)
        self._register_uri_handlers()
        self.set_name("VirTaal")
        self.set_version(__version__.ver)
        self.set_copyright(_("© Copyright 2007-2008 Zuza Software Foundation"))
        self.set_comments(_("Advanced Computer Aided Translation (CAT) tool for localization and translation"))
        self.set_license("""This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Library General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.""")
        self.set_website("http://translate.sourceforge.net/wiki/virtaal/index")
        self.set_website_label(_("VirTaal website"))
        self.set_authors([
                "Friedel Wolff <friedel@translate.org.za>", 
                "Wynand Winterbach <wynand@translate.org.za>", 
                "Dwayne Bailey <dwayne@translate.org.za>",
                ])
        self.set_translator_credits(_("translator-credits"))
        self.set_icon(parent.get_icon())
        # FIXME entries that we may want to add
        #self.set_logo()
        #self.set_documenters()
        #self.set_artists()
        self.connect ("response", lambda d, r: d.destroy())
        self.show()

    def on_url(self, dialog, uri, data):
        try:
            if data == "mail":
                os.system("xdg-email " + link)
            elif data == "url":
                os.system("xdg-open " + link)
        except:
            pass

    def _register_uri_handlers(self):
        """Register the URL and email handlers

        Use xdg-open and xdg-email on Unix, ignore this on other platforms
        """
        if os.name == "posix":
            gtk.about_dialog_set_url_hook(self.on_url, "url")
            gtk.about_dialog_set_email_hook(self.on_url, "mail")
        else:
            pass


