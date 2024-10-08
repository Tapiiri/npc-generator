# template_renderer.py

import os
import logging
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

class TemplateRenderer:
    def __init__(self, config):
        self.template_dir = os.path.join(config.base_dir, 'templates')
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        self.register_filters()

    def register_filters(self):
        self.env.filters['format_modifier'] = self.format_modifier
        self.env.filters['format_date'] = self.format_date
        self.env.filters['humanize'] = self.humanize
        self.env.filters['replace_icons'] = self.replace_icons

    def replace_icons(self, text, icons):
        import re
        from markupsafe import Markup

        def replace_match(match):
            placeholder = match.group(0)
            icon_path = icons.get(placeholder)
            if icon_path:
                return f'<img src="{icon_path}" alt="{placeholder}" class="icon">'
            else:
                return f'<span class="missing-icon">{placeholder}</span>'

        # Use regex to find placeholders
        pattern = re.compile(r'\{[^}]+\}')
        result = pattern.sub(replace_match, text)
        return Markup(result)  # Mark as safe HTML

    @staticmethod
    def format_modifier(value):
        try:
            value = int(value)
            modifier = (value - 10) // 2
            return f"{value} ({modifier:+})"
        except (ValueError, TypeError):
            return value

    @staticmethod
    def format_date(value, format='%Y-%m-%d'):
        if isinstance(value, str):
            try:
                value = datetime.fromisoformat(value)
            except ValueError:
                return value
        return value.strftime(format)

    @staticmethod
    def humanize(value):
        return value.replace('_', ' ').title()

    def render_template(self, npc_data):
        layout = npc_data.get('template_instructions', {}).get('layout', 'detailed')
        template_file = f"{layout}.html"

        try:
            template = self.env.get_template(template_file)
        except Exception as e:
            logging.error(f"Error loading template {template_file}: {e}")
            return None

        try:
            # Unpack npc_data so that its keys are available as variables in the template
            html_content = template.render(**npc_data)
            return html_content
        except Exception as e:
            logging.error(f"Error rendering template for {npc_data.get('attributes', {}).get('name', 'Unknown')}): {e}")
            return None

