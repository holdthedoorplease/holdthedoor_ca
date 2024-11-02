from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_refnode


class SplitArticlesNode(nodes.General, nodes.Element):
    """A custom node for handling paginated articles display."""
    pass


def visit_split_articles_node(self, node):
    """Handles the start of the SplitArticlesNode."""
    self.body.append(self.starttag(node, 'div', CLASS='article-page'))


def depart_split_articles_node(self, node):
    """Handles the end of the SplitArticlesNode."""
    self.body.append('</div>')


class SplitArticlesDirective(SphinxDirective):
    """Custom directive to split articles across multiple pages."""

    has_content = True
    required_arguments = 1  # number of articles per page

    def run(self):
        try:
            num_per_page = int(self.arguments[0])
            assert num_per_page > 0
        except (ValueError, AssertionError):
            raise self.error("Number of articles per page must be a positive integer.")

        # Split content into articles based on num_per_page
        articles = [line.strip() for line in self.content if line.strip()]
        num_pages = (len(articles) + num_per_page - 1) // num_per_page
        nodes_list = []

        for i in range(num_pages):
            page_node = SplitArticlesNode()
            start_idx = i * num_per_page
            end_idx = start_idx + num_per_page
            for article in articles[start_idx:end_idx]:
                para = nodes.paragraph(text=article)
                page_node += para

            # Add "next" and "previous" navigation if needed
            if num_pages > 1:
                nav_text = f'Page {i + 1} of {num_pages}'
                nav_node = nodes.paragraph(text=nav_text)
                page_node += nav_node
                # TODO: Insert logic for creating actual links if necessary

            nodes_list.append(page_node)

        return nodes_list


def setup(app):
    app.add_node(SplitArticlesNode,
                 html=(visit_split_articles_node, depart_split_articles_node))
    app.add_directive('split_articles', SplitArticlesDirective)