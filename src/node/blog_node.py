from src.state.blog_state import StateBlog
from langchain_core.messages import HumanMessage,AIMessage
from src.state.blog_state import Blog

class BlogNode:
    " class repregents the node of blog generation"
    def __init__(self,llm):
        self.llm=llm
    #define a method for title generation
    def title_generation(self,state:StateBlog):
        "create a title for the blog"
        if 'topic' in state  and state['topic']:
            prompt="""you are expert blog content writer. use the markdown formatting
            genrate a blog title for the topic :{topic}. The title should be creative,concise and SEO-friendly
            """
            system_prompt=prompt.format(topic=state['topic'])

            print("[Title Prompt]:",system_prompt)

            response=self.llm.invoke(system_prompt)

            print("[Title response] :",response.content)

            return {"blog":{"title":response.content}}
        else:
            raise ValueError("missing topic in state")
    
    def content_generation(self,state:StateBlog):
        "gennerate a blog content based on the topic and previously generated title"
        if 'topic' in state and state['topic']:
            prompt = """
        You are an expert blog writer. Use Markdown formatting.
        Generate a detailed, engaging blog post with a proper breakdown for the topic: "{topic}".
        Title: "{title}"
             sections, subheadings, and examples where applicable
                """
            system_prompt=prompt.format(topic=state['topic'],
                                            title=state['blog']['title'])
            print("[content prompt]",system_prompt)
                
            response=self.llm.invoke(system_prompt)
            print("[content response]",response.content)

            return {
                "blog":{
                    "title":state['blog']['title'],
                    "content":response.content
                }
            }
        else:
            raise ValueError("missing 'topic in blog state")
    
    def translation(self,state:StateBlog):
        "translate the content into spacific language"
        prompt=""" Tranlate the content into currrent language:{current_language}
        Maintain the orignal tone,style and formatting
        orignal_content
        {blog_content}
        """
        print(state['current_language'])

        blog_content = state.get("blog", {}).get("content")
        if not blog_content:
            raise ValueError("Missing 'content' in blog state for translation.")


        system_message=prompt.format(current_language=state['current_language'],blog_content=blog_content)

        message=[HumanMessage(system_message)]

        content_translation=self.llm.with_structured_output(Blog).invoke(message)

        return {"blog":{"content":content_translation}}
    
    def route(self, state: StateBlog):
        return {"current_language": state['current_language'] }
    
    def route_decision(self,state:StateBlog):
        "Route the content to respecticve translation function"
        if state['current_language']=='Hindi':
            return "hindi"
        elif state['current_language']=='French':
            return "french"
        else:
            return state['current_language']
        
    





        


            
