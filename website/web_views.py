
class WebViews:
    def load_base(user, breadcrumbs, body):
        html = """<!DOCTYPE html><html>        
        <head>
        <title>Monitoring</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon" />
        <link rel="stylesheet" href="/static/mon_app.css" type="text/css" />
        </head>
        <body>
        <div><div class="nav-sidebar">
        <a href="/" class="nav-button1"><svg viewBox="0 0 576 512"><path fill="currentColor" d="M488 312.7V456c0 13.3-10.7 24-24 24H348c-6.6 0-12-5.4-12-12V356c0-6.6-5.4-12-12-12h-72c-6.6 0-12 5.4-12 12v112c0 6.6-5.4 12-12 12H112c-13.3 0-24-10.7-24-24V312.7c0-3.6 1.6-7 4.4-9.3l188-154.8c4.4-3.6 10.8-3.6 15.3 0l188 154.8c2.7 2.3 4.3 5.7 4.3 9.3zm83.6-60.9L488 182.9V44.4c0-6.6-5.4-12-12-12h-56c-6.6 0-12 5.4-12 12V117l-89.5-73.7c-17.7-14.6-43.3-14.6-61 0L4.4 251.8c-5.1 4.2-5.8 11.8-1.6 16.9l25.5 31c4.2 5.1 11.8 5.8 16.9 1.6l235.2-193.7c4.4-3.6 10.8-3.6 15.3 0l235.2 193.7c5.1 4.2 12.7 3.5 16.9-1.6l25.5-31c4.2-5.2 3.4-12.7-1.7-16.9z"></path></svg></a>  
        <a href="/events" class="nav-button2"><svg viewBox="0 0 576 512"><path fill="currentColor" d="M569.517 440.013C587.975 472.007 564.806 512 527.94 512H48.054c-36.937 0-59.999-40.055-41.577-71.987L246.423 23.985c18.467-32.009 64.72-31.951 83.154 0l239.94 416.028zM288 354c-25.405 0-46 20.595-46 46s20.595 46 46 46 46-20.595 46-46-20.595-46-46-46zm-43.673-165.346l7.418 136c.347 6.364 5.609 11.346 11.982 11.346h48.546c6.373 0 11.635-4.982 11.982-11.346l7.418-136c.375-6.874-5.098-12.654-11.982-12.654h-63.383c-6.884 0-12.356 5.78-11.981 12.654z"></path></svg></a>
        <a href="/devices" class="nav-button3"><svg viewBox="0 0 512 512"><path fill="currentColor" d="M480 160H32c-17.673 0-32-14.327-32-32V64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm112 248H32c-17.673 0-32-14.327-32-32v-64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm112 248H32c-17.673 0-32-14.327-32-32v-64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24z"></path></svg></a> 
        <a href="/reports" class="nav-button4"><svg viewBox="0 0 512 512"><path fill="currentColor" d="M500 384c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H12c-6.6 0-12-5.4-12-12V76c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v308h436zM372.7 159.5L288 216l-85.3-113.7c-5.1-6.8-15.5-6.3-19.9 1L96 248v104h384l-89.9-187.8c-3.2-6.5-11.4-8.7-17.4-4.7z"></path></svg></a>
        <a href="/settings" class="nav-button5"><svg viewBox="0 0 512 512"><path fill="currentColor" d="M444.788 291.1l42.616 24.599c4.867 2.809 7.126 8.618 5.459 13.985-11.07 35.642-29.97 67.842-54.689 94.586a12.016 12.016 0 0 1-14.832 2.254l-42.584-24.595a191.577 191.577 0 0 1-60.759 35.13v49.182a12.01 12.01 0 0 1-9.377 11.718c-34.956 7.85-72.499 8.256-109.219.007-5.49-1.233-9.403-6.096-9.403-11.723v-49.184a191.555 191.555 0 0 1-60.759-35.13l-42.584 24.595a12.016 12.016 0 0 1-14.832-2.254c-24.718-26.744-43.619-58.944-54.689-94.586-1.667-5.366.592-11.175 5.459-13.985L67.212 291.1a193.48 193.48 0 0 1 0-70.199l-42.616-24.599c-4.867-2.809-7.126-8.618-5.459-13.985 11.07-35.642 29.97-67.842 54.689-94.586a12.016 12.016 0 0 1 14.832-2.254l42.584 24.595a191.577 191.577 0 0 1 60.759-35.13V25.759a12.01 12.01 0 0 1 9.377-11.718c34.956-7.85 72.499-8.256 109.219-.007 5.49 1.233 9.403 6.096 9.403 11.723v49.184a191.555 191.555 0 0 1 60.759 35.13l42.584-24.595a12.016 12.016 0 0 1 14.832 2.254c24.718 26.744 43.619 58.944 54.689 94.586 1.667 5.366-.592 11.175-5.459 13.985L444.788 220.9a193.485 193.485 0 0 1 0 70.2zM336 256c0-44.112-35.888-80-80-80s-80 35.888-80 80 35.888 80 80 80 80-35.888 80-80z"></path></svg></a> 
        </div>
        <div class="search-div">
        <form id="searchform" action="search" method="GET">
        <svg viewBox="0 0 512 512" class="search-font"><path fill="currentColor" d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"></path></svg>
        <input type="text" name="device" class="text-input" style="width:120px" />
        <input type="button" class="search-button" value="Search" onclick="searchform.submit()" /></form>
        </div>
        <div class="mon-container">
        <div class="user-div">"""
        html += breadcrumbs + """| &nbsp;
        <svg class="user-font" viewBox="0 0 448 512"><path fill="currentColor" d="M224 256c70.7 0 128-57.3 128-128S294.7 0 224 0 96 57.3 96 128s57.3 128 128 128zm89.6 32h-16.7c-22.2 10.2-46.9 16-72.9 16s-50.6-5.8-72.9-16h-16.7C60.2 288 0 348.2 0 422.4V464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48v-41.6c0-74.2-60.2-134.4-134.4-134.4z"></path></svg>
        &nbsp; <a href="/password">""" + user + """</a>&nbsp; (<a href="/logoff">Log Out</a>)</div>"""
        html += body + """</div></div><!--<script src="{% static 'mon_app/js/jquery.min.js' %}"></script>--></body></html>"""
        return html

    def load_refresh(url):
        html = """<div id="refresh"></div>
        <script>
        function refresh() {
        $.ajax({
            url: '""" + url + """',
            success: function(data) {
            $('#refresh').html(data);
            }
        });
        setTimeout(refresh, 60000);
        }    
        $(function(){
            refresh();
        });
        </script>"""
        return html

    def load_bc_home():
        html = """<svg class="bread-font" viewBox="0 0 576 512"><path fill="currentColor" d="M488 312.7V456c0 13.3-10.7 24-24 24H348c-6.6 0-12-5.4-12-12V356c0-6.6-5.4-12-12-12h-72c-6.6 0-12 5.4-12 12v112c0 6.6-5.4 12-12 12H112c-13.3 0-24-10.7-24-24V312.7c0-3.6 1.6-7 4.4-9.3l188-154.8c4.4-3.6 10.8-3.6 15.3 0l188 154.8c2.7 2.3 4.3 5.7 4.3 9.3zm83.6-60.9L488 182.9V44.4c0-6.6-5.4-12-12-12h-56c-6.6 0-12 5.4-12 12V117l-89.5-73.7c-17.7-14.6-43.3-14.6-61 0L4.4 251.8c-5.1 4.2-5.8 11.8-1.6 16.9l25.5 31c4.2 5.1 11.8 5.8 16.9 1.6l235.2-193.7c4.4-3.6 10.8-3.6 15.3 0l235.2 193.7c5.1 4.2 12.7 3.5 16.9-1.6l25.5-31c4.2-5.2 3.4-12.7-1.7-16.9z"></path></svg>
        &nbsp;&nbsp;Home&nbsp;"""  
        return html

    def load_bc_devices():
        html = """<svg class="bread-font" viewBox="0 0 512 512"><path fill="currentColor" d="M480 160H32c-17.673 0-32-14.327-32-32V64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm112 248H32c-17.673 0-32-14.327-32-32v-64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm112 248H32c-17.673 0-32-14.327-32-32v-64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24z"></path></svg>
        &nbsp;&nbsp;Devices&nbsp;&nbsp;"""   
        return html

    def load_bc_device(name):
        html = """<svg class="bread-font" viewBox="0 0 512 512"><path fill="currentColor" d="M480 160H32c-17.673 0-32-14.327-32-32V64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm112 248H32c-17.673 0-32-14.327-32-32v-64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm112 248H32c-17.673 0-32-14.327-32-32v-64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24z"></path></svg>
        &nbsp;&nbsp;<a href="/devices">Devices</a>&nbsp;>&nbsp;""" + name + """&nbsp;"""  
        return html

    def load_bc_device_graph(name, monitor):
        html = """<svg class="bread-font" viewBox="0 0 512 512"><path fill="currentColor" d="M480 160H32c-17.673 0-32-14.327-32-32V64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm112 248H32c-17.673 0-32-14.327-32-32v-64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm112 248H32c-17.673 0-32-14.327-32-32v-64c0-17.673 14.327-32 32-32h448c17.673 0 32 14.327 32 32v64c0 17.673-14.327 32-32 32zm-48-88c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24zm-64 0c-13.255 0-24 10.745-24 24s10.745 24 24 24 24-10.745 24-24-10.745-24-24-24z"></path></svg>
        &nbsp;&nbsp;<a href="/devices">Devices</a>&nbsp;>&nbsp;<a href="/devices/""" + name + """">""" + name + "</a>&nbsp;>&nbsp;" + monitor + """&nbsp;"""
        return html

    def load_bc_events():
        html = """<svg class="bread-font" viewBox="0 0 576 512"><path fill="currentColor" d="M569.517 440.013C587.975 472.007 564.806 512 527.94 512H48.054c-36.937 0-59.999-40.055-41.577-71.987L246.423 23.985c18.467-32.009 64.72-31.951 83.154 0l239.94 416.028zM288 354c-25.405 0-46 20.595-46 46s20.595 46 46 46 46-20.595 46-46-20.595-46-46-46zm-43.673-165.346l7.418 136c.347 6.364 5.609 11.346 11.982 11.346h48.546c6.373 0 11.635-4.982 11.982-11.346l7.418-136c.375-6.874-5.098-12.654-11.982-12.654h-63.383c-6.884 0-12.356 5.78-11.981 12.654z"></path></svg>    
        &nbsp;&nbsp;Events&nbsp;"""  
        return html

    def load_bc_reports():
        html = """<svg class="bread-font" viewBox="0 0 512 512"><path fill="currentColor" d="M500 384c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H12c-6.6 0-12-5.4-12-12V76c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v308h436zM372.7 159.5L288 216l-85.3-113.7c-5.1-6.8-15.5-6.3-19.9 1L96 248v104h384l-89.9-187.8c-3.2-6.5-11.4-8.7-17.4-4.7z"></path></svg>
        &nbsp;&nbsp;Reports&nbsp;"""  
        return html

    def load_bc_settings():
        html = """<svg class="bread-font" viewBox="0 0 512 512"><path fill="currentColor" d="M444.788 291.1l42.616 24.599c4.867 2.809 7.126 8.618 5.459 13.985-11.07 35.642-29.97 67.842-54.689 94.586a12.016 12.016 0 0 1-14.832 2.254l-42.584-24.595a191.577 191.577 0 0 1-60.759 35.13v49.182a12.01 12.01 0 0 1-9.377 11.718c-34.956 7.85-72.499 8.256-109.219.007-5.49-1.233-9.403-6.096-9.403-11.723v-49.184a191.555 191.555 0 0 1-60.759-35.13l-42.584 24.595a12.016 12.016 0 0 1-14.832-2.254c-24.718-26.744-43.619-58.944-54.689-94.586-1.667-5.366.592-11.175 5.459-13.985L67.212 291.1a193.48 193.48 0 0 1 0-70.199l-42.616-24.599c-4.867-2.809-7.126-8.618-5.459-13.985 11.07-35.642 29.97-67.842 54.689-94.586a12.016 12.016 0 0 1 14.832-2.254l42.584 24.595a191.577 191.577 0 0 1 60.759-35.13V25.759a12.01 12.01 0 0 1 9.377-11.718c34.956-7.85 72.499-8.256 109.219-.007 5.49 1.233 9.403 6.096 9.403 11.723v49.184a191.555 191.555 0 0 1 60.759 35.13l42.584-24.595a12.016 12.016 0 0 1 14.832 2.254c24.718 26.744 43.619 58.944 54.689 94.586 1.667 5.366-.592 11.175-5.459 13.985L444.788 220.9a193.485 193.485 0 0 1 0 70.2zM336 256c0-44.112-35.888-80-80-80s-80 35.888-80 80 35.888 80 80 80 80-35.888 80-80z"></path></svg>
        &nbsp;&nbsp;Settings&nbsp;"""  
        return html

    def load_login():
        html = """<!DOCTYPE html>
        <html>
        <head><title>Monitoring</title>
        <link rel="stylesheet" href="/static/mon_app.css" />
        </head>
        <body style="background-color:#325D88">
        <br />
        <br />
        <div style="display:flex;justify-content:center">
        <table style="width:300px"><tr><td>
        <div class="card-div">
        <div class="card-header">Monitoring Login</div>
        <table style="width:100%;">
        <tr>
        <td style="padding-left:10px">
        <form action="verify" method="POST">
        <table>
        <tr><td style="width:150px">Username</td><td style="width:150px"><input type="text" class="text-input" name="username" /></td></tr>
        <tr><td>Password</td><td><input type="password" class="text-input" name="password" /></td></tr>
        <tr><td></td><td style="text-align:right"><input type="submit" class="action-button" value="Login" /></td></tr>
        </table>
        </form>
        </td></tr></table> 
        </div></td></tr></table>
        </div>
        </body>
        </html>"""
        return html

    def load_index_content(index_block_1, index_block_2, index_block_3, index_block_4, index_block_pager):
        html = """<table style="width:100%;">
        <tr><td style="padding-right:4px">
        <div class="card-div">
        <div class="card-header">Host Availability</div>
        """ + index_block_1 + """
        </div></td>
        <td style="padding-left:4px;padding-right:4px">
        <div class="card-div">
        <div class="card-header">Open Events</div>
        """ + index_block_2 + """
        </div></td>
        <td style="padding-left:4px">
        <div class="card-div">
        <div class="card-header">Monitoring Server</div>
        """ + index_block_3 + """
        </div></td></tr>
        <tr><td colspan="3" style="padding-top:8px">
        <div class="card-div">
        <div class="card-header">Host Summary</div>
        <table style="width:100%;table-layout:fixed;"> 
        """ + index_block_4 + """
        </table> 
        <table style="width:100%;table-layout:fixed;">
        <tr><td></td>
        """ + index_block_pager + """
        <td style="width:10px"></td></tr>
        </table></div></td></tr></table>"""
        return html

    def load_basic_page(title, content):
        html = """<table style="width:100%;"><tr><td>
        <div class="card-div">
        <div class="card-header">""" + title + """</div>
        <table style="width:100%;">
        <tr>
        <td style="padding-left:10px">
        """ + content + """
        </td></tr></table> 
        </div></td></tr></table>"""
        return html

    def load_device_content(system, data):
        html = """<table style="width:100%;">
        <tr><td colspan="4" style="padding-bottom:4px;text-align:left">
        <div class="card-div" style="height:45px">
        <div class="card-header">System Information</div>
        <div style="padding-left: 10px">
        """ + system + """
        </div></div></td></tr>
        """ + data + """
        </table>"""
        return html

    def load_events_content(summary, events):
        html = """<table style="width:100%;">
        <tr><td><div class="card-div">
        <div class="card-header">Event Summary</div>
        """ + summary + """ 
        </div></td></tr>
        <tr><td style="text-align: left;padding-top:8px">
        <div class="card-div">
        <div class="card-header">Events</div>
        """ + events + """    
        </div></td></tr></table>"""
        return html

    def load_change_password():
        html = """
        <form action="" method="POST">
        <table>
        <tr><td style="width:150px">Old Password</td><td style="width:150px"><input type="password" class="text-input" name="pass1" /></td></tr>
        <tr><td>New Password</td><td><input type="password" class="text-input" name="pass2" /></td></tr>
        <tr><td></td><td style="text-align:right"><input type="submit" class="action-button" value="Submit" /></td></tr>
        </table>
        </form>"""
        return html

    def load_user_add():
        html = """
        <form action="" method="POST">
        <table>
        <tr><td style="width:150px">Username</td><td style="width:150px"><input type="text" class="text-input" name="username" /></td></tr>
        <tr><td>New Password</td><td><input type="password" class="text-input" name="password" /></td></tr>
        <tr><td>Role</td><td><input type='radio' name='role' value='0' /> User <input type='radio' name='role' value='1' /> Admin</td></tr>
        <tr><td></td><td style="text-align:right"><input type="submit" class="action-button" value="Submit" /></td></tr>
        </table>
        </form>"""
        return html
    
    def load_user_edit_password():
        html = """
        <form action="" method="POST">
        <table>
        <tr><td style="width:150px">Old Password</td><td style="width:150px"><input type="password" class="text-input" name="pass1" /></td></tr>
        <tr><td>New Password</td><td><input type="password" class="text-input" name="pass2" /></td></tr>
        <tr><td></td><td style="text-align:right"><input type="submit" class="action-button" value="Submit" /></td></tr>
        </table>
        </form>"""
        return html
    
    def load_user_edit_role(role):
        html = """
        <form action="" method="POST">
        <table>
        <tr><td>Role</td>
        <td>"""
        if role == 0:
            html += "<input type='radio' name='role' value='0' checked='checked' /> User<input type='radio' name='role' value='1' /> Admin" 
        else:
            html += "<input type='radio' name='role' value='0' /> User<input type='radio' name='role' value='1' checked='checked' /> Admin"
        html += """</td></tr>
        <tr><td></td><td style="text-align:right"><input type="submit" class="action-button" value="Submit" /></td></tr>
        </table>
        </form>"""
        return html
