# from rest_framework_csv.renderers import CSVRenderer
from io import StringIO
import pandas as pd
from rest_framework import renderers


class CSVRenderer(renderers.BaseRenderer):
    media_type = 'text/csv'
    format = 'csv'
    encoding = 'latin-1'
    sep = ','

    def render(self, data, media_type=None, renderer_context=None):
        """
        Renders serialized *data* into CSV. For a dictionary:
        """
        if renderer_context is None:
            renderer_context = {}

        if data is None:
            return ''

        if isinstance(data, dict) and 'results' in data:
            data = data['results']

        if not isinstance(data, list):
            data = [data]

        df = pd.DataFrame(data)
        csv_buffer = StringIO()
        df.to_csv(
            csv_buffer,
            sep=self.sep,
            index=False,
            encoding=self.encoding)

        return csv_buffer.getvalue()
