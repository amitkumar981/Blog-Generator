from src.state.blog_state import StateBlog

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

            print("[Title Prompt]:",system_prompt.strip())

            response=self.llm.invoke(system_prompt)

            print("[Title response] :",response.content)

            return {"blog":{"title":response.content.strip()}}
        else:
            raise ValueError("missing topic in state")
    
    def content_generation(self,state:StateBlog):
        "gennerate a blog content based on the topic and previously generated title"
        if 'topic' in state and state['topic']:
            if 'blog' not in state or 'title' not in state['blog']:
                prompt = """
            You are an expert blog writer. Use Markdown formatting.
            Generate a detailed, engaging blog post with a proper breakdown for the topic: "{topic}".
            Title: "{title}"
            Include sections, subheadings, and examples where applicable
                """
                system_prompt=prompt.format(topic=state['topic'],
                                            title=state['blog']['title'])
                print("[content prompt]",system_prompt.strip())
                
                response=self.llm.invoke(system_prompt)
                print("[content response]",response.content)

                return {
                    "blog":{
                        "title":state['blog']['title'],
                        "content":response.content.strip()
                    }
                }
        else:
            raise ValueError("missing 'topic in blog state")
        






        


            
