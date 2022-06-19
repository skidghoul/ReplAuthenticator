import requests

class ReplAuth:
      def __init__(self, connect_sid = ''):
            if True:
               self.connect_sid = connect_sid
               self.connect_sid

      def auth(
          self,
          site_url = '',
      ):
          if True:
             r = requests.post(
                 'https://replit.com/auth_with_repl_site',
                  headers = {
                          'X-REQUESTED-WITH'.lower(): 'XMLHttpRequest',
                          'Cookie'                  : 'connect.sid=%s' % (self.connect_sid),
                          'Origin'                  : 'https://replit.com',
                          'Referer'                 : 'https://replit.com/auth_with_repl_site?domain=%s' % (site_url)
                  }, json = {'host': '%s' % (site_url)}, cookies = {'connect.sid': self.connect_sid}
             )

             if True:
                try:
                   return r.json()['token']
                except Exception as E:
                      if True:
                         if True:
                            print (E)
                            print (r.json())

                         return None

x = ReplAuth(connect_sid = input('[@] Connect SID: ')).auth(site_url = input('[@] Site URL: '))
x

if True:
   print(x)
   print
