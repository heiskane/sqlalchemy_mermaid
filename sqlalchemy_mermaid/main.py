"""Generate mermaid erDiagram from SQLAlchemy metadata"""
import re

from sqlalchemy.ext.declarative import DeclarativeMeta


def create_mermaid_diagram(base: DeclarativeMeta) -> str:
    """Generate mermaid erDiagram from list of tables"""
    tables = base.metadata.tables.values()
    mermaid_diagram = "erDiagram\n\n"
    for table in tables:
        mermaid_diagram += f"  {table.name} {{"
        for column in table.columns:
            # Get rid of bad characters
            column_type = re.sub(r"[^a-zA-Z]", "", str(column.type))
            mermaid_diagram += f"\n    {column_type} {column.name}"

            if column.primary_key:
                mermaid_diagram += " PK"
            elif column.foreign_keys and not column.primary_key:
                mermaid_diagram += " FK"

        mermaid_diagram += "\n  }\n\n"

    for table in reversed(tables):
        for column in table.columns:
            foreign_keys = column.foreign_keys

            if not foreign_keys:
                continue

            for key in foreign_keys:

                if key.parent is None:
                    raise Exception("ForeignKey somehow does not have a parent column")

                # Not 100% correct but close enough for now
                relation = "}o--||" if key.parent.nullable else "}|--||"

                mermaid_diagram += f'  {key.column.table.name}  {relation} {table.name} : "{column.name}"\n'

    return mermaid_diagram
