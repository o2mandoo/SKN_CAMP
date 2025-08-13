import asyncio
import nest_asyncio
import os  , json
from openai  import OpenAI
from dotenv import load_dotenv


from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client




client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])




class MCP_ChatBot:


    def __init__(self):
        self.session: ClientSession = None
        self.available_tools: list[dict] = []
        self.available_functions: list[dict] = []


    async def process_query(self, query : str):
        # 사용자 메시지로 대화 시작
        messages = [{'role' : 'user', 'content' : query}]


        # MCP 서버에서 받아온 도구 목록을 Openai 함수 스펙으로 변환
        self.available_functions = [
        {
            "name" : tool['name'],
            'description' : tool['description'],
            "parameters" : tool["input_schema"]
        }
        for tool in self.available_tools
        ]


        while True:
            response = client.chat.completions.create(
                model='gpt-4-0125-preview',
                messages=messages,
                functions=self.available_functions,
                function_call='auto',
                max_tokens = 2024,
                temperature = 0.5      
            )


            msg = response.choices[0].message


            if getattr(msg, 'function_call', None):
                func_name = msg.function_call.name
                func_args = json.loads(msg.function_call.arguments)
                print(f"Calling tool --> {func_name} with args {func_args}")
                tool_result = await self.session.call_tool(func_name, arguments=func_args)
               
                messages.append({
                    'role' : 'function',
                    'name' : func_name,
                    'content' : tool_result.content}
                )
                continue
           
            print(msg.content)
            messages.append(
                {
                    'role' : 'assistant',
                    'content' : msg.content
                }
            )
            break


    async def chat_loop(self):
        print("쿼리를 입력하거나 'quit'를 입력해 종료합니다.")
        while True:
            query = input("\nQuery : ").strip()
            if query.lower() == 'quit':
                break
            await self.process_query(query)
            print("\n")


    async def connect_to_server_and_run(self):
        server_params = StdioServerParameters(
            command="uv",
            args=["run", "research_server.py"],
            env=None
        )
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                self.session = session
                # 세션 초기화 및 도구 리스트 가져오기
                await session.initialize()
                response = await session.list_tools()
                tools = response.tools
                print(f"\nConnected to server with tools: {[tool.name for tool in tools]}")
                self.available_tools = [
                    {
                        "name" : tool.name ,
                        "description" : tool.description,
                        "input_schema" : tool.inputSchema
                    }
                    for tool in tools
                ]
                await self.chat_loop()




async def main():
    chatbot = MCP_ChatBot()
    await chatbot.connect_to_server_and_run()


if __name__ == "__main__":
    asyncio.run(main())


