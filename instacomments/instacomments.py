# -*- coding: utf-8 -*-
import re
import requests

"""
    InstaComments 1.0

    By Sinf0r0s0 20/01/2020

    tanks! : https://stackoverflow.com/a/49341049/12651034 and
             https://www.diggernaut.com/blog/

"""


class Instacomments:
    tag_to_re_a_i = 'ProfilePageContainer.js/'
    tag_to_re_a_f = '.js","226'

    tag_to_re_b_i = 'queryId:"'
    tag_to_re_b_f = '",queryParams'

    def __init__(self, uri, max_com=40, timeout=10):
        self.uri = uri
        self.max_com = max_com
        self.time_out = timeout
        self.req = requests.get
        self.nova_pagina = None
        self.list_response = []

    def _rqst(self, url):
        try:
            return self.req(url, timeout=self.time_out)

        except Exception as e:
            print(e)

    def _re_search(self, tag_ini, tag_fin, input):
        return re.search(f'{tag_ini}(.*){tag_fin}', input).group(1)

    #  recover query_hash, tanks: https://www.diggernaut.com/blog/
    def get_query_hash(self):

        r = self._rqst(f'https://www.instagram.com/p/{self.uri}/')
        if r:
            ppc = self._re_search(self.tag_to_re_a_i, self.tag_to_re_a_f, r.text)
            # print(ppc)
            rp = self._rqst(f'https://www.instagram.com/static/bundles/metro/ProfilePageContainer.js/{ppc}.js')
            if rp:
                # print(rp.text)
                return self._re_search(self.tag_to_re_b_i, self.tag_to_re_b_f, rp.text)

            else:
                print('unable to get query hash')

        else:
            print('was not possible to access the page')

    def _req_json(self, query_h, insta_uri, max_p, after=''):
        res = self._rqst(
            f'https://www.instagram.com/graphql/query/?query_hash={query_h}&variables={{"shortcode":"{insta_uri}","first":{max_p},"after":"{after}"}}').json()

        if res:
            self.nova_pagina = res['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']

            for i in res['data']['shortcode_media']['edge_media_to_comment']['edges']:
                self.list_response.append({i['node']['owner']['username']: i['node']['text']})

                if len(self.list_response) == self.max_com:
                    break

    def start(self, query_hash=None):
        if query_hash:
            q_hash = query_hash
        else:
            q_hash = self.get_query_hash()
            print(f'\nUse this query hash as argument in "start()" function to several speed improvement!: "{q_hash}"')

        if q_hash:
            if self.max_com > 0 <= 40:
                self._req_json(q_hash, self.uri, self.max_com)

            if self.nova_pagina:
                while len(self.list_response) < self.max_com:
                    self._req_json(q_hash, self.uri, self.max_com, self.nova_pagina)

        # print(self.list_response)
        print(f'\nwell done! {len(self.list_response)} comments recovered!\n')
        return self.list_response
