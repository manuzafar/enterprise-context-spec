# LangChain Integration

Load Enterprise Context Spec files as LangChain documents for use in RAG pipelines, agents, and chains.

## Installation

```bash
pip install enterprise-context langchain langchain-core
```

## Quick Start

```python
from enterprise_context.langchain import EnterpriseContextLoader

# Load context files
loader = EnterpriseContextLoader([
    "company-context.md",
    "division-context.md",
    "team-context.md"
])

docs = loader.load()

# Use in a retriever
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())
retriever = vectorstore.as_retriever()
```

## Loader Options

### Basic Loading

```python
# Load single file
loader = EnterpriseContextLoader(["company-context.md"])
docs = loader.load()
```

### With Inheritance Merging

```python
# Merge contexts with inheritance before loading
loader = EnterpriseContextLoader(
    files=["company.md", "division.md", "team.md"],
    merge=True  # Applies company → division → team inheritance
)

# Returns single merged document
docs = loader.load()
```

### Section-Based Splitting

```python
# Split into documents by section
loader = EnterpriseContextLoader(
    files=["company-context.md"],
    split_by_section=True
)

# Returns multiple documents, one per section
docs = loader.load()
# [Document(page_content="## Strategic Priorities\n...", metadata={"section": "strategic_priorities"}), ...]
```

### With Metadata

```python
loader = EnterpriseContextLoader(
    files=["company-context.md"],
    metadata={
        "source_type": "enterprise_context",
        "organization": "Acme Corp"
    }
)
```

## Document Structure

Each loaded document includes:

```python
Document(
    page_content="...",  # Markdown content
    metadata={
        "source": "company-context.md",
        "schema": "enterprise-context/v1/company",
        "company": "Acme Corp",
        "updated": "2025-03-01",
        # ... other frontmatter fields
    }
)
```

## Integration with Agents

### Context-Aware Agent

```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from enterprise_context.langchain import EnterpriseContextLoader

# Load context
loader = EnterpriseContextLoader(["company.md", "division.md", "team.md"], merge=True)
context_doc = loader.load()[0]

# Create context tool
def get_enterprise_context(query: str) -> str:
    """Get enterprise context information."""
    return context_doc.page_content

context_tool = Tool(
    name="enterprise_context",
    func=get_enterprise_context,
    description="Get organizational context including strategy, constraints, technology stack, and regulatory requirements."
)

# Create agent with context awareness
llm = ChatOpenAI(model="gpt-4")
agent = create_react_agent(llm, [context_tool], prompt)
executor = AgentExecutor(agent=agent, tools=[context_tool])
```

### RAG with Context

```python
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# Load and embed context
loader = EnterpriseContextLoader(
    files=["company.md", "division.md", "team.md"],
    split_by_section=True
)
docs = loader.load()

vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())

# Create QA chain
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# Query
result = qa.invoke("What is our risk appetite for new technology?")
```

## Custom Retriever

For more control, use the custom retriever:

```python
from enterprise_context.langchain import EnterpriseContextRetriever

retriever = EnterpriseContextRetriever(
    context_dir="/path/to/context",
    embedding_model="text-embedding-3-small",
    search_type="mmr",  # or "similarity"
    k=4
)

# Use in chain
docs = retriever.invoke("budget approval thresholds")
```

## Combining with Other Sources

```python
from langchain.retrievers import EnsembleRetriever

# Enterprise context retriever
context_retriever = EnterpriseContextRetriever(context_dir="./context")

# Code/docs retriever
code_retriever = ...

# Combine
ensemble = EnsembleRetriever(
    retrievers=[context_retriever, code_retriever],
    weights=[0.4, 0.6]
)
```

## Best Practices

### 1. Cache Embeddings

```python
from langchain.storage import LocalFileStore
from langchain.embeddings import CacheBackedEmbeddings

store = LocalFileStore("./cache")
embedder = CacheBackedEmbeddings.from_bytes_store(
    OpenAIEmbeddings(),
    store,
    namespace="enterprise_context"
)
```

### 2. Filter by Section

```python
# Only retrieve from specific sections
retriever = vectorstore.as_retriever(
    search_kwargs={
        "filter": {"section": {"$in": ["constraints", "regulatory", "risk_appetite"]}}
    }
)
```

### 3. Update Detection

```python
import hashlib
from pathlib import Path

def context_changed(files: list[str], cache_file: str = ".context_hash") -> bool:
    """Check if context files have changed."""
    current_hash = hashlib.md5()
    for f in sorted(files):
        content = Path(f).read_bytes()
        current_hash.update(content)

    new_hash = current_hash.hexdigest()

    if Path(cache_file).exists():
        old_hash = Path(cache_file).read_text()
        if old_hash == new_hash:
            return False

    Path(cache_file).write_text(new_hash)
    return True

# Only re-embed if changed
if context_changed(["company.md", "division.md", "team.md"]):
    docs = loader.load()
    vectorstore = Chroma.from_documents(docs, embeddings)
```

## Metadata Filtering

Use metadata for precise retrieval:

```python
# By context level
docs = vectorstore.similarity_search(
    "constraints",
    filter={"schema": "enterprise-context/v1/team"}
)

# By section
docs = vectorstore.similarity_search(
    "budget",
    filter={"section": "funding_model"}
)

# By update date
docs = vectorstore.similarity_search(
    "strategy",
    filter={"updated": {"$gte": "2025-01-01"}}
)
```

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Enterprise Context Spec](../../README.md)
- [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)

## License

MIT License
