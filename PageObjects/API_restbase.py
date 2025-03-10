import requests

from TestData.CP_Test_Data import loginData


class RestBaseClass(object):
    username = loginData.username
    password = loginData.password
    mailinator_mail = loginData.usernameMailinator

    def api_login(self):
        session = requests.Session()
        envName = self.get_env()
        if envName == 'stage':
            url = f'https://stage-auth.vertexcloud.com'
        else:
            # url = f'https://{envName}.equiscript.com/login'
            url = f'https://qa.equiscript.com/'

        print('Log in to URL : %s' % url)
        print(f'USer : {self.username}')

        # query_params = self.get_login_json(envName)
        params = {}
        r = session.get(url=url + '/authorize', params=params)