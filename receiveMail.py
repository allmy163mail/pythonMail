import imaplib, email
import poplib, string


def receivemail(protocals):
    if(protocals == "imap"):
        M = imaplib.IMAP4_SSL("localhost")
        print M
        try:
            try:
                M.login('guest2@test.mikemail.com', '11111111')
            except Exception, e:
                print 'login error: %s' % e
                M.close()
            M.select()
            result, message = M.select()
            typ, data = M.search(None, 'ALL')
            for num in string.split(data[0]):
                try:
                    typ, data = M.fetch(num, '(RFC822)')
                    msg = email.message_from_string(data[0][1])
                    print msg["From"]
                    print msg["Subject"]
                    print msg["Date"]
                    print "_______________________________"
                except Exception, e:
                    print 'got msg error: %s' % e
            M.logout()
            M.close()
        except Exception, e:
            print 'imap error: %s' % e
            M.close()
    if (protocals == "pop"):
        PopServerName = "localhost"
        PopServer = poplib.POP3(PopServerName)
        print PopServer.getwelcome()
        PopServer.user('yourName')
        PopServer.pass_('yourPass')
        r, items, octets = PopServer.list()
        msgid, size = string.split(items[-1])
        r, msg, octets = PopServer.retr(msgid)
        msg = string.join(msg, "\n")
        print msg