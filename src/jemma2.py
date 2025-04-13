from google import genai
import wikipedia as wk
import re
import asyncio

class jemma:
    def __init__(self, request: str):
        # self.requestType = request[:2]
        self.request = request
        # self.response: str
        self.response = None
        self.req_type = re.search(r"^![a-zA-Z0-9]+\s", self.request)
        self.req_type = self.req_type.group()[1:]
        self.req_concept = re.search(r"\s[a-zA-Z].+", self.request)
        self.req_concept = self.req_concept.group()[1:]
        # self.req_type = re.search(self.request, r"^![a-zA-Z]+\s")  #[1:]
        # self.req_concept = re.search(self.request, r"\s[a-zA-Z].+")  #[1:]
        self.client = genai.Client(api_key=
                                   "AIzaSyCyouAaaOBMUqRWCG4UrdwVo_gQzLoNR0Y")
        asyncio.run(self.decision())
        print("done!")

    async def decision(self):
        if "!eli5" == self.req_type:
            self.response = await self.client.models.generate_content(
              model="gemini-2.0-flash", contents=[
                  "Explain the following topic/person like I was 5 years old:",
                  self.req_concept
                ]
            )
        elif "!desc" == self.req_type:
            self.response = await self.client.models.generate_content(
              model="gemini-2.0-flash", contents=[
                  '''Describe the following topic/person with a good amount of
                  details, please and thank you.''',
                  self.req_concept
                ]
            )
        elif "!sum" == self.req_type:
            self.response = await self.client.models.generate_content(
              model="gemini-2.0-flash", contents=[
                  '''Summarize the past chat messages into a full, detailed list
                  of topics covered, please and thank you.''',
                  self.req_concept
                ]
            )
        elif "!rel" == self.req_type:
            self.response = await self.client.models.generate_content(
              model="gemini-2.0-flash", contents=[
                  '''If the concept given is a person, show a list of related
                  people. Else, show a list of related topics to the following
                  concept.''',
                  self.req_concept
                ]
            )
        elif "!wiki" == self.req_type:
            self.response = wk.summary(wk.search(self.req_concept)[0])
        # if "e5" in self.request:
        #     self.response = self.client.models.generate_content(
        #       model="gemini-2.0-flash", contents=[
        #           "Explain the following topic/person like I was 5 years old:",
        #           self.req_concept
        #         ]
        #     )
        # elif "db " in self.request:
        #     self.response = self.client.models.generate_content(
        #       model="gemini-2.0-flash", contents=[
        #           '''Describe the following topic/person with a good amount of
        #           details, please and thank you.''',
        #           self.req_concept
        #         ]
        #     )
        # elif "sum" in self.request:
        #     self.response = self.client.models.generate_content(
        #       model="gemini-2.0-flash", contents=[
        #           '''Summarize the past chat messages into a full, detailed list
        #           of topics covered, please and thank you.''',
        #           self.req_concept
        #         ]
        #     )
        # elif "rel" in self.request:
        #     self.response = self.client.models.generate_content(
        #       model="gemini-2.0-flash", contents=[
        #           '''If the concept given is a person, show a list of related
        #           people. Else, show a list of related topics to the following
        #           concept.''',
        #           self.req_concept
        #         ]
        #     )
        # elif "wiki " in self.request:
        #     self.response = wk.summary(wk.search(self.req_concept)[0])
# result = jemma("do this")
# L 5 decisions, 
