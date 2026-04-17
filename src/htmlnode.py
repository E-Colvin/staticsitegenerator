class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return None

        string_props = ""
        for key, value in self.props.items():
            string_props += f" {key}=\"{value}\""
        
        return string_props

    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self,tag, value, props = None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        
        tag_string = f"<{self.tag}>"
        if self.props is not None:
            tag_string = f"<{self.tag}{self.props_to_html()}>"
        html_string = tag_string+f"{self.value}</{self.tag}>"

        return html_string

    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nProps: {self.props}"

