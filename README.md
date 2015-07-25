Rabidquill.io
=============
An encrypted cloud text document editor.
----------------------------------------

I created this because, while Google Docs is incredibly useful and convenient,
I didn't feel like trusting my documents all the time to Google. So partly for
my own interest, and partly as a fun exercise, I wrote this editor.

A SHA256 cipher is created out of the user's password and saved in a cookie (for now).
That cipher is used to AES256 encrypt the contents of a document before sending it to
the server, which stores only the encrypted document.

When the document is opened later by the user, the server sends the encrypted blob,
and browser-side JavaScript decrypts it.

Copyright (C) 2015  Benjamin J. Thompson

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

I can be reached by these methods:
Email: bjt@rabidquill.com
Twitter: @Benj_Thompson
GitHub: https://github.com/praxeo

