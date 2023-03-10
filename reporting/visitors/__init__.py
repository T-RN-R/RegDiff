from mdutils.mdutils import MdUtils


class Visitor():
    def visit(self):
        pass
class MarkdownVisitor():
    def get_markdown(self, md:MdUtils, data:list) -> MdUtils:
        raise Exception("Please Implement Custom Markdown Visitor")








class MarkdownVisitable():
    def to_markdown(self, md:MdUtils, visitor:MarkdownVisitor):
        return visitor.get_markdown(md, self.data)


class DiffContainer(MarkdownVisitable):
    def __init__(self, data:list[MarkdownVisitable]):
        self.data = data



class AddedContainer(DiffContainer):
    pass


class RemovedContainer(DiffContainer):
    pass


