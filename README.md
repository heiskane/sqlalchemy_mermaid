# SQLAlchemy-Mermaid

Mostly a quick (and dirty) script to generate a [mermaid](https://mermaid-js.github.io/mermaid/) erDiagram from [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) metadata object

## Usage

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mermaid import create_mermaid_diagram

Base = declarative_base()

# Define tables here or import Base from somewhere else

mermaid_diagram = create_mermaid_diagram(Base)

code_block = "```mermaid\n"
code_block += mermaid_diagram
code_block += "```"

with open("example_result.md", "w", encoding="utf-8") as f:
    f.writelines(code_block)
```

Example result (after rendering in VSCode):
![example db diagram](example_result.png)
