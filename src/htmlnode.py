class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={len(self.children)}, props={len(self.props)})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value!")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value!")
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children,props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag!")
        if not isinstance(children, list) or len(children) == 0:
            raise ValueError("ParentNode must have children!")
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag!")
        if not self.children:
            raise ValueError("ParentNode must have children!")

        children_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
