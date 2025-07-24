from langgraph.graph import StateGraph,START,END
from src.state.blog_state import StateBlog
from src.node.blog_node import BlogNode
from src.llm.groq_llm import GROQLLM

class Graph_Builder:
    def __init__(self,llm):
        self.graph_builder=StateGraph(StateBlog)
        self.llm=llm
    
    def build_topic_graph(self):
        self.blog_node_object=BlogNode(self.llm)

        #add Node
        self.graph_builder.add_node('title_creation',self.blog_node_object.title_generation)
        self.graph_builder.add_node('content_creation',self.blog_node_object.content_generation)


        #add edges
        self.graph_builder.add_edge(START,'title_creation')
        self.graph_builder.add_edge('title_creation','content_creation')
        self.graph_builder.add_edge('content_creation',END)
        
        return self.graph_builder

    def compile_graph(self,usecase):
        if usecase=="topic":
           self.build_topic_graph()

        return self.graph_builder.compile()

#code for langsmith studio
llm=GROQLLM().get_llm()

graph_builder=Graph_Builder(llm)

graph=graph_builder.build_topic_graph().compile()


    

    
    

