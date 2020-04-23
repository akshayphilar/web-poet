import parsel

from core_po.responses import HTMLResponse


class HTMLResponseShortcutsMixin:
    """Common shortcut methods for working with HTML responses."""
    _cached_selector = None
    html_response: HTMLResponse

    @property
    def selector(self) -> parsel.Selector:
        """Creates a ``parsel.Selector`` instance for the HTML Response."""
        if self._cached_selector is None:
            self._cached_selector = parsel.Selector(self.html)

        return self._cached_selector

    @property
    def url(self):
        """Shortcut to HTML Response's URL."""
        return self.html_response.url

    @property
    def html(self):
        """Shortcut to HTML Response's content."""
        return self.html_response.content

    def xpath(self, query, **kwargs):
        """Shortcut to XPath selector."""
        return self.selector.xpath(query, **kwargs)

    def css(self, query):
        """Shortcut to CSS selector."""
        return self.selector.css(query)
